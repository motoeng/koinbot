import os
import telebot
from dotenv import load_dotenv
import requests


load_dotenv()

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])
chat_id = os.environ['CHAT_ID']

def send_message(message, link_preview=False, html=True):
    bot.send_message(
        chat_id,
        message,
        parse_mode='html' if html else None,
        link_preview_options=telebot.types.LinkPreviewOptions(is_disabled=not link_preview))

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
    send_message("""
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
/social
/whitepaper
/exchanges
/guides
/website
/programs
/rules
""")

#report
@bot.message_handler(commands=['report'])
def send_report(message):
    send_message("""
Admins, someone needs to be banned
@kuixihe @weleleliano @saleh_hawi @fifty2kph
""")


#website
@bot.message_handler(commands=['website'])
def send_website(message):
    send_message("https://koinos.io", True)


#stake
@bot.message_handler(commands=['stake'])
def send_stake(message):
    send_message("""
🔥 Burn KOIN (similar to staking) for 1 year and earn 4-7% APR!

❓ How does it work? See this video:
https://www.youtube.com/watch?v=v9bhaNLuDms

⛏️ Mining for KOIN with VHP
https://youtu.be/pa2kSYSdVnE?si=kxX4BBbjriL29x6m

⌨️ Run your own Node:
https://docs.koinos.io/validators/guides/running-a-node/

--or--

Join a Pool!
<a href="https://fogata.io">Fogata</a>
<a href="https://burnkoin.com">Burn Koin</a>
""")

#whitepaper
@bot.message_handler(commands=['whitepaper'])
def send_whitepaper(message):
    send_message("""
📄 <a href="https://koinos.io/whitepaper/">Official Whitepaper</a>

🎤️ <a href="https://podcast.thekoinpress.com/episodes/the-koinos-whitepaper">Koin Press PodCast on White Paper</a>

▶️ <a href="https://www.youtube.com/watch?v=v-qFFbDvV2c">Community Member Video</a>
""")


#Get KOIN Virtual Supply
def get_virtual_supply():
    url = 'https://checker.koiner.app/koin/virtual-supply'
    response = requests.get(url)
    data = response.json()
    return data


@bot.message_handler(commands=['supply'])
def handle_supply(message):
    data = get_virtual_supply()
    send_message(f"""The Virtual Supply ($KOIN+$VHP) is: {data}.

For more information, read about Koinos' <a href="https://docs.koinos.io/overview/tokenomics/">tokenomics!</a>""")


#Get VHP Total Supply
def get_vhp_supply():
    url = 'https://checker.koiner.app/vhp/total-supply'
    response = requests.get(url)
    data = response.json()
    return data


@bot.message_handler(commands=['vhpsupply'])
def handle_vhp_supply(message):
    data = get_vhp_supply()
    send_message(f"""The Total Supply of $VHP is: {data}.

For more information, read about Koinos' <a href="https://docs.koinos.io/overview/tokenomics/">tokenomics!</a>""")


#link to Koinos Forum Guides#
@bot.message_handler(commands=['guides', 'docs'])
def handle_guides(message):
    send_message("""
📄 <a href="https://docs.koinos.io">Official Koinos documentation</a>

🌁 <a href="https://www.youtube.com/watch?v=UFniurcWDcM">How to bridge with Chainge Finance</a>

🔮 <a href="https://docs.koinos.io/overview/mana/">Everything you need to know about Mana</a>
""")


#Link to Various social groups
@bot.message_handler(commands=['international'])
def handle_international(message):
    send_message("""🌍 Unofficial International Groups 🌏

🇩🇪 <a href="https://t.me/koinosgermany">Deutsch</a>
🇪🇸 <a href="https://t.me/koinoshispano">Español</a>
🇨🇳 <a href="https://t.me/koinos_cn">中文</a>
🇮🇹 <a href="https://t.me/+8KIVdg8vhIQ5ZGY0">Italiano</a>
🇮🇷 <a href="https://t.me/PersianKoinos">Persian</a>
🇹🇷 <a href="https://t.me/+ND37ePjNlvc4NGE0">Turkish</a>
🇷🇺 <a href="https://t.me/koinosnetwork_rus">Russian</a>
🇳🇱 <a href="https://t.me/KoinosNederland">Dutch</a>
""")


@bot.message_handler(commands=['exchange','exchanges','cex','buy'])
def handle_exchanges(message):
    send_message("""🔮 $KOIN is supported on the following exchanges

🌁 <b>Bridges</b>:
<a href="https://dapp.chainge.finance/?fromChain=ETH&toChain=ETH&fromToken=USDT&toToken=KOIN">Chainge</a>

🌐 <b>DEXs</b>:
<a href="https://app.uniswap.org/explore/tokens/ethereum/0xed11c9bcf69fdd2eefd9fe751bfca32f171d53ae">Uniswap</a>
<a href="https://app.koindx.com/swap">KoinDX</a>

📈 <b>CEXs</b>:
<a href="https://www.mexc.com/exchange/KOIN_USDT">MEXC</a>
<a href="https://bingx.com/en/spot/KOINUSDT/">BingX</a>
<a href="https://www.biconomy.com/exchange/KOIN_USDT">Biconomy</a>
<a href="https://www.coinstore.com/#/spot/KOINUSDT">Coinstore</a>
<a href="https://exchange.lcx.com/trade/KOIN-EUR">LCX</a>

🚨 Exchange Listings are always being pursued! We cannot discuss potential or in progress listings. \
You are free to request specific exchanges but do not be disappointed when you do not receive a response.
""")

