from selenium import webdriver
from bs4 import BeautifulSoup
import time
import  csv

browser=webdriver.Chrome('chromedriver.exe')
url='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser.get(url)
time.sleep(10)
planet_data=[]
def scrape():
    headers=['name','light_years_from_earth','planet_mass','stellar_magnitude','discovery_date']
    soup=BeautifulSoup(browser.page_source,"html.parser")
    for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
        li_tags=ul_tag.find_all("li")
        temp_list=[]
        for index,li_tag in enumerate(li_tags):
            if index==0:
               temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
    with open('data.csv','w',newline="") as f:
        writer=csv.writer(f)
        writer.writerow(headers)
        writer.writerows(planet_data)
        
        
            
    
    
scrape()