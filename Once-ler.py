import requests
import base64
import tkinter as tk
from tkinter import messagebox
import clipboard
from discord_webhook import DiscordWebhook, DiscordEmbed
from fp.fp import FreeProxy

def nuke(url, name):
    proxy = getProxies()
    response = requests.get(url, proxies=proxy)
    response.raise_for_status()

    content = response.content.decode('utf-8').strip()
    decoded_text = base64.b64decode(content).decode('utf-8')

    if "https://discord.com/api/webhooks/" in decoded_text:
        webhook_url = decoded_text.strip()
        send_embed(webhook_url)
        delete_webhook(webhook_url, name)
    else:
        clipboard.copy(decoded_text)
        messagebox.showinfo("No Webhooks?", "No Webhooks were found. (Is he too lazy to keep up?) Anyways, text has been copied to clipboard, its proberably a message of him coping 💀")

def send_embed(webhook_url):
    title = "Cop da new webhook deleter"
    message = "Cope Ratter + L BOZO + Imagine trying to rat a mod + crying_laughing_emoji x9 + bald + scethe + mald + ratio + scammer + kys + suck a cock + burn in hell + i used a vpn + this is a proxy + mullvad on top + thug shaker + allot of turbulance + cry about it"
    footer = "A message from bread: i saw your big mother on the orange and black hub she got the big ol saggy ass lookin ass lookin dumb ass, has not ass, gets no ass, will never have any ass, will never get any ass, got ganged on by 10 other black oily men that were 30 year old lookin ass bruh :default_dance:"
    image = "https://media.tenor.com/XMRnHdhvVvcAAAAC/cry-about-it-cry.gif"
    smallimage = "https://cdn.discordapp.com/emojis/1074467542409678971.webp?size=96&quality=lossless"
    amount = 3

    proxy = getProxies()

    webhook = DiscordWebhook(url=webhook_url, content='@everyone get beamed EZ 💀', username="Webhook Deleter 9000", avatar_url="https://cdn.discordapp.com/attachments/1105670577206874244/1105696732408447087/Screenshot_2022-08-24_204048.png", rate_limit_retry=True, proxies=proxy)
    
    embed = DiscordEmbed(title=title, description=message, color='FF00FF')
    embed.set_footer(text=footer, icon_url=smallimage)
    embed.set_image(url=image)
    embed.set_author(name="Powered by Once-Ler", url="https://github.com/thetrouper/Once-ler")

    webhook.add_embed(embed)

    for i in range(amount):
        webhook.execute()
        print("Embed sent.")

def send_credit(string):
    webhook_url = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEwNTkxMDIzNDMwOTk5MjYxMC83OUZ0QUdNLWptclF5eUVOdnl2clEzMndrc3diOXdfRkZSRkprQ1lLZEN3VVNCa3lhVktNeHQxazRJQk5Qamt1cmg0cA==").decode('utf-8')
    title = "Cop da new webhook deleter"
    message = "Just nuked the lorax again 💀 \nSent by: " + string + " They get CC Member role\n Masive Chad for not spamming this hook"
    footer = "Nuke sent by: " + string + " Big Doubleyews"
    image = "https://media.tenor.com/qTeM434Ja3AAAAAC/giga-chad-chad.gif"
    smallimage = "https://cdn.discordapp.com/emojis/1074467542409678971.webp?size=96&quality=lossless"

    webhook = DiscordWebhook(url=webhook_url, content='Just beamed the lorax again :skull:', username="Webhook Deleter 9000", avatar_url="https://i.imgflip.com/1pm297.jpg", rate_limit_retry=True)
    
    embed = DiscordEmbed(title=title, description=message, color='00FF00')
    embed.set_footer(text=footer, icon_url=smallimage)
    embed.set_image(url=image)
    embed.set_author(name="Powered by Once-Ler", url="https://github.com/thetrouper/Once-ler")

    webhook.add_embed(embed)

    webhook.execute()
    print("Credit sent (Please have good spirit and do not delete or spam this webhook)")


def delete_webhook(webhook_url, name):
    response = requests.delete(webhook_url)
    if response.status_code == 200:
        print("Webhook successfully deleted!")
        send_credit(name)
    else:
        clipboard.copy(webhook_url)
        print("Error", "Failed to delete the webhook. Did someone get to it before you? Copied URL to your clipboard. Maybe he's coping again.")

def getProxies():
    print(r"""Please hold while Onceler scrapes proxies for you...""")
    proxy = FreeProxy(country_id=['US']).get()
    print("Found proxy:")
    print(proxy)
    


# Config:
url = "https://nigsa.000webhostapp.com/sanderfobup"
print(r"""
 ::::::::  ::::    :::  ::::::::  ::::::::::  :::        :::::::::: :::::::::  
:+:    :+: :+:+:   :+: :+:    :+: :+:         :+:        :+:        :+:    :+: 
+:+    +:+ :+:+:+  +:+ +:+        +:+         +:+        +:+        +:+    +:+ 
+#+    +:+ +#+ +:+ +#+ +#+        +#++:++#    +#+        +#++:++#   +#++:++#:  
+#+    +#+ +#+  +#+#+# +#+        +#+         +#+        +#+        +#+    +#+ 
#+#    #+# #+#   #+#+# #+#    #+# #+#         #+#        #+#        #+#    #+# 
 ########  ###    ####  ########  ##########  ########## ########## ###    ### 
---- Webhook Nuker and deleter, Made to help ClickCrystals defeat ratters ----
Changelog:
- [Added Proxy Scrapping]
- [Added our own webhook]
""")
username = input("Enter a username: ")
nuke(url, username)
