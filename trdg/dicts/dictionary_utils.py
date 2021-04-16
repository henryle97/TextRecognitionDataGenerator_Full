

def get_dictionary_from_file(file_path):
    with  open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
        dictionary = set()
        for line in lines:
            word = line.split(" ")[1]
            dictionary.add(word)

    return dictionary

def save_file(outpath, data):
    """
    save data to the file
    :param outpath:
    :param data: list
    :return:
    """

    with open(outpath, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(line + "\n")


if __name__ == "__main__":
    file_path = "3k_annotation.txt"
    outpath = "./dict_3k.txt"

    dictionary = get_dictionary_from_file(file_path)
    save_file(outpath, dictionary)

