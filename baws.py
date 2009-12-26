#authors: Abe Barth-Werb, Alex Willingham
#goal: postal service style game dev
#design: bidirectional shooter


#todo:now
#simple black and white kamakazee enemies




#todo: long term
#make library to procedurally generate sprites of basic geometrys


import pygame, math
pygame.init()
resolution_x = 600
resolution_y = 400
screen = pygame.display.set_mode((resolution_x,resolution_y))
scroll = [0,0] #[0,-1]
world = pygame.Surface((600,4000)) #this would be the dimensions of the level
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
        self.image = pygame.Surface([15,30])
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
        self.setShape(self.rect.width,self.rect.height)
    def update(self):
        self.rect = self.rect.move(self.direction)
        self.rounding = add(self.rounding, modOne(self.direction))
        self.rect = self.rect.move(floor(self.rounding))
        self.rounding = modOne(self.rounding)
class player(block):
    def __init__(self):
        block.__init__(self)
        self.shooting = False
        self.cooldown = 0
        self.firerate = 10
    def shoot(self):
        global allsprites
        temp =  bullet()
        temp.rect.center = p.rect.center
        temp.setWhite()
        temp.direction = [3,0]
        allsprites.add(temp)
        temp =  bullet()
        temp.rect.center = p.rect.center
        temp.setBlack()
        temp.direction = [-3,0]
        allsprites.add(temp)
    def update(self):
        block.update(self)
        if (self.cooldown > 0):
            self.cooldown = self.cooldown -1
        if (self.cooldown < 1) and (self.shooting):
            self.shoot()
            self.cooldown = self.firerate

        #keep player on screen, fixed to use window instead of world
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > resolution_y:
            self.rect.bottom = resolution_y
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > resolution_x:
            self.rect.right = resolution_x
            
        
        
class bullet(block):
    def __init__(self):
        block.__init__(self)
        self.setColor([100,0,0])
        self.setShape(7,7)
    def update(self):
        block.update(self)
        #here goes checking for collision with enemy group
        
        #kill bullet when it is off screen
        if self.rect.right < 0:
            allsprites.remove(self)
        if self.rect.left > resolution_x:
            allsprites.remove(self)
        if self.rect.bottom < 0:
            allsprites.remove(self)
        if self.rect.top > resolution_y:
            allsprites.remove(self)
    def setWhite(self):
        self.setColor([255,255,255])
    def setBlack(self):
        self.setColor([0,0,0])
def processevent(e):
    global running
    global p
    if e.type == pygame.QUIT:
        running = False
    if e.type == pygame.KEYDOWN:
        global screen 
        if e.key == pygame.K_w:
            p.direction = add(p.direction,[0,-2])
        elif e.key == pygame.K_s:
            p.direction = add(p.direction,[0,2])
        elif e.key == pygame.K_a:
            p.direction = add(p.direction,[-2,0])
        elif e.key == pygame.K_d:
            p.direction = add(p.direction,[2,0])
        elif e.key == pygame.K_SPACE:
            global p
            p.shooting = True
            
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
            p.shooting = False
            #global scroll
            #scroll = negate(scroll)
            #p.direction = add (p.direction, negate(scroll))

            
def draw():
    global screen
    global p

    world.fill([50,50,50])
    allsprites.draw(world)
    screen.blit(world,drawloc)
    pygame.display.update()

p = player()
p.direction = negate(scroll)
allsprites = pygame.sprite.Group()
whiteAllyBullets = pygame.sprite.Group()
blackAllyBullets = pygame.sprite.Group()


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

