"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio

from userbot.utils import admin_cmd



@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "call":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @mrconfused ,`Please Connect me to my lil bro,Shivamani `",
            "`User Authorised.`",
            "`Calling Shivamani `  `At +919848022338`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Shivamani : May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @mrconfsed the cat ",
            "`Shivamani : OMG!!! Long time no see, Wassup cat...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Shivamani : Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Shivamani : Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Shivamani : Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
