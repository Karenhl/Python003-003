from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()

    browser.get("https://www.douban.com")
    time.sleep(3)

    browser.switch_to_frame(browser.find_elements_by_tag_name('iframe')[0])
    
    bhtml = browser.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]')
    bhtml.click()
    time.sleep(1)

    browser.find_element_by_xpath('//*[@id="username"]').send_keys('123456')
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
    time.sleep(1)      

    browser.find_element_by_xpath('//a[contains(@class,"btn-account")]').click()

    print(browser.get_cookies())
except Exception as e:
    print(e)
finally:
    browser.close()