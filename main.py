from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import functions

PATH = r"C:\Users\sopuch\Desktop\chromedriver\chromedriver.exe"
URL = 'https://nowyprofil.wp.pl/rejestracja/'
driver = webdriver.Chrome(PATH)
time.sleep(5)

driver.get(URL)


name_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/'
                                          'div[3]/form/div[1]/div[1]/div/input')
lastname_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/'
                                              'div/div[3]/form/div[1]/div[2]/div/input')
'''To Do
kobieta_chechbox =
mezczyzna_checbox =
'''
day_of_birth_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/'
                                            'div[3]/form/div[3]/fieldset/div/div[1]/input')


'''To Do
month_of_birth_list =
year_of_birth_list = 
'''

login_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/'
                                           'div[3]/form/div[4]/div/div[1]/div[1]/input')
password_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/'
                                              'div[3]/form/div[5]/div/div[1]/div[1]/input')
repeat_password_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[3]/'
                                                     'form/div[5]/div/div[2]/div/input')
'''password_remainder_question_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/'
                                                               'div[2]/div/div[3]/form/div[6]/div/div[3]/'
                                                               'div/div/button[2]').click()'''

password_remainder_question_btn = driver.find_element_by_xpath("//*[contains(text(),'Pytanie pomocnicze')]").click()


select = Select(driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/'
                                             'div/div[3]/form/div[6]/div/div[4]/div/div/select'))
select.select_by_value('q7')

password_remainder_question_dropdown = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/'
                                                                    'div/div[3]/form/div[6]/div/'
                                                                    'div[4]/div/div/select')
password_remainder_answer = driver.find_element_by_xpath('/html/body/div[2]/div/'
                                                         'div/div[2]/div/div[3]/form/div[6]/div/div[4]/div/div/select')

account_type_rb = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div[3]/'
                                               'form/div[7]/div[1]/fieldset/div[2]/div[1]/div/input')
account_type_rb.click()

free_account_policy = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/'
                                                   'div/div[3]/form/div[7]/div[2]/div[1]/label').click()

free_account_policy_unclick = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/'
                                                           'div[3]/form/div[7]/div[2]/div[6]/label').click()



password_remainder_answer = driver.find_element_by_xpath('/html/body/div[2]/div/div/'
                                                         'div[2]/div/div[3]/form/div[6]/div/div[4]/input')


# Filling fields by functions return value
name = functions.random_name()
lastname = functions.random_lastname()
login = functions.random_login()
login_list = functions.login_list(login)
password = functions.random_password()
password_list = functions.password_list(password)
gender = functions.random_gender()
validator = functions.login_password_validator(password, login)
DAY_OF_BIRTH = functions.random_birth_day()
MONTH_OF_BIRTH = functions.random_birth_month()
YEAR_OF_BIRTH = functions.random_birth_year()

print(f"Name: {name}\n"
      f"Lastname: {lastname}\n"
      f"Login: {login}\n"
      f"Login list: {login_list}\n"
      f"Password: {password}\n"
      f"Password list: {password_list}\n"
      f"Gender: {gender}\n"
      f"Validator: {validator}\n")

name_field.send_keys(name)
lastname_field.send_keys(lastname)
day_of_birth_field.send_keys(DAY_OF_BIRTH)
login_field.send_keys(login)
password_field.send_keys(password)
repeat_password_field.send_keys(password)
password_remainder_answer.send_keys('Pizza')



# driver.close()