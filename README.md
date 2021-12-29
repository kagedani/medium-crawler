# :whale2: Medium articles aggregator :whale2:
This is a python project to develop a Medium articles aggregator for a certain tag.
In the code the tag used is **cloud**, but it can be changed pretty easily :champagne:
 
## Setup :wine_glass:
After cloning the repo, you need to log in to Telegram on your phone or through the [web portal](https://web.telegram.org/k/).

Search for [BotFather](https://botostore.com/c/botfather/) and create your own first bot :raised_hands:  
Give it a name and an id, @BotFather will give you an HTTP API token that you will need to insert in the code:

`telegram_bot_token = 'YOUR_TOKEN'`

After that, you need to look for your newly created bot and send a message on its chat like shown below:
<img width="685" alt="Immagine 2021-12-29 154044" src="https://user-images.githubusercontent.com/41054906/147673544-0ab1f1a8-bcba-4bf5-ab52-9df632a489f3.png">

Now, you need to open your favourite web browser and visit the following url: [https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates](https://api.telegram.org/bot<YOUR_TOKEN>/getUpdates)

You will see something like: `{"ok":true,"result":[...]}`
from there you need to extract the field called `chat_id` and paste it in the code:

`telegram_chat_id = '<YOUR_CHAT_ID>'`

as simple as it looks :fire: 

## Run 
You need to run the main.py file, and it's done, script will send to your bot all the articles present on the first page for the **cloud** tag on Medium 

