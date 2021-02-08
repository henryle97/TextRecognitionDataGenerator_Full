import os
import re
def run():
    root_dir = 'data_160k'
    paths = os.listdir(root_dir)
    test_size = 0.1
    test_size_idx = int(len(paths) * test_size)

    train_paths = paths[test_size_idx:]
    test_paths = paths[:test_size_idx]


    with open("train_id.txt", 'w', encoding='utf-8') as f:
        for path in train_paths:
            label = path.split("_")[1].replace("#", "/")
            label = re.sub(r"[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#\$%&\\\'\(\)h\*\+,-\./:;<=>\?@\[\]\^_`\{\|\}\~ ]", "", label)
            path_img = root_dir + "/" + path
            f.write(path_img + "\t" + label + "\n")

    with open("test_id.txt", 'w', encoding='utf-8') as f:
        for path in test_paths:
            label = path.split("_")[1].replace("#", "/")
            label = re.sub(r"[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#\$%&\\\'\(\)h\*\+,-\./:;<=>\?@\[\]\^_`\{\|\}\~ ]", "", label)
            path_img = root_dir + "/" + path
            f.write(path_img + "\t" + label + "\n")


if __name__ == "__main__":
    # run()
    label = "8211067f-feb0-47d6-ba74-5faf3c44d3ee_Xã Kim Thư, Huyện Thanh Oai, Hà Nội_8211067f-feb0-47d6-ba74-5faf3c44d3ee.jpg"
    label = label.split("_")[1].replace("#", "/")

    # label = re.sub(
    #     r"[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!\"#\$%&\\\'\(\)h\*\+,-\./:;<=>\?@\[\]\^_`\{\|\}\~ ]",
    #     "", label)
    # path_img = root_dir + "/" + path
    # f.write(path_img + "\t" + label + "\n")
    print(label)


