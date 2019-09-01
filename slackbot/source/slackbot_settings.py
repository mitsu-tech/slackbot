import os
from os.path import join, dirname
from dotenv import load_dotenv

# .envを読み込む
env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)

# .envからbotアカウントのトークンを取得
API_TOKEN= os.environ.get("API_TOKEN")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER"),
DB_PASSWD = os.environ.get("DB_PASSWD"),
DB = os.environ.get("DB")

# このBotが行う処理が見つからなかった時に返すメッセージ
DEFAULT_REPLY = "I don't understand."

# プラグインスクリプトを置いてあるサブディレクトリ名
PLUGINS = ['plugins']