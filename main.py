#!/usr/bin/env python3
# -*- coding : utf-8 -*-

#
#   Peitify - DiscordBot
#       for - Peilien Youtube Channel
#

msg = r"""
   ___      _ __  _ ___    
  / _ \___ (_) /_(_) _/_ __
 / ___/ -_) / __/ / _/ // /
/_/   \__/_/\__/_/_/ \_, / 
                    /___/   

    【Peitify - DiscordBot】
                for - Youtube : Peilien Channel

"""

import os
import sys
import logging

import discord

import tools.file
import tools.global_const as g


print(msg)

#======================================================================
# logging設定
# MEMO : https://zenn.dev/dencyu/articles/2b58f669bcd473

# Example:
# logger.debug("message") # デバッグ用ログ
# logger.info("message") # 通常ログ
# logger.warning("message") # 処理の続行が可能なレベルのワーニングログ
# logger.error("message") # 処理の続行が不可能なレベルのエラーログ
# logger.critical("message") # スクリプト全体に影響が出るレベルのクリティカルエラーログ

logger = logging.getLogger("Peitify")
logger.setLevel(logging.DEBUG)

format = "%(levelname)-9s %(asctime)s [%(filename)s:%(lineno)d] %(message)s"

st_handler = logging.StreamHandler()
st_handler.setLevel(logging.DEBUG)
st_handler.setFormatter(logging.Formatter(format))

fl_handler = logging.FileHandler(filename="peitify_system.log", encoding="utf-8")
fl_handler.setLevel(logging.DEBUG)
fl_handler.setFormatter(logging.Formatter(format))

logger.addHandler(st_handler)
logger.addHandler(fl_handler)

logger.info("Peitify - STARTUP")


#======================================================================
# config.yaml 読み込み
data = tools.file.load_yaml("config.yaml")

if not tools.file.validation_config(data):
    logger.error("configファイルのバリデーションチェックに失敗しました")
    sys.exit()

g.TOKEN = data["TOKEN"]

logger.info("configファイルを正常にロードしました")


#======================================================================

bot = discord.Bot(intents=discord.Intents.all())

#======================================================================
# 起動時に実行
@bot.event
async def on_ready():
    logger.info("Discordにログインしました")

    g.BOT_AUTHOR_ID = bot.user.id
    g.BOT_AUTHOR_NAME = bot.user.name

    logger.info("以下のBotアカウントでログインしています")
    logger.info("UserName  :  " + bot.user.name)
    logger.info("UserID    :  " + str(bot.user.id))

#======================================================================

# cogsディレクトリ以下の.pyファイルをCogとしてロード
for file_name in os.listdir("cogs"):
    if file_name.endswith(".py"):
        bot.load_extension(f"cogs.{file_name[:-3]}")


bot.run(g.TOKEN)
