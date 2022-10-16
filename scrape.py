from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import json



class Scraper():

    def scrape(self,username):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        url = f"https://www.tiktok.com/@{username}?lang=en"


        userData = []
        userVideoData = []

        driver.get(url)
        # Get username 
        username = driver.find_element(By.CLASS_NAME, "tiktok-b7g450-H2ShareTitle").text
        # Get Avatar 
        avatar = driver.find_element(By.CLASS_NAME, "tiktok-1zpj2q-ImgAvatar").get_attribute("src")

        userInfo = driver.find_elements(By.TAG_NAME, "strong")

        for user in userInfo:
            if(user.get_attribute("title") == "Following"):
                userFollowing = user.text
            if(user.get_attribute("title") == "Followers"):
                userFollowers = user.text
            if(user.get_attribute("title") == "Likes"):
                userLikes = user.text
        # userDesc = driver.find_element(By.CLASS_NAME, "tiktok-1n8z9r7-H2ShareDesc")
        # userDescription = userDesc.text

        userUsername = username
        userAvatarSrc = avatar
        x = 0
        videos = driver.find_elements(By.CLASS_NAME, "tiktok-x6y88p-DivItemContainerV2")
        for video in videos:
            videoImg = video.find_element(By.TAG_NAME, "img").get_attribute("src")
            videoImgPlaceholder = videoImg
            videoSrc = video.find_element(By.TAG_NAME, "a").get_attribute("href")
            videoLink = videoSrc
            userVideoInfo = {
                "Image": videoImg,
                "Source": videoSrc
            }
            userVideoData.append(userVideoInfo)

        userFullData = {
            "Username": userUsername,
            "AvatarSrc": userAvatarSrc,
            "Following": userFollowing,
            "Followers": userFollowers,
            "Likes": userLikes,
            # "Description": userDescription,
            "AllVideos": userVideoData

        }

        
        cleanData = json.dumps(userFullData)
        return json.loads(cleanData)



