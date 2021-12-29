from Logger import Logger
from MediumAggregator import Medium
import requests
import logging
import json
from datetime import date

telegram_bot_token = '<bot_token>'
telegram_chat_id = '<chat_id>'
EXPLOSION_EMOJI = '\U0001F4A5'
COMPUTER_MAN_EMOJI = '\U0001F4CC'


def send_telegram_message(message):
    url = "https://api.telegram.org/bot" + telegram_bot_token + "/sendMessage"
    data = {
        "text": message,
        "chat_id": telegram_chat_id,
        "parse_mode": "html"
    }
    try:
        response = requests.post(url, params=data)
        logging.info(json.dumps(response.text))
    except Exception as e:
        logging.error(f'Error during telegram message sending phase..')
        logging.error(e)


if __name__ == "__main__":
    logger = Logger()
    medium_aggregator = Medium()

    cloud_df = medium_aggregator.medium_aggregate(medium_aggregator.CLOUD_CATEGORY)
    py_df = medium_aggregator.medium_aggregate(medium_aggregator.PYTHON_CATEGORY)
    prg_df = medium_aggregator.medium_aggregate(medium_aggregator.PROGRAMMING_CATEGORY)
    dev_df = medium_aggregator.medium_aggregate(medium_aggregator.DEVELOPER_CATEGORY)

    full_df = cloud_df

    if not full_df.empty:
        today = date.today().strftime("%B %d, %Y")
        code_html = f'<b>Medium top 10 articles for Cloud - {today}</b>'
        for i in range(len(full_df)):
            code_html += f"\n\n {EXPLOSION_EMOJI} Title: {full_df['title'].iloc[i]} \n {COMPUTER_MAN_EMOJI} Url: {full_df['url'].iloc[i]} \n\n"
        send_telegram_message(code_html)