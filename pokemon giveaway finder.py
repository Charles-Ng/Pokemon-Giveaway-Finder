import praw
import re
import ctypes
import time
import os
from datetime import datetime


def getGiveawayData():
    last_title=""
    user_agent = ("PokemonGiveawayNotifier Bot v1")
    client_id = 'F4Q-MDi1y_2XaA'
    client_secret = 'bYUZ2ZTib1KFaMUvvMDoZ75yy6Q'

    r = praw.Reddit(user_agent=user_agent, client_id=client_id,
                    client_secret=client_secret)

    plaza = r.subreddit("pokemonplaza")
    giveaway = r.subreddit("pokemongiveaway")
    trades = r.subreddit("pokemontrades")

    for x in plaza.new(limit=2):
        if x.link_flair_text == "Giveaway":

            ctypes.windll.user32.MessageBoxW(0, "pokemon plaza\n" + x.title +
            "\n timestamp:" + str(datetime.now()), "Giveaway Alert", 1)
            #os.startfile(r"C:\Users\User\Downloads\2012 - Kanye West Presents G.O.O.D. Music - Cruel Summer\12 - Don't Like.flac")

    for y in giveaway.new(limit=2):

        if y.link_flair_text == "Hacked/Cloned Giveaway" and y.title != last_title:
            last_title = y.title
            ctypes.windll.user32.MessageBoxW(0,
                "pokemon giveaway has a HACKED giveaway\n"
                + y.title + "\n Timestamp: " + str(datetime.now()),
                "Giveaway Alert", 1)
            #os.startfile(r"C:\Users\User\Downloads\2012 - Kanye West Presents G.O.O.D. Music - Cruel Summer\12 - Don't Like.flac")


        #elif y.link_flair_text == "Normal Giveaway":
            #ctypes.windll.user32.MessageBoxW(0,
            #"pokemon giveaway has a normal giveaway \n" +
            #y.title + "Timestamp: " + str(datetime.now()),
                         #"Giveaway Alert", 1)

    #for z in trades.new(limit=2):
        #if z.link_flair_text == "Giveaway":
            #ctypes.windll.user32.MessageBoxW(0, "pokemon trades\n" + z.title +
            #"\n timestamp:" + str(datetime.now()), "Giveaway Alert", 1)

if __name__ == "__main__":
    try:

        while True:
            getGiveawayData()
            time.sleep(6)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Internet disconnected", "Fuck this world", 1)





