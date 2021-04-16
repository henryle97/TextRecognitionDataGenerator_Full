import glob
import random
import string
import unicodedata

def gen_email(num_email):
    with open('email.txt', 'w') as f:
        for _ in range(num_email):
            extensions = ['com', 'net', 'org', 'gov']
            domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier']

            winext = extensions[random.randint(0, len(extensions) - 1)]
            windom = domains[random.randint(0, len(domains) - 1)]

            acclen = random.randint(1, 20)

            winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

            finale = winacc + "@" + windom + "." + winext
            f.write(finale + "\n")

# gen_email(200)
def gen_address(num_add=200):
    with open('address.txt', 'w') as f:
        for _ in range(num_add):
            acclen = random.randint(1, 3)
            address = '/'.join(''.join(random.choice(string.digits) for _ in range(random.randint(1, 3)) )for _ in range(1,acclen+2))

            f.write(address+'\n')

def gen_website(num_web=100):
    with open('web.txt', 'w') as f:
        for _ in range(num_web):
            extensions = ['com', 'net', 'org', 'gov']
            prefixes = ['http://www', 'www']
            # domains = ['gmail', 'yahoo', 'comcast', 'verizon', 'charter', 'hotmail', 'outlook', 'frontier']

            winext = extensions[random.randint(0, len(extensions) - 1)]
            # windom = domains[random.randint(0, len(domains) - 1)]
            prefix = prefixes[random.randint(0, len(prefixes) - 1)]

            acclen = random.randint(1, 20)

            winacc = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(acclen))

            finale = prefix + "." +  winacc + "." + winext
            f.write(finale + "\n")

# gen_website(100)

def gen_phonenumber(num_phone):
    with open('phone_number.txt', 'w') as f:
        for _ in range(num_phone):
            prefixes = ['+', '0']
            leng_phone = [8,9,10]

            prefix = prefixes[random.randint(0, len(prefixes) - 1)]
            if prefix == '+':
                prefix_num = random.randint(1, 200)
                prefix = prefix + str(prefix_num)

            leng_rnd = random.choice(leng_phone)
            post_phone_number = ''.join(random.choice(string.digits) for _ in range(leng_rnd))
            full_phone_number = prefix + post_phone_number

            f.write(full_phone_number + "\n")


def gen_id(num_id=300):
    with open('id.txt', 'w') as f:
        for _ in range(num_id):
            leng_phone = [9, 12]
            leng_rnd = random.choice(leng_phone)
            id = ''.join(random.choice(string.digits) for _ in range(leng_rnd))

            f.write(id + "\n")

import json
import tqdm
import random
random.seed(1997)
def load_add_json():
    root_data = "vietnam_dataset/data"
    paths = glob.glob(root_data + "/*")
    print(len(paths))

    thi_tran = ['Thị trấn', 'TT.', 'TT']
    phuong = ['Phường', 'P.', 'P']
    thanhpho = ['Thành phố', 'TP', 'TP.']
    quan = ['Quận', 'Q.', 'Q']
    city_tth = ['Thừa Thiên-Huế', 'T-T-Huế', 'Thừa-Thiên Huế']
    city_hcm = ['Hồ Chí Minh', 'HCM']

    address_full = set()

    with open('address_full.txt', 'w', encoding='utf8') as f_w:
        for path in tqdm.tqdm(paths):
            with open(path, 'r', encoding='utf8') as f:
                print(f)
                try:
                    js = json.load(f)
                except Exception as err:
                    print(err)
                    print(path)
                    continue
                # print(js)
                # print(js.keys())
                city = js['name']
                provines = js['district']
                for provine in provines:
                    provine_name = provine['name']
                    provine_pre = provine['pre']
                    xa_list = provine['ward']
                    street_list = provine['street']
                    # print(street_list)
                    for xa in xa_list:
                        xa_name = xa['name']
                        xa_pre = xa['pre']

                        # f.write()
                        num_rand = random.random()

                        if xa_pre == "Thị trấn":
                            xa_pre = random.choice(thi_tran)
                        if xa_pre == "Phường":
                            xa_pre = random.choice(phuong)
                        if provine_pre == 'Thành phố':
                            provine_pre = random.choice(thanhpho)
                        if provine_pre == 'Quận':
                            provine_pre = random.choice(quan)

                        # full add

                        if city == "Thừa Thiên Huế":
                            if random.random() > 0.8:
                                city == random.choice(city_tth)
                        if city == "Hồ Chí Minh":
                            if random.random() > 0.8:
                                city == "HCM"

                        rand_numb = random.random()
                        add1 = ", ".join([xa_pre + " " + xa_name, provine_pre + " " + provine_name, city])
                        add2 = ", ".join([xa_name, provine_name, city])
                        add3 = ", ".join([provine_name, city])
                        add4 = ", ".join([provine_pre + " " + provine_name, city])
                        add5 = ", ".join([xa_pre + " " + xa_name])
                        add6 = ", ".join([xa_name])
                        adds = [add1, add2, add5, add6]
                        adds_2 = [add3, add4]
                        for add in random.sample(adds, k=3):
                            add = unicodedata.normalize('NFC', add.strip())
                            address_full.add(add)

                        for add in random.sample(adds_2, k=1):
                            add = unicodedata.normalize('NFC', add.strip())
                            address_full.add(add)
                            # f_w.write(add.strip() + "\n")
                    for street in random.sample(street_list, k=min(5, len(street_list))):
                        street = street.strip()
                        if len(street) == 1:
                            continue
                        if len(street) == 2:
                            if random.random() < 0.8:
                                continue
                        street = unicodedata.normalize("NFC", street.strip())
                        address_full.add(street)

        for add in address_full:
            f_w.write(add + "\n")

import re
def clean_data(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    with open(file_path, 'w') as f2:
        for line in lines:
            line = re.sub("[^]")
            f2.write(line + "\n")



if __name__ == "__main__":
    load_add_json()
    # import chardet
    # import io
    # import unicodedata
    # f = io.open("./vietnam_dataset/data/HN.json", 'r', encoding='utf8').read()
    # print(unicodedata.normalize('NFC', f))
