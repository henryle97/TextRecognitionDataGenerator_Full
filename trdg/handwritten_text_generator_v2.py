import os
import pickle
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import torch
from PIL import Image, ImageColor
from collections import namedtuple
import warnings
from  trdg.handwritten_model.handwritten import HandwritingSynthesisNetwork
from trdg.handwritten_model import params as pr
import os

# import params as pr
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'

warnings.filterwarnings("ignore")
#
# vocab = np.load(pr.vocab_path)
# print("Vocab: ", vocab)
# char2idx = {x: i for i, x in enumerate(vocab)}
# device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
#
# model = HandwritingSynthesisNetwork(
#     len(vocab),
#     pr.dec_hidden_size, pr.dec_n_layers,
#     pr.n_mixtures_attention, pr.n_mixtures_output,
#     device
# )
# model.load_state_dict(torch.load(pr.load_path, map_location=torch.device('cpu')))
# model = model.to(device)




def _sample(e, mu1, mu2, std1, std2, rho):
    cov = np.array([[std1 * std1, std1 * std2 * rho], [std1 * std2 * rho, std2 * std2]])
    mean = np.array([mu1, mu2])

    x, y = np.random.multivariate_normal(mean, cov)
    end = np.random.binomial(1, e)
    return np.array([x, y, end])


def _split_strokes(points):
    points = np.array(points)
    strokes = []
    b = 0
    for e in range(len(points)):
        if points[e, 2] == 1.0:
            strokes += [points[b : e + 1, :2].copy()]
            b = e + 1
    return strokes


def _cumsum(points):
    sums = np.cumsum(points[:, :2], axis=0)
    return np.concatenate([sums, points[:, 2:]], axis=1)


def preprocessing_str(sent, vocab):
    chars = list(sent)
    chars = [c for c in chars if c in vocab]
    return "".join(chars)

def sent2idx(sent, char2idx):
    return np.asarray([char2idx[c] for c in sent])

def _sample_text_v2(model, text, vocab, char2idx):
    device = model.device
    string_processed = preprocessing_str(text, vocab)
    # print("Processed: ", string_processed)
    chars = torch.from_numpy(
        sent2idx(string_processed, char2idx)
    ).long()[None].to(device)
    chars_mask = torch.ones_like(chars).float().to(device)

    with torch.no_grad():
        coords = model.sample(chars, chars_mask, maxlen=pr.MAX_STROKE_LENGTH)[0].cpu().numpy()
        coords = coords[:, [1, 2, 0]]   # [x, y, e]
    return coords



def _crop_white_borders(image):
    image_data = np.asarray(image)
    grey_image_data = np.asarray(image.convert("L"))
    # plt.imshow(grey_image_data)
    # plt.show()
    non_empty_columns = np.where(grey_image_data.min(axis=0) < 255)[0]
    non_empty_rows = np.where(grey_image_data.min(axis=1) < 255)[0]
    # from IPython import embed; embed()
    cropBox = (
        min(non_empty_rows),
        max(non_empty_rows),
        min(non_empty_columns),
        max(non_empty_columns),
    )
    image_data_new = image_data[
        cropBox[0] : cropBox[1] + 1, cropBox[2] : cropBox[3] + 1, :
    ]
    # plt.imshow(image_data_new)
    # plt.show()
    return Image.fromarray(image_data_new)


def _join_images(images, padding_size=35):
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths) + padding_size * (len(images)-1)
    max_height = max(heights)

    compound_image = Image.new("RGBA", (total_width, max_height))

    x_offset = 0
    for im in images:
        compound_image.paste(im, (x_offset, 0))
        x_offset += im.size[0] + padding_size

    return compound_image


def align_strokes(coords):
    """
    corrects for global slant/offset in handwriting strokes
    """
    coords = np.copy(coords)
    X, Y = coords[:, 0].reshape(-1, 1), coords[:, 1].reshape(-1, 1)
    X = np.concatenate([np.ones([X.shape[0], 1]), X], axis=1)
    offset, slope = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y).squeeze()
    theta = np.arctan(slope)
    rotation_matrix = np.array(
        [[np.cos(theta), -np.sin(theta)],
         [np.sin(theta), np.cos(theta)]]
    )
    coords[:, :2] = np.dot(coords[:, :2], rotation_matrix) - offset
    return coords


def generate(model, vocab, char2idx, text, text_color=None, align=True):

    images = []
    # colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
    # c1, c2 = colors[0], colors[-1]
    #
    # color = "#{:02x}{:02x}{:02x}".format(
    #     rnd.randint(min(c1[0], c2[0]), max(c1[0], c2[0])),
    #     rnd.randint(min(c1[1], c2[1]), max(c1[1], c2[1])),
    #     rnd.randint(min(c1[2], c2[2]), max(c1[2], c2[2])),
    # )

    for word in text.split(" "):
        # print("Word: ",  word)
        word += " "

        coords = _sample_text_v2(
            model, word, vocab, char2idx
        )
        # print(coords)
        # break

        fig, ax = plt.subplots(1, 1)
        fig.patch.set_visible(False)
        ax.axis("off")


        strokes = np.concatenate(
            [coords[:, 2:3], np.cumsum(coords[:, :2], axis=0)],
            axis=1
        )

        if align:
            strokes[:, 1:] = align_strokes(strokes[:, 1:])

        stroke = []
        color_pen = rnd.choice(['blue', 'black', 'red'])
        linewidth = rnd.choice([2,3, 4,5, 8, 12])
        # linewidth =
        for eos, x, y in strokes:
            stroke.append((x, y))
            if eos == 1:
                xs, ys = zip(*stroke)
                ys = np.array(ys)
                plt.plot(xs, ys, 'k', c=color_pen, linewidth=linewidth)
                stroke = []

        if stroke:
            xs, ys = zip(*stroke)
            ys = np.array(ys)
            plt.plot(xs, ys, 'k', c=color_pen, linewidth=linewidth)


        # plt.show()
        # for stroke in _split_strokes(_cumsum(np.array(coords))):
        #     plt.plot(stroke[:, 0], -stroke[:, 1], color=color)

        fig.patch.set_alpha(0)
        fig.patch.set_facecolor("none")
        # plt.show()

        canvas = plt.get_current_fig_manager().canvas
        canvas.draw()

        s, (width, height) = canvas.print_to_buffer()
        image = Image.frombytes("RGBA", (width, height), s)
        mask = Image.new("RGB", (width, height), (0, 0, 0))

        # plt.imshow(image)
        images.append(_crop_white_borders(image))
        # plt.show()
        plt.close()

    return _join_images(images), mask


if __name__ == "__main__":
    img, _ = generate(model, vocab, device, char2idx, "nghiêng", text_color="#000000")
    print('mask', _)
    plt.imshow(np.asarray(img))
    plt.show()
