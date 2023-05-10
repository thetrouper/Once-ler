import requests
import base64
import tkinter as tk
from tkinter import messagebox
import clipboard
from discord_webhook import DiscordWebhook, DiscordEmbed

def scrape(url):
    response = requests.get(url)
    response.raise_for_status()

    content = response.content.decode('utf-8').strip()
    decoded_text = base64.b64decode(content).decode('utf-8')

    if "https://discord.com/api/webhooks/" in decoded_text:
        webhook_url = decoded_text.strip()
        send_embed(webhook_url)
        delete_webhook(webhook_url)
    else:
        clipboard.copy(decoded_text)
        messagebox.showinfo("No Webhooks?", "No Webhooks were found. (Is he too lazy to keep up?) Anyways, text has been copied to clipboard, its proberably a message of him coping 💀")

def send_embed(webhook_url):
    title = "Cop da new webhook deleter"
    message = "Cope Ratter + L BOZO + Imagine trying to rat a mod + crying_laughing_emoji x9 + bald + scethe + mald + ratio + scammer + kys + suck a cock + burn in hell + i used a vpn + this is a proxy + mullvad on top + thug shaker + allot of turbulance + cry about it"
    footer = "A message from bread: i saw your big mother on the orange and black hub she got the big ol saggy ass lookin ass lookin dumb ass, has not ass, gets no ass, will never have any ass, will never get any ass, got ganged on by 10 other black oily men that were 30 year old lookin ass bruh :default_dance:"
    image = "https://media.tenor.com/XMRnHdhvVvcAAAAC/cry-about-it-cry.gif"
    smallimage = "https://cdn.discordapp.com/emojis/1074467542409678971.webp?size=96&quality=lossless"
    ilosc = 3

    webhook = DiscordWebhook(url=webhook_url, content='@everyone get beamed EZ 💀', username="Webhook Deleter 9000", avatar_url="https://cdn.discordapp.com/attachments/1105670577206874244/1105696732408447087/Screenshot_2022-08-24_204048.png", rate_limit_retry=True)
    
    embed = DiscordEmbed(title=title, description=message, color='FF00FF')
    embed.set_footer(text=footer, icon_url=smallimage)
    embed.set_image(url=image)

    webhook.add_embed(embed)

    for i in range(ilosc):
        webhook.execute()
        print("Embed sent.")

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 200:
        print("Webhook successfully deleted!")
    else:
        clipboard.copy(webhook_url)
        print("Error", "Failed to delete the webhook. Did someone get to it before you? Copied URL to your clipboard. Maybe he's coping again.")


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
""")
scrape(url)
