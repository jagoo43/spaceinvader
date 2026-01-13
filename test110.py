import math
import random
import pygame
SCREENWIDTH=800
SCREENHIEGHT=500
FPS=60
PLAYERWIDTH=64
PLAYERHIEGHT=64
PLAYERSPEED=3
ENEMYWIDTH=64
ENEMYHIEGHT=64
BULLETWIDTH=32
BULLETHIEGHT=32
PLAYERSTARTX=370
PLAYERSTARTY=380
ENEMYSTARTYMIN=50
ENEMYSTARTMAX=150
ENEMYSPEEDX=2
ENEMYSPEEDY=40
BULLETSPEEDY=6
COLLISONDITANCE=27
pygame.init()
screen=pygame.display.set_mode((SCREENWIDTH,SCREENHIEGHT))
pygame.display.set_caption("Space Invader Game")
clock=pygame.time.Clock()
background=pygame.image.load("bg1.png")
background=pygame.transform.scale(background,(SCREENWIDTH,SCREENHIEGHT))
playerimg=pygame.image.load("spaceship.png")
playerimg=pygame.transform.scale(playerimg(PLAYERWIDTH,PLAYERHIEGHT))
playerx=PLAYERSTARTX
playery=PLAYERSTARTY
playerxchange=0
enemyimg=[]
enemyx=[]
enemyY=[]
enemyxchange=[]
enemyychange=[]
numofenemies=6
for i in range(numofenemies):
    img=pygame.image.load("alien.png")
    img=pygame.transform.scale(img,ENEMYWIDTH,ENEMYHIEGHT)
    enemyimg.append(img)
    enemyx.append(random.randint(0,SCREENWIDTH=ENEMYWIDTH))
    enemyY.append(random.randint(ENEMYSTARTYMIN,ENEMYSTARTMAX))
    enemyxchange.append(ENEMYSPEEDX)
    enemyychange.append(ENEMYSPEEDY)
bulletimg=pygame.image.load("bullet.png")
bulletimg=pygame.transform.scale(bulletimg,(BULLETWIDTH,BULLETHIEGHT))
bulletx=0
bullety=PLAYERSTARTX
bulletstate="ready"
scorevalue=0
font=pygame.font.Font("freesansbold.ttf",33)
overfont=pygame.font.Font("freesansbold.ttf",63)
def showscore(x,y):
    score=font.render(f"Score:{scorevalue}",True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext():
    overtext=overfont.render("GAME OVER",True,(255,255,255))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg{i},(x,y))
def firebullett(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+PLAYERWIDTH//2-BULLETWIDTH//2,y))
def iscollision(enemyX,enemyY,bulletx,bullety):
    distance=math.sqrt((enemyX-bulletx)**2+(enemyY-bullety)**2)
    return distance<COLLISONDITANCE
running=True
while running:
    clock.tick(FPS)
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerxchange=-PLAYERSPEED
            if event.key==pygame.K_RIGHT:
                playerxchange=PLAYERSPEED
            if event.key==pygame.K_SPACE and bulletstate=="ready":
                bulletx=playerx
                firebullett(bulletx,bullety)
        if event.type==pygame.KEYUP:
            if event.key in (pygame.K_LEFT,pygame.K_RIGHT):
                playerxchange=0
    playerx+=playerxchange
    playerx=max(0,min(playerx,SCREENWIDTH-PLAYERWIDTH))
    for i in range(numofenemies):
        if enemyY[i]>340:
            for j in range(numofenemies):
                enemyY[j]=2000
            gameovertext()
            break
        enemy[i]+=enemyxchange[i]
        if enemy[i]<=0 or enemyx[i]>=SCREENWIDTH-ENEMYWIDTH:
            enemyxchange[i]*=-1
            enemyY[i]+=enemyychange[i]
        if iscollision(enemyx[i],enemyY[i],bulletx,bullety):
            bullety=PLAYERSTARTY
            bulletstate="ready"
            scorevalue+=1
            enemyx[i]=random.randint(0,SCREENWIDTH-ENEMYWIDTH)
            enemyY[i]=random.randint(ENEMYSTARTYMIN,ENEMYSTARTMAX)
        enemy(enemyx[i],enemyY[i],i)
    if bullety<=0:
        bullety=PLAYERSTARTY
        bulletstate="ready"
    elif bulletstate=="fire":
        firebullett(bulletx,bullety)
        bullety-=BULLETSPEEDY
    player(playerx,playery)
    showscore(10,10)
    pygame.display.update