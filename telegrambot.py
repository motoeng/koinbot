import os
import telebot
from dotenv import load_dotenv
import requests


load_dotenv()

bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])
chat_id = os.environ['CHAT_ID']

def get_programs():
    url = 'https://deploy-preview-114--koinos-io.netlify.app/api/programs'
    response = requests.get(url)
    data = response.json()
    return data['programs']

def make_program_blurb(program):
    return """⚡️ <b><a href="{url}">{title}</a></b>
👉 {subtitle}
{shortDescription}
""".format_map(program)

def send_message(message, link_preview=False, html=True):
    bot.send_message(
        chat_id,
        message,
        parse_mode='html' if html else None,
        link_preview_options=telebot.types.LinkPreviewOptions(is_disabled=not link_preview))

#welcome message
@bot.message_handler(func=lambda message: message.new_chat_members is not None)
def welcome_new_user(message):
    programs = get_programs()
    top_program_message = None
    has_program_image = False

    if len(programs) > 0:
        program = programs[0]

        top_program_message = f"""
🔮 Featured Program:

{make_program_blurb(program)}
"""

        if program['images'] != None and program['images']['banner'] != None:
            has_program_image = True
            top_program_message = f"""<a href="{program['images']['banner']}">&#8205;</a>"""

    for user in message.new_chat_members:
        message = f"""Welcome {user.first_name}!

We are glad you are here! To get started, we recommend you take a look at current /programs and take a moment to review the /rules.

Please feel free to ask questions.

🚨 Remember: Admins will never DM you first. They will never ask for your keys or seed phrases. \
If you suspect someone is impersonating an admin, please /report them.
"""

        if top_program_message != None:
            message += top_program_message

        send_message(message, link_preview=has_program_image)

#list of commands
@bot.message_handler(commands=['help'])
def send_help(message):
    send_message("""
You may use the following Commands:
/claim
/guides
/exchanges
/international
/price
/programs
/projects
/roadmap
/rules
/social
/stake
/supply
/vhpsupply
/wallets
/website
/whitepaper
""")

#report
@bot.message_handler(commands=['report'])
def send_report(message):
    send_message("""
Admins, someone needs to be banned
@kuixihe @weleleliano @saleh_hawi @fifty2kph
""")


#website
@bot.message_handler(commands=['website', 'websites'])
def send_website(message):
    send_message('<a href="https://koinos.io">Koinos Website</a>', True)


#stake
@bot.message_handler(commands=['stake'])
def send_stake(message):
    send_message("""
🔥 Burn KOIN (similar to staking) for 1 year and earn 4-8% APR!

❗ <a href="https://www.youtube.com/watch?v=v9bhaNLuDms">Koinos Overview: Minders, Holders, and Developers</a>

⛏️ <a href="https://youtu.be/pa2kSYSdVnE?si=kxX4BBbjriL29x6m">How to mine $KOIN with $VHP</a>

⌨️ <a href="https://docs.koinos.io/validators/guides/running-a-node/">Run your own node</a>

<b>--or--</b>

🔥 Join a Pool!
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

For more information, read about Koinos' <a href="https://docs.koinos.io/overview/tokenomics/">tokenomics</a>!""")


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

For more information, read about Koinos' <a href="https://docs.koinos.io/overview/tokenomics/">tokenomics</a>!""")


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
📍 <a href="https://koinos.io/">The official Koinos Network roadmap</a>
""")


#Link to price chat and MEXC
@bot.message_handler(commands=['price'])
def handle_price(message):
    send_message("""🚨 Please keep price chats out of this group. \
To talk about price, please visit the <a href="https://t.me/thekoinosarmy">Koinos Army Telegram</a>!

💵 Find the price of $KOIN on <a href="https://www.coingecko.com/en/coins/koinos">CoinGecko</a>.""")


#Provides information about Koinos Wallets
@bot.message_handler(commands=['wallets'])
def handle_wallets(message):
    send_message("""💳 These are the recommended wallets to use with Koinos! \
Choose one or use a combination for security and accessibility!

