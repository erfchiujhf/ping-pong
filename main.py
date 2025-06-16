from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

height = 500
width = 600
window = display.set_mode((width, height))
back = (62, 235, 0)
window.fill(back)
display.set_caption('пинг-понг')
run = True
finish = False
fps = 60
speed_x = 3
speed_y = 3
clock = time.Clock()
racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 520, 200, 50, 150, 4)
ball = GameSprite('La-Vaca-Saturno-Saturnita-PNG.png', 200, 200, 50, 50, 4)
font.init()
font1 = font.SysFont('Arial', 100)
loser1 = font1.render('1 lose', True, (74, 23, 123))
loser2 = font1.render('2 lose', True, (56, 1, 30))
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > height - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(loser1, (200, 200))
        if ball.rect.x > width:
            finish = True
            window.blit(loser2, (200, 200))
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(fps)
