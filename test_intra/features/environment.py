from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
def before_all(context):
    context.serv = Service()
    context.driver = webdriver.Chrome(service=context.serv)
    context.driver.get("https://profile.intra.42.fr")
    context.driver.find_element(By.ID, "user_login").send_keys("vduchi")
    context.driver.find_element(By.ID, "user_password").send_keys("Valerio.58472")
    context.driver.find_element(By.NAME, "commit").click()

def after_all(context):
    context.driver.quit()