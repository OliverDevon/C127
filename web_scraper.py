

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

start_url = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome("/chromedriver")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data =[]
    for i in range(0,203):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ultag in soup.find_all("ul",attrs={"class", "exoplanet"}):
            litag=ultag.find_all("li")
            temp_list = []
            for index, litag in enumerate(litag):
                if index==0:
                    temp_list.append(litag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(litag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element(by = By.XPATH,value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper.csv", "w") as f:
        csvwriter = csv.writer(f)
        csv.writerow(headers)
        csv.writerows(planet_data)
scrape()


