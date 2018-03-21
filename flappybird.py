

import pygame
import bird
import gamefunctions as gf

pygame.init()



screen = pygame.display.set_mode((800,512))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
done = False	

title=pygame.image.load('title.png')
title_rect=title.get_rect()
title_rect.center=(400,200)

font=pygame.font.Font("freesansbold.ttf", 48)
button_rect=pygame.Rect(250,245,200,50)
score_rect=pygame.Rect(250,170,200,50)
play=font.render('      PLAY',True,(0,255,0),(255,255,255))
play.set_colorkey((255,255,255))
restart=font.render('RESTART',True,(0,255,0),(255,255,255))
restart.set_colorkey((255,255,255))
bg=bird.background(screen)
ld=bird.land(screen)

def run_game(bg,ld):
	done=False
	bd=bird.bird(screen)
	blk=pygame.sprite.Group()

	for i in range(0,5):
		blk.add(bird.blocker(800+300*i,150,1))
		blk.add(bird.blocker(800+300*i,300,-1))
	
	while not done:

		event=pygame.event.poll()
		if event.type == pygame.QUIT:
			done = True
				
		gf.check_event(event,bd)
		score=gf.state_update(bd,blk,screen)
		gf.screen_update(bd,blk,bg,ld,screen)	
		pygame.display.flip()
		clock.tick(60)
#		print(clock.get_fps())
		if score > 0:
			return score

score=-1
while not done:
	event=pygame.event.poll()
	if event.type == pygame.QUIT:
		done = True
	bg.blitme()
	ld.blitme()	
		
	if score == -1:
		screen.blit(title,title_rect)
		screen.blit(play,button_rect)
	else:
		score_str=font.render('Score:'+str(score),True,(0,0,0),(255,255,255))
		score_str.set_colorkey((255,255,255))
		screen.blit(score_str,score_rect)
		screen.blit(restart,button_rect)
#	pygame.draw.rect(screen,(0,255,0),button_rect,1)
	pygame.display.flip()
	clock.tick(60)
	if event.type == pygame.MOUSEBUTTONDOWN:
		pos=pygame.mouse.get_pos()
		if button_rect.collidepoint(pos):
			score=run_game(bg,ld)

	
# Close the window and quit.
pygame.quit()

