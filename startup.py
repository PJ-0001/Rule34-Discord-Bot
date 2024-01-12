# Intro---------------------------------------------------------------------------------------------------------------------------

# So this is a small project of mine, called Nigga Balls Project, Which i work on for fun it utilzes the pycord libary and also it has some funny functions!


# -------------------------------------------------------------------------------------------------------------------------------




# Lib---------------------------------------------------------------------------------------------------------------------------

# py-cord
# random
# requests

# -------------------------------------------------------------------------------------------------------------------------------

# Variables ---------------------------------------------------------------------------------------------------------------------------
Authy = "PUT YOUR TOKEN HEREEEEE"

user_skills = {
    951419076759158866: ["Programming", "Skinny", "Dumbass"],
    855149753808191519: ["Strength", "Lives in the Gym", "Righthand is stronger then left"],
}


# -------------------------------------------------------------------------------------------------------------------------------------




# Imports -----------------------------------------------------------------------------------------------------------------------------
import discord
from discord.ext import commands
import requests
import json
import random
# ------------------------------------------------------------------------------------------------------------------------------------

# Intents ----------------------------------------------------------------------------------------------------------------------------
intents = discord.Intents.all() 
client = discord.Client(intents=intents)

bot = commands.Bot()
# ------------------------------------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print("Runnin :D")

# Commands ---------------------------------------------------------------------------------------------------------------------------

@bot.slash_command(name="hello", description="Just Talk to the bot", guild_ids=[1194765918694293705])
async def first_slash(ctx): 
    await ctx.respond("Hi!!!")


@bot.slash_command(name="catfact", description="a funny fact about pussy's", guild_ids=[1194765918694293705])
async def catfact(ctx):
    response = requests.get("https://meowfacts.herokuapp.com/")
    if response.status_code == 200:
        fact = response.json()["data"][0]
        await ctx.respond(f"Did you know? {fact}")
    else:
        await ctx.respond("Failed to fetch a cat fact. Meow.")

@bot.slash_command(name="8ball", description="an eightball just a eightball", guild_ids=[1194765918694293705])
async def magic_8_ball(ctx):
    responses = [
        "Yes",
        "No",
        "Ask again later",
        "Definitely not",
        "Absolutely!",
        "Maybe",
        "Cannot predict now",
    ]
    await ctx.respond(f"The magic 8-ball says: {random.choice(responses)}")

@bot.slash_command(name="compliment", description="Receive a random compliment.", guild_ids=[1194765918694293705])
async def compliment(ctx):
    compliments = [
        "You're as cool as a cucumber.",
        "You're a shining star.",
        "If you were a vegetable, you'd be a cute-cumber.",
    ]
    await ctx.respond(random.choice(compliments))

@bot.slash_command(name="insult", description="Deliver a random light-hearted insult.", guild_ids=[1194765918694293705])
async def insult(ctx):
    insults = [
        "You're so slow, you could watch paint dry and still feel like a speed demon.",
        "If you were any dumber, we'd have to water you twice a week.",
        "Your IQ is lower than bedrock, but at least bedrock is useful.",
    ]
    await ctx.respond(random.choice(insults))
    
@bot.slash_command(name="thomas", description="What does the fatass have to say", guild_ids=[1194765918694293705])
async def thomas(ctx):
    thomas_responses = [
        "Pwease stop bullying me.",
        "#CertifiedFatass.",
        "I'm a discord mod, bitch.",
    ]
    await ctx.respond(random.choice(thomas_responses))


@bot.slash_command(name="diceroll", description="Roll a six-sided die.", guild_ids=[1194765918694293705])
async def diceroll(ctx):
    result = random.randint(1, 6)
    await ctx.respond(f"You rolled a {result}!")

@bot.slash_command(name="coinflip", description="Flip a coin and get either heads or tails.", guild_ids=[1101861617483907082])
async def coinflip(ctx):
    result = random.choice(["Heads", "Tails"])
    await ctx.respond(f"The coin landed on: {result}!")

