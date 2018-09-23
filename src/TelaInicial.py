import pygame

class TelaInicial():

	def __init__(self,tela):
		self.tela = tela

	def telaInicial(self):
		self.printTela()
		var = True
		while var:
			var = self.checarEventos()


	def printTela(self):
		self.tela.fill((0,0,0))
		font = pygame.font.SysFont("tahoma.TTF",60)
		font2 = pygame.font.SysFont("tahoma.TTF",40)
		font3 = pygame.font.SysFont("tahoma.TTF",30)
		ping = font.render("Ping for one",True,(255,255,255))
		enter = font2.render("enter = play",True,(255,255,255))
		esc = font2.render("esc = exit",True,(255,255,255))
		controls = font2.render("controls = arrow keys",True,(255,255,255))
		credits = font2.render("",True,(255,255,255))
		credits2 = font3.render("Bruno Dantas - 2013-2017",True,(255,255,255))
		rec = self.tela.get_rect()
		self.tela.blit(ping,(rec.centerx-ping.get_rect().width/2,rec.top+100))
		self.tela.blit(enter,(rec.centerx-enter.get_rect().width/2,rec.top+250))
		self.tela.blit(esc,(rec.centerx-esc.get_rect().width/2,rec.top+275))
		self.tela.blit(controls,(rec.centerx-controls.get_rect().width/2,rec.top+400))
		self.tela.blit(credits,(rec.centerx-credits.get_rect().width/2,rec.top+570))
		self.tela.blit(credits2,(rec.centerx-credits2.get_rect().width/2,rec.top+600))
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