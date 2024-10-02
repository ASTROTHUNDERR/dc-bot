from discord.ext import commands

from bot import Bot

class Commands(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')


async def setup(bot: Bot):
    await bot.add_cog(Commands(bot))