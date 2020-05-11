import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from pages.useful_functions import clear_text_box, username_generator, password_Generator, \
    random_four_digit_PIN


class Costa:

    def __init__(self, info, email):
        self.path = 'driver/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.baseURL = 'http://www.orangecoastcollege.edu/Pages/home.aspx'
        self.driver.get(self.baseURL)



        self.firstname = info.get("firstname")
        self.lastname = info.get("lastname")
        self.ssn_number = info.get("ssn")
        self.phone_num = info.get("phone_num")
        self.alter_phone = info.get("parent_phone")
        self.emailid = email
        self.sex = info.get("sex")

        #change if you want
        #############################
        self.birth_month = "3"
        self.birth_day = "24"
        self.birth_year = "1997"
        self.street_address = '2701 Fairview Rd'
        self.city = 'Costa Mesa'
        self.state = 'CA'
        self.zipcode = '92626'
        ##########################

        self.username = None
        self.password = password_Generator(15)
        self.PIN = random_four_digit_PIN()
        self.security_question_1 = 'Where did your parents meet?'
        self.answer_1 = 'in Parallel universe'
        self.security_question_2 = 'What was the make and model of your first car?'
        self.answer_2 = 'Toyota Toy Car'
        self.security_question_3 = 'In what city or town was your first job?'
        self.answer_3 = 'Handjob city'

        self.cccid = None

    #########____main_____###########
    def start_process(self):
        self.find_apply_button()
        self.openccc_apply_page_1()
        self.openccc_apply_page_2()
        self.openccc_apply_page_3()
        self.account_created_page()

        self.collegeApplication()
        self.save_info()

    def openccc_apply_page_1(self):
        self._click_by_link_text('Create an Account')
        self._click_button_by_ID('accountFormSubmit')

        # name stuff.....
        self._set_input_by_id('inputFirstName', self.firstname)
        self._click_button_by_ID('inputHasNoMiddleName')
        self._set_input_by_id('inputLastName', self.lastname)
        self._click_button_by_ID('hasOtherNameNo')
        self._click_button_by_ID('hasPreferredNameNo')

        # DOB stuff....
        self.set_date_box(self.birth_month, self.birth_day, None, 'inputBirthDateMonth', 'inputBirthDateDay', None)
        self._set_input_by_id('inputBirthDateYear', self.birth_year)
        self.set_date_box(self.birth_month, self.birth_day, None, 'inputBirthDateMonthConfirm',
                          'inputBirthDateDayConfirm', None)
        self._set_input_by_id('inputBirthDateYearConfirm', self.birth_year)

        # SSN stuff...

        self._click_button_by_ID('inputSSNTypeSSN')
        self._set_input_by_id('inputSsn', self.ssn_number)
        self._set_input_by_id('inputSsnConfirm', self.ssn_number)
        self.click_continue_button()

    def openccc_apply_page_2(self):
        # Email_stuff....
        self._set_input_by_id('inputEmail', self.emailid)
        self._set_input_by_id('inputEmailConfirm', self.emailid)

        # Telephone stuff....

        self._set_input_by_id('inputSmsPhone', self.phone_num)
        self._set_input_by_id('inputAlternatePhone', self.alter_phone)

        # address stuff....
        time.sleep(2)
        self._set_input_by_id('inputStreetAddress1',self.street_address)
        self._set_input_by_id('inputCity', self.city)
        self.set_select('inputState', self.state)
        self._set_input_by_id('inputPostalCode', self.zipcode)
        time.sleep(1)
        self.click_continue_button()

    def openccc_apply_page_3(self):
        # username_password stuff....

        username_error_flag = True
        while username_error_flag:
            try:
                self.username = username_generator(8)
                self._set_input_by_id('inputUserId', self.username)
                error = WebDriverWait(self.driver, 40).until(
                    EC.presence_of_element_located((By.ID, 'userIdStatus'))
                ).text
                username_error_flag = False
            except NoSuchElementException:
                username_error_flag = True

        self._set_input_by_id('inputPasswd', self.password)
        self._set_input_by_id('inputPasswdConfirm', self.password)

        # security_pin stuff...

        self._set_input_by_id('inputPin', self.PIN)
        self._set_input_by_id('inputPinConfirm', self.PIN)

        # security_Questions_stuff...

        self.set_select('inputSecurityQuestion1', "1")
        self._set_input_by_id('inputSecurityAnswer1', self.answer_1)

        self.set_select('inputSecurityQuestion2', "2")
        self._set_input_by_id('inputSecurityAnswer2', self.answer_2)

        self.set_select('inputSecurityQuestion3', "16")
        self._set_input_by_id('inputSecurityAnswer3', self.answer_3)

        # captcha_stuff
        self.solve_captha()
        self.click_continue_button()

    def solve_captha(self):
        os.system('cls')
        time.sleep(1)
        print("Psstt.. I'm not smart enough to solve CAPTCHA by myself :(")
        time.sleep(2)
        print('need your Intelligence')
        time.sleep(2)
        print('Please solve captcha for me ^^')
        time.sleep(2)
        is_solved = 'n'
        while is_solved != 'y':
            is_solved = input("Have you solved CAPTCHA (y/n) ? : ").lower()
            if is_solved != 'y':
                print("Okay solve i'm waiting....")
                time.sleep(12)
        time.sleep(1)
        print("Sshheeww.. Thank you!.. owe you EDU mail :D")

    def account_created_page(self):
        waiting = True
        while waiting:
            try:
                cccid = WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.ccc-id'))
                ).text
                self.cccid = cccid
                waiting = False
            except NoSuchElementException:
                waiting = True
        self._click_button_by_XPATH('//*[@id="registrationSuccess"]/button')

    def click_continue_button(self):
        self._click_button_by_ID('accountFormSubmit')

    def find_apply_button(self):
        try:
            self._click_by_link_text('Apply Now')
        except NoSuchElementException:
            self._click_by_link_text('APPLY')



    ##################################################################
    ############### college Application page #########################

    # MAIN DRIVER
    def collegeApplication(self):
        self.waiting_for_application_page()
        self.enrollment()
        self.currentMailingAddress_page()
        self.education_page()
        self.citizenship_page()
        self.residency_page()
        self.needs_interests_page()
        self.demographic_page()
        self.supplemental_question_page()
        self.submission_page()
        self.confimation_page()
        self.application_survey_page()
        self.click_submit_and_finish()
        self.logout()


    # FUNCTIONS USED IN COLLEGE-APPLICATION
    ################################################
    def waiting_for_application_page(self):
        print("You must be tired by solving CAPTCHA")
        print("Now you just relax....")
        waiting = True
        while waiting:
            try:
                print("Filling college application form for you ....")
                title = WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'view-title'))
                ).text
                if title == 'College Application':
                    waiting = False
            except NoSuchElementException:
                waiting = True

    def enrollment(self):
        time.sleep(5)
        self.set_select('inputTermId', 'CAP_3975')
        self.set_select('inputEduGoal', 'O')
        self.set_select('inputMajorId', 'CAP_27262')
        time.sleep(5)
        self._click_App_continue()

    def currentMailingAddress_page(self):
       self._click_button_by_ID('inputAddressSame')
       self._click_App_continue()

    def education_page(self):
        #College Enrollment Status
        self.set_select('inputEnrollmentStatus', '1')

        #High School Education
        self.set_select('inputHsEduLevel', '4')
        time.sleep(2)
        self.set_date_box("5","14",None,"inputHsCompMM","inputHsCompDD",None)
        self._set_input_by_id('inputHsCompYYYY',"2015")

        self._click_button_by_ID('inputCaHsGradNo')
        self._click_button_by_ID('inputCaHs3yearNo')
        self._click_button_by_ID('inputHsAttendance3')

        #High School Transcript Information
        self._set_input_by_id('inputGPA', '3.72')
        self.set_select('inputHighestEnglishCourse','1')
        time.sleep(1.5)
        self.set_select('inputHighestEnglishGrade','B+')
        self.set_select('inputHighestMathCourseTaken','12')
        time.sleep(1.5)
        self.set_select('inputHighestMathTakenGrade','A-')


        self._click_App_continue()

    def citizenship_page(self):
        self.set_select('inputCitizenshipStatus', '1')
        self.set_select('inputMilitaryStatus', 'B')
        self._click_App_continue()

    def residency_page(self):
        #California Residence
        self._click_button_by_ID('inputCaRes2YearsYes')

        #Out-of-State Activities
        self._click_button_by_ID('inputCaOutsideTax')
        time.sleep(2)
        self._set_input_by_id('inputCaOutsideTaxYear','2019')

        #Special Residency Categories
        self._click_button_by_ID('inputCaCollegeEmpNo')
        self._click_button_by_ID('inputCaSchoolEmpNo')
        self._click_button_by_ID('inputCaSeasonalAgNo')
        self._click_button_by_ID('inputHomelessYouthNo')
        self._click_button_by_ID('inputIsEverInFosterCareNo')


        self._click_App_continue()

    def needs_interests_page(self):
        # main language
        self._click_button_by_ID('inputEnglishYes')

        # financial_assitance..stuff
        self._click_button_by_ID('inputFinAidInfoYes')
        self._click_button_by_ID('inputAssistanceYes')

        # atheletic_intereset stuff..
        self._click_button_by_ID('inputAthleticInterest1')

        # program_and service stuff...
        self._click_button_by_ID('inputCounseling')
        self._click_button_by_ID('inputEOPS')
        self._click_button_by_ID('inputHealthServices')
        self._click_button_by_ID('inputEmploymentAssistance')
        self._click_button_by_ID('inputVeteranServices')


        self._click_App_continue()

    def demographic_page(self):
        if self.sex == "M":
            value = "Male"
        else:
            value = "Female"

        self.set_select('inputGender', value)
        self.set_select('inputTransgender', 'No')
        self.set_select('inputOrientation', 'StraightHetrosexual')

        # parent education
        self.set_select('inputParentGuardianEdu1', '7')
        self.set_select('inputParentGuardianEdu2', '2')

        # race/Ethnicity
        self._click_button_by_ID('inputHispanicNo')

        self._click_button_by_ID('inputRaceEthnicity300')
        time.sleep(2)
        self._click_button_by_ID('inputRaceEthnicity302')


        self._click_App_continue()

    def supplemental_question_page(self):
        #birthplace
        self._set_input_by_id('_supp_TEXT_1', self.city)
        self.set_select('_supp_STATE_1',self.state)

        #Prior Enrollment
        self._click_button_by_ID('YESNO_2_no')
        self._click_button_by_ID('YESNO_3_no')

        #High School Students Only
        self.set_select('_supp_MENU_1','09')

        if self.sex == "F":
            self._click_button_by_ID('_supp_CHECK_1')
            self._click_button_by_ID('_supp_CHECK_2')
        else:
            self._click_button_by_ID('_supp_CHECK_23')
            self._click_button_by_ID('_supp_CHECK_24')
            self._click_button_by_ID('_supp_CHECK_39')

        self._click_App_continue()

    def submission_page(self):
        self._click_button_by_ID('inputConsentYes')
        self._click_button_by_ID('inputESignature')
        self._click_button_by_ID('inputFinancialAidAck')
        self._click_button_by_ID('submit-application-button')

    def confimation_page(self):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.NAME, '_eventId_finish'))
        ).click()

    def application_survey_page(self):
        self._click_button_by_ID('inputEnglishVerySatisfied')
        self._click_button_by_ID('RecommendYes')

        text_area = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'inputComments'))
        )
        text_area.send_keys("Thank you very much for making our life Easier!!")

        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.NAME, '_eventId_submit'))
        ).click()

    def click_submit_and_finish(self):
        time.sleep(2)
        self._click_button_by_XPATH("//button[contains(.,'Sign Out & Finish')]")

    def _click_App_continue(self):
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.NAME, '_eventId_continue'))
        ).click()
        time.sleep(1)


    ################################################################################################
    #                                                                                              #
    #                                   useful function                                            #
    #                                                                                              #
    #################################################################################################

    #for selecting date works only if...select and options are availble!
    def set_date_box(self, month=None, day=None, year=None, month_id=None, day_id=None, year_id=None):

        if month_id != None:
            select_month_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, month_id)))
            select_month = Select(select_month_box)
            select_month.select_by_value(month)

        if day_id != None:
            select_day_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, day_id)))
            select_day = Select(select_day_box)
            select_day.select_by_value(day)

        if year_id != None:
            select_year_box = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.ID, year_id)))
            select_year = Select(select_year_box)
            select_year.select_by_value(year)

    def _click_button_by_XPATH(self, button_XPATH):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, button_XPATH))).click()

    def _click_button_by_ID(self, button_ID):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, button_ID))).click()

    def _set_input_by_id(self, input_box_id, input_value):
        input_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, input_box_id))
        )
        clear_text_box(input_box)
        input_box.send_keys(input_value)

    def _set_input_by_XPATH(self, input_box_XPATH, input_value):
        input_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, input_box_XPATH))
        )
        clear_text_box(input_box)
        input_box.send_keys(input_value)

    def _click_by_link_text(self, text):
        WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.LINK_TEXT, text))
        ).click()

    def set_select(self, select_ID, value):
        box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, select_ID)))

        option = Select(box)
        option.select_by_value(value)

    def set_select_by_class(self, class_name, value):
        box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name)))

        option = Select(box)
        option.select_by_value(value)

    #################################################################################################
    def save_info(self):
        print("======================")
        print("{}".format(self.cccid))
        print("PIN number ==> {}".format(self.PIN))
        print("emailID ==> {}".format(self.emailid))
        print("Password ==> {}".format(self.password))
        print("=========================")
        print("all info are saved!")

        with open("accountinfo.txt",'a') as txtFile:
            txtFile.writelines("===================================================\n")
            txtFile.writelines("{}\n".format(self.cccid))
            txtFile.writelines("PIN number ==> {}\n".format(self.PIN))
            txtFile.writelines("emailID ==> {}\n".format(self.emailid))
            txtFile.writelines("Password ==> {}\n".format(self.password))
            txtFile.writelines("SSN-Number ==> {}\n".format(self.ssn_number))
            txtFile.writelines("Phone_number ==> {}\n".format(self.phone_num))
            txtFile.writelines("Security Questions\n")
            txtFile.writelines("Q.1> {}\n".format(self.security_question_1))
            txtFile.writelines("A.1> {}\n".format(self.answer_1))
            txtFile.writelines("Q.2> {}\n".format(self.security_question_2))
            txtFile.writelines("A.2> {}\n".format(self.answer_2))
            txtFile.writelines("Q.3> {}\n".format(self.security_question_3))
            txtFile.writelines("A.3> {}\n".format(self.answer_3))
            txtFile.writelines("===================================================\n")

    def logout(self):
        WebDriverWait(self.driver, 40).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Return'))).click()
