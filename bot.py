import discord

from discord.ext import commands

EXTS = [
    'exts.commands'
]

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            status=discord.Status.online,
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        for extension in EXTS:
            try:
                await self.load_extension(extension)
            except Exception as e:
                print('Error while loading an extension: ', e)

        print(f'{self.user.name} is running!')

    async def on_message(self, message: discord.Message):
        await self.process_commands(message)