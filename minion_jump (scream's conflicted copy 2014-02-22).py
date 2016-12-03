bif="building.jpg"
mic1="mini.png"
mic2="mini2.png"
mic3="mini3.png"
over="gameover.jpg"
select="doodle_select.jpg"
stn="ball.png"
home="homepage.jpg"
plat="plank.png"
hlp="help.jpg"
credit="credit.jpg"
import pygame, sys
from pygame.locals import *
import random
import os.path
high=0
f=open("high.txt","r")
high=f.read()
high=int(high)
f.close()
pygame.init()
screen=pygame.display.set_mode((320,420),0,32)
#img=pygame.Surface((50,5))
#img.fill((0,0,0))
pygame.display.set_caption("MINION JUMP")
background=pygame.image.load(bif).convert()
doodle1=pygame.image.load(mic1).convert_alpha()
c=pygame.image.load(credit).convert_alpha()
doodle2=pygame.image.load(mic2).convert_alpha()
doodle3=pygame.image.load(mic3).convert_alpha()
gameover=pygame.image.load(over).convert()
st=pygame.image.load(stn).convert_alpha()
ds=pygame.image.load(select).convert_alpha()
hp=pygame.image.load(home).convert_alpha()
img=pygame.image.load(plat).convert_alpha()
help1=pygame.image.load(hlp).convert_alpha()

l=[]
score=0
s=[]
class obs:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class stones:
    def __init__(self):
        self.x=random.randint(0,260)
        self.y=0
stone=stones()
s.append(stone)

def initialise():
    pygame.mixer.music.load("Faint2.mp3")
    pygame.mixer.music.play(-1,0.0)
    q=obs(180,400)
    l.append(q)
    w=obs(random.randint(0,260),350)
    l.append(w)
    e=obs(random.randint(0,260),300)
    l.append(e)
    r=obs(random.randint(0,260),250)
    l.append(r)
    t=obs(random.randint(0,260),200)
    l.append(t)
    y=obs(random.randint(0,260),150)
    l.append(y)
    u=obs(random.randint(0,260),100)
    l.append(u)
    v=obs(random.randint(0,260),50)
    l.append(v)

initialise()
class player:
    def __init__(self):
        self.x=l[0].x
        self.y=l[0].y-55
        

play=player()
def draw_obs():
    for i in range(len(l)):
        x=l[i].x
        y=l[i].y
        screen.blit(img,(x,y))

def draw_stone():
    for i in range(len(s)):
        x=s[i].x
        y=s[i].y
        screen.blit(st,(x,y))


def collide():
    flag=0
    for i in range(len(l)):
        if (play.x> (l[i].x-30) and play.x < (l[i].x+50)):
            if (play.y>=(l[i].y-56) and play.y<(l[i].y-54)):
                flag=1
    return flag
def stone_collide():
    flag=0
    for i in range(len(s)):
        if s[i].x > play.x -28 and s[i].x <play.x+28:
            if s[i].y > play.y-25 and s[i].y < play.y + 52:
                flag=1
        if s[i].y==play.y and s[i].x==play.x:
            flag=1
    return flag

count=0
speed=12
def stone_fall():
    for i in range(len(s)):
        s[i].y+=1
        if s[i].y>420:
            s[i].x=random.randint(0,260)
            s[i].y=0

def draw(c,score):
    if c==0:
        play.y+=1
    else:
        if play.y>200:
            play.y-=1
        else:
            for i in range(len(l)):
                l[i].y+=1
            stone_fall()
            if l[0].y>420:
                del l[0]
                s=obs(random.randint(0,260),50)
                l.append(s)
                score+=5
    if play.x<-29:
        play.x=319
    if play.x>320:
        play.x=1
    return score
d=0
def doodle_select():
        flag=0
        x=1
        while x:
            screen.blit(ds,(0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_1:
                        flag=1
                        x=0
                        break
                    if event.key==K_2:
                        flag=2
                        x=0
                    if event.key==K_3:
                        flag=3
                        x=0
                        break
        return flag

def start_screen():
        l1=[]
        x3=1
        flag=1
        while x3:
                screen.blit(hp,(0,0))
                pygame.display.update()

                for event in pygame.event.get():
                        if event.type==KEYDOWN:
                                if event.key==K_p:
                                        start=1
                                        x3=0
                                        break
                                if event.key==K_e:
                                        screen.blit(c,(0,0))
                                        pygame.display.update()
                                        pygame.time.wait(1000)
                                        pygame.quit()
                                        sys.exit()
                                if event.key==K_c:
                                    flag=doodle_select()
                                if event.key==K_i:
                                    while not pygame.key.get_pressed()[K_h]:
                                        screen.blit(help1,(0,0))
                                        pygame.display.update()
                                        pygame.event.get()


                                        
                                    
                                    

        l1.append(start)
        l1.append(flag)
        return l1

              

                        
m=0    
sta=[0,1]      
while True:
    m=0
    for event in pygame.event.get():
        if event.type== quit:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            x2=1
            if event.key==K_SPACE:
                while x2:
                    for event in pygame.event.get():
                        if event.key==K_p:
                            x2=0
                            break
    if play.y>370 or d==1 :
            pygame.mixer.music.load("gover.mp3")
            pygame.mixer.music.play(0,0.0)
            if(high<score):
                f=open("high.txt","w")
                f.write(str(score))
                f.close()
                f=open("high.txt","r")
                high=f.read()
                high=int(high)
                f.close()
            x1=1
            while x1:
                for event in pygame.event.get():
                    if event.type==KEYDOWN:
                        if event.key==K_p:
                            l=[]
                            initialise()
                            play.x=l[0].x
                            play.y=l[0].y-55
                            x1=0
                            score=0
                            speed=10
                            for i in range(len(s)-1):
                                s.pop()
                            for i in range(len(s)):
                                s[i].y=0
                                s[i].x=random.randint(0,260)
                                screen.blit(st,(stone.x,stone.y))
                            break
                        if event.key==K_h:
                                l=[]
                                initialise()
                                play.x=l[0].x
                                play.y=l[0].y-55
                                x1=0
                                score=0
                                speed=10
                                for i in range(len(s)-1):
                                    s.pop()
                                for i in range(len(s)):
                                        s[i].y=0
                                        s[i].x=random.randint(0,260)
                                        screen.blit(st,(stone.x,stone.y))
                                        break
                                sta=start_screen()
                                
                   # else:
                if m==0:
                    pygame.time.wait(1500)
                m=1
                screen.blit(gameover,(0,0))
                font = pygame.font.SysFont("ravie", 40)
                text = font.render(str(score), 1, (0,0,0))
                screen.blit(text, (140,200))
                font = pygame.font.SysFont("ravie", 25)
                text = font.render("HIGH SCORE", 1, (0,0,0))
                screen.blit(text, (17,255))
                font = pygame.font.SysFont("ravie", 25)
                text = font.render(str(high), 1, (0,0,0))
                screen.blit(text, (226,254))
                pygame.display.update()
    if sta[0]==0:
            sta=start_screen()
        
    screen.blit(background,(0,0))
    draw_obs()
    stone_fall()
    draw_stone()
    f=collide()
    if(f==1):
        count=80
    score=draw(count,score)
    if score==50:
        speed=10
    if score==100:
        speed=9
    if score==150:
        speed=8
    if score==200:
        speed=7
        if len(s)==1:
            z=stones()
            s.append(z)
    if score==250:
        speed=6
    if score==300:
        speed=5
        if len(s)==2:
            z=stones()
            s.append(z)
    if score==500:
        speed=5
        if len(s)==3:
            z=stones()
            s.append(z)
    d=stone_collide()
    font = pygame.font.Font(None, 16)
    text = font.render("SCORE : ", 1, (10, 10, 10))
    screen.blit(text,(240,20))
    text = font.render(str(score), 1, (0,0,0))
    screen.blit(text, (290,20))
    if event.type==KEYDOWN:
        if event.key==K_LEFT:
            play.x-=1
        if event.key==K_RIGHT:
            play.x+=1
    if sta[1]==1:
        screen.blit(doodle1,(play.x,play.y))
    if sta[1]==2:
        screen.blit(doodle2,(play.x,play.y))
    if sta[1]==3:
        screen.blit(doodle3,(play.x,play.y))

    pygame.time.wait(speed)	
    if count!=0:
        count-=1           
    pygame.display.update()



    
