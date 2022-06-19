from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("12429107"))
API_HASH = getenv("2c1096dfd767dfdfab961bb2fffe6be3")
BOT_TOKEN = getenv("5460956456:AAGNuaLQU0hyeAsXKpGcx7RcoDqO6qRPPSk")
SESSION_NAME = getenv("SESSION_NAME", "AgCPWadB_J78YNwtlMrgOWiRPWFwBnug6tISp6TEZvBqHB1cvbHErzrrcP3xF3XeP5yLIc7WMs96BhDDTAosZND6TYM-2FA3mICJv0KgKmV4hVfP5gCTTX6088ll2esv_Q0jpaBlWx8fzO688KzN7dUEMuefP7S8hYUOgk-7zCFMEQ4qzd5ZkF2VJSeMcs8ZDw_2PoHFouIUNqNIRJfVsMGPgWB3J-JQUIXQUjI3mp1P2j2Rt7UQFct2bO_0QumvaflPhMLm-Xodq15EgmgpDyMWN5p4FmqprmOikPCVcZJzFXQv_05uZKcERKaiGlIMFCOtCURAPNGezhdGgTsVNFr8AAAAATLkklEA")

# mandatory vars
OWNER_USERNAME = getenv("5386549632")
ALIVE_NAME = getenv("5386549632")
BOT_USERNAME = getenv("Iwjsiwbot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/bbaj8/SOURCE-Freedom")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "QQQLO")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QQQLO")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("mongodb+srv://hussein87:Hussein87@cluster0.wynpz.mongodb.net/?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "").split())
OWNER_ID = list(map(int, getenv("5386549632").split()))
SUDO_USERS = list(map(int, getenv("5386549632").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
