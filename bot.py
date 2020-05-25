from colored import fore, style
from discord.ext import commands

bot = commands.Bot(command_prefix="guci!")
TOKEN = "TOKEN"

class log:
    def status(msg):
        print(fore.BLUE, '[i]', style.RESET, end="")
        print(msg)

    def finished(msg):
        print(fore.GREEN, f'[+]', style.RESET, end="")
        print(msg)

    def warning(msg):
        print(fore.ORANGE_1, f'[*]', style.RESET, end="")
        print(msg)

    def error(msg):
        print(fore.RED, f'[!]', style.RESET, end="")
        print(msg)

@bot.event
async def on_ready():
    log.status("Loading Token ...")
    log.finished("Bot has connected to server!")

@bot.event
async def on_member_join(member):
    log.status(f"{member.nick} has joined server")
    role = discord.utils.get(member.server.roles, name="Normální žid")
    await bot.add_role(member, role)
    log.finished(f"Member {member.nicj} has been assigned role {role} with name Normální Žid")

bot.run(TOKEN)
