import os
import telebot
from dotenv import load_dotenv
import requests


load_dotenv()

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])
chat_id = os.environ['CHAT_ID']

#welcome message
@bot.message_handler(func=lambda message: message.new_chat_members is not None)
def welcome_new_user(message):
    for user in message.new_chat_members:
        bot.send_message(
            message.chat.id,
            f"Welcome, {user.first_name}! Admins will NEVER DM you! Use /help for some quick info and feel free to ask questions!"
        )

#list of commands
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, """
You may use the following Commands:
/supply
/vhpsupply
/stake
/price
/wallets
/claim
/international
/projects
/roadmap
/media
/whitepaper
/buy
/guides
/website
""")

#report
@bot.message_handler(commands=['report'])
def send_report(message):
    bot.send_message(chat_id,"""
Admins, someone needs to be banned
@kuixihe @weleleliano @saleh_hawi @fifty2kph
""")


#website
@bot.message_handler(commands=['website'])
def send_website(message):
    bot.send_message(chat_id,"""
http://koinos.io
""")


#stake
@bot.message_handler(commands=['stake'])
def send_stake(message):
    bot.send_message(chat_id,"""
⚡Burn KOIN (similar to staking) for 1 year and earn 4-7% APR!

⚡How does it work? See this video:
https://www.youtube.com/watch?v=v9bhaNLuDms

⚡Mining for KOIN with VHP
https://youtu.be/pa2kSYSdVnE?si=kxX4BBbjriL29x6m

⚡Run your own Node:
https://docs.koinos.io/validators/guides/running-a-node/

--or--

Join a Pool!
https://fogata.io
https://burnkoin.com
""")

#whitepaper
@bot.message_handler(commands=['whitepaper'])
def send_whitepaper(message):
    bot.send_message(chat_id,"""

⚡Official Whitepaper: https://koinos.io/whitepaper/
⚡Koin Press PodCast on White Paper: https://podcast.thekoinpress.com/episodes/the-koinos-whitepaper
⚡Community Member Video: https://www.youtube.com/watch?v=v-qFFbDvV2c
""")

#social
@bot.message_handler(commands=['social'])
def send_social(message):
    bot.send_message(chat_id,"""

⚡Official Discord: https://discord.gg/VqvRhfHFHH
⚡Official Youtube: https://www.youtube.com/channel/UCamXqlj7q14TllcrCM0ikkw
⚡Website: http://koinos.io
⚡Claim Website: https://claim.koinos.io
⚡X/Twitter: http://x.com/koinosnetwork
⚡Youtube: http://youtube.com/koinosblockchain
⚡Development Docs: http://docs.koinos.io
""")


#Get KOIN Virtual Supply
def get_data1():
    url = 'https://checker.koiner.app/koin/virtual-supply'
    response = requests.get(url)
    data = response.json()
    return data


@bot.message_handler(commands=['supply'])
def send_data1(message):
    data = get_data1()
    bot.send_message(message.chat.id, f'The Virtual Supply ($KOIN+$VHP) is: {data}. For more information, see https://medium.com/@kuixihe/demystifying-the-koinos-blockchain-marketcap-7bf0baaa70fe')


#Get VHP Total Supply
def get_data2():
    url = 'https://checker.koiner.app/vhp/total-supply'
    response = requests.get(url)
    data = response.json()
    return data


@bot.message_handler(commands=['vhpsupply'])
def send_data2(message):
    data = get_data2()
    bot.send_message(message.chat.id, f'The Total Supply of $VHP is: {data}.')


#link to Koinos Forum Guides#
@bot.message_handler(commands=['guides', 'docs'])
def send_guides(message):
    bot.send_message(chat_id, """
⚡Koinos documentation can be found at https://docs.koinos.io

Bridging USDT via Chainge Finance: https://koinos-social.vercel.app/post/228/11

Everything You Need to Know About Mana: https://docs.koinos.io/overview/mana/
""")


#Link to Various social groups
@bot.message_handler(commands=['international'])
def send_international(message):
    bot.send_message(chat_id,"""🚨Non-Official International Groups!

Deutsch: https://t.me/koinosgermany
Español: https://t.me/koinoshispano
中文: https://t.me/koinos_cn
Italiano: https://t.me/+8KIVdg8vhIQ5ZGY0
Persian: https://t.me/PersianKoinos
Turkish: https://t.me/+ND37ePjNlvc4NGE0
Russian: https://t.me/koinosnetwork_rus
Dutch: https://t.me/KoinosNederland
""")


@bot.message_handler(commands=['exchange','exchanges','cex','buy'])
def send_exchange(message):
    bot.send_message(chait_id,"""⚡KOIN is supported on the following exchanges:

Chainge (Bridge): https://dapp.chainge.finance/?fromChain=ETH&toChain=ETH&fromToken=USDT&toToken=KOIN
Uniswap (DEX): https://app.uniswap.org/explore/tokens/ethereum/0xed11c9bcf69fdd2eefd9fe751bfca32f171d53ae
MEXC: https://www.mexc.com/exchange/KOIN_USDT
BingX: https://bingx.com/en/spot/KOINUSDT/
Biconomy: https://www.biconomy.com/exchange/KOIN_USDT
Coinstore: https://www.coinstore.com/#/spot/KOINUSDT
LCX: https://exchange.lcx.com/trade/KOIN-EUR
KoinDX (DEX): https://app.koindx.com/swap

🚨Exchange Listings are always being pursued! We cannot discuss potential or in progress exchange listings. \
You are free to request specific exchanges but do not be disappointed when you do not receive a response.
""")

