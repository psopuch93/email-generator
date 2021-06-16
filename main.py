from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import functions

PATH = r"C:\Users\sopuch\Desktop\chromedriver\chromedriver.exe"
URL = 'https://nowyprofil.wp.pl/rejestracja/'
driver = webdriver.Chrome(PATH)
time.sleep(5)

driver.get(URL)

# functions

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
password_remainder_question_btn = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/'
                                                               'div[3]/form/div[6]/div/div[3]/div/div/button[1]')

'''To Do
question_selection


#password_remainder_answer_field = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/
div/div[3]/form/div[6]/div/div[4]/input')

#free_account_checkbox = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/'
                                                     'div/div[3]/form/div[6]/div/div[4]/input')

legal_info_all_checkbox =
optional_unclick_checkbox = 

'''

# Filling fields
name = functions.random_name()
lastname = functions.random_lastname()
login = functions.random_login()
password = functions.random_password()

name_field.send_keys(name)
lastname_field.send_keys(lastname)
day_of_birth_field.send_keys(15)
login_field.send_keys(login)
password_field.send_keys(password)
repeat_password_field.send_keys(password)
# password_remainder_answer_field.send_keys('Pizza')



# driver.close()