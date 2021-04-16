import numpy as np
import tqdm
import re

import unicodedata

regex = '[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!"#$%&''()*+,-./:;<=>?@[\]^_`{|}~ ]'
print(len(regex) - 3)
vocab = set()

def create_strings_from_file_v2(filename, count, min_words, max_words, outfile):
    """
        Create all strings by reading lines in specified files
    """

    strings = []
    with open(outfile, 'w') as f_out:
        with open(filename, "r", encoding="utf8") as f:
            lines = [l.strip() for l in f.read().splitlines() if len(l) > 0]
            if len(lines) == 0:
                raise Exception("No lines could be read in file")

            ids_rnd = np.random.permutation(len(lines)-1)[:count]
            for idx in tqdm.tqdm(ids_rnd):
                words = lines[idx].split(" ")
                len_rnd = np.random.randint(min_words, max_words)
                st = np.random.randint(0, max(1, len(words) - len_rnd))
                start = np.random.choice([0, st, st, st])
                words_choice = words[start:start+len_rnd]
                string = " ".join(words_choice)
                string = re.sub(regex, " ", string)
                string = unicodedata.normalize('NFC', string)
                vocab.update(list(string))
                try:
                    f_out.write(string + '\n')
                except:
                    print(string)
                    break


        # return strings
        print(sorted(vocab))
        print(len(vocab))

# def merge(file_list, output):
#     with open(output, 'w', encoding='utf-8')

if __name__ == "__main__":

    create_strings_from_file_v2('VNESEcorpus.txt', 30000, 1, 7, 'sent_sort.txt')
    create_strings_from_file_v2('VNESEcorpus.txt', 50000, 7, 10, 'sent_medium.txt')
    create_strings_from_file_v2('VNESEcorpus.txt', 120000, 10, 15, 'sent_long.txt')