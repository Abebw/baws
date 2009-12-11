#authors: Abe Barth-Werb 
#goal: postal service style game dev
#design: bidirectional shooter


#todo
#add bidirection mode
#for alex: add yourself to author line
#add some enemy craft
#add a system so things enterence can b scripted (then we have a simple level system)
#prevent player from leaving screen

import pygame, math
pygame.init()
screen = pygame.display.set_mode((600,400))
world = pygame.Surface((3000,400)) #this would be the dimensions of the level
clock = pygame.time.Clock()
drawloc = [0,0]
running=True

def add(x,y):
    return [x[0]+y[0], x[1]+y[1]]
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

    world.fill([0,0,0])
    allsprites.draw(world)
    screen.blit(world,drawloc)
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
    #drawloc[0] = drawloc[0] - 1 this line makes the camera move right
    for e in pygame.event.get():
        processevent(e)
    draw()
    clock.tick(60)
