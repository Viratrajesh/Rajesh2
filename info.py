import re, logging
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '23361081')  #api id of your telegram id
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '0605c5395b91ead763072251e20c3417') #api hash of your telegram id
if len(API_HASH) == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '6876657536:AAEV5S7NClr1LE12d2oDY2le783J6aX8OXU') #bot token from botfather
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '80')) #don't change anything 

# Bot pics
PICS = (environ.get('PICS', 'https://graph.org/file/e537c89c4ec532a0bdc6d.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '5371238852,5861377019,5102717153') #apni tg id daalo
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1002030715343').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')

REQUEST_TO_JOIN_MODE = is_enabled('REQUEST_TO_JOIN_MODE', True)
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '-1002294468496').split()]
if len(AUTH_CHANNEL) == 0:
    print('Info - AUTH_CHANNEL is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '-1002289263173') #bot log channel -1005293546253
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
IS_FSUB = is_enabled('IS_FSUB', True)

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '') #support group id ex:  -1002936246860
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "") #mongo db url
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/Askmovies2_bot')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/Askmovies4')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/Askmovieslink3')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/Tutorial01Ask")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/Tutorial01Ask/5")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds 
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10)) #don't change anything in Language 
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'english hindi telugu tamil kannada malayalam').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "krownlinks.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "5d9250c00801b067d7f83bfe54c4fba484505447")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
STICKERS_IDS = (
    "CAACAgQAAxkBAAEK99dlfC7LDqnuwtGRkIoacot_dGC4zQACbg8AAuHqsVDaMQeY6CcRojME CAACAgQAAxkBAAELqxll8CcG-MZx9mIOXgaHSzLc9uyxswACaxQAAlrdEVOJDG3cIZuWLzQE"
).split()

# boolean settings 
GROUP_FSUB = is_enabled('GROUP_FSUB', True) 
PM_SEARCH = is_enabled('PM_SEARCH', True) #switch True or False for searching results in bot pm😃
IS_VERIFY = is_enabled('IS_VERIFY', True)
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', True)


PAYMENT_QR = environ.get('PAYMENT_QR', 'http://graph.org/file/cacbbea472e5a48ce0d64.jpg') #telegraph link of your QR code 
UPI_ID = environ.get('UPI_ID', 'Rajesh1162005@okaxis') # Add your upi id here
# for stream
IS_STREAM = is_enabled('IS_STREAM', True) #true if you want stream feature active in your bot
BIN_CHANNEL = environ.get("BIN_CHANNEL", "") #if is_stream = true then add a channel id ex: -10026393639
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "") #if heroku then paste the app link here ex: https://heroku......./
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()
