from discord_webhook import DiscordWebhook, DiscordEmbed
from datetime import datetime
import os

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/960907714547048458/mLkQJgoSSogT4zMo3hvqZ9yEKU95JrRnGO8GzNK5JMXbKzIQXV7zlGlN9Cp5z0_lRQZ2', username="AGUNG GANTENG")


# get datatime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


# setup embed
embed = DiscordEmbed(title='Database Backup created!',
                     description=dt_string, color=242424)
webhook.add_embed(embed)


# attach file
var = os.popen(
    "mysqldump --databases --user=root --password=").read()
webhook.add_file(file=var, filename='memekujang.sql')

# execute
response = webhook.execute()
