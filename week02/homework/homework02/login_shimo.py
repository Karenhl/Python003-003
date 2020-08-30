from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("https://shimo.im/login?from=home")
    user = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')
    user.send_keys('1234@qq.com')
    time.sleep(1)

    password = browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')
    password.send_keys('1234')
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()
    time.sleep(10)
except Exception as e:
    print(e)
finally:
    browser.close()
