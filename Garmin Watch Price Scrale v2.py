from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



checkList = ['https://www.amazon.com/Garmin-Forerunner-Smartwatch-Advanced-Dynamics/dp/B07QLVHBLF/ref=sr_1_3?crid=RJQSG97487W5&dchild=1&keywords=garmin+245+music&qid=1588790490&sprefix=garmin+245%2Caps%2C175&sr=8-3',
            'https://buy.garmin.com/en-US/US/p/646690/pn/010-02120-21',
             'https://www.bestbuy.com/site/garmin-forerunner-245-music-gps-heart-rate-monitor-running-smartwatch-black/6348787.p?skuId=6348787']


options = webdriver.ChromeOptions()

# NB. when v8 stable is released you can use with 'com.sec.android.app.sbrowser'
options.add_experimental_option('androidPackage', 'com.sec.android.app.sbrowser')
options.add_experimental_option('androidActivity', 'com.sec.android.app.sbrowser.SBrowserMainActivity')
options.add_experimental_option('androidDeviceSocket', 'Terrace_devtools_remote')
options.add_experimental_option('androidExecName', 'Terrace')


driverpath = './chromedriver' #replace if chromedriver is in a different folder 
driver = webdriver.Chrome(driverpath)

price_list = {}


def getAmazonPrice(url):
    driver.get(url)
    price_bl = driver.find_element_by_id("priceblock_ourprice")
    price_list["Amazon_Black"] = price_bl.text
    print("Amazon Prices: \n" + "Black Garmin 245 Music: " + price_bl.text)
    #---------Navigate to white watch site and get price for white:
    driver.find_element_by_id("color_name_1").click()
        #wait for page to load with price info
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "priceblock_ourprice"))
    )
    except:
        print("Timeout")
    driver.implicitly_wait(10)
    price_wht = driver.find_element_by_id("priceblock_saleprice")
    print("White Garmin 245 Music :" + price_wht.text)
    price_list["Amazon_White"] = price_wht.text
    #----------Navigate to blue watch site and get price for blue watch:
    driver.find_element_by_id("color_name_2").click()
        #wait for page to load with price info
    try:
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "priceblock_saleprice"))
    )
    except:
        print("Timeout")
    #driver.implicitly_wait(10)
    price_blu = driver.find_element_by_id("priceblock_saleprice")
    price_list["Amazon_Blue"] = price_blu.text
    print("Blue Garmin 245 Music: " + price_blu.text)
    return


def getGarminPrice(url):
    page = requests.get(url)
    html = page.text
    bsObj = BeautifulSoup(html,'html.parser')
    Garminprice = bsObj.find(id="js__product__price__main").find("span", {"class":"amount"}).get_text()
    print("Garmin website:\n"+"Black: "+Garminprice)
    price_list["Garmin_Black"] = Garminprice
    return


def getBestBuyPrice(url):
    driver.get(url)
    BB_blk_price = driver.find_element_by_xpath("//div[@class = 'priceView-hero-price priceView-customer-price']/span[1]")
    price_list["BestBuy_Black"] = BB_blk_price.text
    print("Best Buy Prices: \n" + "Black Garmin 245 Music : " + BB_blk_price.text)

    # ---------Navigate to blue watch site and get price for blue:
    driver.find_element_by_xpath(
        "//a[@href = 'https://www.bestbuy.com/site/garmin-forerunner-245-music-gps-heart-rate-monitor-running-smartwatch-aqua/6348791.p?skuId=6348791']").click()
    # wait for page to load with price info
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class = 'priceView-hero-price priceView-customer-price']/span[1]"))
        )
    except:
        print("Timeout")
    BB_blu_price = driver.find_element_by_xpath(
        "//div[@class = 'priceView-hero-price priceView-customer-price']/span[1]")
    price_list["BestBuy_Blue"] = BB_blu_price.text
    print("Blue Garmin 245 Music :" + BB_blu_price.text)

    # ---------Navigate to white watch site and get price for white:
    driver.find_element_by_class_name("ficon-caret-right").click()
    driver.implicitly_wait(2)
    driver.find_element_by_xpath(
        "//a[@href = 'https://www.bestbuy.com/site/garmin-forerunner-245-music-gps-heart-rate-monitor-running-smartwatch-white/6348788.p?skuId=6348788']").click()
    # wait for page to load with price info
    '''try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class = 'priceView-hero-price priceView-customer-price']/span[1]"))
        )
    except:
        print("Timeout")'''
    driver.implicitly_wait(5)
    BB_wht_price = driver.find_element_by_xpath(
        "//div[@class = 'priceView-hero-price priceView-customer-price']/span[1]")
    print("White Garmin 245 Music :" + BB_wht_price.text)
    price_list["BestBuy_White"] = BB_wht_price.text
    return


getAmazonPrice(checkList[0])
getGarminPrice(checkList[1])
getBestBuyPrice(checkList[2])
print(price_list)
driver.quit()
