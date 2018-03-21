import pygame

class bird(pygame.sprite.Sprite):
	def __init__(self,screen):
		super().__init__()
		self.x=300
		self.y=180
		self.g=0.2
		self.v=0
		self.image=pygame.image.load('bird.png')
		self.rect=self.image.get_rect()	
		self.rect.inflate(-5,-5)
		self.rect.x=300
		self.rect.y=self.y
		self.screen=screen
		self.score=0
		
	def blitme(self):
		self.screen.blit(self.image,[self.x,self.y])
		
	def update(self):
		self.y+=self.v
		self.v+=self.g
		self.rect.y=self.y
		
class blocker(pygame.sprite.Sprite):
	def __init__(self,x,y,flag):
		super().__init__()
		self.flag=flag
		self.x=x
		self.y=y
		self.v=-5
		if flag ==1:
			self.image=pygame.image.load('pipe_down.png')
		else:
			self.image=pygame.image.load('pipe_up.png')
		self.rect=self.image.get_rect()
		self.rect.x=self.x
		if flag==1:
			self.rect.bottom=y
		else:
			self.rect.top=y
			
	def blitme(self):
		self.screen.blit(self.image,[self.x,self.y])
			
	def update(self):
		self.x+=self.v
		self.rect.x=self.x	
			
class background():
	def __init__(self,screen):
		self.screen=screen
		self.image=pygame.image.load('bg.png')
		self.rect=self.image.get_rect()
		self.x=0
	def blitme(self):
		for i in range(0,5):
			self.screen.blit(self.image,[self.x+i*288,0])
	def update(self):
		self.x+=-5
		if self.x < -290:
			self.x+=288

class land():
	def __init__(self,screen):
		self.screen=screen
		self.image=pygame.image.load('land.png')
		self.rect=self.image.get_rect()
		self.x=0
	def blitme(self):
		for i in range(0,5):
			self.screen.blit(self.image,[self.x+i*288,400])
	def update(self):
		self.x+=-5
		if self.x < -290:
			self.x+=288
			
	
