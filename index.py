from selenium import webdriver
import time
import requests
import shutil
import os

user = os.getlogin()
driver = webdriver.Chrome()
directory = './pics/'
input_content = input('Enter what you wanna search: ')
url = 'https://www.google.com/search?q=' + \
    str(input_content)+'&source=lnms&tbm=isch&sa=X&ved=2ahUKEwie44_AnqLpAhUhBWMBHUFGD90Q_AUoAXoECBUQAw&biw=1920&bih=947'
iterate = int(input('Enter how many pictures you want: '))


def save_img(inp, img, i):
    global directory
    print('save image', i, '……')
    try:
        filename = inp+str(i)+'.jpg'
        response = requests.get(img, stream=True)
        image_path = os.path.join(directory, filename)
        with open(image_path, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
    except Exception:
        pass


def find_urls(inp, url, driver, iterate):
    driver.get(url)
    time.sleep(3)
    for j in range(1, iterate+1):
        imgurl = driver.find_element_by_xpath(
            '//div//div//div//div//div//div//div//div//div//div['+str(j)+']//a[1]//div[1]//img[1]')
        print('*'*20, '>', imgurl)
        imgurl.click()
        time.sleep(15)
        img = driver.find_element_by_xpath(
            '//body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
        print('======>', img)
        save_img(inp, img, j)


find_urls(input_content, url, driver, iterate)
