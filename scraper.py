from selenium import webdriver
import csv
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
# import pandas as pd

import requests
start_time = time.time()

url =   "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"

OK=0
FAILED=-1


fieldnames = ["Institute","Academic Program Name","Quota","Seat Type","Gender","Opening Rank","Closing Rank","year","rounds"]
            
fileName = "jossaDataset.csv"
with open(fileName,'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)



driver = webdriver.Chrome()

def Parsing(url):
    driver.get(url=url)
    years = elementFind('//a[@class="chosen-single"]','//li[@class="active-result"]')
    # driver.quit()
    # time.sleep(0.5)
    # print(range(len(years)),range(len(rounds)))
    for i in range(len(years)):
        # driver.get(url)
        rounds = elementFind('//a[@class="chosen-single"]','//li[@class="active-result"]')
        
        for j in range(len(rounds)):
            # print(f"Status Code {}")
            year = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',i)
            
            rnd =clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',j)
            if rnd==None:break         

            insti_type = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)

            insti_name = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)

            acadProgramm = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)

            category = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)
            
            driver.find_element(By.XPATH,'//input[@type="submit"]').click()
            print(year,rnd)
            time.sleep(1.3)
            dataScraper(year,rnd)
    
            driver.get(url)
            
   
            # driver.set_res


 
def dataScraper(year:str,rnd:int):
    # print("scappring")
    
    
    table = driver.find_elements(By.TAG_NAME,'tr')
    with open(fileName,'a',newline='') as file:
        writer = csv. writer(file)

        for elem in table: 
            if elem.get_attribute('class')=="bg-secondary text-white":
                  continue
   
            text =elem.find_elements(By.TAG_NAME,'td')
            data_list = [data.text for data in text ]
            # print(data_list)
            
            data_list.append(year)
            data_list.append(rnd)
            writer.writerow(data_list)
        
    print(f"For year {year} and round {rnd} done moving on.....")
    # print(print(data.text))
    # while(True):

    # csv.DictWriter()


def clickElement(Locator:str,Locator2:str,index:int):
    temp = driver.find_elements(By.XPATH,Locator)
    # print(temp.text,temp.tag_name)
    

    for item in temp:
        if item.text=='--Select--':   
            item.click()
            # print("clicked")
        # print(item.text)
    
    time.sleep(1)
    try:
        dropdown = driver.find_elements(By.XPATH,Locator2)

        text=dropdown[index].text
        dropdown[index].click()
        # print(text)
        return text
        
    except:
        print("Some error occured for ",index)
        pass
        

def elementFind(locator:str,Locator2:str):
    temp =driver.find_element(By.XPATH,locator)
    # print(temp.text)
    if temp.text == '--Select--':
        temp.click()
    # for x in temp:
    #     if x.text =='--Select--' :
    #         x.click()
    try:
        dropdown = driver.find_elements(By.XPATH,Locator2)
        # for i in dropdown:
        #     print(i.text)
        return dropdown
    except:
        print("Some error occured")
Parsing(url=url)




endtime = time.time()

print("Runtime for the scrapper script ",endtime-start_time)