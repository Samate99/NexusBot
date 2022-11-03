import discord
from discord.ext import commands
from discord_buttons_plugin import *
import requests



TOKEN = ''

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!',intents=intents)
buttons = ButtonsClient(bot)


@bot.command()
async def nexus(ctx):

    await chooser(ctx)


@bot.event
async def on_ready():
	print("The bot is ready!")

@bot.command()
async def howtouse(ctx):
    howtouse = "**How to use:**" + '\n' + "**Tpye !PLAYER**" + '\n'+ "For Steam datas use steam ID" + '\n'+ "For faceit datas use faceit name " + '\n'+ "**Tpye !elosystem**" + '\n'+ "And you get information about faceit elos" + '\n'+ "**Tpye !ranksystem**" + '\n'+ "And you get information about steam ranks" + '\n'+ "**Tpye !guns**"  + '\n'+ "And you get information about csgo guns" + '\n'
    await ctx.reply(howtouse)    


async def chooser(ctx):
    await buttons.send(
        content="Az egyesület",
        channel=ctx.channel.id,
        components=[
            ActionRow([
                Button(
                    label="Nexus",
                    style=ButtonType().Primary,
                    custom_id="button_one"

                ),
                Button(
                    label="Tagok",
                    style=ButtonType().Primary,
                    custom_id="button_two",
                ),
                Button(
                    label="Informaciok",
                    style=ButtonType().Primary,
                    custom_id="button_three",
                )
            ]
            )
        ]
    )

@buttons.click
async def button_two(ctx):
    await ctx.reply("steam choosed!")


@buttons.click
async def button_one(ctx):
    await ctx.reply("steam choosed!")

@buttons.click
async def button_three(ctx):
	await ctx.reply("You can send ephemeral messages too!", flags = MessageFlags().EPHEMERAL)






@bot.event
async def on_ready():
    print('A BOT ELINDULT {0.user} NÉVEN'.format(bot))


bot.run(TOKEN)

