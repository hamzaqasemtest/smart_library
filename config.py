import configparser

config = configparser.ConfigParser()
config.read("config.ini")

AZURE_CHATBOT_API_KEY = config["AZURE_CHATBOT"]["AZURE_CHATBOT_API_KEY"]
AZURE_CHATBOT_ENDPOINT = config["AZURE_CHATBOT"]["AZURE_CHATBOT_ENDPOINT"]
AZURE_CHATBOT_OPENAI_VERSION = config["AZURE_CHATBOT"]["AZURE_CHATBOT_OPENAI_VERSION"]

SECRET_KEY = config["ENCRYPTION"]["SECRET_KEY"]
ALGORITHM = config["ENCRYPTION"]["ALGORITHM"]

app_config_main = config['app_config']['main_file']
app_config_host = config['app_config']['host']
app_config_port = config['app_config']['port']
app_config_reload = config['app_config']['reload']

DB_DIALECT = config["DATABASE"]["DB_DIALECT"]
DB_USERNAME = config["DATABASE"]["DB_USERNAME"]
DB_PASSWORD = config["DATABASE"]["DB_PASSWORD"]
DB_HOST = config["DATABASE"]["DB_HOST"]
DB_PORT = config["DATABASE"]["DB_PORT"]
DB_NAME = config["DATABASE"]["DB_NAME"]