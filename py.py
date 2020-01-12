import discord
import os
import datetime
import asyncio


client = discord.Client()


@client.event
async def on_ready():
  print("login")
  print(client.user.name)
  print(client.user.id)
  print("------------------")
  await client.change_presence(game=discord.Game(name='', type=1))

@client.event
async def on_message(message):
  RN = "[로인온라인 시스템]"
  if message.content == "r!":
    await client.send_message(message.channel, "`[로인온라인 공식 시스템]\nr! => 로인온라인 봇에 관한 도움말을 확인합니다.\nr!시스템 => 디스코드 봇의 시스템 정보를 확인합니다.\nr!내정보 => 나의 디스코드 정보를 확인합니다.\nr!문의 => 디스코드봇 제작자에게 문의 보냅니다.`")
  else:
    if message.content[2:5] == "DM":
      if message.author.id == "419810897058463754":
        member = discord.utils.get(client.get_all_members(), id=message.content[5:23])
        await client.send_message(member, RN + " 제작자 : " + message.content[24:])
      else:
        await client.send_message(message.channel, RN + " [ " + message.author.name + " ] 님 당신은 이 명령어를 사용할 권한이 없습니다.")
    if message.content[2:5] == "내정보":
      date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
      embed = discord.Embed(color=0x00ff00)
      embed.add_field(name="이름", value=message.author.name, inline=True)
      embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
      embed.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일", inline=True)
      embed.add_field(name="아이디", value=message.author.id, inline=True)
      embed.set_thumbnail(url=message.author.avatar_url)
      await client.send_message(message.channel, embed=embed)
    if message.content[2:5] == "시스템":
      embed = discord.Embed(color=0x0028ff)
      embed.add_field(name="제작자", value="헌덴[HUNDEN]", inline=True)
      embed.add_field(name="제작일", value="2020.01.12", inline=True)
      embed.add_field(name="버전", value="v2.1[BETA]", inline=True)
      embed.add_field(name="아이디", value="9423129273201274", inline=True)
      await client.send_message(message.channel, embed=embed)
    if message.content[2:5] == "문의":
      if message.content[6:]:
        if message.channel.is_private and message.author.id != "665768509707518033":
          await client.send_message(discord.utils.get(client.get_all_members(), id="419810897058463754"), message.author.name + "(" + message.author.id + ") : " + message.content)
      else:
        await client.send_message(message.channel, RN + " 제작자에게 문의 보낼 메세지를 적어주세요.")
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
