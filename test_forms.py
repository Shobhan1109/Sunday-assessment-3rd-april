import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def setUp2():
    global driver, userid, logpass, name, dob, address, pincode, mobile, email, password, conpassword
    userid = input("Enter the login email id:")
    logpass = input("Enter the login password:")
    name = input("Ente user name:")
    dob = input("Enter your date of birth with - separated:")
    address = input("Enter the address:")
    pincode = input("Enter the pincode:")
    mobile = input("Enter the mobile number:")
    email = input("Enter the email:")
    password = input("Enter the password:")
    conpassword = input("Reenter password:")
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_userdata(setUp2):
    driver.get("https://iprimedtraining.herokuapp.com/training.php")
    driver.find_element_by_name("loginEmail").send_keys(userid)
    time.sleep(1)
    driver.find_element_by_name("loginpass").send_keys(logpass)
    time.sleep(1)
    driver.find_element_by_name("loginbtn").click()
    time.sleep(1)
    driver.find_element_by_name("name").send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[4]").click()
    time.sleep(1)
    driver.find_element_by_name("dob").send_keys(dob)
    time.sleep(1)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(1)
    driver.find_element_by_name("Pincode").send_keys(pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(mobile)
    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("pass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_name("cnfpass").send_keys(conpassword)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[11]/td[2]/div/input").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[12]/td[2]/button").click()
    time.sleep(8)