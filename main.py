import os
import cloudscraper
from dhooks import Webhook, Embed
import requests

print("Webhook is ready")

webhook = Webhook("https://discord.com/api/webhooks/1059402304178114570/7rkHpv78VL0i3PP1LIWiRRxdiCacIxThMeWh7ehF1jzAvFAnfdQEgE4q82qSg1gJT0h2")
scraper = cloudscraper.create_scraper()

rain_active = False
while True:
  if rain_active == False:
    r = scraper.get("https://api.bloxflip.com/chat/history").json()['rain']
    if r['active'] == True:
      prize = str(r['prize'], ",")[:-2]
      host = r['host']
      getduration = r['duration']
      convert = (getduration/(1000*60))%60
      duration = (int(convert))
      userid = requests.get(f"https://api.roblox.com/users/get-by-username?username={host}").json()['Id']
      thumburl = (f"https://www.roblox.com/headshot-thumbnail/image?userId={userid}&height=50&width=50&format=png")
      embed = Embed(title=f"{host} is hosting a chat rain!", url="https://bloxflip.com", color=0xFFC800)
      embed.add_field(name="Rain Amount", value=f"{prize} R$", inline=True)
      embed.add_field(name="Expiration", value=f"{duration} minutes", inline=True)
      embed.add_field(name="Host", value=f"[{host}](https://www.roblox.com/users/{userid}/profile)", inline=True)
      embed.set_timestamp()
      embed.set_thumbnail(url=thumburl)
      webhook.send("@everyone", embed=embed)
      if r['active'] == True:
        print(f"Bloxflip Rain!\nRain Amount:\n{prize}\nExpiration\n{duration}\nHost\n{host}")
        rain_active = True
      else:
        rain_active = False