#Mana Descriptor
@bot.message_handler(commands=['mana'])
def hanlde_mana(message):
    send_message("""
🔮 Mana is behind the magic of Koinos. Every KOIN inherently contains Mana, \
which is used when using the Koinos blockchain. And just like in video games, \
your Mana recharges over time letting you continue to use Koinos forever!

<a href="https://docs.koinos.io/overview/mana/">Learn more about Mana!</a>
""")


#Media Links
@bot.message_handler(commands=['media','social'])
def handle_media(message):
    send_message("""
🔮 <b>Official Koinos Media</b>
<a href="https://twitter.com/koinosnetwork">Koinos Network X</a>
<a href="https://twitter.com/TheKoinosGroup">Koinos Group X</a>
<a href="https://discord.koinos.io">Discord</a>
<a href="https://medium.com/koinosnetwork">Medium</a>
<a href="https://www.youtube.com/@KoinosNetwork">YouTube</a>

⚡ <b>Unofficial Koinos Media</b>
<a href="https://koinosnews.com/">Koinos News</a>
<a href="https://www.youtube.com/@motoengineer.koinos">motoengineer YouTube</a>
<a href="https://t.me/KoinosNews">Koinos News Telegram</a>
<a href="https://t.me/thekoinosarmy">Koinos Army Telegram</a>

Also check out /international for international communities!
""")


#Listing of Koinos Projects
@bot.message_handler(commands=['projects'])
def handle_projects(message):
    send_message("""
🔮 Existing Koinos Projects 🔮

📄 <b>dApps:</b>
<a href="https://koindx.com">KoinDX</a>
<a href="https://kollection.app">Kollection</a>
<a href="https://koincity.com">Koincity</a>
<a href="https://koinosbox.com/nicknames">Nicknames</a>
<a href="https://kanvas-app.com">Kanvas</a>
<a href="https://planetkoinos.com/space_striker.html">Space Striker</a>
<a href="https://koinosgarden.com">Koinos Garden</a>

⛏️ <b>Mining Pools:</b>
<a href="https://fogata.io">Fogata</a>
<a href="https://burnkoin.com">Burn Koin</a>

🔍 <b>Block Explorers:</b>
<a href="https://koiner.app">Koiner</a>
<a href="https://koinosblocks.com">KoinosBlocks</a>

💳 <b>Wallets:</b>
<a href="https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl">Kondor</a>
<a href="https://konio.io">Konio</a>
<a href="https://portal.armana.io">Portal</a>

💻 <b>Misc:</b>
<a href="https://planetkoinos.com/koinos_ai.html">Koinos AI</a>
""")


#Link to Koinos Roadmap
@bot.message_handler(commands=['roadmap'])
def handle_roadmap(message):
   send_message("""
📍 The official Koinos Network Roadmap:

https://koinos.io/
""")


#Link to price chat and MEXC
@bot.message_handler(commands=['price'])
def handle_price(message):
    send_message("""🚨 Please keep price chats out of this room. \
To talk about price, please visit the Koinos Army Chat Group!

<a href="https://t.me/thekoinosarmy">Koinos Army Telegram</a>

💵 Find the price of $KOIN here: https://www.coingecko.com/en/coins/koinos""")


#Provides information about Koinos Wallets
@bot.message_handler(commands=['wallets'])
def handle_wallets(message):
    send_message("""💳 These are the recommended wallets to use with Koinos!

⚡️ <b>Kondor Wallet</b> ⚡️
👉 Browser extension wallet for Chrome and Brave
Created by Julian Gonzalez
Open Sourced: https://github.com/joticajulian/kondor
Donate or sponsor Julians work:  https://github.com/sponsors/joticajulian
Link to download: https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl

⚡️ <b>Konio Wallet</b> ⚡️
👉 Mobile Wallet for iOS & Android
Created by Adriano Foschi
Open Sourced: https://github.com/konio-io/konio-mobile
Link to download: https://konio.io""")


#Give Claim Information
@bot.message_handler(commands=['claim'])
def handle_claim(message):
    send_message("""

⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️⚡️⚠️

CLAIM INFORMATION!

⚡️You are only eligible if you held your ERC-20 KOIN token during the snapshot. To verify, find your wallet address in this snapshot record: https://t.me/koinos_community/109226

⚡️You will need a Koinos Wallet to hold your main net $KOIN tokens! Use Kondor.

⚡️SAVE YOUR PRIVATE KEYS OR SEED PHRASES!!!!!!!!

⚡️Kondor Wallet is ONLY available for Chrome and Brave. Make sure you have the latest version!: https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl

⚡️ Video Tutorial on how to claim: https://youtu.be/l-5dHGqUSj4

 ⚡️Document tutorial on how to claim: https://medium.com/@kuixihe/a-complete-guide-to-claiming-koin-tokens-edd20e7d9c40.

⚡️There is no time limit to claiming. You may claim at any time you wish!
""")

def get_programs():
    url = 'https://deploy-preview-114--koinos-io.netlify.app/api/programs'
    response = requests.get(url)
    data = response.json()
    return data['programs']

@bot.message_handler(commands=['programs'])
def handle_programs(message):
    programs = get_programs()

    if len(programs) == 0:
        send_message("🚨 There are no featured programs at this time.")
        return

    message = "🔮 Koinos featured programs!\n"
    image = None

    for program in programs:
        message += """
⚡️ {title}
👉 {subtitle}
{shortDescription}
{url}
""".format_map(program)

        if image == None and program['images'] != None and program['images']['banner'] != None:
            image = program['images']['banner']
            image = 'https://deploy-preview-114--koinos-io.netlify.app/images/eok-image.png'

    if image != None:
        message = f"""<a href="{image}">&#8205;</a>""" + message

    send_message(message, True)

@bot.message_handler(commands=['rules','guidelines'])
def handle_rules(message):
    send_message("There are no rules!\n\n...yet")

bot.polling()


