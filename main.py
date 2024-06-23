import discord
import random
import os
from discord.ext import commands
import asyncio
import res

with open("token.txt", "r") as f: # Membaca token dari file token.txt
    token = f.read() # Menyimpan token ke dalam variabel token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Database resep sederhana
recycle = {
    'kulit pisang': 'Pisang yang sudah matang dapat dijadikan smoothie atau pisang goreng.',
    'botol plastic': 'mobil mainan.',
    'sedotan plastic': 'perhiasan gelang.',
    }
not_recycle = {
    'batery': 'sampah ini tidak bisa di daur ulang'
    'bola lampu':'sampah ini tidak bisa di daur ulang'
}
@bot.command('recycle')
async def sampah_daur_ulang(ctx , item :str):
        if item.lower() in recycle:
            await ctx.send(f"sampah daur ulang {item.capitalize()}: {recycle[item.lower()]}")
        else:
            await ctx.send("maaf kami belum mencari hal tersebut")

@bot.command('not_recycle')
async def cannot_recycle(ctx , item :str):
        if item.lower() in recycle:
            await ctx.send(f"sampah ini tidak bisa di daur ulang{item.capitalize()}: {recycle[item.lower()]}")
        else:
            await ctx.send("maaf kami belum mencari hal tersebut")
