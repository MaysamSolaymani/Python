from instabot import Bot
import os,datetime

bot = Bot()
#Initiate bot
bot.login(username = "username", password = "password")
#Get Caption
mg = open(os.path.dirname(__file__) + "\\Caption.txt", "r")
img = open(os.path.dirname(__file__) + "\\image.jpg", 'rb')
bot.upload_photo(img, caption=f.read())
