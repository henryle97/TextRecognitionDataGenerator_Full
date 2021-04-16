import os
import random
import re
import glob
import tqdm
import unicodedata


def rename(directory='address'):
    paths = glob.glob(directory + '/*')
    for path in tqdm.tqdm(paths):
        label = os.path.basename(path)
        label = unicodedata.normalize('NFC', label)
        label = label.encode('utf-8').strip()
        label = label.decode(errors='ignore')
        label = re.sub(
            r"[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#\$%&\\\'\(\)h\*\+,-\./:;<=>\?@\[\]\^_`\{\|\}\~ ]",
            "", label)
        new_path = os.path.join(os.path.dirname(path), label)
        os.rename(path, new_path)


subdirs = ['address', 'date', 'id', 'fullname']


def run():
    # shutil.rmtree("")
    with open("train_160k.txt", 'w', encoding='utf8') as train_f:
        with open("test_160k.txt", 'w', encoding='utf8') as test_f:
            for subdir in subdirs:
                root_dir = subdir
                paths = os.listdir(root_dir)
                random.shuffle(paths)
                print(len(paths))
                test_size = 0.1
                test_size_idx = int(len(paths) * test_size)

                train_paths = paths[test_size_idx:]
                test_paths = paths[:test_size_idx]

                for path in tqdm.tqdm(train_paths):
                    label = path.split("_")[1].replace("#", "/")
                    # label = unicodedata.normalize('NFC', label)
                    # label = label.encode('utf-8').strip()
                    # label = label.decode(errors='ignore')
                    # label = re.sub(
                    #     r"[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#\$%&\\\'\(\)h\*\+,-\./:;<=>\?@\[\]\^_`\{\|\}\~ ]",
                    #     "", label)
                    path_img = root_dir + "/" + path
                    new_path = root_dir + "/" + path.split("_")[0] + ".jpg"
                    os.rename(path_img, new_path)
                    train_f.write(new_path + "\t" + label + "\n")

                for path in tqdm.tqdm(test_paths):
                    label = path.split("_")[1].replace("#", "/")
                    # label = unicodedata.normalize('NFC', label)
                    # label = label.encode('utf-8').strip()
                    # label = label.decode(errors='ignore')
                    # label = re.sub(
                    #     r"[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#\$%&\\\'\(\)h\*\+,-\./:;<=>\?@\[\]\^_`\{\|\}\~ ]",
                    #     "", label)
                    path_img = root_dir + "/" + path
                    new_path = root_dir + "/" + path.split("_")[0] + ".jpg"
                    os.rename(path_img, new_path)
                    test_f.write(new_path + "\t" + label + "\n")


if __name__ == "__main__":
    run()
    # rename('address')

    # 00970894-a9fa-446b-984b-3d9744f77281



