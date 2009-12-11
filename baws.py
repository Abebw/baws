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
#add some enemy craft
#add a system so things enterence can b scripted (then we have a simple level system)

import pygame
pygame.init()
screen = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
running=True

def add(x,y):
    return [x[0]+y[0], x[1]+y[1]]
class block (pygame.sprite.Sprite):
    #uglyness warning: color is a helper variable because i didnt wannt pull outthe colour from the block changing color wont do anythign untill the block is resized
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,15])
        self.image.fill([100,100,100])
        self.color = [100,100,100]
        self.rect = self.image.get_rect()
        self.rect.center = [100,100]
        self.direction = [0,0]
    def setShape(self, w, h):
        i = pygame.Surface([w,h])
        i.fill(self.color)
        temp  = pygame.Rect(0,0,w,h)
        temp.center = self.rect.center
        self.image = i
        self.rect = temp
    def setColor(self, c):
        self.color = c
        self.image.fill(c)
    def update(self):
        self.rect = self.rect.move(self.direction)

def processevent(e):
    global running
    global p
    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYDOWN:
        global temp
        print temp.rect
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
    allsprites.draw(screen)
    pygame.display.update()

p = block()
allsprites = pygame.sprite.Group()
temp = block()
temp.rect.center = [200,200]
temp.setShape(20,75)
temp.setColor((255,255,0))
allsprites.add(temp)
allsprites.add(p)

while running:
    allsprites.update()
    for e in pygame.event.get():
        processevent(e)
    draw()
    clock.tick(60)
