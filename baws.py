#authors: Abe Barth-Werb 
#goal: postal service style game dev
#design: bidirectional shooter


#for abe or if alex feels up to it:
#make  an intermedairy camera surface (so you draw to that and that surface takes care of drawing the correct part of the world)
#post to github
#email alex with github loc
#add bidirection mode

#for alex: 
#add yourself to author line
#add movment of the player (maybe a boost or something have fun with it)
#add some enemy craft
#add a system so things enterence can b scripted (then we have a simple level system)

import pygame
pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running=True

def add(x,y):
    return [x[0]+y[0], x[1]+y[1]]
class Player (pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.Surface([30,15])
        self.image.fill([100,100,100])
        self.rect = self.image.get_rect()
        self.rect.center = [100,100]
        self.direction = [0,0]
    def update(self):
        self.rect = self.rect.move(self.direction)

def processevent(e):
    global running
    global p
    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_w:
            p.direction = add(p.direction,[0,-2])
        elif e.key == pygame.K_s:
            p.direction = add(p.direction,[0,2])
        elif e.key == pygame.K_a:
            p.direction = add(p.direction,[-2,0])
        elif e.key == pygame.K_d:
            p.direction = add(p.direction,[2,0])
    if e.type == pygame.KEYUP:
        if e.key == pygame.K_w:
            p.direction = add(p.direction,[0,2]) 
        elif e.key == pygame.K_s:
            p.direction = add(p.direction,[0,-2])
        elif e.key == pygame.K_a:
            p.direction = add(p.direction,[2,0])
        elif e.key == pygame.K_d:
            p.direction = add(p.direction,[-2,0])
                
            
def draw():
    global screen
    global p

    screen.fill([0,0,0])
    screen.blit(p.image, p.rect)
    pygame.display.update()

p = Player()

while running:
    p.update()
    for e in pygame.event.get():
        processevent(e)
    draw()
    clock.tick(60)
