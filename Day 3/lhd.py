from selenium import webdriver
from selenium.webdriver.common.by import By
# from db import *
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://mlh.io")

# hacks = get_hackathons("MLH")
# print(hacks)
class MLH:
    def __init__(self,name,start_date,end_date,location,mode,image,url):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.mode = mode
        self.image = image
        self.url = url
        self.website = "MLH"
    
    def __lt__(self,other):
        myname = self.name.upper()
        othername = other.name.upper()
        return myname < othername
        


attend_button = driver.find_element_by_class_name('join-area-btn')
attend_button.click()
driver.switch_to.window(driver.window_handles[0])
hackathons = []
try:
    for l in range(1,27):
        name = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div['+str(l)+']/div/a')
        url = name.get_attribute('href')
        name = name.get_attribute('title')
        start = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div['+str(l)+']/div/a/div/meta[1]')
        start = start.get_attribute('content')
        end = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div['+str(l)+']/div/a/div/meta[2]')
        end = end.get_attribute('content')
        location = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div['+str(l)+']/div/a/div/div[4]/span[2]')
        location = location.get_attribute('innerHTML')
        mode = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div['+str(l)+']/div/a/div/div[1]/div')
        mode = mode.get_attribute('innerHTML')
        mode = mode.strip()
        image = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div['+str(l)+']/div/a/div/div[3]/img')
        image = image.get_attribute('src')
        hack = MLH(name,start,end,location,mode,image,url)
        # print(hack.name)
        # check_hackathon(hack)
        hackathons.append(hack)
except:
    print("All scraped")

hackathons.sort()
for i in hackathons:
    print(i.name+" "+i.location+" "+i.mode+" "+i.start_date+"-"+i.end_date)
driver.quit()