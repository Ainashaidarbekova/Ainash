import pygame 

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.mixer.music.load("back.mp3")
im4=pygame.image.load("dead.png")
d1 = 1200
d2 = 1200
pygame.mixer.music.play(-1) 

ss = pygame.mixer.Sound("sss.wav")

class snaryad():
	def __init__(self, x, y, facing):
		self.x = x
		self.y = y
		self.facing = facing

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 5)



class tank():
	def __init__(self, x, y, facing, img, t1x):
		self.x = x
		self.y = y
		self.facing = facing
		self.t1x = t1x
		self.img = img
		self.orig = img
		self.font = pygame.font.Font(None,30)
		self.text = self.font.render(str("Жизни: "), True, (255,0,0))
		self.score = 3

	
	def draw(self):
		screen.blit(self.img, (self.x, self.y))
		text2 = self.font.render(str(self.score), True, (255,0,0))
		screen.blit(self.text, (self.t1x, 20))
		screen.blit(text2, (self.t1x + 100, 20))

	def transform(self, facing, angel): #одна картинка на 360
		self.img = pygame.transform.rotate(self.orig, angel)
		self.facing = facing

	def move(self):
		if self.facing == "right": 	self.x += 5 
		if self.facing == "left":	self.x -= 5
		if self.facing == "up":		self.y -= 5
		if self.facing == "down":	self.y += 5
		if self.x == -120: 			self.x = 1100
		elif self.x == 1120: 		self.x = -100 
		elif self.y == 920: 		self.y = -100
		elif self.y == -120: 		self.y = 900


def collision(bullets, t2):
	for bullet in bullets:
		if bullet.x >= t2.x and bullet.x <= t2.x + 125 and bullet.y >= t2.y and bullet.y <= t2.y + 57 and t2.facing == "right" :
			t2.score -= 1
			bullets.pop(bullets.index(bullet))	
		if bullet.x >= t2.x and bullet.x <= t2.x + 125 and bullet.y >= t2.y and bullet.y <= t2.y + 57 and t2.facing == "left" :
			t2.score -= 1
			bullets.pop(bullets.index(bullet))
		if bullet.x >= t2.x and bullet.x <= t2.x + 57 and bullet.y >= t2.y and bullet.y <= t2.y + 120 and t2.facing == "up" :
			t2.score -= 1
			bullets.pop(bullets.index(bullet))
		if bullet.x >= t2.x and bullet.x <= t2.x + 57 and bullet.y >= t2.y and bullet.y <= t2.y + 120 and t2.facing == "down" :
			t2.score -= 1
			bullets.pop(bullets.index(bullet))


def bull_move(self):
	for bullet in self : #пуля летит в направлении танка
		if bullet.x <= 1000 and bullet.x>= 0 and bullet.y >=0 and bullet.y<=800:
			if bullet.facing == "right":	
				bullet.x += 10 
			if bullet.facing == "left":		
				bullet.x -= 10
			if bullet.facing == "up":		
				bullet.y -= 10
			if bullet.facing == "down":		
				bullet.y += 10
		else: #пуля уничтожается
			self.pop(self.index(bullet))

def bull_add(self, instance, x, y):
	bull_x = self.x + x # координаты пули красиво вылетают 
	bull_y = self.y + y
	if len(instance) < 5:  #колличество пуль меньше пяти 
		instance.append(snaryad(bull_x, bull_y, self.facing))




done = False
t1_img = pygame.image.load("tank1.png").convert_alpha()
t2_img = pygame.image.load("tank2.png").convert_alpha()
bullets = []
bullets2 = []
FPS = 60
clock = pygame.time.Clock()


t1 = tank(800,600,'up', pygame.image.load("tank1.png"), 850)
t2 = tank(100,100,'up', pygame.image.load("tank2.png"), 0)

while not done:
	
	mill = clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RETURN and t1.facing == "up":
				bull_add(t1, bullets, 27, -5)
				pygame.mixer.Sound.play(ss)
			if event.key == pygame.K_RETURN and t1.facing == "right":
				bull_add(t1, bullets, 120, 27)
				pygame.mixer.Sound.play(ss)
			if event.key == pygame.K_RETURN and t1.facing == "down" :
				bull_add(t1, bullets, 27, 120)
				pygame.mixer.Sound.play(ss)
			if event.key == pygame.K_RETURN and t1.facing == "left" :
				bull_add(t1, bullets, -5, 27)
				pygame.mixer.Sound.play(ss)
			if event.key == pygame.K_SPACE and t2.facing == "up":
				bull_add(t2, bullets2, 27, -5)
				pygame.mixer.Sound.play(ss)
			if event.key == pygame.K_SPACE and t2.facing == "right":
				bull_add(t2, bullets2, 120, 27)
				pygame.mixer.Sound.play(ss)
			if event.key == pygame.K_SPACE and t2.facing == "down" :
				bull_add(t2, bullets2, 27, 120)
				pygame.mixer.Sound.play(ss)
			if event.key == pygame.K_SPACE and t2.facing == "left" :
				bull_add(t2, bullets2, -5, 27)
				pygame.mixer.Sound.play(ss)

	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_ESCAPE:
			done = True
		elif event.key == pygame.K_RIGHT:
			t1.transform("right", -90) 
		elif event.key == pygame.K_LEFT:
			t1.transform("left", 90)
		elif event.key == pygame.K_UP:
			t1.transform("up", 0)
		elif event.key == pygame.K_DOWN:
			t1.transform("down", 180)
		elif event.key == pygame.K_a:
			t2.transform("left", 90)
		elif event.key == pygame.K_d:
			t2.transform("right", -90)
		elif event.key == pygame.K_w:
			t2.transform("up", 0)
		elif event.key == pygame.K_s:
			t2.transform("down", 180)

	bull_move(bullets)
	bull_move(bullets2)
	t1.move()
	t2.move()
	
	screen.fill((0, 0, 0))
	t1.draw()
	t2.draw()
	collision(bullets, t2)
	collision(bullets2, t1)
	for bullet in bullets: # класс.рисовать
		bullet.draw(screen)
	for bullet in bullets2:
		bullet.draw(screen)
	screen.blit(im4, (d1, d2)) #бэкграунд
	if t2.score <= 0:
		d1 = -100
		d2 = -100
		screen.blit(im4, (d1, d2))
	if t1.score <= 0:
		d1 = -100
		d2 = -100
		screen.blit(im4, (d1, d2))
	pygame.display.update()
	pygame.display.flip()