# © Copyright 2022 Yusuf Özçetin
#
# This file is part of EgoistBot.
#
# EgoistBot is free software: you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# EgoistBot is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with EgoistBot. If not, see
# <https://www.gnu.org/licenses/>.

# First, import all the necessary modules.

import discord
from discord import app_commands
import os
import requests
import json
import random
from bs4 import BeautifulSoup
from keep_alive import keep_alive

# The 'getAtaturkQuote()' function has been completely revamped! Now it powers up from the AtaturkQuotesAPI. For detailed information, see: https://github.com/egoistpizza/AtaturkQuotesAPI

def getAtaturkQuote(lang = "tr"):
  try:
    
      # Send a GET request to the AtatürkQuotesAPI
      response = requests.get(f"http://3.147.64.168/{lang}")

      # Check if the request was successful (status code 200)
      if response.status_code == 200:
        
          # Parse the JSON response
          json_data = response.json()

          # Check if the "quote" key exists in the JSON data
          if 'quote' in json_data:
            
              # Return the Atatürk quote as a string
              return json_data['quote']
            
          else:
              return "Error: 'quote' key not found in JSON response"

      else:
          return f"Error: Unable to fetch Atatürk quote. Status Code: {response.status_code}"

  except Exception as e:
      return f"Error: {str(e)}"

# Define a list of greeting words to detect greetings in the message content and a list of corresponding responses for those greetings.

salute = ["selam", "Selam", "slm", "Selam", "merhaba", "Merhaba"]
takeTheSalute = [
    "Aleyküm Selam", "as", "As", "AS",
    "Aleyküm Selam Çok Sevgili Mümin Kardeşim", "Merhaba!"
]

# Define a list of depressive keywords to check in the message content.

depressiveWords = [
    "üzgün", "kızgın", "ağlamaklı", "yalnız", "çaresiz", "depresif", "yıkık",
    "terkedilmiş"
]

# Initialize the Discord events.

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Define a command called "getping" that responds with the current latency.

