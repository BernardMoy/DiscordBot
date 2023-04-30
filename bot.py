import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
from testlist import testlist
from savedtestlist import savedtestlist
from wordlist import wordlist
from savedwordlist import savedwordlist
from pokelist import pokelist
from savedpokelist import savedpokelist
from pokelistsamelen import pokelistsamelen
from mythical import mythical
from legendary import legendary
import datetime
from datetime import date
import math
client=discord.Client()
from itertools import combinations

#BOOLEAN--------------------------------------------------
counter=0
playingwordle=False
ongoing=False
playinggd=False
playing24=False
playerhp=20
dragonhp=50
gdjumping=False
gridoutput=''
playinggridgame=False
playingpf=False
breaking=False
playingttt=False
placed=False
playing2048=False
usedautoplay=False
testtime=0
usingrngtest=False
#---------------------------------------------------------

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  channel=client.get_channel(791942824601190400)
  await channel.send('Hi')

  activity = discord.Game(name="( ͡° ͜ʖ ͡°) | -help")
  await client.change_presence(status=discord.Status.online, activity=activity)

  bot=commands.Bot(command_prefix='-',help_command=None)



import trains


@client.event
async def on_message(msg):
  await trains.on_message(msg)   #import the file and then call the function there

  #check msg not from bot
  if msg.author==client.user:
    return

  #help

  if msg.content.lower()=="-help":
    embedhelp=discord.Embed(
      title='List of commands',
      description='',
      color=0xffa8c2,
    )
    embedhelp.set_footer(text='Bot created on 29/6/2022 | Thanks for playing!')
    
    embedhelp.add_field(name="General",value="`-random` -- give a random integer between 0 and 100 \n`-ping` -- ping the user\n`-spam` -- spam message! \n`-stop` -- stop the spam \n`-counter` -- count the no. of messages sent \n`-slot` `-megaslot` `-8D` -- some randomizers",inline=False)
    
    embedhelp.add_field(name="Games",value="`-spawn` -- spawn a dragon!\n`-wordle` -- play wordle! \n`-solve` -- solve a wordle i.e. cheat\n`-24` -- play a 24points game\n`-gd` -- 1 fps geometry dash\n`-gridgame` -- A random grid game\n`-pf` -- Pathfinding test\n`-tictactoe` -- TicTacToe with AI\n`-2048` -- 2048 Game!\nGet hint from Pokétwo bot to use pokemon solver",inline=False)
    embedhelp.set_thumbnail(url=client.user.avatar_url)
    await msg.channel.send(embed=embedhelp)
    
  #msg response


  global coin

  if msg.content.startswith('-testing'):
    with open ('Data.py') as f:
      await msg.channel.send(f.read())


  if msg.content.lower()=="-sp4":
    await msg.channel.send("<:sp4_NO_BG:951301868301209601>")
  if msg.content.lower()=="-test2":
    await msg.channel.send(":heart:")
  if msg.content.lower()=="-random":
    await msg.channel.send(random.randint(0,100))
    
  if msg.content.lower()=="-ping":
    await msg.channel.send(msg.author.mention)

  


    
    
  if msg.content.lower()=="-slot" or msg.content.lower()=="-slots":
    result=""
    for i in range(3):
      f=random.randint(1,5)
      if f==1:
        result=result+" 🌸 "
      elif f==2:
        result=result+" 🍭 "
      elif f==3:
        result=result+" 🌟 "
      elif f==4:
        result=result+" 💎 "
      elif f==5:
        result=result+" 🍀 "
    await msg.channel.send("`"+result+"`")
    if result[1]==result[4]==result[7]:
      await msg.channel.send(msg.author.mention+" GG!! :) \n Give you a thumbsup :thumbsup:")
      
  if msg.content.lower()=='-megaslot' or msg.content.lower()=='-mslot':

    result2=""
    for i in range(20):
      f=random.randint(1,5)
      if f==1:
        result2=result2+" 🌸 "
      elif f==2:
        result2=result2+" 🍭 "
      elif f==3:
        result2=result2+" 🌟 "
      elif f==4:
        result2=result2+" 💎 "
      elif f==5:
        result2=result2+" 🍀 "
    
    embed1=discord.Embed(
      title='MEGASlot!',
      description=result2,
      color=discord.Color.random()
    )
    embed1.set_footer(text='1 in 195 for a special blessing. Good luck')
    await msg.channel.send(embed=embed1)
    #special blessing
    if "🌟  🌟  🌟  🌟  🌟" in result2:
      await msg.channel.send(msg.author.mention+"Your slot have a lot of STARS\n Give you Moy's DSE Result blessing ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️")

  #8D
  global mid
  
  if msg.content.lower()=='-8d':
    Dnum=random.randint(0,30)
    mid=''
    for i in range(Dnum):
      mid=mid+'='

    embedD=discord.Embed(
      title='8D',
      description='8'+mid+'D',
      color=discord.Color.random()
    )
    embedD.set_footer(text="I don't know what this is")
    await msg.channel.send(embed=embedD)

    
  #goodnight
  embed3=discord.Embed(
    title="It's time to sleep...",
    description="You would become stronger the next day.",
    color=0x34b4eb
  )
  if msg.content.lower()=="gn":
    await msg.channel.send(msg.author.mention+" Goodnight! Don't ever let me see you online again")
    await msg.channel.send(embed=embed3)




  
  if msg.author.id==480261318603964441 and msg.content.lower()=='i am sad':
    embedt=discord.Embed(
      title='Today is '+str(datetime.date.today())+'.',
      color=0xf5425a
    )
    embedt.set_footer(text="Progress: 0/5+0/9\nDo you remember your dream(both the real ones.. and that on 29/6?\n")

    
    embedt2=discord.Embed(
      color=0xf5425a
    )
    embedt2.set_footer(text="You should probably stop asking why me and you are treated different\nWe would bear the responsibility for you (as promised last year!)\nYou should not be upset by things that do not contribute to your progress.\nOr I am glad you are sad now rather than later.\nAugust topics are nowhere comparable to July topics.")
   


    await msg.channel.send(embed=embedt)
    await msg.channel.send(embed=embedt2)
    await msg.channel.send(msg.author.mention+" Goodnight! Don't ever let me see you online again")
    await msg.channel.send(embed=embed3)
    await msg.channel.send('Good luck!')














    


    
  #pokesolver --------------- yourpoke2=your input

  global yourpoke
  global yourpoke2
  global pokelist
  global savedpokelist
  global pokelistsamelen
  
  if msg.content.startswith('The pokémon is'):
    yourpoke=msg.content[15:len(msg.content)-1]
    yourpoke2=''
    for i in yourpoke:
      if i=="\\": 
        yourpoke2=yourpoke2+''
      else:
        yourpoke2=yourpoke2+i
          
    #reset
    pokelist=list(savedpokelist)
    pokelistsamelen=list(savedpokelist)
    
    #check length
    for k in savedpokelist:
      if len(k)!=len(yourpoke2):
        pokelistsamelen.remove(k)
        pokelist.remove(k)
        
    #check character
    for j in range(0,len(yourpoke2)):
      if yourpoke2[j]!='_':
        for l in pokelistsamelen:
          if l[j]!=yourpoke2[j] and l in pokelist:
            pokelist.remove(l)
        
    pokeembed=discord.Embed(
      title='Pokemon Solver',
      description=str(len(pokelist))+' pokemon found!',
      color=0xfffb00
    ) 
    pokeembed.set_footer(text=yourpoke2+' | Imagine using p!hint lmao')

    await msg.channel.send(embed=pokeembed)

    if len(pokelist)==1:
      await msg.channel.send(''.join(pokelist))
    else:
      await msg.channel.send(pokelist)

    #mythical / legendary
    for element in pokelist:
      if element in mythical:
        await msg.channel.send(msg.author.mention+' A mythical pokemon appeared!')
        break

    for element in pokelist:
      if element in legendary:
        await msg.channel.send(msg.author.mention+' A legendary pokemon appeared!')
        break





    
  #wordle -------------------------------------------
  global wordlist
  global savedwordlist
  global wordleans
  global count
  global playingwordle

  
  if msg.content.lower()=='-wordle':
    playingwordle=True
    wordpos=random.randint(0,2313)
    wordleans=savedwordlist[wordpos]
    print(wordleans)
    embedbegin=discord.Embed(
      title='Wordle | Try: 0',
      description=(' ⬛  ⬛  ⬛  ⬛  ⬛ '),
      color=0xb342f5
    )
    embedbegin.set_footer(text='Reply with -[YourWord] e.g. -crane')
    await msg.channel.send(embed=embedbegin)
    count=0
    
  if len(msg.content)==6 and msg.content.startswith('-') and playingwordle:
    yourans=msg.content[1:6].lower()

    if yourans in savedwordlist:
      try:
        count+=1
        wordleoutput=""
        for i in range(5):
          if yourans[i]==wordleans[i]:
            wordleoutput=wordleoutput+' 🟩 '
          elif yourans[i] in wordleans:
            wordleoutput=wordleoutput+' 🟨 '
          else:
            wordleoutput=wordleoutput+' ⬛ '
        wordleembed=discord.Embed(
          title='Wordle | Try: '+str(count),
          description=wordleoutput,
          color=0xb342f5
        )
        wordleembed.set_footer(text='Your word: '+yourans)
        await msg.channel.send(embed=wordleembed)
        if wordleoutput==' 🟩  🟩  🟩  🟩  🟩 ':
          wordleans=''
          await msg.channel.send(msg.author.mention+ ' You win! GG :)')
          playingwordle=False
      except:
        await msg.channel.send('')
    elif playingwordle:
      await msg.channel.send('Word not in database!')
    
  #wordlesolver---------------------savedwordlist=template
  global testlist 
  global savedtestlist
 

  #info
  if msg.content.lower()=='-solve':
    embed4=discord.Embed(
      title='How to use wordle solver',
      description='- use `-solvegreen` to input your green squares \n- use `-solveyellow` to input your yellow squares\n - use `0` to represent unknown tiles.\n- use `-solveblack` to input your black squares.\n- Order doesnt matter when using `-solveblack` \n- use `-solvereset` to reset.',
      color=0x03fcba
    )
    embed4.set_footer(text='Example:\ncrane 🟩🟨⬛⬛🟨\ninput \n-solvegreen c0000\n-solveyellow 0r00e\n-solveblack an')
    await msg.channel.send(embed=embed4)
    
    #reset
  if msg.content.lower()=='-solvereset':
    wordlist=list(savedwordlist)
    await msg.channel.send('Wordlist reset!')
 
    #green
  if msg.content.startswith('-solvegreen'):
    word1=msg.content[12:len(msg.content)]
    for i in range(len(word1)):
      if word1[i]!='0':
        for sample in savedwordlist:
          if sample[i]!=word1[i] and sample in wordlist:
            wordlist.remove(sample)
            
    embedgreen=discord.Embed(
      title='Submitted 🟩: '+word1,
      description=str(len(wordlist))+' possible words found!',
      color=0x69ffae
    )
    await msg.channel.send(embed=embedgreen)  
    
    await msg.channel.send(wordlist)
    
    #yellow
  if msg.content.startswith('-solveyellow'):
    word2=msg.content[13:len(msg.content)]
    for i in range(len(word2)):
      if word2[i]!='0':
        for sample in savedwordlist:
          if word2[i] not in sample and sample in wordlist or word2[i]==sample[i] and sample in wordlist:
            wordlist.remove(sample)
            
    embedyellow=discord.Embed(
      title='Submitted 🟨: '+word2,
      description=str(len(wordlist))+' possible words found!',
      color=0xfff069
    )
    await msg.channel.send(embed=embedyellow)  
    
    await msg.channel.send(wordlist)

    #black
  if msg.content.startswith('-solveblack'):
    word3=msg.content[12:len(msg.content)]
    for i in range(len(word3)):
      for sample in savedwordlist:
        if word3[i] in sample and sample in wordlist:
          wordlist.remove(sample)
          
    embedblack=discord.Embed(
      title='Submitted ⬛: '+word3,
      description=str(len(wordlist))+' possible words found!',
      color=000000
    )
    await msg.channel.send(embed=embedblack)
  
    await msg.channel.send(wordlist)
        

      
    
    

  if msg.content=='-testlistremove':
    testlist.remove(1)
    
  if msg.content=='-testlistrestore':
    testlist=savedtestlist
    
  if msg.content=='-testlist':
    await msg.channel.send(testlist)



      
  #24Points
  global playing24
  
  if msg.content=='-24':
    playing24=True
    poker=""
    number=""
    for i in range(4):
      k=random.randint(1,4)
      if k==1:
        poker=poker+' ♠ '
      if k==2:
        poker=poker+' ♥ '
      if k==3:
        poker=poker+' ♦ '
      if k==4:
        poker=poker+' ♣ '

    global a
    global b
    global c
    global d
    
    a=random.randint(1,13)
    b=random.randint(1,13)
    c=random.randint(1,13)
    d=random.randint(1,13)

    if a==1:
      number=number+' A '
    elif a==11:
      number=number+' J '
    elif a==12:
      number=number+' Q '
    elif a==13:
      number=number+' K '
    else:
      number=number+' '+str(a)+' '
    
    if b==1:
      number=number+' A '
    elif b==11:
      number=number+' J '
    elif b==12:
      number=number+' Q '
    elif b==13:
      number=number+' K '
    else:
      number=number+' '+str(b)+' '
      
    if c==1:
      number=number+' A '
    elif c==11:
      number=number+' J '
    elif c==12:
      number=number+' Q '
    elif c==13:
      number=number+' K '
    else:
      number=number+' '+str(c)+' '

      
    if d==1:
      number=number+' A '
    elif d==11:
      number=number+' J '
    elif d==12:
      number=number+' Q '
    elif d==13:
      number=number+' K '
    else:
      number=number+' '+str(d)+' '
  
    
    #embed
    embed2=discord.Embed(
      title='24 Points',
      description='` a  b  c  d `\n'+'`'+number+'`'+"\n"+'`'+poker+'`',
      color=0xFF9DC2
    )
    embed2.set_footer(text='Use + , - , * , / and () to obtain 24. \nA, J, Q, K = 1, 11, 12, 13\nUSE a, b, c, d TO REPRESENT THE 4 NUMBERS\nType your answer!   e.g.(a-b)*(c+d)\n---------------------\nUse -end to end game\nUse -24 to start a new round')
    await msg.channel.send(embed=embed2)
    #embedend

    msg.content=''
    
  if msg.content=='-end' and playing24:
      playing24=False
      await msg.channel.send('Game ended')
  
  if playing24:
    
    #check illegal symbols
    if '**' in msg.content or '//' in msg.content or '%' in msg.content or '^' in msg.content:
      await msg.channel.send('You typed some illegal symbols.')
    #check numbers
    elif '0' in msg.content or '1' in msg.content or '2' in msg.content or '3' in msg.content or '4' in msg.content or '5' in msg.content  or '6' in msg.content or '7' in msg.content or '8' in msg.content or '9' in msg.content:
      await msg.channel.send('Use a, b, c, d instead of numbers!')
    #check if used all a b c d
    elif msg.content.count('a')!=1 or msg.content.count('b')!=1 or msg.content.count('c')!=1 or msg.content.count('d')!=1:
      await msg.channel.send('You must use all 4 numbers (a ,b ,c ,d) ONCE!')
    #check if can calculate
    else:
      try:
        embed24=discord.Embed(
          title='Your answer',
          description='`'+msg.content+'` = '+str(eval(msg.content)),
          color=0xffc587
        )
        embed24.set_footer(text='Math god?')
        await msg.channel.send(embed=embed24)
        if eval(msg.content)==24:
          await msg.channel.send(msg.author.mention+' You solved it! GG!')
          playing24=False
       
      except:
        if msg.content!='':
          await msg.channel.send('You typed weird things.')

  if "p!c" in msg.content:
    await msg.add_reaction("<:pingpong:843058170342801418>")

  #Grid game ===================================================================================================



  global playinggridgame
  global gridx
  global gridy
  global embedgrid2
  global grid2
  global health
  global amt
  global storedgridx
  global storedgridy
  global dragonx
  global dragony
  global instructions

  instructions="Type -spread <6 to 300> to create a path.\nSpreading will alert the dragon according to the amount you spread.\n------------------\nYellow squares generate on black squares.\n> Yellow squares are safe. You cannot walk on black squares.\nPurple and green squares generate when a yellow square is repeatedly spread.\n> Purple squares will hurt you.\n> Green squares will alert the dragon to approach you (by 1 or 2 squares).\nRed squares generate when purple squares are repeatedly spread.\n> Red squares will leave you on one health, and will kill you if you already have one health.\nBlue squares are the dragon's trail.\n> Blue squares change any red squares into green ones, and vice versa. It also deletes other blue squares.\nWhite squares generate when something spreads onto blue squares.\n> White squares teleport you to the opposite side of the map.\n------------------\nUse -u -r -l -d to move\nType -end to end game"

  async def printgrid():
    global gridoutput
    gridoutput=''
    for row in grid2:
      for i in row:
        gridoutput=gridoutput+i
      gridoutput=gridoutput+'\n'

  #start
  if msg.content.lower()=='-gridgame' and not playinggridgame:
    health=4
    grid2 = [['⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', ],
             ['⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', ],
             ['⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', ],
             ['⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', ],
             ['⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', ],
             ['⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '⬛ ', '🕳️ ', ], ]
    playinggridgame=True
    gridx=0
    gridy=0
    dragonx=4
    dragony=11
    grid2[gridx][gridy]='😀 '
    grid2[dragonx][dragony]='🐉 '
    await printgrid()
    embedgrid2 = discord.Embed(title='A random game' + ' | Your health: ' +str(health), description=gridoutput,
                               color=0xc9f8ff)
    embedgrid2.set_footer(
      text=instructions)
    await msg.channel.send(embed=embedgrid2)

  #functions
  async def blockfx():
    global dragonx
    global dragony
    global health
    global playinggridgame
    global gridx
    global gridy

    if grid2[gridx][gridy]=='🟪 ':
      health-=1
    elif grid2[gridx][gridy]=='🟥 ' and health>1:
      health=1
    elif grid2[gridx][gridy] == '🟥 ' and health == 1:
      health=0
    elif grid2[gridx][gridy]=='🟩 ':


      for i in range(random.randint(1,2)):
        grid2[dragonx][dragony] = '🔹 '

        if abs(dragonx - gridx) > abs(dragony - gridy) or abs(dragonx - gridx) == abs(dragony - gridy):
          if dragonx - gridx < 0:
            dragonx += 1  # downwards
          elif dragonx - gridx > 0:
            dragonx -= 1  # upwards

        elif abs(dragonx - gridx) < abs(dragony - gridy):
          if dragony - gridy < 0:
            dragony += 1  # rightwards
          elif dragony - gridy > 0:
            dragony -= 1  # leftwards

        if dragonx == gridx and dragony == gridy and playinggridgame:
          await msg.channel.send('You were eaten by the dragon!')
          health=0
          playinggridgame = False

        grid2[dragonx][dragony] = '🐉 '



    elif grid2[gridx][gridy] == '🔹 ':
      for i in range(6):
        for j in range(12):
          if grid2[i][j] == '🟥 ':
            grid2[i][j] = '🟩 '
          elif grid2[i][j] == '🟩 ':
            grid2[i][j] = '🟥 '
          elif grid2[i][j]=='🔹 ':
            grid2[i][j]='⬛ '

    elif grid2[gridx][gridy]=='⬜ ':
      grid2[gridx][gridy]='⬛ '
      gridx=5-gridx
      gridy=11-gridy
      grid2[gridx][gridy] = '😀 '





  #Move
  #RIGHT
  if msg.content.lower()=='-right' and playinggridgame or msg.content.lower()=='-r' and playinggridgame:

    if gridy<11 and grid2[gridx][gridy+1]!='⬛ ':

      grid2[gridx][gridy]='⬛ '
      gridy+=1
      await blockfx()
      grid2[gridx][gridy]='😀 '


      await printgrid()
      embedgrid2 = discord.Embed(title='A random game'+' | Your health: '+str(health), description=gridoutput, color=0xc9f8ff)
      embedgrid2.set_footer(
      text=instructions)
      await msg.channel.send(embed=embedgrid2)

      # checkdeath
      if health == 0:
        playinggridgame = False
        await msg.channel.send('You died!')
      elif gridx==dragonx and gridy==dragony:
        playinggridgame=False
        health=0
        await msg.channel.send('You were eaten by the dragon!')
      # checkwin
      if grid2[5][11] == '😀 ':
        playinggridgame = False
        await msg.channel.send(msg.author.mention + ' YOU WIN GG!!')

    else:
      await msg.channel.send('You would hit the wall.')

  # UP
  if msg.content.lower() == '-up' and playinggridgame or msg.content.lower() == '-u' and playinggridgame:

    if gridx>0 and grid2[gridx-1][gridy]!= '⬛ ':

      grid2[gridx][gridy] = '⬛ '
      gridx -= 1
      await blockfx()
      grid2[gridx][gridy] = '😀 '

      await printgrid()
      embedgrid2 = discord.Embed(title='A random game' + ' | Your health: ' + str(health), description=gridoutput,
                                   color=0xc9f8ff)
      embedgrid2.set_footer(text=instructions)
      await msg.channel.send(embed=embedgrid2)

      #checkdeath
      if health==0:
        playinggridgame=False
        await msg.channel.send('You died!')
      elif gridx == dragonx and gridy == dragony:
        playinggridgame = False
        health=0
        await msg.channel.send('You were eaten by the dragon!')
      #checkwin
      if grid2[5][11] == '😀 ':
        playinggridgame=False
        await msg.channel.send(msg.author.mention+' YOU WIN GG!!')

    else:
      await msg.channel.send('You would hit the wall.')

  # DOWN
  if msg.content.lower() == '-down' and playinggridgame or msg.content.lower() == '-d' and playinggridgame:

    if gridx <5 and grid2[gridx+1][gridy] != '⬛ ':
      grid2[gridx][gridy] = '⬛ '
      gridx += 1
      await blockfx()
      grid2[gridx][gridy] = '😀 '

      await printgrid()
      embedgrid2 = discord.Embed(title='A random game' + ' | Your health: ' + str(health), description=gridoutput,
                                   color=0xc9f8ff)
      embedgrid2.set_footer(text=instructions)
      await msg.channel.send(embed=embedgrid2)

      # checkdeath
      if health == 0:
        playinggridgame = False
        await msg.channel.send('You died!')
      elif gridx==dragonx and gridy==dragony:
        playinggridgame=False
        health=0
        await msg.channel.send('You were eaten by the dragon!')
      # checkwin
      if grid2[5][11] == '😀 ':
        playinggridgame = False
        await msg.channel.send(msg.author.mention + ' YOU WIN GG!!')

    else:
      await msg.channel.send('You would hit the wall.')

  # LEFT
  if msg.content.lower() == '-left' and playinggridgame or msg.content.lower() == '-l' and playinggridgame:

    if gridy >0 and grid2[gridx][gridy - 1] != '⬛ ':
      grid2[gridx][gridy] = '⬛ '
      gridy -= 1
      await blockfx()
      grid2[gridx][gridy] = '😀 '

      await printgrid()
      embedgrid2 = discord.Embed(title='A random game' + ' | Your health: ' + str(health), description=gridoutput,
                                   color=0xc9f8ff)
      embedgrid2.set_footer(
        text=instructions)
      await msg.channel.send(embed=embedgrid2)

      # checkdeath
      if health == 0:
        playinggridgame = False
        await msg.channel.send('You died!')
      elif gridx==dragonx and gridy==dragony:
        playinggridgame=False
        health=0
        await msg.channel.send('You were eaten by the dragon!')
      # checkwin
      if grid2[5][11] == '😀 ':
        playinggridgame = False
        await msg.channel.send(msg.author.mention + ' YOU WIN GG!!')

    else:
      await msg.channel.send('You would hit the wall.')


#--------------------------------------------------------------------------------------------------------------

  #colour (SPREADING)
  async def color():
    if grid2[gridx][gridy] == '🟨 ': #yellow
      num=random.randint(0,2)
      if num==0:
        grid2[gridx][gridy]='🟩 '
      else:
        grid2[gridx][gridy] = '🟪 '
    elif grid2[gridx][gridy] == '🟪 ': #purple
      grid2[gridx][gridy] = '🟥 '
    elif grid2[gridx][gridy] == '🟥 ': #red
      grid2[gridx][gridy] = '🟥 '
    elif grid2[gridx][gridy]=='🟩 ': #green
      grid2[gridx][gridy] = '🟩 '
    elif grid2[gridx][gridy]=='🔹 ': #blue
      grid2[gridx][gridy]='⬜ '
    elif grid2[gridx][gridy]=='⬜ ': #white
      grid2[gridx][gridy]='⬜ '
    else:
      grid2[gridx][gridy] = '🟨 '

  #end
  if msg.content.lower()=='-end' and playinggridgame:
    playinggridgame=False
    await msg.channel.send('Game ended!')

  #Spreading
  global amt

  if msg.content.lower()=='-spread' and playinggridgame:
    await msg.channel.send('Please state the amount you want to spread from 6 to 300, e.g. -spread 10')

  if msg.content.startswith('-spread') and playinggridgame:
    amt=int(msg.content[8:len(msg.content)])
    if amt>5 and amt<301:

      storedgridx=gridx
      storedgridy=gridy
      for i in range(amt):
        rndlist=[1,2,3,4]
        randomnumber=rndlist[random.randint(0,3)]
        #RIGHT
        if randomnumber==1 and gridy<11:
          gridy+=1
          await color()
        #UP
        elif randomnumber==2 and gridx>0:
          gridx-=1
          await color()
        #DOWN
        elif randomnumber==3 and gridx<5:
          gridx+=1
          await color()
        #LEFT
        elif randomnumber==4 and gridy>0:
          gridy-=1
          await color()

      #RESTORE
      gridx=storedgridx
      gridy=storedgridy
      grid2[gridx][gridy] = '😀 '

      #dragon pathfinding-------------------------------------------------------

      global times

      if amt>5 and amt<13:
        times=1
      elif amt>12 and amt<40:
        times=2
      elif amt>39 and amt<82:
        times=3
      elif amt>81 and amt<178:
        times=5
      elif amt>177:
        times=7


      for i in range(times):
        if playinggridgame:
          grid2[dragonx][dragony]='🔹 '

          if abs(dragonx-gridx)>abs(dragony-gridy) or abs(dragonx-gridx)==abs(dragony-gridy):
            if dragonx-gridx<0:
              dragonx+=1 #downwards
            elif dragonx-gridx>0:
              dragonx-=1 #upwards

          elif abs(dragonx-gridx)<abs(dragony-gridy):
            if dragony-gridy<0:
              dragony+=1 #rightwards
            elif dragony-gridy>0:
              dragony-=1 #leftwards
              
          if dragonx==gridx and dragony==gridy and playinggridgame:
            await msg.channel.send('You were eaten by the dragon!')
            playinggridgame=False
            health=0

          grid2[dragonx][dragony] = '🐉 '


    #fail
    else:
      await msg.channel.send('The amount of spreading must be between 6 and 300.')

    grid2[5][11]='🕳️ '

    await printgrid()
    embedgrid2 = discord.Embed(title='A random game' + ' | Your health: ' +str(health), description=gridoutput,
                               color=0xc9f8ff)
    embedgrid2.set_footer(
      text=instructions)
    await msg.channel.send(embed=embedgrid2)


#First 1000 lines of code only

client.run('token_goes_here')


