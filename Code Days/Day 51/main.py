from email import message
from internet_speed_twitter_bot import InternetSpeedTwitterBot

IDEAL_UP_SPEED = 1
IDEAL_DOWN_SPEED = 1

testBot = InternetSpeedTwitterBot()

testBot.getInternetSpeed()

if float(testBot.down) > IDEAL_DOWN_SPEED and float(testBot.up) > IDEAL_UP_SPEED:
    message = f"#100DaysOfPython Day 51: Pretty great, these are my mobile internet speeds. Down: {testBot.down} - Up: {testBot.up}"
    testBot.tweet_at_provider(message)
else:
    message = f"#100DaysOfPython Day 51: Oh no, these are my mobile internet speeds. Down: {testBot.down} - Up: {testBot.up}"
    testBot.tweet_at_provider(message)