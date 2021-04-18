import re

import tqdm

def filter(all, filter='word_dict_order.txt'):
    with open(all, 'r') as all_file:

        all_words = all_file.readlines()
        with open(filter, 'r') as filter_file:
            filter_words = filter_file.readlines()
            with open('word_dict_en.txt', 'w') as f:
                for w in tqdm.tqdm(all_words):
                    if w not in filter_words and ' ' not in w:
                        f.write(w)

def remove_non_vietnamese(vi_file, en_file, outpath):
    with open(vi_file, 'r', encoding='utf-8') as f:
        words = [word.strip() for word in f.readlines()]

    with open(en_file, 'r', encoding='utf-8') as f:
        en_words = [word.strip() for word in f.readlines()]
    words = set(words)
    en_words = set(en_words)
    vi_words = []
    for word in words:
        if word in en_words or ' ' in word:
            continue
        else:
            word = re.sub(r'[@!#$%^&*()_+,./;\[\]{}\\|\'-=]', '', word)
            vi_words.append(word)
    vi_words = sorted(vi_words)
    with open(outpath, 'w', encoding='utf-8') as f:
        for word in vi_words:
            f.write(word + '\n')


if __name__ == '__main__':
    # filter("word_dict_all_order_eng_vi.txt", "word_dict_order.txt")
    remove_non_vietnamese('vi_dictionary_hw.txt', 'words_eng.txt', 'vi_dictionary_hw_2.txt')

