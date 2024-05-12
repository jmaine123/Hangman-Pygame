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


periodic_dict = {"Periodic Table": []}

# def contains_number(string):
#     for i in list(string):
#         if i.isdigit():
#             return True
#     return False

    

class Scraper:
    
    def getInfo(self):       
        url = f'https://www.science.co.il/elements/'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        s = soup.prettify()
        print(s)
        dom = etree.HTML(str(soup))
        elements = dom.xpath('//tbody/tr/td[@class="lft"][1]/text()')
        

        for element in elements:
            # print(flower)           
            periodic_dict["Periodic Table"].append(element)
    
    



def main():
    project = Scraper()
    project.getInfo()
    

    # opening file in write mode (binary) 
    file = open("periodic-table.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(periodic_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()