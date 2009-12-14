#authors: Abe Barth-Werb, Alex Willingham
#goal: postal service style game dev
#design: bidirectional shooter


#todo
#add some enemy craft
#add a system so things enterence can b scripted (then we have a simple level system) !!Suggestion at bottom (also source of nasty console spam)

import pygame, math
pygame.init()
resolution_x = 600
resolution_y = 400
screen = pygame.display.set_mode((resolution_x,resolution_y))
scroll = [-1,0]
world = pygame.Surface((3000,400)) #this would be the dimensions of the level
clock = pygame.time.Clock()
drawloc = [0,0]
running=True

def add(x,y):
    return [x[0]+y[0], x[1]+y[1]]
def negate(x):
    return [-1* x[0], -1*x[1]]
def floor(x):
    return [math.floor(x[0]),math.floor(x[1])]
def ceiling(x):
    return [math.ceil(x[0]),math.ceil(x[1])]
def modOne(x):
    return [x[0]%1,x[1]%1]
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
        self.rounding = [0,0]
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
        if self.rect.top < 0:
            self.rect = self.rect.move([0,2])
        if self.rect.bottom > resolution_y:
            self.rect = self.rect.move([0,-2])
        if self.rect.left < 0:
            self.rect = self.rect.move([2,0])
        if self.rect.right > resolution_x:
            self.rect = self.rect.move([-2,0])
        self.rounding = add(self.rounding, modOne(self.direction))
        self.rect = self.rect.move(floor(self.rounding))
        self.rounding = modOne(self.rounding)
def processevent(e):
    global running
    global p
    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYDOWN:
        global screen 
        print screen
        if e.key == pygame.K_w:
            p.direction = add(p.direction,[0,-2])
        elif e.key == pygame.K_s:
            p.direction = add(p.direction,[0,2])
        elif e.key == pygame.K_a:
            p.direction = add(p.direction,[-2,0])
        elif e.key == pygame.K_d:
            p.direction = add(p.direction,[2,0])
        elif e.key == pygame.K_SPACE:
            global scroll
            p.direction = add(p.direction, scroll)
    if e.type == pygame.KEYUP:
        if e.key == pygame.K_w:
            p.direction = add(p.direction,[0,2]) 
        elif e.key == pygame.K_s:
            p.direction = add(p.direction,[0,-2])
        elif e.key == pygame.K_a:
            p.direction = add(p.direction,[2,0])
        elif e.key == pygame.K_d:
            p.direction = add(p.direction,[-2,0])
        elif e.key == pygame.K_SPACE:
            global scroll
            scroll = negate(scroll)
            p.direction = add (p.direction, negate(scroll))

            
def draw():
    global screen
    global p

    world.fill([0,0,0])
    allsprites.draw(world)
    screen.blit(world,drawloc)
    pygame.display.update()

p = block()
p.direction = negate(scroll)
allsprites = pygame.sprite.Group()
temp = block()
temp.rect.center = [200,200]
temp.setShape(20,75)
temp.setColor((255,255,0))
allsprites.add(temp)
allsprites.add(p)

while running:
    allsprites.update()
    drawloc = add(drawloc, scroll)
    for e in pygame.event.get():
        processevent(e)
    draw()
    clock.tick(60)
    #print pygame.time.get_ticks() / 60  #here's a solution to having entrances scripted.  Simply get a number off of the timer.
                                            #then a level will have statements like "if time == whatever:  horde_of_banshees()"
#    if pygame.time.get_ticks() % 300 == 0:
#        print pygame.time.get_ticks()/60

