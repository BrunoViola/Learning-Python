import discord
import requests

def get_weather(city):
   base_url = f"http://wttr.in/{city}?format=%C+%t&lang=en"
   try:
       response = requests.get(base_url)
       response.raise_for_status()
       return response.text.strip()
   except requests.RequestException as e:
       print(f"There was an error while I was trying to get the weather: {e}")
       return "I couldn't get the weather for this city."

class MyClient(discord.Client):
   async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))
   
   async def on_message(self, message):
      if message.author == self.user:
         return

      if message.content.startswith('$'):
         city = message.content[1:]
         weather_info = get_weather(city)
         await message.channel.send(weather_info)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('TOKEN')