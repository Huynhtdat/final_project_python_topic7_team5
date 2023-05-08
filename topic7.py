from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# mở form login của instagram
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

# nhập tài khoản mật khẩu vào
username_input = driver.find_element_by_name('username')
username_input.send_keys('tan_dat.gin203')
password_input = driver.find_element_by_name('password')
password_input.send_keys('0812459019')
password_input.submit()
time.sleep(5)

# tạo danh sách tài khaonr để nhắn tin (các tài khoản đã được follow)
usernames = ['tdatt_03', 'n.minhduc_2902', 'nguyettrang.nguyenthi.16']

# biến kiểm tra đã chạy lần đầu tiên hay chưa
first_iteration = True

for user in usernames:
    # tìm tài khoản
    driver.get(f'https://www.instagram.com/{user}/')
    time.sleep(5)

    # click vào message để vào trang nhắn tin
    message_button = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div")
    message_button.click()
    time.sleep(5)

    if first_iteration:
        # tắt thông báo
        message_button = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
        message_button.click()
        time.sleep(3)
        first_iteration = False

    # nhập nội dung tin nhắn
    text_area = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    text_area.send_keys('hello')
    time.sleep(2)

    # click send tin nhắn
    send_button = driver.find_element_by_xpath(
        "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div")
    send_button.click()
    time.sleep(5)

# đóng trình duyệt
driver.quit()
