import pygame
import random
import bird

def check_event(event,bd):
	if event.type==pygame.MOUSEBUTTONDOWN:
		bd.v+=-5
		
def state_update(bd,blk,screen):	
	for i in blk.sprites():
		if i.x < -400:
			blk.remove(i)
			bd.score+=1
	space=110-int(bd.score/10)
	space=max(75,space)
	if len(blk.sprites()) < 10:
		r=random.randint(106,306)
		blk.add(bird.blocker(1100,r-space,1))
		blk.add(bird.blocker(1100,r+space,-1))	
	bd.update()
	blk.update()	
	coll=pygame.sprite.spritecollide(bd,blk,0)	
	if len(coll) > 0 or bd.y >380 or bd.y < 0:
		return bd.score
	return -1

def screen_update(bd,blk,bg,ld,screen):
	bg.update()
	bg.blitme()	
	blk.draw(screen)	
	bd.blitme()
	font=pygame.font.Font("freesansbold.ttf", 48)
	score_str=font.render('Score:'+str(bd.score),True,(0,255,0),(255,255,255))
	score_str.set_colorkey((255,255,255))
	screen.blit(score_str,pygame.Rect(250,0,200,50))
	ld.update()
	ld.blitme()
