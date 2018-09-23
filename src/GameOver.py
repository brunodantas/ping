import pygame

class GameOver():

	def __init__(self,tela,score):
		self.tela = tela
		self.score = score

	def gameOver(self):
		self.printTela()
		var = True
		while var:
			var = self.checarEventos()


	def printTela(self):
		self.tela.fill((0,0,0))
		font = pygame.font.SysFont("tahoma.TTF",60)
		font2 = pygame.font.SysFont("tahoma.TTF",40)
		gameover = font.render("Game Over",True,(255,255,255))
		score = font.render("score: "+str(self.score),True,(255,255,255))
		enter = font2.render("enter = play again",True,(255,255,255))
		esc = font2.render("esc = exit",True,(255,255,255))
		rec = self.tela.get_rect()
		self.tela.blit(gameover,(rec.centerx-gameover.get_rect().width/2,rec.top+200))
		self.tela.blit(score,(rec.centerx-score.get_rect().width/2,rec.top+250))
		self.tela.blit(enter,(rec.centerx-enter.get_rect().width/2,rec.top+400))
		self.tela.blit(esc,(rec.centerx-esc.get_rect().width/2,rec.top+425))
		pygame.display.flip()


	def checarEventos(self):
		for x in pygame.event.get():
			if x.type == pygame.QUIT:
				pygame.quit()

			elif x.type == pygame.KEYDOWN:
				if x.key == pygame.K_ESCAPE:
					pygame.quit()
				elif x.key == pygame.K_RETURN:
					return False
		return True