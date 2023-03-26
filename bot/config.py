import os

import yaml
import dotenv
from pathlib import Path

config_dir = Path(__file__).parent.parent.resolve() / "config"

# load yaml config
# with open(config_dir / "config.yml", 'r') as f:
#     config_yaml = yaml.safe_load(f)

# load .env config
config_env = dotenv.dotenv_values(config_dir / "config.env")

# config parameters
# telegram_token = config_yaml["telegram_token"]
# openai_api_key = config_yaml["openai_api_key"]
# use_chatgpt_api = config_yaml.get("use_chatgpt_api", True)
# allowed_telegram_usernames = config_yaml["allowed_telegram_usernames"]
# new_dialog_timeout = config_yaml["new_dialog_timeout"]
# enable_message_streaming = config_yaml.get("enable_message_streaming", True)
# mongodb_uri = f"mongodb://mongo:{config_env['MONGODB_PORT']}"
telegram_token = os.getenv('TELEGRAM_TOKEN')
openai_api_key =  os.getenv('OPENAI_API_KEY')
use_chatgpt_api =  os.getenv('USE_CHATGPT_API', True)
allowed_telegram_usernames =  os.getenv("TELEGRAM_USERNAMES", "").split(',')
new_dialog_timeout =  int(os.getenv("NEW_DIALOG_TIMEOUT", 300))
enable_message_streaming = os.getenv('ENABLE_MESSAGE_STREAMING', True)
mongodb_uri = "mongodb://mongo:"+config_env.get('MONGODB_PORT', "27017")
print("Value of 'allowed_telegram_usernames' environment variable :", str(allowed_telegram_usernames))

# chat_modes
with open(config_dir / "chat_modes.yml", 'r') as f:
    chat_modes = yaml.safe_load(f)

# models
with open(config_dir / "models.yml", 'r') as f:
    models = yaml.safe_load(f)
