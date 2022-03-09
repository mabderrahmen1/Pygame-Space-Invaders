
import pygame,sys,os
import random,math


from pygame.constants import K_a, K_d, K_w


pygame.init()

FPS=60
widht,height=800,600
screen=pygame.display.set_mode((widht,height))
pygame.display.set_caption("space invaders")
BLACK=(255,255,255)
clock = pygame.time.Clock()
vel=1
font=pygame.font.SysFont('comic sans',40)
spawnCooldown=30


#assets loading
spaceBackground=pygame.image.load(os.path.join("assets\\spaceBackground.jpg"))
spaceBackground=pygame.transform.scale(spaceBackground,(widht,height))
spaceShip=pygame.image.load(os.path.join("assets\\spaceShip.png"))
spaceShip=pygame.transform.scale(spaceShip,(100,100))
invaderBlack=pygame.image.load(os.path.join("assets\\invader.png"))
invaderBlack=pygame.transform.scale(invaderBlack,(80,80))
invaderRed=pygame.image.load(os.path.join("assets\\invaderRed.png"))
invaderRed=pygame.transform.scale(invaderRed,(50,50))
invaderGreen=pygame.image.load(os.path.join("assets\\invaderGreen.png"))
invaderGreen=pygame.transform.scale(invaderGreen,(50,50))
invaderBlue=pygame.image.load(os.path.join("assets\\invaderBlue.png"))
invaderBlue=pygame.transform.scale(invaderBlue,(100,50))
invaderOrange=pygame.image.load(os.path.join("assets\\invaderOrange.png"))
invaderOrange=pygame.transform.scale(invaderOrange,(50,50))
bulletImage=pygame.image.load(os.path.join("assets\\bullet.png"))
bulletImage=pygame.transform.scale(bulletImage,(25,25))



def drawText(text,font,color,surface,x,y):
    textObj=font.render(str(text),1,color)
    textRect=textObj.get_rect()
    textRect.topleft=(x,y)
    surface.blit(textObj,textRect)



def isCollision(x,y,x1,y1):
    distance=math.sqrt(math.pow(x-x1,2)+math.pow(y-y1,2))
    if distance<=50:
        return True
    else:
        return False


def main():
    score=0
    invadersList=[invaderBlue,invaderGreen,invaderOrange,invaderRed]
    run=True
    shipx,shipy=300,500
    invaderx=[0]
    invadery=[0]
    invaderVel=[0.5]
    invaderImage=[invaderRed]
    i=0
    bulletVel=2
    numInvaders=6
    #bullet
    bullety=shipy-20
    bulletx=shipx+40
    bulletState="ready"
    while run:
        pygame.display.update()
        screen.blit(spaceBackground,(0,0))
        base=pygame.Rect(0,height-100,widht,height)
        
        bullet=pygame.Rect(bulletx,bullety-20,25,25)
        #invaders spawn
        for i in range(numInvaders):
            invaderx.append(random.randint(0,widht-80))
            invaderImage.append(random.choice(invadersList))
            invadery.append(random.randint(0,150))
            invaderVel.append(0.5)  
            invader=[pygame.Rect(invaderx[i],invadery[i],100,100)]
            invader.append(invader)
            
                
        #invader mouvements
        for i in range(numInvaders):
            invaderx[i]+=invaderVel[i]
            if invaderx[i]>=widht-100 :
                invaderVel[i]=-0.5
                invadery[i]+=20
            elif  invaderx[i]<=0:
                invadery[i]+=20
                invaderVel[i]=0.5
 
            
            if isCollision(bulletx,bullety,invaderx[i],invadery[i]): 
                bullety=shipy-20
                bulletState="ready"
                invadery[i]=0
                score+=10
            if isCollision(invaderx[i],invadery[i],shipx,shipy):
                sys.exit()
                
            screen.blit(invaderImage[i],(invaderx[i],invadery[i]))
            
            
        
                
        #ship mouvements
        ship=pygame.Rect(shipx,shipy,100,100)
        screen.blit(spaceShip,(shipx,shipy))
        
        keysPressed=pygame.key.get_pressed()
        if keysPressed[K_d] and shipx<widht-100:
            shipx+=vel
        if keysPressed[K_a] and shipx>0:
            shipx-=vel

                
            #bullet mouvements
        if bulletState=="fire":
            screen.blit(bulletImage,(bulletx,bullety))
            bullety-=bulletVel
            #bulletx=shipx+40
            

        #bullet collision
        if bullety<=0 :
            bulletState="ready"
            bullety=shipy-20
            bulletx=shipx+40
            
            
        drawText("Score :",font, BLACK,screen,0,0)
        drawText(score,font,BLACK,screen,100,0)
        
        #lose the game
        
           

        i+=1   

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==K_w:
                    bulletx=shipx+40
                    bulletState="fire"



    pygame.quit()
    sys.exit()


main()