@tree.command(name="getping",
              description="Pong!",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def getping(interaction):
    await interaction.response.send_message(
        f"Pong! In {round(client.latency * 1000)}ms")

# Scrape Ege Fitness quotes from a website. <Source: https://gymsozluk.com/blog/ege-fitness-sozleri/>

url = "https://gymsozluk.com/blog/ege-fitness-sozleri/"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
egeFitnessQuotes = soup.find().find_all("p")

# Fetch inspirational quotes using the ZenQuotes API. <https://zenquotes.io/>

def getQuote():
    response = requests.get("https://zenquotes.io/api/random")
    jsonData = json.loads(response.text)
    quote = jsonData[0]["q"] + " -" + jsonData[0]["a"]
    return (quote)

# Manually store Turkish "Fight Club" quotes in the following list.

fightClubQuotes = [
    "Eski bir deyiş vardır… İnsanlar hep sevdiklerini incitir diye. Bu hep iki yönlüdür aslında.",
    "Hangisi daha kötü, cehennem mi, hiçlik mi?",
    "Başıma bir silah daya ve duvarları beynimle boya .",
    "Acı ve çelişki olmasaydı hiçbir şeyimiz olmazdı.",
    "Sahip olduklarının bir gün kölesi olursun.",
    "Acı ve fedakarlık olmadan hiçbir şey yapamazsın.",
    "Sen başıma gelen en kötü şeysin.",
    "Bizim büyük savaşımız kendi ruhlarımızla. Büyük ruhlarımız ise hayatlarımız.",
    "Ancak her şeyi kaybettikten sonra her şeyi yapmakta özgür oluruz.",
    "Bir tümörüm olsa, adını Marla koyardım.",
    "Babalarımız bizim için tanrı modeliydi.",
    "Sahip olduklarımız bize sahip oluyor.",
    "Zaman geçtikçe sıfır noktasına yaklaşıyoruz.",
    "Ağzınızda bir silah varken ve silahın namlusu dişlerinizin arasındayken ancak sesli harflerle konuşabilirsiniz.",
    "Hiçbir zaman kusursuz olmayayım.",
    "Kurtar beni, tyler, kusursuz ve tamamlanmış olmaktan kurtar.",
    "Gülüşünde iğrenc bir çaresizlik var.",
    "Ben Jack’in dışlanmışlık hissedeniyim.",
    "Bize dünyanın b*kundan ve pisliğinden başka bir şey bırakmadılar.",
    "Her şeyi kontrol etmeye çalışmaktan vazgeç. Bırak ne olacaksa olsun. Bırak olsun. (Tyler)",
    "Başka bir yerde, başka bir zamanda uyanabilseydim, başka bir insan olarak uyanabilir miydim?",
    "Hiçbir zaman tamamlanmış olmayayım, ne olur.",
    "Hiçbir zaman halimden memnun olmayayım.",
    "Dibe vurmadan özgür olamazsın.",
    "Kavga etmeden nasıl bir şey olduğunu bilemeyiz. Yara izim olmadan ölmek istemiyorum. Hadi, hevesim geçmeden vur bir tane!",
    "İnsan sevdiğini öldürür diye bir söz vardır ya. Aslında bakın, insanı öldüren hep sevdiğidir.",
    "Bizim neslimiz Büyük Depresyon’u ya da Büyük Savaş’ı yaşamadı. Bizim savaşımız ruhsal bir savaş. Bizim depresyonumuz kendi hayatlarımız.",
    "Kendini geliştirmek mastürbasyondur, kendini yok etmek ise asıl soruların cevabı…",
    "Sizler işiniz değilsiniz. Sizler paranız kadar değilsiniz. Sizler bindiğiniz arabalarınız değilsiniz. Kredi kartlarınızın limitleri değilsiniz. Sizler iç çamaşırı değilsiniz. Sizler dünyanın dans edip şarkı söyleyen pisliklerisiniz.",
    "Tüm umudunuzu kaybetmek özgürlüktür.",
    "Hepimiz aynı pisliğin lacivertleriyiz.",
    "Damağındaki o küçük çizik, dilinle oynamasan hemen geçer ama duramıyorsun. Oynuyorsun.",
    "Marla! Beni garip bir dönemimde tanıdın."
]

# Send a Mustafa Kemal Atatürk quote. * New languages added. *

@tree.command(name="mka-tr",
              description="Türkçe - Mustafa Kemal Atatürk alıntısı.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote())

@tree.command(name="mka-en",
              description="English - Mustafa Kemal Atatürk quote.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("en"))

@tree.command(name="mka-zh",
              description="中文 - 穆斯塔法-凯末尔-阿塔图尔克名言。",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("zh"))

@tree.command(name="mka-fr",
              description="Français - Citation de Mustafa Kemal Atatürk.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("fr"))

@tree.command(name="mka-de",
              description="Deutsch - Mustafa Kemal Atatürk Zitat.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("de"))

@tree.command(name="mka-it",
              description="Italiano - Citazione di Mustafa Kemal Atatürk.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("it"))

@tree.command(name="mka-ja",
              description="日本語 - ムスタファ・ケマル・アタチュルクの言葉。",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("ja"))

@tree.command(name="mka-ko",
              description="한국어 - 무스타파 케말 아타튀르크 인용문.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("ko"))

@tree.command(name="mka-pl",
              description="Polski - cytat Mustafy Kemala Atatürka.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("pl"))

@tree.command(name="mka-ru",
              description="На русском языке - цитата Мустафы Кемаля Ататюрка.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("ru"))

@tree.command(name="mka-es",
              description="Español - Cita de Mustafa Kemal Atatürk.",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def mka(interaction):
    await interaction.response.send_message(getAtaturkQuote("es"))

# Retrieve and send a quote from Ege Fitness obtained through web scraping.

@tree.command(name="egefitness",
              description="Ege Fitness alıntısı",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def egefitness(interaction):
    await interaction.response.send_message(
        (str(random.choice(egeFitnessQuotes)).replace("<p>", "").replace(
            "</p>", "").replace("<br/>", "")))

# Retrieve and send random inspirational quotes from ZenQuotes. (SlashCommand)

@tree.command(name="inspiration",
              description="A random inspirational quote",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def inspiration(interaction):
    quote = getQuote()
    await interaction.response.send_message(quote)

# Send one of the stored Fight Club quotes when requested. (SlashCommand)

@tree.command(name="tylerdurden",
              description="Tyler Durden (Fight Club) alıntısı",
              guild=discord.Object(os.environ['TEST_GUILD_ID']))
async def tylerdurden(interaction):
    await interaction.response.send_message(random.choice(fightClubQuotes))

# Notify when the bot is successfully logged into Discord.

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(os.environ['TEST_GUILD_ID']))
    print("Ready!")

# Detect in-line commands and respond accordingly.

@client.event
async def on_message(message):

    # Exclude the bot's own messages from observation.

    if message.author == client.user:
        return

    # Handle specific commands and respond accordingly.

    elif message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    elif message.content.startswith("$selam"):
        await message.channel.send("Selam!")

    elif message.content.startswith("$sa"):
        await message.channel.send("Aleyküm Selam!")

    # Retrieve and send random inspirational quotes from ZenQuotes.

    elif message.content.startswith("$ilham"):
        quote = getQuote()
        await message.channel.send(quote)

    # Retrieve and send a random Mustafa Kemal Atatürk quote from the Atatürk Sözleri API.

    elif message.content.startswith("$mka"):
        quote = getMkaQuote()
        await message.channel.send(quote)

    # Send one of the stored Fight Club quotes when requested.

    elif message.content.startswith(
            "$fightclub") or message.content.startswith("$tylerdurden"):
        await message.channel.send(random.choice(fightClubQuotes))

    # Retrieve and send a quote from Ege Fitness obtained through web scraping.

    elif message.content.startswith("$egefitness"):
        await message.channel.send(
            str(random.choice(egeFitnessQuotes)).replace("<p>", "").replace(
                "</p>", "").replace("<br/>", ""))

    # Automatically read and audit messages.

    msg = message.content

    # Respond with random greetings to detected greeting words.

    if any(word in msg for word in salute):
        await message.channel.send(random.choice(takeTheSalute))

    # Respond with Ege Fitness quotes to messages containing depressive content.

    if any(word in msg for word in depressiveWords):
        await message.channel.send(
            str(random.choice(egeFitnessQuotes)).replace("<p>", "").replace(
                "</p>", "").replace("<br/>", ""))

# Keep the bot online 24/7 by receiving 1 HTTP request every 5 minutes.

keep_alive()

# Log the bot into Discord using the TOKEN variable.

client.run(os.environ['TOKEN'])
