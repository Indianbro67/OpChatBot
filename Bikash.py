from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re


API_ID = os.environ.get("API_ID", "26670684") 
API_HASH = os.environ.get("API_HASH", "60592bded0f25a9633a8133601f2c779") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6289264953:AAG1N1Q3_KXM-V2KB-nDb9LFlMXq9WpZPv8") 
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
BOT_IMAGE = os.environ.get("BOT_IMAGE", "https://telegra.ph/file/8718de4a731b087ffd12a.jpg")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Pooja_Service_Bot")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "Black_Devil_Admin")
SUPPORT_GROUP = os.environ.get("SUPPORT_GROUP", "https://t.me/adult_girls_chatting_groupp")
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/adult_updates")


bot = Client(
    "V_Chat_Bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(filters.command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_audio(audio=f"https://dl.sndup.net/hp75/How%20To%20Download%20Restricted%20Photo%20and.mp3",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝗦𝗲𝗻𝗱 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗢r 𝗚𝗿𝗼𝘂𝗽 𝗟𝗶𝗻𝗸 . \n𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐑𝐞𝐬𝐭𝐫𝐢𝐜𝐭𝐞𝐝 𝐏𝐡𝐨𝐭𝐨 𝐚𝐧𝐝 𝐕𝐢𝐝𝐞𝐨

┏━━━━━━━━━━━━━━━━━┓
┣❥︎ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ➪ » [ʙʟᴀᴄᴋ ᴅᴇᴠɪʟ](https://t.me/Black_Devil_Admin)
┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 ➪ » [𝐀𝐝𝐮𝐥𝐭𝐬 𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/adult_updates)
┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ➪ » [𝐆𝐢𝐫𝐥𝐟𝐫𝐢𝐞𝐧𝐝 𝟒𝐔 ❤](https://t.me/adult_girls_chatting_groupp)
┗━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐀𝐬 𝐚 𝐀𝐝𝐦𝐢𝐧 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐂𝐡𝐚𝐭.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ɪɴᴠɪᴛᴇ ᴀɴᴅ ɢᴇᴛ ᴠɪᴘ ᴀᴄᴄᴇꜱꜱ 🗝️🔐", url=f"https://telegram.me/share/url?url=https://t.me/save_all_file_bot?start=1521651151")
                ]
                
           ]
        ),
    )
    
    
@bot.on_message(filters.command(["/start", f"start@{BOT_USERNAME}", "/alive", ".alive", "#bikash", "#aditya"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
        await message.reply_audio(audio=f"https://dl.sndup.net/hp75/How%20To%20Download%20Restricted%20Photo%20and.mp3", 
         caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━ 
 💥 𝗦𝗲𝗻𝗱 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗢r 𝗚𝗿𝗼𝘂𝗽 𝗟𝗶𝗻𝗸 . \n𝐓𝐨 𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝 𝐑𝐞𝐬𝐭𝐫𝐢𝐜𝐭𝐞𝐝 𝐏𝐡𝐨𝐭𝐨 𝐚𝐧𝐝 𝐕𝐢𝐝𝐞𝐨 
  
 ┏━━━━━━━━━━━━━━━━━┓ 
 ┣❥︎ 𝐂𝐫𝐞𝐚𝐭𝐨𝐫 ➪ » [ʙʟᴀᴄᴋ ᴅᴇᴠɪʟ](https://t.me/Black_Devil_Admin) 
 ┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 ➪ » [𝐀𝐝𝐮𝐥𝐭𝐬 𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/adult_updates) 
 ┣❥︎ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ➪ » [𝐆𝐢𝐫𝐥𝐟𝐫𝐢𝐞𝐧𝐝 𝟒𝐔 ❤](https://t.me/adult_girls_chatting_groupp) 
 ┗━━━━━━━━━━━━━━━━━┛ 
  
 💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐀𝐬 𝐚 𝐀𝐝𝐦𝐢𝐧 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 
 𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐂𝐡𝐚𝐭. 
 ━━━━━━━━━━━━━━━━━━━━━━━━**""", 
     reply_markup=InlineKeyboardMarkup( 
             [ 
                 [ 
                     InlineKeyboardButton( 
                         "ɪɴᴠɪᴛᴇ ᴀɴᴅ ɢᴇᴛ ᴠɪᴘ ᴀᴄᴄᴇꜱꜱ 🗝️🔐", url=f"https://telegram.me/share/url?url=https://t.me/save_all_file_bot?start=1521651151") 
                 ] 
  
            ] 
         ), 
     )



@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "💥 𝐇𝐞𝐲 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀 𝐀𝐝𝐦𝐢𝐧 💥"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:
        v.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"🌷 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🥀!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        await message.reply_text(f"🌷𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐭 𝐃𝐢𝐬𝐚𝐛𝐥𝐞𝐝 🥀!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    vdb = MongoClient(MONGO_URL)    
    v = vdb["vDb"]["v"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_v = v.find_one({"chat_id": message.chat.id})
    if not is_v:           
        await message.reply_text(f"💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐫𝐞𝐚𝐝𝐲𝐄𝐧𝐚𝐛𝐥𝐞𝐝🌷!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    if is_v:
        v.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"💥 𝐕 𝐂𝐡𝐚𝐭𝐛𝐨𝐭 𝐈𝐬 𝐄𝐧𝐚𝐛𝐥𝐞𝐝 🌷!\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")
    

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**🇮🇳 𝐔𝐬𝐚𝐠𝐞 🌷 :**\n/chatbot [on|off] 𝐎𝐧𝐥𝐲 𝐆𝐫𝐨𝐮𝐩 🇮🇳 !\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷")


@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def vai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def vstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       if not is_v:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       vdb = MongoClient(MONGO_URL)
       v = vdb["vDb"]["v"] 
       is_v = v.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_v:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def vprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def vprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       
bot.run()
