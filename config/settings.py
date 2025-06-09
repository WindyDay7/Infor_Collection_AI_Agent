# config/settings.py

import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "settings.ini"))
# print(config)
# API keys
SERPAPI_KEY = config["api"]["serpapi_key"]
MOTA_API_KEY = config["api"]["mota_api_key"]
OPEN_ROUTER_API_KEY = config["api"]["open_router_api_key"]

# Search settings
NEWS_QUERY = int(config["search"]["news_query"])
NUM_ARTICLES = int(config["search"]["num_articles"])

# Output
OUTPUT_DIR = config["output"]["output_dir"]

# HTTP headers
USER_AGENT = config["http"]["user_agent"]

# Cookies (as dict)
COOKIES = dict(config.items("cookies"))

# LOG configuration
LOG_LEVEL = config["log"]["log_level"]
LOG_FILE = config["log"]["log_file"]

# MODELS configuration
MODELS = dict(config.items("models"))

# QUERY_LIST
QUERY_LIST = config["queries"]["query_list"].split(",")

# EMAIL configuration
EMAIL_USER = config["email"]["email_user"]
EMAIL_PASSWORD = config["email"]["email_password"]
EMAIL_RECEIVER = config["email"]["email_receiver"]