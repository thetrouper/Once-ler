import requests
import base64
import clipboard
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
from fp.fp import FreeProxy

def run_nuke_periodically(url, username, use_base, delay):
    while True:
        nuke(url, username, use_base)
        time.sleep(float(delay) / 1000)
        
def nuke(url, name, useBase):
    proxy = getProxies()
    response = requests.get(url, proxies=proxy)
    response.raise_for_status()

    content = response.content.decode('utf-8').strip()
    if useBase == "y":
        decoded_text = base64.b64decode(content).decode('utf-8')
    else:
        decoded_text = content

    if "https://discord.com/api/webhooks/" in decoded_text:
        webhook_url = decoded_text.strip()
        send_embed(webhook_url)
        delete_webhook(webhook_url, name)
    else:
        clipboard.copy(decoded_text)
        print("No Webhooks?", "No Webhooks were found. " + webhook_url + " Copied to clipboard. (Is he coping????)")

def send_embed(webhook_url):
    botName = "Webhook Deleter 9000"
    avatar = "https://cdn.discordapp.com/attachments/1105670577206874244/1105696732408447087/Screenshot_2022-08-24_204048.png"
    title = "Cop da new webhook deleter"
    content = "@everyone get beamed EZ 💀"
    message = "Cope Ratter + L BOZO + Imagine trying to rat a mod + crying_laughing_emoji x9 + bald + scethe + mald + ratio + scammer + kys + suck a cock + burn in hell + i used a vpn + this is a proxy + mullvad on top + thug shaker + allot of turbulance + cry about it"
    footer = "A message from bread: i saw your big mother on the orange and black hub she got the big ol saggy ass lookin ass lookin dumb ass, has not ass, gets no ass, will never have any ass, will never get any ass, got ganged on by 10 other black oily men that were 30 year old lookin ass bruh :default_dance:"
    image = "https://media.tenor.com/XMRnHdhvVvcAAAAC/cry-about-it-cry.gif"
    smallimage = "https://cdn.discordapp.com/emojis/1074467542409678971.webp?size=96&quality=lossless"
    author = "Powered by Once-Ler"
    author_url = "https://github.com/thetrouper/Once-ler"
    amount = 3
    color = "FF00FF"

    proxy = getProxies()

    webhook = DiscordWebhook(url=webhook_url, content=content, username=botName, avatar_url=avatar, rate_limit_retry=True, proxies=proxy)
    
    embed = DiscordEmbed(title=title, description=message, color=color)
    embed.set_footer(text=footer, icon_url=smallimage)
    embed.set_image(url=image)
    embed.set_author(name=author, url=author_url)

    webhook.add_embed(embed)

    for i in range(amount):
        webhook.execute()
        print("Embed sent.")

def send_credit(string):
    webhook_url = base64.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTEwNTkxMDIzNDMwOTk5MjYxMC83OUZ0QUdNLWptclF5eUVOdnl2clEzMndrc3diOXdfRkZSRkprQ1lLZEN3VVNCa3lhVktNeHQxazRJQk5Qamt1cmg0cA==").decode('utf-8')
    title = "Cop da new webhook deleter"
    message = "Just nuked the lorax again 💀 \nSent by: " + string + " They get CC Member role\n Masive Chad for not spamming this hook"
    footer = "Nuke sent by: " + string + " Big W's"
    image = "https://media.tenor.com/qTeM434Ja3AAAAAC/giga-chad-chad.gif"
    smallimage = "https://cdn.discordapp.com/emojis/1074467542409678971.webp?size=96&quality=lossless"

    webhook = DiscordWebhook(url=webhook_url, content='Just beamed the lorax again :skull:', username="Webhook Deleter 9000", avatar_url="https://i.imgflip.com/1pm297.jpg", rate_limit_retry=True)
    
    embed = DiscordEmbed(title=title, description=message, color='00FF00')
    embed.set_footer(text=footer, icon_url=smallimage)
    embed.set_image(url=image)
    embed.set_author(name="Powered by Once-Ler", url="https://github.com/thetrouper/Once-ler")

    webhook.add_embed(embed)

    webhook.execute()
    print("Credit sent (Please have good faith and do not delete or spam this webhook)")


def delete_webhook(webhook_url, name):
    response = requests.delete(webhook_url)
    if response.status_code == 200:
        print("Webhook successfully deleted!")
        send_credit(name)
    else:
        clipboard.copy(webhook_url)
        print("Error", "Failed to delete the webhook. Did someone get to it before you? " + webhook_url + " Copied the URL for you.")

def getProxies():
    print("Please hold while Onceler scrapes proxies for you...")
    proxy = FreeProxy(country_id=['US']).get()
    print("Found proxy: " + proxy)    


# Config:
print(r"""
 _____                                 __                      
/\  __`\                              /\ \                     
\ \ \/\ \     ___      ___      __    \ \ \         __   _ __  
 \ \ \ \ \  /' _ `\   /'___\  /'__`\   \ \ \  __  /'__`\/\`'__\
  \ \ \_\ \ /\ \/\ \ /\ \__/ /\  __/    \ \ \L\ \/\  __/\ \ \/ 
   \ \_____\\ \_\ \_\\ \____\\ \____\    \ \____/\ \____\\ \_\ 
    \/_____/ \/_/\/_/ \/____/ \/____/     \/___/  \/____/ \/_/ 
                                                           
----[ All in one URL Scraper, Webhook nuker, and Deleter. ]----
Changelog:
- [Added Proxy Scrapping]
- [Added our own webhook]
- [Updated the banner]
- [Added delayed requests]
- [added custom URL to scrape]
- [Added base64 option]
- [Removed PopUps]
""")
username = input("Who do you want to be credited as: ")
url = input("URL to scrape (use default for lorax URL): ")
useBase = input("Use base64 decode? (y/n): ")
delay = input("How long in between each attempt? (Miliseconds): ")
if url == "default": 
    url = "https://nigsa.000webhostapp.com/sanderfobup"
else: 
    url = url
run_nuke_periodically(url, username, useBase, delay)
