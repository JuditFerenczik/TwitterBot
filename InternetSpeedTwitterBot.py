from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from secrets import TWITTER_EMAIL,TWITTER_PASSWORD, PROMISED_UP, PROMISED_DOWN, TWITTER_USERNAME


class InternetSpeedTwitterBot:
    def __init__(self,driver):
        self.down = 0
        self.up = 0
        self.driver = webdriver.Chrome(service=Service(driver))

    def get_internet_speed(self):
        print("Lets get the current speed")
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        cookie_button = self.driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookie_button.click()

        sleep(1)
        go_button = self.driver.find_element(By.CSS_SELECTOR, "div.start-button a")
        go_button.click()

        sleep(2)
        down_up = self.driver.find_elements(By.CSS_SELECTOR, "div.result-data span.result-data-large")
        print(down_up[0].text, down_up[1].text)
        while down_up[1].text == "--":
            sleep(3)
            down_up = self.driver.find_elements(By.CSS_SELECTOR, "div.result-data span.result-data-large")
            print(down_up[0].text, down_up[1].text)
        self.down = float(down_up[0].text)
        self.up = float(down_up[1].text)
        return [down_up[0].text, down_up[1].text]

    def tweet_at_provider(self):
        print("Lets check your internet speed!!")
        if (self.down < PROMISED_DOWN) and (self.up < PROMISED_UP):
            self.driver.get("https://twitter.com/home")

            sleep(2)
            username = self.driver.find_element(By.CSS_SELECTOR, "input")
            username.send_keys(TWITTER_EMAIL)
            sleep(2)
            username.send_keys(Keys.ENTER)
            sleep(2)

            print(len(self.driver.find_elements(By.CSS_SELECTOR, "input")))
            if len(self.driver.find_elements(By.CSS_SELECTOR, "input")) == 1:
                middle = self.driver.find_element(By.CSS_SELECTOR, "input")
                middle.send_keys(TWITTER_USERNAME)
                sleep(2)
                middle.send_keys(Keys.ENTER)
                sleep(2)
            password = self.driver.find_elements(By.CSS_SELECTOR, "input")
            password[1].send_keys(TWITTER_PASSWORD)
            sleep(2)
            password[1].send_keys(Keys.ENTER)

            sleep(2)
            tweet_container = self.driver.find_element(By.CSS_SELECTOR, "div.public-DraftEditor-content[contenteditable=true] span")
            tweet_message = f"My internet in sooo slow again, it is just {self.down} down and {self.up} up contrary to the promised {PROMISED_DOWN} down and {PROMISED_UP} up"
            tweet_container.send_keys(tweet_message)

            sleep(2)
            tweet_container.send_keys(Keys.ENTER)
            sleep(2)
            send_tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div")
            send_tweet.click()

            sleep(1)
            accept_cookies = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div")
            accept_cookies.click()
            sleep(2)
            self.driver.quit()
