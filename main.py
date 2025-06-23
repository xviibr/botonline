import discord
from discord.ext import commands
import os 

from myserver import server_on  # เรียกใช้ฟังก์ชัน server_on เพื่อเริ่มเซิร์ฟเวอร์ Flask

# กำหนด Intents ที่จำเป็น
# Intents คือชุดของ "เหตุการณ์" ที่บอทของคุณต้องการรับจาก Discord
# ตัวอย่างเช่น, Message Content Intent จำเป็นสำหรับการอ่านข้อความ
# คุณต้องเปิดใช้งาน Intents เหล่านี้ใน Discord Developer Portal ของบอทด้วย
intents = discord.Intents.default()
intents.message_content = True  # จำเป็นสำหรับบอทที่อ่านข้อความในช่อง

# สร้าง Bot instance
# command_prefix คือคำนำหน้าสำหรับคำสั่งของบอท (เช่น !hello, ?info)
bot = commands.Bot(command_prefix='!', intents=intents)

# เหตุการณ์เมื่อบอทพร้อมใช้งาน
@bot.event
async def on_ready():
    print(f'เข้าสู่ระบบในชื่อ {bot.user.name} ({bot.user.id})')
    print('บอทพร้อมใช้งานแล้ว!')
    print('---')

# ตัวอย่างคำสั่ง: คำสั่ง "hello"
@bot.command()
async def hello(ctx):
    """
    บอทจะตอบกลับด้วยข้อความทักทาย
    """
    await ctx.send('สวัสดีครับ! แมวเป้ามาแล้ว!')

# ตัวอย่างคำสั่ง: คำสั่ง "ping"
@bot.command()
async def ping(ctx):
    """
    บอทจะตอบกลับด้วย "Pong!"
    """
    await ctx.send('Pong!')

# ตัวอย่างคำสั่ง: คำสั่ง "echo"
@bot.command()
async def echo(ctx, *, message):
    """
    บอทจะพูดซ้ำข้อความที่คุณพิมพ์หลังจากคำสั่ง
    ตัวอย่าง: !echo สวัสดีทุกคน
    """
    await ctx.send(message)

    server_on()  # เรียกใช้ฟังก์ชัน server_on เพื่อเริ่มเซิร์ฟเวอร์ Flask

# รันบอทด้วย Token ของคุณ
# แทนที่ 'YOUR_BOT_TOKEN' ด้วย Token จริงของบอทคุณ
# ห้ามเผยแพร่ Token นี้ให้ใครทราบเด็ดขาด!
bot.run(os.getenv('TOKEN'))  # ใช้ os.getenv เพื่อดึง Token จากตัวแปรสภาพแวดล้อม