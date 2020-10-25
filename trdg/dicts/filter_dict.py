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

filter("word_dict_all_order_eng_vi.txt", "word_dict_order.txt")