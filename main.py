from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import os

webhook = DiscordWebhook(url='YOUR_WEBHOOK', username="Database BOT")


# get datatime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


# setup embed
embed = DiscordEmbed(title='Database Backup created!',
                     description=dt_string, color=242424)
webhook.add_embed(embed)


# attach file
var = os.popen(
    "mysqldump --databases --user=YOUR_DATABASE_USERNAME --password=YOUR_DATABASE_PASSWORD YOUR_DATABASE_NAME").read()
webhook.add_file(file=var, filename='database.sql')

# execute
response = webhook.execute()
