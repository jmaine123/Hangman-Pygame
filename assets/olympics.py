from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from lxml import etree, html
import time
import requests
import re
import pandas as pd
import requests
import json
import time
from selenium.webdriver.common.by import By
from dataclasses import dataclass, asdict
from tqdm import tqdm
import pickle


olympics_dict = {"Olympic Sports": []}

# def contains_number(string):
#     for i in list(string):
#         if i.isdigit():
#             return True
#     return False

    

class Scraper:
    
    def getInfo(self):       
        url = f'https://www.google.com/search?q=all+olympics+sports&sca_esv=a2f1cf1b706ff5c6&sxsrf=ADLYWIIOn0WUcBgUg6pqgiB2_SGwobrbUw%3A1715530475664&ei=6-pAZtaQKLig5NoP-qOL0Aw&ved=0ahUKEwiWsumEwYiGAxU4EFkFHfrRAsoQ4dUDCBI&uact=5&oq=all+olympics+sports&gs_lp=Egxnd3Mtd2l6LXNlcnAiE2FsbCBvbHltcGljcyBzcG9ydHMyChAjGIAEGCcYigUyBRAAGIAEMgYQABgHGB4yBhAAGAcYHjIFEAAYgAQyBhAAGAgYHjIGEAAYCBgeMgYQABgIGB4yBhAAGAgYHjIGEAAYCBgeSKYJUKcDWKcDcAF4AZABAJgBO6ABO6oBATG4AQPIAQD4AQGYAgKgAkTCAgoQABiwAxjWBBhHmAMAiAYBkAYIkgcBMqAH0Qc&sclient=gws-wiz-serp'
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        print('start')
        driver.get(url)
        r = requests.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        s = soup.prettify()
        print(s)
        dom = etree.HTML(str(soup))
        
        sports = dom.xpath('//div[@data-attrid="Munin"]/text()')
        

        for sport in sports:
            # print(flower)           
            olympics_dict["Olympic Sports"].append(sport)
    
    



def main():
    project = Scraper()
    project.getInfo()
    

    # opening file in write mode (binary) 
    file = open("olympic-sports.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(olympics_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()