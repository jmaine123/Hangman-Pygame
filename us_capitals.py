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


capitals_dict = {"Capitals": []}

# def contains_number(string):
#     for i in list(string):
#         if i.isdigit():
#             return True
#     return False

    

class Scraper:
    
    def getInfo(self):       
        url = f'https://ballotpedia.org/List_of_capitals_in_the_United_States'
        driver = webdriver.Chrome()
        driver.implicitly_wait(20)
        print('start')
        driver.get(url)
        r = requests.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        s = soup.prettify()
        print(s)
        dom = etree.HTML(str(soup))
        # states = dom.xpath('//main/descendant::figure/table/tbody/tr/td[1]/span/a/text()')
        # capitals = dom.xpath('//main/descendant::figure/table/tbody/tr/td[2]/span/text()')
        
        capitals = dom.xpath('//div[@class="scrollable-table-container"]/table/tbody/tr/td/b/a/text()')
        # print(len(states))
        # print(len(capitals))
        
        # countries_dict["Courses"] = countries

        for i, capital in enumerate(capitals):
            # print(state)
            # print(capitals[i])
            # full_cap = f'{capitals[i]}, {state}'            
            capitals_dict["Capitals"].append(capital)
    
    



def main():
    project = Scraper()
    project.getInfo()
    
    print(capitals_dict)

    # opening file in write mode (binary) 
    file = open("capitals.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(capitals_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()