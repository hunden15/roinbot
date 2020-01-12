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
  serverf = "Online"
  servert = "Online"
  if message.content.startswith("!도움말"):
    await client.send_message(message.channel, "[도움말]\n!도움말 = 스넷봇 도움말을 확인합니다.\n!정보 = 나의 디스코드 정보를 확인합니다.\n!제작자 = 스넷봇 제작자의 정보를 확인합니다.\n!서버 = 서버 명령어에 대한 도움말을 확인합니다.\n!파트너 = 파트너 명령어에 대한 도움말을 확인합니다.\n\n[ 문의는 디스코드봇 1대1채팅으로 해주세요. ]")
  if message.content.startswith("닥쳐"):
    await client.send_message(message.channel, "[스넷봇] 닭을 왜 쳐!!!!!!!")
  if message.channel.is_private and message.author.id != "665460521050439710":
    await client.send_message(discord.utils.get(client.get_all_members(), id="419810897058463754"), message.author.name + "(" + message.author.id + ") : " + message.content)
  if message.content.startswith("!DM"):
    if message.author.id == "419810897058463754":
      member = discord.utils.get(client.get_all_members(), id=message.content[4:22])
      await client.send_message(member, "[스넷봇] 제작자 답변 : " + message.content[23:])
    else:
      await client.send_message(message.channel, "[스넷봇] [ " + message.author.name + " ] 님 당신은 이 명령어를 사용할 권한이 없습니다.")
  if message.content.startswith("응아니야"):
    await client.send_message(message.channel, "[스넷봇] 응 너도 응 아니야")
  if message.content.startswith("반사"):
    await client.send_message(message.channel, "[스넷봇] 너 반에서 사랑하는 사람 있구나? ㅋㅋㅋㅋㅋㅋㅋ")
  if message.content.startswith("!정보"):
    date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
    embed = discord.Embed(color=0x00ff00)
    embed.add_field(name="이름", value=message.author.name, inline=True)
    embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
    embed.add_field(name="이름", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일", inline=True)
    embed.add_field(name="아이디", value=message.author.id, inline=True)
    embed.set_thumbnail(url=message.author.avatar_url)
    await client.send_message(message.channel, embed=embed)
  if message.content == "!파트너":
    await client.send_message(message.channel, "[스넷봇 파트너 시스템]\n!파트너 목록 = 파트너 목록을 확인합니다.")
  else:
    if message.content[5:7] == "목록":
      list = ['HUNDEN', '후야']
      await client.send_message(message.channel, "\n".join(list))
  if message.content.startswith("!제작자"):
    await client.send_message(message.channel, "[스넷봇 제작자의 정보]\n제작자 본명: 비공개\n제작자 닉네임: 헌덴[HUNDEN]\n제작자 나이: 16살[2020년도 기준]\n제작자 디스코드: HUNDEN#1422\n[ 제작자 사칭 주의하세요! ]")
  if message.content == "!서버":
    await client.send_message(message.channel, "[스넷봇 서버 시스템]\n!서버 목록 = 스넷봇서버의 목록을 확인합니다.\n!서버 <서버이름> = 스넷봇서버를 접속합니다.")
  else:
    if message.content[4:6] == "목록":
      await client.send_message(message.channel, "[스넷봇 서버 시스템]\n1. SERVER-1 :: (" + serverf + ")\n2. SERVER-2 :: (" + servert +")")
    if message.content[4:12] == "SERVER-1":
      if serverf == "Online":
        await client.send_message(message.channel, "[스넷봇 서버 시스템] 스넷봇서버와 디스코드서버를 연결중 입니다...")
        await client.send_message(message.channel, "[스넷봇 서버 시스템] (" + message.author.name + ")님이 서버채널1에 접속하셨습니다.")
      if serverf == "Offline":
        await client.send_message(message.channel, "[스넷봇 서버 시스템] 해당 서버는 오프라인서버 입니다.")
    if message.content[4:12] == "SERVER-2":
      if serverf == "Online":
        await client.send_message(message.channel, "[스넷봇 서버 시스템] 스넷봇서버와 디스코드서버를 연결중 입니다...")
        await client.send_message(message.channel, "[스넷봇 서버 시스템] (" + message.author.name + ")님이 서버채널2와 연결 도중 오류가 발생하였습니다.\n[스넷봇 서버 시스템] 스넷봇 제작자에게 문의 코드를 보내십시오. `XEHZ02`,`EXAW821`")
      if serverf == "Offline":
        await client.send_message(message.channel, "[스넷봇 서버 시스템] 해당 서버는 오프라인서버 입니다.")
        
    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
