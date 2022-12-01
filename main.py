import pygame
import time
from data import textlist,textposlist
pygame.init()

clock = pygame.time.Clock()
size = width, height = 800,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('What the hell man im so confused')
font = pygame.font.Font('freesansbold.ttf', 24)

standing = pygame.image.load("stand.png")
up = pygame.image.load("up.png")
down = pygame.image.load("down.png")
left = pygame.image.load("left.png")
right = pygame.image.load("right.png")
flap = pygame.image.load("flap.png")
def addtext(textadd,textpos):
    text = font.render(textadd, True, (0, 0, 0), (225,225,225))
    screen.blit(text, textpos)
    
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    
class spike(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class ju(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
class Room(object):
    wall_list = None
    spike_list = None
    enemy_sprites = None
    ju_list = None
 
    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.spike_list = pygame.sprite.Group()
        self.ju_list = pygame.sprite.Group()

        
class Room1(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 560
        walls = [[0, 0, 20, 600, (20,20,10)], #left wall
                 [780, 0, 20, 500, (20,20,10)], #top right
                 [780, 580, 100, 20, (20,20,10)], #bottom right
                 [20, 0, 760, 20, (20,20,10)], #top wall
                 [20, 580, 760, 20, (20,20,10)], #bottom wall
                 [180, 460, 400, 20, (30,30,40)] #middle 
                ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
class Room2(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 560
        walls = [[0, 0, 20, 500, (20,20,10)], #top left
                 [0, 580, 100, 20, (20,20,10)], #bottom left
                 [780, 0, 20, 20, (20,20,10)], #top right
                 [780, 80, 20, 600, (20,20,10)], #bottom right
                 [20, 0, 760, 20, (20,20,10)], #top wall
                 [20, 580, 760, 20, (20,20,10)], #bottom wall
                 [20, 460, 600, 20, (30,30,40)], #middle
                 [180, 400, 600, 20, (30,30,40)], #middle
                 [760, 300, 300, 20, (30,30,40)],
                 [690, 80, 300, 20, (30,30,40)],
                 [20, 200, 130, 20, (30,30,40)]
                ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
class Room3(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 40
        walls = [[0, 0, 20, 20, (20,20,10)], #top right
                 [0, 80, 20, 600, (20,20,10)],
                 [780, 0, 20, 250, (20,20,10)],
                 [780, 350, 20, 250, (20,20,10)],
                 [20, 0, 760, 20, (20,20,10)],
                 [20, 580, 760, 20, (20,20,10)],
                 [20, 80, 300, 20, (30,30,40)],
                 [20, 160, 100, 20, (30,30,40)],
                 [500, 160, 280, 20, (30,30,40)],
                 [20, 500, 100, 20, (30,30,40)],
                 [300, 400, 89, 20, (30,30,40)],
                 [580, 250, 220, 20, (20,20,10)],
                ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
class Room4(Room):
    def __init__(self):
        self.startx = 40
        self.starty = 560
        super().__init__()
        walls = [[0, 0, 20, 250, (20,20,10)],
                 [0, 350, 20, 250, (20,20,10)],
                 [780, 80, 20, 600, (20,20,10)], #top right
                 [20, 0, 800, 20, (20,20,10)], #top wall
                 [20, 580, 760, 20, (20,20,10)], #bottom wall
                 [180, 460, 400, 20, (30,30,40)],
                 [180, 200, 400, 20, (30,30,40)],
                 [580, 300, 220, 20, (20,20,10)]#middle 
                ]
        spikey = [[190, 430, 200, 20, (200,20,20)]]
        
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
            
class Room5(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 40
        walls = [[0, 0, 20, 20, (20,20,10)],
                 [0, 80, 20, 600, (20,20,10)],
                 [780, 20, 20, 500, (20,20,10)], #top right
                 [20, 0, 800, 20, (20,20,10)], #top wall
                 [20, 580, 760, 20, (20,20,10)], #bottom wall
                 [40, 80, 600, 20, (20,20,10)],#middle
                 [80, 200, 900, 20, (20,20,10)],
                 [20, 400, 220, 20, (20,20,10)],
                 [690, 560, 760, 20, (20,20,10)]
                ]
        spikey = [[90, 79, 200, 10, (200,0,10)],[490, 79, 190, 20, (200,20,20)], [80, 189, 300, 20, (200,20,10)],[20, 579, 800, 20, (200,20,10)]
                  ]
        
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
class Room6(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 560
        walls = [[780, 0, 20, 20, (20,20,10)],
                 [780, 80, 20, 600, (20,20,10)],
                 [0, 20, 20, 500, (20,20,10)], #top right
                 [20, 0, 800, 20, (20,20,10)], #top wall
                 [20, 580, 760, 20, (20,20,10)],
                 [20, 500, 100, 20, (20,20,10)],
                 [20, 400, 100, 20, (20,20,10)],
                 [20, 300, 100, 20, (20,20,10)],
                 [750, 200, 100, 20, (20,20,10)]
                ]
        spikey = [
                  ]
        
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
class Room7(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 40
        walls = [[0, 0, 20, 20, (20,20,10)],
                 [0, 80, 20, 600, (20,20,10)], #top right
                 [20, 0, 800, 20, (20,20,10)], #top wall
                 [20, 80, 400, 20, (20,20,10)],
                 [20, 580, 800, 20, (20,20,10)],
                 [780,20,20,540,(20,20,10)]
                ]
        spikey = [
                 [300, 300, 480, 10, (200,30,40)],
                 [20, 450, 400, 10, (200,30,40)],
                 [500, 150, 280, 10, (200,30,40)],
                 [20, 200, 200, 10, (200,30,40)]
                  ]
        
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
            
class Room8(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 560
        walls = [[0, 0, 20, 20, (20,20,10)],
                 [0, 0, 20, 540, (20,20,10)], #top right
                 [20, 0, 800, 20, (20,20,10)], #top wall
                 [0, 580, 800, 20, (20,20,10)],
                 [780,100,20,540,(20,20,10)],
                 [180, 460, 400, 20, (30,30,40)],
                 [600, 20, 20, 400, (30,30,40)]
                ]
        spikey = [[180, 480, 20, 120, (200,30,40)],
                 [560, 480, 20, 120, (200,30,40)]
                  ]
        jus = [[620, 300, 160, 20, (30,30,150)]]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
        for item in jus:
            jjj = ju(item[0], item[1], item[2], item[3], item[4])
            self.ju_list.add(jjj)
            
class Room9(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 40
        walls = [[0, 0, 20, 20, (20,20,10)],
                 [0,100,20,540,(20,20,10)], #top right
                 [20, 0, 800, 20, (20,20,10)], #top wall
                 [0, 580, 800, 20, (20,20,10)],
                 [780,20,20,540,(20,20,10)]
                ]
        spikey = [[100, 180, 20, 400, (200,30,40)],
                 [300, 20, 20, 400, (200,30,40)],
                 [500, 180, 20, 400, (200,30,40)],
                 [700, 20, 20, 400, (200,30,40)]
                  ]
        jus = [[20, 20, 760, 560, (30,30,150)]]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
        for item in jus:
            jjj = ju(item[0], item[1], item[2], item[3], item[4])
            self.ju_list.add(jjj)

class Room10(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 560
        walls =  [[0,20,20,540,(20,20,10)], #top right
                 [20, 0, 800, 20, (20,20,10)], #top wall
                 [0, 580, 800, 20, (20,20,10)],
                 [780,80,20,540,(20,20,10)],
                 [0, 520, 100, 20, (20,20,10)]
                ]
        spikey = [
                 [100, 579, 600, 20, (200,30,40)]
                  ]
        jus = [[200, 400, 20,20, (30,30,150)],[500, 100, 20,20, (30,30,150)]]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
        for item in jus:
            jjj = ju(item[0], item[1], item[2], item[3], item[4])
            self.ju_list.add(jjj)

class Room11(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 40
        walls =  [[0,80,20,540,(20,20,10)], #top right
                 [0, 0, 900, 20, (20,20,10)], #top wall
                 [0, 580, 800, 20, (20,20,10)],
                 [780,0,20,800,(20,20,10)],
                 [60, 80, 400, 20, (20,20,10)]
                ]
        spikey = [
                  ]
        jus = [[500,80,20,500,(30,30,150)]]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
        for item in jus:
            jjj = ju(item[0], item[1], item[2], item[3], item[4])
            self.ju_list.add(jjj)

class Room12(Room):
    def __init__(self):
        super().__init__()
        self.startx = 40
        self.starty = 40
        walls =  [[0,80,20,540,(20,20,10)], #top right
                 [0, 0, 900, 20, (20,20,10)], #top wall
                 [0, 580, 800, 20, (20,20,10)],
                 [780,0,20,800,(20,20,10)],
                 [60, 80, 400, 20, (20,20,10)]
                ]
        spikey = [
                  ]
        jus = [[500,80,20,500,(30,30,150)]]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
        for item in spikey:
            spi = spike(item[0], item[1], item[2], item[3], item[4])
            self.spike_list.add(spi)
        for item in jus:
            jjj = ju(item[0], item[1], item[2], item[3], item[4])
            self.ju_list.add(jjj)
class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    jumpcount = 3
    grounded = False
    downpressed = False
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image = standing
        self.rect = self.image.get_rect()
        self.rect.y = x
        self.rect.x = y
 
    def movements(self, x, y):
        self.change_x += x
        self.change_y += y
        
    def moves(self, spiks, startx,starty):
        block_hit_list = pygame.sprite.spritecollide(self, spiks, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.x = startx
                self.rect.y= starty
                self.change_x =0
                self.change_y =0
                time.sleep(0.3)
            else:
                self.rect.x = startx
                self.rect.y= starty
                self.change_x =0
                self.change_y =0
                time.sleep(0.3)
 
        
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.x = startx
                self.rect.y= starty
                self.change_x =0
                self.change_y =0
                time.sleep(0.3)
            else:
                self.rect.x = startx
                self.rect.y= starty
                self.change_x =0
                self.change_y =0
                time.sleep(0.3)
    def mov(self, bots):
        if(len(bots)!=0):
            block_hit_list = pygame.sprite.spritecollide(self, bots, False)
            for block in block_hit_list:
                self.jumpcount+=1
                
    def move(self, walls):
        
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
                self.change_x = 0
            else:
                self.rect.left = block.rect.right
                self.change_x = 0
 
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                self.change_y = 0
                self.jumpcount = 3
            else:
                self.rect.top = block.rect.bottom
                self.change_y = 0
        
        if(self.change_x <-10):
            self.change_x =-10
        elif(self.change_x >10):
            self.change_x =10
        if(self.change_x >0):
            self.change_x -=0.1
        elif(self.change_x <0):
            self.change_x +=0.1
        if(self.change_y<0):
            self.change_y+=0.1
        elif(self.change_y>0 and Player.change_y < 100):
            self.change_y-=0.1
        elif(self.change_y>20):
            self.change_y=20
        elif(self.change_y<-20):
            self.change_y=-20
        if(self.downpressed == True):
            self.change_y+=0.2
            if(self.change_y>3):
                self.change_y = 3
        else:
            self.change_y+=0.5
        if(self.rect.y >600):
                self.rect.y = 540
                self.change_y=0
                self.rect.x+=30
    def looking(self):
        clock.tick(200)
        x = round(self.change_x)
        y = round(self.change_y)
        if(self.downpressed == True):
            self.image = flap
        elif(x>1):
            self.image =right
        elif(x<1):
            self.image =left
        else:
            self.image =standing
booliscool = True
def main():
    global booliscool
    player = Player(40,40)
    movingsprites = pygame.sprite.Group()
    booliscool = True
    rooms = []
 
    room = Room1()
    rooms.append(room)
 
    room = Room2()
    rooms.append(room)
 
    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)

    room = Room5()
    rooms.append(room)

    room = Room6()
    rooms.append(room)

    room = Room7()
    rooms.append(room)
    
    room = Room8()
    rooms.append(room)
    
    room = Room9()
    rooms.append(room)

    room = Room10()
    rooms.append(room)

    room = Room11()
    rooms.append(room)
    
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    done = False
 
    while not done:
        for event in pygame.event.get():
            pressed = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == ord('r'):
                    player.rect.x = current_room.startx
                    player.rect.y = current_room.starty
                    player.change_x =0
                    player.change_y =0
                if (event.key ==pygame.K_UP or event.key ==pygame.K_SPACE or event.key ==pygame.K_w) and player.jumpcount > 0:
                    player.movements(0, -5)
                    player.jumpcount -=1
                
                    
            if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                player.movements(-3,0)
            if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                player.movements(3, 0)
            if pressed[pygame.K_h] and pressed[pygame.K_p]:
                booliscool = False
                time.sleep(0.5)
                
                
            if (pressed[pygame.K_UP] or pressed[pygame.K_SPACE] or pressed[pygame.K_w]) and player.jumpcount == 0:
                player.downpressed = True
            else:
                player.downpressed = False
                
        if(booliscool == False):
            
            current_room_no += 1
            current_room = rooms[current_room_no]
            player.rect.x = current_room.startx
            player.rect.y = current_room.starty
            player.change_x =0
            player.change_y =0
            booliscool = True

        player.move(current_room.wall_list)
        player.mov(current_room.ju_list)
        player.moves(current_room.spike_list,current_room.startx,current_room.starty)
        screen.fill((225,225,225))
        current_room.ju_list.draw(screen)
        current_room.wall_list.draw(screen)
        current_room.spike_list.draw(screen)
        
        
        if player.rect.x > 850:
            player.rect.y -= 10
            player.rect.x += 100
            player.change_y =0 
            current_room_no += 1
            current_room = rooms[current_room_no]
            player.rect.x = 20
            
                
        if player.rect.x < 0 :
            player.rect.y -= 10
            player.change_y =0 
            current_room_no -= 1
            current_room = rooms[current_room_no]
            player.rect.x = 780
            
        if(current_room_no==0):
            addtext(textlist[0],textposlist[0])
            addtext(textlist[1],textposlist[1])
            addtext(textlist[2],textposlist[2])
            addtext(textlist[3],textposlist[3])
        elif(current_room_no==1):
            addtext(textlist[4],textposlist[4])
        elif(current_room_no==5):
            addtext(textlist[5],textposlist[5])
        elif(current_room_no==10):
            addtext(textlist[6],textposlist[6])
            addtext(textlist[7],textposlist[7])
            
        player.looking()
        screen.blit(player.image, (player.rect.x,player.rect.y))
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()
"""
make level
platofrms in level
spikes
enemy
make presentation
"""
