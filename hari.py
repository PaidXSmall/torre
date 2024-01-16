import random
import requests
import re
from bs4 import BeautifulSoup
import asyncio
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InputMediaPhoto, ChatPermissions, Message
from pyrogram.errors import UserNotParticipant
from pyrogram import Client, filters, enums
from Script import script
from config import *
from database import db

async def not_subscribed(client, message):
    await db.add_user(client, message)
    if not FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(FORCE_SUB, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True

class temp(object):
    U_NAME = None
    B_NAME = None

app = Client(
  name='hari',
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)


@app.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[InlineKeyboardButton(text="📢 Join Update Channel 📢", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "**Sᴏʀʀy Dᴜᴅᴇ Yᴏᴜ'ʀᴇ Nᴏᴛ Jᴏɪɴᴇᴅ My Cʜᴀɴɴᴇʟ 😐. Sᴏ Pʟᴇᴀꜱᴇ Jᴏɪɴ Oᴜʀ Uᴩᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ Tᴏ Cᴄᴏɴᴛɪɴᴜᴇ**"
    try:
        user = await client.get_chat_member(FORCE_SUB, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="Sᴏʀʀy Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))


@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    buttons = [[
      InlineKeyboardButton('〆 ᴏᴍɢ x ʙᴏᴛ 〆', url=f'https://t.me/OMGxBotz')
    ],[
      InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
      InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(
      photo=random.choice(PICS),
      caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
      reply_markup=reply_markup,
      parse_mode=enums.ParseMode.HTML
    )

@app.on_callback_query(filters.create(lambda _, __, ___: True))
async def callback_query_handler(client: Client, query: CallbackQuery):
    for key, value in enumerate(movie_list):
        if query.data == str(key):
            if movie_list[int(query.data)] in real_dict.keys():
                for i in real_dict[movie_list[int(query.data)]]:
                    await query.message.reply_text(text=f"{i}",
                        parse_mode=enums.ParseMode.HTML
                    )                   
    if query.data == "close_data":
        await query.message.delete()
    
    elif query.data == "start":
        buttons = [[
            InlineKeyboardButton('〆 ᴏᴍɢ x ʙᴏᴛ 〆', url=f'https://t.me/OMGxBotz')
            ],[      
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about')
        ]] 
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.START_TXT.format(query.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "help":
        buttons = [[
            InlineKeyboardButton('⇍ ʙᴀᴄᴋ ⇏', callback_data='start')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
    elif query.data == "about":
        buttons = [[
            InlineKeyboardButton('« ʙᴀᴄᴋ', callback_data='start'),
            InlineKeyboardButton('ᴄʟᴏsᴇ ↺', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await client.edit_message_media(
            query.message.chat.id, 
            query.message.id, 
            InputMediaPhoto(random.choice(PICS))
        )
        await query.message.edit_text(
            text=script.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        
@app.on_message(filters.command("1tmv"))
async def start(client, message):
    m = await message.reply_text(
        #chat_id=message.chat.id,
        text="<b>ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ғᴏʀ 𝟷𝟶 ꜱᴇᴄᴏɴᴅꜱ.....🤖</b>",
        reply_to_message_id=message.id
    )
    #m = await message.reply_text("", parse_mode=enums.ParseMode.HTML)
    tamilmv()
    await m.delete()
    hi = await message.reply_photo(photo=random.choice(TMVPICS), caption = "<b>ʜᴇʏ 👋\n\nsᴇʟᴇᴄᴛ ᴀ ᴍᴏᴠɪᴇ ғʀᴏᴍ ᴛʜᴇ ʟɪꜱᴛ\n\n🙂</b>", reply_markup=make_keyboard(), parse_mode=enums.ParseMode.HTML)
    await asyncio.sleep(50)
    await hi.delete()

def make_keyboard():
    buttons = [
        InlineKeyboardButton(value,f"mv callback_data=str(key))") for key, value in enumerate(movie_list)
    ]
    buttons.append([InlineKeyboardButton('Close the List ', callback_data='close_data')])
    return InlineKeyboardMarkup(inline_keyboard=buttons)



#@app.on_message()
def tamilmv():
    mainUrl = 'https://www.1tamilmv.prof/'
    mainlink = []
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Connection':'Keep-alive',
        'sec-ch-ua-platform': '"Windows"',
    }
    
    global movie_dict 
    movie_dict = {}
    global real_dict
    real_dict  = {}
    web = requests.request("GET",mainUrl,headers=headers)
    soup = BeautifulSoup(web.text,'lxml')
    linker = []
    magre = []
    badtitles = []
    realtitles = []
    global movie_list
    movie_list = []

    num = 0
    
    temps = soup.find_all('div',{'class' : 'ipsType_break ipsContained'})

    for i in range(21):
        title = temps[i].findAll('a')[0].text
        badtitles.append(title)
        links = temps[i].find('a')['href']
        content = str(links)
        linker.append(content)
        
    for element in badtitles:
        realtitles.append(element.strip())
        movie_dict[element.strip()] = None
    #print(badtitles)
    movie_list = list(movie_dict)
        
    for url in linker:

        html = requests.request("GET",url)
        soup = BeautifulSoup(html.text,'lxml')
        pattern=re.compile(r"magnet:\?xt=urn:[a-z0-9]+:[a-zA-Z0-9]{40}")
        bigtitle = soup.find_all('a')
        alltitles = []
        filelink = []
        mag = []
        for i in soup.find_all('a', href=True):
            if i['href'].startswith('magnet'):
                mag.append(i['href'])
                
        for a in soup.findAll('a', {"data-fileext": "torrent", 'href': True}):
            filelink.append(a['href'])
            alltitles.append(a.text)


        for p in range(0,len(filelink)):
#             #print(f"*{alltitles[p]}* -->\n🧲 `{mag[p]}`\n🗒️->[Torrent file]({filelink[p]})")
            try:
              real_dict.setdefault(movie_list[num],[])
              real_dict[movie_list[num]].append({"Title": alltitles[p], "TorrentFile": filelink[p]})
              #real_dict[movie_list[num]].append((f"*{alltitles[p]}* -->\n🧲 `{mag[p]}`\n🗒️->[Torrent file]({filelink[p]})"))
            except:
              pass
            
        num = num + 1
        
def select_mv(update, context):
    query = update.callback_query
    user_id = query.from_user.id
    data = query.data
    #print("data : ", data)
    msg = query.message
    data = data.split(" ")
    uid = int(data[1])
    data = data[2]
    global movie_list
    global real_dict
    '''
    try:
        task_info = listener_dict[task_id]
    except:
        return editMessage("This is an old task", msg)
    
    uid = task_info[0]
    u_name = task_info[1]
    '''
    
    if user_id != uid and not CustomFilters._owner_query(user_id):
        return query.answer(text="This task is not for you!", show_alert=True)
    #print("data1 : ", data)
    #print("Movie Dict : " , movie_list)
    #sendMessage(f"<b>Here's your Movie links 🎥</b>", query.bot, msg)
    if data == "cancel":
        query.answer()
        editMessage('🥰', msg)
    for key , value in enumerate(movie_list):
        if data == f"{key}":
            if movie_list[int(data)] in real_dict.keys():
                for file_data in real_dict[movie_list[int(data)]]:
                    LOGGER.info(f"{file_data}")
                    title = file_data["Title"]
                    torrent_file_url = file_data["TorrentFile"]
                    
                    # Download the torrent file
                    response = requests.get(torrent_file_url)
                    file_name = f"{title}.torrent"
                    query.bot.send_document(chat_id=msg.chat_id, document=response.content, filename=file_name, caption=title + "\n\nPGV_da")
                    
            else:
                sendMessage(f"<b>Torrent Files Not Available</b>", query.bot, msg)

def list_tmv(update, context):
    msg_id = update.message.message_id
    user_id = update.message.from_user.id 
    u_name = update.message.from_user.first_name
    
    lm = sendMessage("<b>Please wait for 10 seconds...🤖</b>", context.bot, update.message)
    tamilmv()
    deleteMessage(context.bot, lm)
    #listener_dict[msg_id] = [user_id, u_name]
    sendMarkup("Select a Movie from the list 🙂 : ", context.bot, update.message, reply_markup=makeKeyboard(user_id))


print("hari bot start💥")

if __name__ == '__main__':
    app.run()