#Mana Descriptor
@bot.message_handler(commands=['mana'])
def send_mana(message):
    bot.send_message(chat_id,"""
⚡Koinos blockchain features a new concept called “mana” that is the most innovative solution to the halting problem since the invention of Ethereum’s “gas.”
It is a property of the KOIN token that gets “consumed” as a user performs fee-less transactions,
but that also regenerates over time (100% in 5 days).
""")


#Media Links
@bot.message_handler(commands=['media','social'])
def send_international(message):
    bot.send_message(chat_id,"""

⚡Koinos Media Links
Twitter: https://twitter.com/TheKoinosGroup
Twitter: https://twitter.com/koinosnetwork
Discord: https://discord.koinos.io
YouTube: https://www.youtube.com/@KoinosBlockchain
Medium: https://medium.com/koinosnetwork

⚡Unofficial:
Koinos News: https://koinosnews.com/
motoengineer YouTube: https://www.youtube.com/@motoengineer.koinos
Koinos Telegram News: https://t.me/KoinosNews
""")


#Listing of Koinos Projects
@bot.message_handler(commands=['projects'])
def send_projects(message):
    bot.send_message(chat_id,"""
⚡Existing Koinos Projects!

📄dApps:
KoinDX: http://koindx.com
Kollections: http://kollection.app
Koin City http://koincity.com
Nicknames https://koinosbox.com/nicknames
Kanvas http://kanvas-app.com
Space Striker http://planetkoinos.com/space_striker.html
Koinos Garden http://koinosgarden.com

⛏️Mining Pools:
Fogata: http://fogata.io
BurnKoin: http://burnkoin.com

🔍Block Explorers:
Koiner: http://koiner.app
KoinosBlocks: http://koinosblocks.com

💳Wallets:
Kondor Wallet: https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl
Konio Wallet: http://konio.io
Portal: http://portal.armana.io

💻Misc:
Koinos AI: http://planetkoinos.com/koinos_ai.html
""")


#Link to Koinos Roadmap
@bot.message_handler(commands=['roadmap'])
def send_roadmap(message):
   bot.send_message(chat_id,"""
⚡The official Koinos Network Roadmap:
https://koinos.io/
""")


#Link to price chat and MEXC
@bot.message_handler(commands=['price'])
def send_price(message):
    bot.send_message(chat_id, """🚨Please keep price chats out of this room!
🚨To talk about price, please visit the Koinos Army Chat Group!

Link:⚡️https://t.me/thekoinosarmy

💵Find the price of $KOIN here: https://www.coingecko.com/en/coins/koinos""")


#Provides information about Koinos Wallets
@bot.message_handler(commands=['wallets'])
def send_wallets(message):
    bot.send_message(chat_id, """🚨These are the recommended wallets to use with Koinos!🚨

⚡️Kondor Wallet⚡️
👉Browser extension wallet for Chrome and Brave
Created by Julian Gonzalez
Open Sourced: https://github.com/joticajulian/kondor
Donate or sponsor Julians work:  https://github.com/sponsors/joticajulian
Link to download: https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl

⚡️Konio Wallet⚡️
👉Mobile Wallet for iOS & Android
Created by Adriano Foschi
Open Sourced: https://github.com/konio-io/konio-mobile
Link to download: http://konio.io""")


#Give Claim Information
@bot.message_handler(commands=['claim'])
def send_claim(message):
    bot.send_message(chat_id, """

⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️

CLAIM INFORMATION!

⚡️You are only eligible if you held your ERC-20 KOIN token during the snapshot. To verify, find your wallet address in this snapshot record: https://t.me/koinos_community/109226

⚡️You will need a Koinos Wallet to hold your main net $KOIN tokens! Use Kondor or My Koinos Wallet

⚡️SAVE YOUR PRIVATE KEYS OR SEED PHRASES!!!!!!!!

⚡️Kondor Wallet is ONLY available for Chrome and Brave. Make sure you have the latest version!: https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl

⚡️ Video Tutorial on how to claim: https://youtu.be/l-5dHGqUSj4

 ⚡️Document tutorial on how to claim: https://medium.com/@kuixihe/a-complete-guide-to-claiming-koin-tokens-edd20e7d9c40.

⚡️There is no time limit to claiming. You may claim at any time you wish!
""")

def get_programs():
    url = 'https://koinos.io/api/featured-programs'
    response = requests.get(url)
    data = response.json()
    return data

@bot.message_handler(commands=['programs'])
def send_programs(message):
    programs = get_programs()

    if len(programs) == 0:
        bot.send_message("🚨There are no featured programs at this time.")
        return

    message = "⚡️Koinos featured programs!⚡️\n"

    for program in programs:
        message += """
⚡️{name}
👉{subtitle}
{shortDescription}
{website}
""".formatMap(program)

    bot.send_message(message)

bot.polling()


