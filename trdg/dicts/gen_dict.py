import random
import string


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
            leng_phone = [9,10, 12]
            leng_rnd = random.choice(leng_phone)
            id = ''.join(random.choice(string.digits) for _ in range(leng_rnd))

            f.write(id + "\n")
gen_id(200)