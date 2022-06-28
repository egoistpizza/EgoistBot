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

from flask import Flask
from threading import Thread

# Flask is a web application framework.
# Through this code and UptimeRobot, EgoistBot receives 1 HTTP request every 5 minutes, so it has the ability to be online 24/7.

app = Flask('')

@app.route('/')

def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
