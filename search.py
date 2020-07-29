import webbrowser
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC;

driver = webdriver.Chrome(r"C:\Users\nafi.DESKTOP-Q4U6HNF\Desktop\chromedriver.exe");
print("what do you want to search")
print("--------------------------")
y=input()
driver.get("https://www.youtube.com")
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input"))).send_keys(y)
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon"))).click()
WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow"))).click()
print("--------------------------")
print("what do you want to search next")
print("--------------------------")
z=input()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input"))).clear()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input"))).send_keys(z)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button/yt-icon"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-img-shadow"))).click()
print("bye, thanks for using me	!! ;)")

