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



# First, we import all the modules that will be needed.

import discord
import os
import requests
import json
import random
from bs4 import BeautifulSoup
from keep_alive import keep_alive

# We save the "greeting" words to be checked in the content of the message to the "salute" list, and the messages to be responded to in the "takeTheSalute" list.

salute = ["selam","Selam","slm","Selam","merhaba","Merhaba"]
takeTheSalute = ["Aleyküm Selam","as","As","AS","Aleyküm Selam Çok Sevgili Mümin Kardeşim","Merhaba!"]

# We save the depressive keywords to be checked in the message content.

depressiveWords = ["üzgün","kızgın","ağlamaklı","yalnız","çaresiz","depresif","yıkık","terkedilmiş"]

# We are starting Discord events.

client = discord.Client()

# We get Ege Fitness quotes from a website using web scraping. <https://gymsozluk.com/blog/ege-fitness-sozleri/>

url = "https://gymsozluk.com/blog/ege-fitness-sozleri/"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
egeFitnessQuotes = soup.find().find_all("p")

# We pull inspirational quotes using the ZenQuotes API. <https://zenquotes.io/>

def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  jsonData = json.loads(response.text)
  quote = jsonData[0]["q"] + " -" + jsonData[0]["a"]
  return(quote)

# We get over 180 Mustafa Kemal ATATÜRK quotes using the Atatürk Sözleri API. <https://github.com/orhanemree/ataturk-sozleri-api>

def getMkaQuote():
  response = requests.get("https://ataturk-sozleri-api.herokuapp.com/")
  jsonData = json.loads(response.text)
  mkaQuote = jsonData["quote"]
  return mkaQuote

# We have manually saved the Turkish versions of the quotes from Fight Club to the list below.

fightClubQuotes = ["Eski bir deyiş vardır… İnsanlar hep sevdiklerini incitir diye. Bu hep iki yönlüdür aslında.","Hangisi daha kötü, cehennem mi, hiçlik mi?","Başıma bir silah daya ve duvarları beynimle boya .","Acı ve çelişki olmasaydı hiçbir şeyimiz olmazdı.","Sahip olduklarının bir gün kölesi olursun.","Acı ve fedakarlık olmadan hiçbir şey yapamazsın.","Sen başıma gelen en kötü şeysin.","Bizim büyük savaşımız kendi ruhlarımızla. Büyük ruhlarımız ise hayatlarımız.","Ancak her şeyi kaybettikten sonra her şeyi yapmakta özgür oluruz.","Bir tümörüm olsa, adını Marla koyardım.","Babalarımız bizim için tanrı modeliydi.","Sahip olduklarımız bize sahip oluyor.","Zaman geçtikçe sıfır noktasına yaklaşıyoruz.","Ağzınızda bir silah varken ve silahın namlusu dişlerinizin arasındayken ancak sesli harflerle konuşabilirsiniz.","Hiçbir zaman kusursuz olmayayım.","Kurtar beni, tyler, kusursuz ve tamamlanmış olmaktan kurtar.","Gülüşünde iğrenc bir çaresizlik var.","Ben Jack’in dışlanmışlık hissedeniyim.","Bize dünyanın b*kundan ve pisliğinden başka bir şey bırakmadılar.","Her şeyi kontrol etmeye çalışmaktan vazgeç. Bırak ne olacaksa olsun. Bırak olsun. (Tyler)","Başka bir yerde, başka bir zamanda uyanabilseydim, başka bir insan olarak uyanabilir miydim?","Hiçbir zaman tamamlanmış olmayayım, ne olur.","Hiçbir zaman halimden memnun olmayayım.","Dibe vurmadan özgür olamazsın.","Kavga etmeden nasıl bir şey olduğunu bilemeyiz. Yara izim olmadan ölmek istemiyorum. Hadi, hevesim geçmeden vur bir tane!","İnsan sevdiğini öldürür diye bir söz vardır ya. Aslında bakın, insanı öldüren hep sevdiğidir.","Bizim neslimiz Büyük Depresyon’u ya da Büyük Savaş’ı yaşamadı. Bizim savaşımız ruhsal bir savaş. Bizim depresyonumuz kendi hayatlarımız.","Kendini geliştirmek mastürbasyondur, kendini yok etmek ise asıl soruların cevabı…","Sizler işiniz değilsiniz. Sizler paranız kadar değilsiniz. Sizler bindiğiniz arabalarınız değilsiniz. Kredi kartlarınızın limitleri değilsiniz. Sizler iç çamaşırı değilsiniz. Sizler dünyanın dans edip şarkı söyleyen pisliklerisiniz.","Tüm umudunuzu kaybetmek özgürlüktür.","Hepimiz aynı pisliğin lacivertleriyiz.","Damağındaki o küçük çizik, dilinle oynamasan hemen geçer ama duramıyorsun. Oynuyorsun.","Marla! Beni garip bir dönemimde tanıdın."]

# We make it notify when successful login to Discord.

@client.event
async def on_ready():
  print("{0.user} olarak giriş yapıldı.".format(client))  
  
@client.event
async def on_message(message):
  
  # We make sure it doesn't moderate its own messages.
  
  if message.author == client.user:
    return

  # We make it respond directly to the command.
  
  elif message.content.startswith("$hello"):
    await message.channel.send("Hello!")
    
  elif message.content.startswith("$selam"):
    await message.channel.send("Selam!")
  
  elif message.content.startswith("$sa"):
    await message.channel.send("Aleyküm Selam!")
  
  # We make it return random inspirational quotes we get from ZenQuotes.
  
  elif message.content.startswith("$ilham"):
    quote = getQuote()
    await message.channel.send(quote)
  
  # We make it return the random Mustafa Kemal ATATÜRK word it gets from the Atatürk Sözleri API.
  
  elif message.content.startswith("$mka"):
    quote = getMkaQuote()
    await message.channel.send(quote)
  
  # We make it return the Fight Club quotes we received manually.
  
  elif message.content.startswith("$fightclub") or message.content.startswith("$tylerdurden"):
    await message.channel.send(random.choice(fightClubQuotes))
  
  # We make it return the Ege Fitness words we obtained with web scraping.
  
  elif message.content.startswith("$egefitness"):
    await message.channel.send(str(random.choice(egeFitnessQuotes)).replace("<p>","").replace("</p>","").replace("<br/>",""))
  
  # We make it automatically read and audit messages.
  
  msg = message.content
  
  # We provide random responses to the detected "greeting" words.
  
  if any(word in msg for word in salute):
    await message.channel.send(random.choice(takeTheSalute))
  
  # We make sure that he responds to messages with depressive content with the words of EgeFitness.
  
  if any(word in msg for word in depressiveWords):
    await message.channel.send(str(random.choice(egeFitnessQuotes)).replace("<p>","").replace("</p>","").replace("<br/>",""))

# We ensure that the bot stays online 24/7 by receiving 1 HTTP request in 5 minutes.
    
keep_alive()

# We call the necessary variable TOKEN so that the bot can log into Discord.

client.run(os.environ['TOKEN'])
