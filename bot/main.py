import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("тест")

bot.run("MTA2MTk3MTk4MjY4MzQ3MTk0Mw.GUa4lu.vvnsa5MlDZNQo-jm4Kf75sFvNJJWESXr-FeyMc")