@bot.slash_command(name="dadjoke", description="Get a classic dad joke.", guild_ids=[1194765918694293705])
async def dad_joke(ctx):
    response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "text/plain"})
    if response.status_code == 200:
        joke = response.text
        await ctx.respond(joke)
    else:
        await ctx.respond("Failed to fetch a dad joke. Dad must be busy telling them elsewhere.")


@bot.slash_command(name="randomnumber", description="Generate a random number within a specified range.", guild_ids=[1194765918694293705])
async def random_number(ctx, min_value: int, max_value: int):
    if min_value >= max_value:
        await ctx.respond("Invalid range. The minimum value must be less than the maximum value.")
    else:
        result = random.randint(min_value, max_value)
        await ctx.respond(f"Your random number is: {result}")


@bot.slash_command(name="poll", description="Create a simple yes/no poll.", guild_ids=[1194765918694293705])
async def poll(ctx, question: str):
    embed = discord.Embed(title="Poll", description=question, color=0x3498db)
    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Options", value="✅ Yes\n❌ No", inline=False)
    message = await ctx.respond(embed=embed)
    await message.add_reaction("✅") 
    await message.add_reaction("❌") 


@bot.slash_command(name="bussin", description="The bot will sent some NSFW", guild_ids=[1194765918694293705])   # NSFW COMMAND
async def send_image(ctx):
    try:
        api_url = f"https://nekobot.xyz/api/image?type=pgif"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            image_url = data["message"]
            await ctx.respond(image_url)
        else:
            await ctx.respond(f"Failed to fetch image from the API. Status code: {response.status_code}")
    except Exception as e:
        await ctx.respond(f"An error occurred: {e}")
        
    
@bot.slash_command(name="myskills", description="Get information about your skills.",guild_ids=[1194765918694293705])
async def my_skills(ctx):
    user_id = ctx.author.id
    if user_id in user_skills:
        skills_list = "\n".join(user_skills[user_id])
        response = f"Your skills:\n{skills_list}"
        await ctx.respond(response)
    else:
        await ctx.respond("You don't have skills registered.")


@bot.slash_command(name="randomcat", description="Get a random cat image", guild_ids=[1101861617483907082])
async def random_cat(ctx):
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        if response.status_code == 200:
            cat_data = response.json()[0]
            cat_url = cat_data["url"]
            embed = discord.Embed(title="Random Cat", color=0x3498db)
            embed.set_image(url=cat_url)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("Failed to fetch a random cat image. Meow.")
    except Exception as e:
        await ctx.respond(f"An error occurred: {e}")



# Moderation Commands ---------------------------------------------------------------------------------------------------------------
        

@bot.slash_command(name='kick', description = "Kick a member from the current guild!", guild_ids=[1101861617483907082])
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'**{member}** has been kicked. Reason: {reason}')
    else:
        await ctx.send('You do not have the required permissions to kick members.')

@bot.slash_command(name='ban', description = "ban a member from the current guild!", guild_ids=[1101861617483907082])
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'**{member}** has been banned. Reason: {reason}')
    else:
        await ctx.send('You do not have the required permissions to ban members.')

@bot.slash_command(name='mute', description = "mute a member from the current guild!", guild_ids=[1101861617483907082])
async def mute(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not muted_role:
            muted_role = await ctx.guild.create_role(name='Muted')
        await member.add_roles(muted_role, reason=reason)
        await ctx.send(f'**{member}** has been muted. Reason: {reason}')
    else:
        await ctx.send('You do not have the required permissions to mute members.')

@bot.slash_command(name='unmute', description = "unmute a member from the current guild!", guild_ids=[1101861617483907082])
async def unmute(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, name='Muted')

        if muted_role and muted_role in member.roles:
            await member.remove_roles(muted_role)
            await ctx.send(f'**{member}** has been unmuted.')
        else:
            await ctx.send('The member is not muted.')
    else:
        await ctx.send('You do not have the required permissions to unmute members.')


# -----------------------------------------------------------------------------------------------------------------------------------

# You stupid this is to run the bot.
bot.run(Authy)
