#create a Maze game!
from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (60, 60))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "izquierda"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "derecha"
        if self.rect.x >= win_width - 85:
            self.direction = "izquierda"

        if self.direction == "izquierda":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

            

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Laberinto")
background = transform.scale(image.load("Cancha.jpg"), (win_width, win_height))

packman = Player("Vinicius.png", 5, win_height - 80, 4)
monster = Enemy("Arbitro.png", win_width - 80, 280, 2)
final = GameSprite("Balon.png", win_width - 120, win_height - 80, 0)
w1 = Wall(145, 0, 45, 100, 20, 450, 10)
w2 = Wall(100, 50, 30, 100, 479, 380, 10)
w3 = Wall(50, 0, 15, 100, 20, 10, 380)
w4 = Wall(25, 0, 30, 225, 110, 10, 370)
w5 = Wall(25, 0, 30, 350, 20, 10, 370)
w6 = Wall(25, 0, 30, 475, 110, 10, 370)


game= True
finish = False
clock = time.Clock()
FPS = 60

font.init()
font = font.Font(None, 70)
win = font.render("Ganaste!", True, (255, 215, 0))
lose = font.render("Perdiste!", True, (180, 0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:    
        window.blit(background,(0, 0))
        packman.update()
        monster.update()
        
        monster.reset()
        final.reset()
        packman.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()

        if sprite.collide_rect(packman, monster) or sprite.collide_rect(packman, w1) or  sprite.collide_rect(packman, w2) or sprite.collide_rect(packman, w3) or sprite.collide_rect(packman, w4) or sprite.collide_rect(packman, w5) or sprite.collide_rect(packman, w6):
            finish = True
            window.blit(lose, (200, 200))
            #kick.play()

        if sprite.collide_rect(packman, final):
            finish = True
            window.blit(win, (200, 200))
            #money.play()

    display.update()
    clock.tick(FPS)