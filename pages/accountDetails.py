import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from pages.useful_functions import new_tab, switch_to


class AccountDetail:

    def __init__(self):
        self.path = 'driver/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.path)
        self._firstname = None
        self._fatherName = None
        self._lastname = None
        self._sex = None
        self._ssn = None
        self._phone_num = None
        self._parent_phone_num = None

    def _generate_names(self):
        print("Generating names......")
        baseURL = 'https://www.randomlists.com/fake-name-generator'

        self.driver.get(baseURL)

        data = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'Rand-stage')))

        list_of_names = data.find_elements_by_tag_name('li')
        num_of_names = len(list_of_names)
        index = random.choice(range(1, num_of_names))
        name = list_of_names[index].text.strip()

        index = random.choice(range(1, num_of_names))

        self._fatherName = list_of_names[index].text.strip().split()[0]
        self._firstname = name.split()[0]
        self._lastname = name.split()[1]
        self._sex = random.choice(['M', 'F'])

    def _generate_ssn(self):
        print("Generating SSN....")
        baseURL = 'https://www.ssn-verify.com/generate'

        state_control_ID = 'state'
        year_control_ID = 'year'
        btn_submit_ID = 'ssn-submit'
        result_ssn_CLASS_NAME = 'result-ssn'

        new_tab(self.driver, baseURL)
        switch_to(self.driver, 'generate')

        self.set_select(state_control_ID, "california")

        self.set_select(year_control_ID, "1997")

        self._click_button_by_ID(btn_submit_ID)

        time.sleep(3)

        ssn_number = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, result_ssn_CLASS_NAME))).text

        self._ssn = ssn_number

    def _generate_phone_number(self):
        print("Generating phone numbers....")

        baseURL = 'https://www.fakephonenumber.org/UnitedStates/phone_number_generator?state=CA'

        new_tab(self.driver, baseURL)
        switch_to(self.driver, 'fakephonenumber')

        self._phone_num = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/ul[1]/li[1]/p[1]/a'))).text
        self._parent_phone_num = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div/div[2]/div[3]/div/ul[1]/li[2]/p[1]/a'))).text

    def getInfo(self):
        info = {}
        self._generate_names()
        self._generate_ssn()
        self._generate_phone_number()
        print("Done!")
        info["firstname"] = self._firstname
        info["lastname"] = self._lastname
        info["sex"] = self._sex
        info["ssn"] = self._ssn
        info["fathername"] = self._fatherName
        info["phone_num"] = self._phone_num
        info["parent_phone"] = self._parent_phone_num

        self.driver.quit()
        return info

    def _click_button_by_ID(self, button_ID):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, button_ID))).click()

    def set_select(self, select_ID, value):
        box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, select_ID)))

        option = Select(box)
        option.select_by_value(value)
