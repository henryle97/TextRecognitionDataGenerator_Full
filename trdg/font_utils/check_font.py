import glob
import os

from PIL import ImageFont, Image, ImageDraw, ImageColor
import random as rnd

font_dir = "../fonts/vn"
text = "BỐC"
print(text)

def check(font_size=32, space_width = 1.0, character_spacing=0, text_color= "#000000", word_split=False):
    fonts = glob.glob(font_dir + "/*")
    print(len(fonts))
    for font in fonts:

        image_font = ImageFont.truetype(font=font, size=font_size, encoding='utf-8')

        space_width = int(image_font.getsize(" ")[0] * space_width)

        if word_split:
            splitted_text = []
            for w in text.split(" "):
                splitted_text.append(w)
                splitted_text.append(" ")
            splitted_text.pop()
        else:
            splitted_text = text

        piece_widths = [
            image_font.getsize(p)[0] if p != " " else space_width for p in splitted_text
        ]
        text_width = sum(piece_widths)
        if not word_split:
            text_width += character_spacing * (len(text) - 1)

        text_height = max([image_font.getsize(p)[1] for p in splitted_text])
        print(font, text_height)
        txt_img = Image.new("RGBA", (text_width, text_height+20), (0, 0, 0, 0))
        txt_mask = Image.new("RGB", (text_width, text_height), (0, 0, 0))

        txt_img_draw = ImageDraw.Draw(txt_img)
        txt_mask_draw = ImageDraw.Draw(txt_mask, mode="RGB")
        txt_mask_draw.fontmode = "1"

        colors = [ImageColor.getrgb(c) for c in text_color.split(",")]
        c1, c2 = colors[0], colors[-1]

        fill = (
            rnd.randint(min(c1[0], c2[0]), max(c1[0], c2[0])),
            rnd.randint(min(c1[1], c2[1]), max(c1[1], c2[1])),
            rnd.randint(min(c1[2], c2[2]), max(c1[2], c2[2])),
        )

        for i, p in enumerate(splitted_text):
            txt_img_draw.text(
                (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
                p,
                fill=fill,
                font=image_font,
            )
            txt_mask_draw.text(
                (sum(piece_widths[0:i]) + i * character_spacing * int(not word_split), 0),
                p,
                fill=((i + 1) // (255 * 255), (i + 1) // 255, (i + 1) % 255),
                font=image_font,
            )
        if 'serpents' in font:
            txt_img.convert('RGB').save('check.jpg')
        size = font_size
        margins = (5,5,5,5)
        width = -1
        margin_top, margin_left, margin_bottom, margin_right = margins
        horizontal_margin = margin_left + margin_right
        vertical_margin = margin_top + margin_bottom
        print(txt_img.size)
        new_width = int(
            txt_img.size[0]
            * (float(size - vertical_margin) / float(txt_img.size[1]))
        )
        if new_width <=0:
            continue
        resized_img = txt_img.resize(
            (new_width, size - vertical_margin), Image.ANTIALIAS
        )
        background_width = width if width > 0 else new_width + horizontal_margin
        background_height = size + 64

        background_img = Image.new("L", (background_width, background_height), 255).convert("RGBA")
        background_img.paste(resized_img, (margin_left, margin_top+20), resized_img)

        final_img  = background_img.convert('RGB')
        final_img.save("font_img_2/" + os.path.basename(font) + "img.jpg")

def remove():
    error_dir = 'error'
    errors = glob.glob(error_dir + "/*")
    for error in errors:
        font_name = os.path.basename(error)[:-7]
        print(font_name)
        os.remove(font_dir + "/" + font_name)


if __name__ == "__main__":
    # check()
    remove()