"""
from os import getenv


API_ID = int(getenv("API_ID", "20054245"))
API_HASH = getenv("API_HASH", "431f22f320ed5d69225d3b3fc253fc0d")
BOT_TOKEN = getenv("BOT_TOKEN", "7064501216:AAEOQMaqLGL5e6TBau-8dYhRxUk5yrG3738")
OWNER_ID = int(getenv("OWNER_ID", "5034929962"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6050277919 5034929962").split()))
MONGO_URL = getenv("mongodb+srv://Arjunbabe:Sm1pFd4pQMu5syFM@cluster0.mpx2ar5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002034072106"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002034072106"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

