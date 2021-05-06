from time import sleep, time
from glob import glob
from multiprocessing import Pool
from itertools import repeat
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.interactions.Actions
import os

def search_iphone():
    webdriver driver = new FirefoxDriver()
    drive.get("http://www.flipkart.com")
    driver.manage().window().maximize()
    driver.manage().timeout(10)
    Actions f = new Actions(driver)
    WebElement mainmenu= driver.findElement(By.xpath("//*[@id='fk-mainhead-id']/div[2]/div/div[1]/ul/li[1]/a"))
    act.moveToElement(mainmenu).build().perform()
    WebElement mobiles = driver.findElement(By.xpath("//*[@id='menu-electronics-tab-0-content']/ul[1]/li[1]/a"))
    mobiles.click()
    Phones = driver.findElements(By.xpath("//div[@id='list-tagcloud']/div[2]/a"))
    print (Phones.size())
    i=0
    for(i in i<Phones.size,i+):
        print(Phones.get(i).getText())
        if(Phones.get(i).getText().equals("iPhone"):
            Phones.get(i).click()
    WebElement searchbox = driver.findElement(By.xpath("//*[@id='searchbox']/li[2]/form/input[4]"))
    searchbox.sendKeys("XR");//in search box search for XR
    driver.findElement(By.xpath("//*[@id='searchbox']/li[2]/form/input[5]")).click();
    print("total Amount =="+data.size())
    for(i in data.size(), i+):
        print(data.get(i).getText())
    if(data.get(i).getText().contains("XR")):
        String link = data.get(i).getAttribute("href")
        alllink.add(link)))
        print(alllink.size())
        for(i in i<alllink.size()i+):
            print(alllink.get(i))
            driver.get(alllink.get(i))
            info = driver.findElements(By.xpath("//div[@class='cart-table']/div[starts-with(@class,'line seller-item')]/div[4]/a"))
                print(info.size())
            for (j=0 j<info.size(),j+):
                print(info.get(j).getText())

driver.close()




