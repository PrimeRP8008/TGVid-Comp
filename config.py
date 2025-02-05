import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27419615")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "2f4b181296f0a2615a85471a1c72df44") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7490418925:AAFP4cS942dEwa3g-JCTZpAcaDCtAy8TP3Q") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '-1001991806323' '-1001923994578') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://rohitl3031:CNHkZh4Nkgv0mUuJ@cluster0.cgmci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","rohitl3031") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "1534632634")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002098787584')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://www.imghippo.com/i/EsCE5278QOA.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
