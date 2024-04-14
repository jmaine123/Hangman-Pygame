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
        url = f'https://www.50states.com/tools/thelist.htm'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        s = soup.prettify()
        print(s)
        dom = etree.HTML(str(soup))
        states = dom.xpath('//main/descendant::figure/table/tbody/tr/td[1]/span/a/text()')
        capitals = dom.xpath('//main/descendant::figure/table/tbody/tr/td[2]/span/text()')
        
        # countries_dict["Courses"] = countries

        for i, state in enumerate(states):
            # print(state)
            # print(capitals[i])
            full_cap = f'{capitals[i]}, {state}'            
            capitals_dict["Capitals"].append(full_cap)
    
    



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