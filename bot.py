import os

from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TWITCH_TOKEN')


class Strik3riaBot(commands.Bot):

    def __init__(self):
        super().__init__(token=TOKEN, prefix='!', initial_channels=['strik3ria'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}')

bot = Strik3riaBot()
bot.run()
