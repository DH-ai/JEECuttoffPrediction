from selenium import webdriver
import csv
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
# import pandas as pd
# from selenium.webdriver.remote.webelement import WebElement
import requests
start_time = time.time()
print("Started ...... ")
url =   "https://josaa.admissions.nic.in/applicant/seatmatrix/openingclosingrankarchieve.aspx"




fieldnames = ["Institute","Academic Program Name","Quota","Seat Type","Gender","Opening Rank","Closing Rank","year","rounds"]
            
fileName = "jossaDataset2.csv"
with open(fileName,'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)



driver = webdriver.Chrome()

def Parsing(url):
    driver.get(url=url)
    years = elementFind('//a[@class="chosen-single"]','//li[@class="active-result"]')
    # driver.quit()
    time.sleep(0.5)
    
    # print(range(len(years)),range(len(rounds)))
    p=0
    for i in range(len(years)):
        # rounds =driver.find_element(locate_with(By.XPATH,locator1).to_right_of(By.XPATH,'(//div[@class="row mb-3"])[2]//label')).click()
        
        rounds= [6,6,6,6,7,7,7,6]
        
        
        for j in range(rounds[p]):
         
            # print(f"Status Code {}")
            
            
            year = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',i)
            rnd =clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',j)
            print(year,rnd)

            insti_type = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)
            insti_name = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)
            acadProgramm = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)
            category = clickElement('//a[@class="chosen-single"]','//li[@class="active-result"]',0)
            driver.find_element(By.XPATH,'//input[@type="submit"]').click()
           
            
            
            dataScraper(year,rnd)
            driver.get(url)
    
        p+=1
   
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
        
    print(f"For year {year} and round {rnd} done at {int((time.time()-start_time )//60)} minutes passed moving on.....")



def clickElement(Locator:str,Locator2:str,index:int):
    temp = driver.find_elements(By.XPATH,Locator)
    # print(temp.text,temp.tag_name)
    
    
    # time.sleep(1.4)
    for item in temp:
        if item.text=='--Select--':   
            item.click()

    try:
        
        
        dropdown = driver.find_elements(By.XPATH,Locator2)

        text=dropdown[index].text
        
        
        dropdown[index].click()
        return text
    except:
        print("Some error occured at ",index)
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
         
        temp.click()     
        return dropdown
    except:
        print("Some error occured")
Parsing(url=url)



endtime = time.time()

print("Runtime for the scrapper script : ",(endtime-start_time)//60)