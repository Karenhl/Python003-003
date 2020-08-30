from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get(url="https://movie.douban.com/subject/1292052/")
browser.find_element_by_xpath('//*[@id="hot-comments"]/a').click()

time.sleep(10)
print(browser.page_source)
browser.close()