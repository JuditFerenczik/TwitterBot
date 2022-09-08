from secrets import CHROME_DRIVER_PATH
from InternetSpeedTwitterBot import InternetSpeedTwitterBot


twitter = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
speed = twitter.get_internet_speed()
print("Down: ", speed[0])
print("Up: ", speed[1])
print("Down: ", twitter.down)
print("Up: ", twitter.up)
twitter.tweet_at_provider()
