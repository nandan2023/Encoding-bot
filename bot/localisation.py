#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AbirHasan2005

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "Hello, This is a Telegram Video Encoder Bot. \n\n Please send me any Telegram big video file I will compress it as  small video file! \n\n/help for more details. \n\nOwner : @Sensei_Rimuru"
   
    ABS_TEXT = " Please don't be selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ.... \n"
    
    UPLOAD_START = "ᴜᴘʟᴏᴀᴅɪɴɢ.... \n"
    
    COMPRESS_START = "ᴛʀʏɪɴɢ ᴛᴏ ᴇɴᴄᴏᴅᴇ..."
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "ᴇɴᴄᴏᴅᴇᴅ ʙʏ Rulf"

    COMPRESS_PROGRESS = "🕛 ᴇᴛᴀ {}\n♻️ ᴘʀᴏɢʀᴇss {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "ᴛʜᴜᴍʙɴᴀɪʟ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ...✅"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "ᴍᴇᴅɪᴀ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ... ✅"
    
    SAVED_RECVD_DOC_FILE = "ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ...✅"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "ɴᴏ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ғᴏᴜɴᴅ...❌"
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already one Process going on! ⚠️ \n\nCheck Live Status on Anime Sensei Logs."
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Hi, I am Video Compressor Bot."
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
