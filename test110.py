import math,random,pygame
SCREENWIDTH=800
SCREENHEIGHT=500
FPS=60
PLAYERWIDTH=64
PLAYERHEIGHT=64
PLAYERSPEED=3
ENEMYWIDTH=64
ENEMYHEIGHT=64
BULLETWIDTH=32
BULLETHEIGHT=32
PLAYERSTARTX=370
PLAYERSTARTY=380
ENEMYSTARTYMIN=50
ENEMYSTARTYMAX=150
ENEMYSPEEDX=2
ENEMYSPEEDY=40
BULLETSPEEDY=6
COLLISIONDISTANCE=27
pygame.init()
screen=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Space Invader Game")
clock=pygame.time.Clock()
background=pygame.image.load("img34.png")
background=pygame.transform.scale(background,(SCREENWIDTH,SCREENHEIGHT))
playerimg=pygame.image.load("spaceship.png")
playerimg=pygame.transform.scale(playerimg,(PLAYERWIDTH,PLAYERHEIGHT))
enemyimg=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
numofenemies=6
for i in range(numofenemies):
    img=pygame.image.load("alien.png")
    img=pygame.transform.scale(img,(ENEMYWIDTH,ENEMYHEIGHT))
    enemyimg.append(img)
    enemyx.append(random.randint(0,SCREENWIDTH-ENEMYWIDTH))
    enemyy.append(random.randint(ENEMYSTARTYMIN,ENEMYSTARTYMAX))
    enemyxchange.append(ENEMYSPEEDX)
    enemyychange.append(ENEMYSPEEDY)
bulletimg=pygame.image.load("bullet.png")
bulletimg=pygame.transform.scale(bulletimg,(BULLETWIDTH,BULLETHEIGHT))
bulletx=0
bullety=PLAYERSTARTY
bulletstate="ready"
playerx=PLAYERSTARTX
playery=PLAYERSTARTY
playerxchange=0
scorevalue=0
font=pygame.font.Font("freesansbold.ttf",32)
overfont=pygame.font.Font("freesansbold.ttf",64)
def showscore(x,y):
    score=font.render(f"Score:{scorevalue}",True,(255,255,255))
    screen.blit(score,(x,y))
def gameovertext():
    overtext=overfont.render("GAME OVER",True,(255,255,255))
    screen.blit(overtext,(200,200))
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def firebullet(x,y):
    global bulletstate
    bulletstate="fire"
    screen.blit(bulletimg,(x+PLAYERWIDTH//2-BULLETWIDTH//2,y))
def iscollision(ex,ey,bx,by):
    return math.sqrt((ex-bx)**2+(ey-by)**2)<COLLISIONDISTANCE
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
                firebullet(bulletx,bullety)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerxchange=0
    playerx+=playerxchange
    if playerx<0:playerx=0
    if playerx>SCREENWIDTH-PLAYERWIDTH:playerx=SCREENWIDTH-PLAYERWIDTH
    for i in range(numofenemies):
        if enemyy[i]>340:
            for j in range(numofenemies):
                enemyy[j]=2000
            gameovertext()
            break
        enemyx[i]+=enemyxchange[i]
        if enemyx[i]<=0 or enemyx[i]>=SCREENWIDTH-ENEMYWIDTH:
            enemyxchange[i]*=-1
            enemyy[i]+=enemyychange[i]
        if iscollision(enemyx[i],enemyy[i],bulletx,bullety):
            bullety=PLAYERSTARTY
            bulletstate="ready"
            scorevalue+=1
            enemyx[i]=random.randint(0,SCREENWIDTH-ENEMYWIDTH)
            enemyy[i]=random.randint(ENEMYSTARTYMIN,ENEMYSTARTYMAX)
        enemy(enemyx[i],enemyy[i],i)
    if bullety<=0:
        bullety=PLAYERSTARTY
        bulletstate="ready"
    if bulletstate=="fire":
        firebullet(bulletx,bullety)
        bullety-=BULLETSPEEDY
    player(playerx,playery)
    showscore(10,10)
    pygame.display.update()
pygame.quit()
