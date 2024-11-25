import os
import discord

# Initialize intents
intents = discord.Intents.default()
intents.message_content = True  # Ensure this is enabled in the Developer Portal

# Create the Discord client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Load token from environment variables
token = os.getenv("TOKEN")
if not token:
    print("Error: Discord bot token not found. Please add it to the environment variables or Secrets panel.")
    exit(1)

# Run the bot
try:
    client.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print("Error: Rate limited by Discord servers (429 Too Many Requests).")
        print("Check your bot's usage and refer to Discord's API guidelines.")
    else:
        print(f"Unexpected HTTP error: {e}")
        raise
except discord.LoginFailure:
    print("Error: Invalid Discord token. Please check your environment variable.")
    exit(1)
