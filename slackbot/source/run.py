import os
from os.path import join, dirname
from dotenv import load_dotenv
from slackbot.bot import Bot


def main():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    print("start bot")
    main()