⚡️ <a href="https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl"><b>Kondor Wallet</b></a>
💻 Browser extension wallet for Chrome and Brave
Created by Julian Gonzalez
<a href="https://github.com/joticajulian/kondor">Kondor Github</a>
<a href="https://github.com/sponsors/joticajulian">Sponsor Julian</a>

⚡️ <a href="https://konio.io"><b>Konio Wallet</b></a>
📱 Mobile Wallet for iOS & Android
Created by Adriano Foschi
<a href="https://github.com/konio-io/konio-mobile">Koinio Github</a>

⚡️ <a href="https://tangem.com"><b>Tangem Wallet</b></a>
📱 Hardware Wallet for iOS & Android
More secure but less dApp support
""")


#Give Claim Information
@bot.message_handler(commands=['claim'])
def handle_claim(message):
    send_message("""

⚠️ Claim information ⚠️

⚡️ You are only eligible if you held your ERC-20 KOIN token during the snapshot. \
To verify, find your wallet address in this <a href="https://t.me/koinos_community/109226">snapshot record</a>.

⚡️ You will need a Koinos Wallet to hold your main net $KOIN tokens! Use \
<a href="https://chrome.google.com/webstore/detail/kondor/ghipkefkpgkladckmlmdnadmcchefhjl">Kondor</a> to manage your $KOIN.

🚨 SAVE YOUR PRIVATE KEYS OR SEED PHRASES!!! 🚨

🚨 Seriously, did you back up your private key or seed phrase? We cannot recover them if you lose them.

▶️ <a href="https://youtu.be/l-5dHGqUSj4">Video Tutorial on how to claim.</a>

📄 <a href="https://medium.com/@kuixihe/a-complete-guide-to-claiming-koin-tokens-edd20e7d9c40">Document tutorial on how to claim.</a>

⚡️ There is no time limit to claiming. You may claim at any time you wish!
""")

@bot.message_handler(commands=['programs'])
def handle_programs(message):
    programs = get_programs()

    if len(programs) == 0:
        send_message("🚨 There are no featured programs at this time.")
        return

    message = "🔮 Koinos featured programs!\n"
    image = None

    for program in programs:
        message += make_program_blurb(program)

        if image == None and program['images'] != None and program['images']['banner'] != None:
            image = program['images']['banner']

    if image != None:
        message = f"""<a href="{image}">&#8205;</a>""" + message

    send_message(message, True)

@bot.message_handler(commands=['rules','guidelines'])
def handle_rules(message):
    send_message("""Welcome to the Koinos Telegram community!

We kindly ask that you follow a few rules to help foster a positive environment which will in turn foster innovation!

✅ <b>Share and discuss your projects</b>
We strongly encourage builders to talk about their products, share current features, discuss future plans, \
and seek feedback.

✅ <b>Focus on building and innovation</b>
Engage in discussions about dApps, their features, user experiences, and upcoming developments.

✅ <b>Embrace constructive feedback</b>
Constructive feedback is actionable information which helps improve products and services. \
If your feedback doesn't provide a pathway for improvement, please reconsider sharing it.

✅ <b>Professional and respectful tone</b>
Be courteous, offer constructive feedback, and ensure conversations remain valuable for all members, especially newcomers.

✅ <b>Contribute to the ecosystem</b>
Offer insights, share resources, and provide feedback that helps the community grow and learn.

✅ <b>Avoid promotion of non-utility tokens and projects</b>
Please refrain from promoting non-dApp items such as meme tokens, non-utility NFTs, or other projects that \
do not contribute meaningful utility to the Koinos ecosystem. If you would like to do this, please consider \
joining the <a href="https://t.me/thekoinosarmy">Koinos Army Telegram</a>.

✅ <b>Avoid off-topic and nonsensical content</b>
Please avoid filling it with off-topic discussions. For more relaxed conversations, \
consider joining the <a href="https://t.me/thekoinosarmy">Koinos Army Telegram</a>.

✅ <b>Enforcement and community collaboration</b>
Our community thrives when we collaborate to uphold these guidelines. \
Please remind others so long as you are courteous. \
This group is intended to be welcoming to all, especially newcomers. \
It is not a free speech zone for all topics. \
If these limitations feel onerous, members are encouraged to seek alternative venues.
""")

bot.polling()


