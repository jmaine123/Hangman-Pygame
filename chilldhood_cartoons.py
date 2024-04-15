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


childhood_dict = {"Childhood Cartoons": []}

def contains_number(string):
    for i in list(string):
        if i.isdigit():
            return True
    return False

    

class Scraper:
    def getInfo(self):
        
        for i in range(1,3):
            url = f'https://www.listchallenges.com/100-childhood-tv-shows/list/{i}'
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            s = soup.prettify()
            dom = etree.HTML(str(soup))
            tv_shows = dom.xpath('//div[@class="item-image-wrapper"]/img/@alt')

            for show in tv_shows:
                
                if contains_number(show) == False:
                    childhood_dict["Childhood Cartoons"].append(show)
    
    



def main():
    project = Scraper()
    project.getInfo()
    
    print(childhood_dict)

    # opening file in write mode (binary) 
    file = open("childhood_cartoons.txt", "wb") 
    
    # serializing dictionary  
    pickle.dump(childhood_dict, file)
    
    # closing the file 
    file.close()

if __name__ == "__main__":
    main()