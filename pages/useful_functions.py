import os
import random
import secrets
import string
import time

from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.common.keys import Keys


def new_tab(driver, url):
    driver.execute_script('''window.open("{}","_blank");'''.format(url))


def clear():
    return os.system('cls')


def random_four_digit_PIN():
    return random.choice(range(1000, 10000))


def clear_text_box(elem):
    time.sleep(2)
    while elem.get_attribute('value') != '':
        elem.send_keys(Keys.BACKSPACE)


def random_day():
    return random.choice(range(1, 31))


def random_month():
    return random.choice(range(1, 13))


def grab_username_from_email(email):
    return email.split('@')[0]


def random_name(stringlength):
    lettersAndDigits = string.ascii_letters
    return ''.join(secrets.choice(lettersAndDigits) for i in range(stringlength)).lower().title()


def username_generator(stringlength):
    # Generate a random string of letters and digits
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(secrets.choice(lettersAndDigits) for i in range(stringlength)).lower()


def password_Generator(stringlength):
    letter_digit_symbol = string.ascii_letters + string.digits * 2
    letter_digit_symbol = ''.join(random.sample(letter_digit_symbol, len(letter_digit_symbol)))
    return ''.join(secrets.choice(letter_digit_symbol) for i in range(stringlength))


def dot_trick(username):
    emails = list()

    username_length = len(username)
    combinations = pow(2, username_length - 1)

    padding = "{0:0" + str(username_length - 1) + "b}"
    with open('gmail_id.txt', 'w') as txtfile:
        txtfile.write(username + '\n')
        for i in range(0, combinations):
            bin = padding.format(i)
            full_email = ""

            for j in range(0, username_length - 1):
                full_email += (username[j])
                if bin[j] == "1":
                    full_email += "."
            full_email += (username[j + 1])
            res = full_email + "@gmail.com\n"
            txtfile.writelines(res)
            emails.append(res)
    return emails


# with open('gmail_id.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(username)


def generate_mail(username):
    total_generated_id = pow(2, len(username) - 1)
    random_number = secrets.choice(range(1, total_generated_id))
    new_email_ids = []
    # username = 'vicky0x07'
    try:
        with open('gmail_id.txt', 'r') as readfile:
            email_ids = readfile.readlines()
            if email_ids[0].strip() == username:
                print('No need to generate...already have file')
                return email_ids[random_number].rstrip()
            else:
                print("Generating new email_ids")
                new_email_ids = dot_trick(username)
                return new_email_ids[random_number].rstrip()
    except FileNotFoundError:
        new_email_ids = dot_trick(username)
        return new_email_ids[random_number].rstrip()


def get_tabs_info(driver):
    handles = driver.window_handles
    dict_tabs_handle = {}

    for handle in handles:
        driver.switch_to.window(handle)
        dict_tabs_handle[driver.current_url.split('//')[1].lower()] = handle

    return dict_tabs_handle


def switch_to(driver, title_or_url):
    opened_tabs = get_tabs_info(driver)
    handle = [v for k, v in opened_tabs.items() if title_or_url in k].pop()
    time.sleep(2)

    try:
        print("Trying to switch to {}".format(title_or_url))
        driver.switch_to.window(handle)
    except InvalidArgumentException:
        print("please check there is no such title named '{}'".format(title_or_url))
        print("Currently opened tabs are {}".format(opened_tabs.keys()))
        print(opened_tabs)
