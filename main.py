import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

TW_LOGIN_URL = "https://twitter.com/i/flow/login"
SPEED_TEST_URL = "https://www.speedtest.net/"
PROMISED_DOWN = 200
PROMISED_UP = 10

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class TwitterComplaintBot:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.up = 0
        self.down = 0

    def internet_speed(self):
        self.driver.get(SPEED_TEST_URL)

        try:
            pop_up = self.driver.find_element(By.CSS_SELECTOR, "button[id='onetrust-accept-btn-handler']")
            pop_up.click()
        except NoSuchElementException:
            pass

        time.sleep(1)
        go_btn = self.driver.find_element(By.CSS_SELECTOR, "a[aria-label='start speed test - connection type multi']")
        go_btn.click()
        time.sleep(60)

        self.down = float(self.driver.find_element(By.CSS_SELECTOR, "span[class='result-data-large number result-data-value download-speed']").text)
        print(self.down)
        time.sleep(2)

        self.up = float(self.driver.find_element(By.CSS_SELECTOR, "span[class='result-data-large number result-data-value upload-speed']").text)
        print(self.up)

        if PROMISED_DOWN > self.down or PROMISED_UP > self.up:
            self.tweet_to_provider()

    def tweet_to_provider(self):
        self.driver.get(TW_LOGIN_URL)
        time.sleep(5)

        email = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
        email.click()
        email.send_keys("example.gmail.com")
        time.sleep(5)

        try:
            next_btn = self.driver.find_element(By.CSS_SELECTOR, "button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-ywje51 r-184id4b r-13qz1uu r-2yi16 r-1qi8awa r-3pj75a r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
            next_btn.click()
        except ElementClickInterceptedException:
            dismiss_btn = self.driver.find_element(By.CSS_SELECTOR, "button[data-testid='xMigrationBottomBar']")
            dismiss_btn.click()
            time.sleep(2)
            next_btn = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='ocfEnterTextNextButton']")
            next_btn.click()

        time.sleep(5)
        try:
            password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
            password.click()
            password.send_keys("Example")
            time.sleep(2)
        except NoSuchElementException:
            username = self.driver.find_element(By.CSS_SELECTOR, "input[name='text']")
            username.click()
            username.send_keys("Example")
            time.sleep(3)
            next_btn2 = self.driver.find_element(By.CSS_SELECTOR, "button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
            next_btn2.click()
            time.sleep(5)
            password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
            password.click()
            password.send_keys("Example")
            time.sleep(2)

        login_btn = self.driver.find_element(By.CSS_SELECTOR, "button[class='css-175oi2r r-sdzlij r-1phboty r-rs99b7 r-lrvibr r-19yznuf r-64el8z r-1fkl15p r-1loqt21 r-o7ynqc r-6416eg r-1ny4l3l']")
        login_btn.click()
        time.sleep(8)

        tweet_content = self.driver.find_element(By.CSS_SELECTOR, "div[class='r-1oszu61 r-1niwhzg r-vqxq0j r-deolkf r-6koalj r-1mlwlqe r-eqz5dr r-1ebb2ja r-crgep1 r-ifefl9 r-bcqeeo r-t60dpp r-bnwqim r-13wfysu r-417010']")
        tweet_content.click()
        time.sleep(1)

        tweet_text = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")
        tweet_text.click()
        tweet_text.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(3)

        post_btn = self.driver.find_element(By.CSS_SELECTOR, "span[class='css-1jxf684 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-a023e6 r-rjixqe']")
        post_btn.click()
        time.sleep(5)


bot = TwitterComplaintBot()
bot.internet_speed()

