import pygame
import time
from Bola import Bola
from Jogador import Jogador
from ParedeHorizontal import ParedeHorizontal
from ParedeVertical import ParedeVertical
from TelaInicial import TelaInicial
from GameOver import GameOver
import threading
import random
from queue import Queue


class Jogo():

	def __init__(self,tela):
		self.jogador = Jogador(0,640/3)
		bola = Bola(3*960/4,640/2,-420,30*random.randint(-10,10))
		self.parede1 = ParedeHorizontal("src/g/ping_pong_wall.png",0,0)
		self.parede2 = ParedeHorizontal("src/g/ping_pong_wall2.png",0,640-10)
		self.parede3 = ParedeVertical("src/g/ping_pong_fundo.png",960-10,0,10,640,False)
		self.r,self.g,self.b = 0,0,0
		self.tela = tela
		self.bolas = [bola]
		self.inicializarSons()
		tempo = current_milli_time = lambda: int(round(time.time() * 1000))
		random.seed(tempo)
		# pygame.mixer.init()
		self.scoreFont = pygame.font.SysFont("tahoma.TTF",60)
		self.score = 0

		self.up = pygame.rect.Rect(0,-200,960,200)
		self.down = pygame.rect.Rect(0,640,960,200)
		self.right = pygame.rect.Rect(960,0,200,640)

		self.obstaculos = [self.parede1,self.parede2,self.parede3,self.jogador,self.up,self.down,self.right]
		self.q = Queue()
		self.st = threading.Thread(target=self.tocar_som, daemon=True)
		self.st.start()

	def iniciar(self):
		TelaInicial(self.tela).telaInicial()
		while True:
			self.jogo()
			GameOver(self.tela,self.score).gameOver()
			self.__init__(self.tela)

	def jogo(self):
		self.segundos = 0
		clock = pygame.time.Clock()
		var = True
		while(var):
			self.segundos = clock.tick(60)/1000.0
			
			var = self.checarEventos()
			self.atualizarBola()
			self.atualizarTela()
			if not self.bolas:
				var = False

	def checarEventos(self):
		for x in pygame.event.get():
			if x.type == pygame.QUIT:
				return pygame.quit()
			elif x.type == pygame.KEYDOWN:
				if x.key == pygame.K_DOWN:
					if not (self.jogador.colliderect(self.parede2)):
						self.jogador.mover(False,self.segundos)
				elif x.key == pygame.K_UP:
					if not (self.jogador.colliderect(self.parede1)):
						self.jogador.mover(True,self.segundos)
		return True

	def atualizarBola(self):
		for bola in self.bolas:
			bola.mover(self.segundos)
			if bola.left < -90 or bola.left>960:
				self.bolas.remove(bola)
				# if random.randint(0,2)==0:
				# 	self.som3.play()
				continue
			indice = bola.collidelist(self.obstaculos)
			if indice != -1:
				self.atualizarCor()
				if self.obstaculos[indice]==self.jogador:
					self.q.put(bola.centery - self.jogador.centery)
					self.score += 1
					b = self.jogador.colidirBola(bola)
					self.bolas.append(b)

				elif self.obstaculos[indice]==self.up:
					bola.top = 40
				elif self.obstaculos[indice]==self.down:
					bola.top = 600
				elif self.obstaculos[indice]==self.right:
					bola.right = 950
				else:
					# self.som2.play()
					self.obstaculos[indice].colidirBola(bola)


	def atualizarTela(self):
		self.tela.fill((self.r,self.g,self.b))
		self.tela.blit(self.jogador.superficie,self.jogador)
		self.tela.blit(self.parede1.superficie,self.parede1)
		self.tela.blit(self.parede2.superficie,self.parede2)
		self.tela.blit(self.parede3.superficie,self.parede3)
		score = self.scoreFont.render(str(self.score),True,(255,255,255))
		rec = self.tela.get_rect()
		self.tela.blit(score,(rec.centerx-score.get_rect().width/2,rec.top+50))
		for bola in self.bolas:
			self.tela.blit(bola.superficie,bola)
		pygame.display.flip()

	def inicializarSons(self):
		self.sons = []
		self.som2 = pygame.mixer.Sound("src/s/ping_pong_8bit_plop.ogg")
		self.som3 = pygame.mixer.Sound("src/s/ping_pong_8bit_peeeeeep.ogg")
		# i=1
		# while(i<=14):
		# 	self.sons.append(pygame.mixer.Sound("src/s/ping_pong_8bit_beeep"+str(i)+".ogg"))
		# 	i+=1
		import os
		s = [os.fsdecode("src/s/piano/"+x) for x in sorted(os.listdir("src/s/piano"))]
		s = s[24:48]
		self.sons = [pygame.mixer.Sound(x) for x in s if x.endswith(".wav")]			

	def atualizarCor(self):
		acrescimo = 1#random.randint(5,25)
		n = random.randint(1,3)
		i = random.randint(0,1)
		if i == 0:
			if n==1:
				self.r = (self.r + acrescimo)%255
			elif n==2:
				self.g = (self.g + acrescimo)%255
			else:
				self.b = (self.b + acrescimo)%255
		elif i==1:
			if n==1:
				if self.r>acrescimo:
					self.r -= acrescimo
			elif n==2:
				if self.g>acrescimo:
					self.g -= acrescimo
			else:
				if self.b>acrescimo:
					self.b -= acrescimo
		# elif i==2:
		# 	if random.randint(0,512)==23:
		# 		self.r = 255 - self.r
		# 		self.g = 255 - self.g
		# 		self.b = 255 - self.b

	def tocar_som(self):
		nch = pygame.mixer.get_num_channels()
		channels = [pygame.mixer.Channel(x) for x in range(0,nch)]
		h = self.jogador.height
		i = 0
		while True:
			a = self.q.get() + self.jogador.height/2
			s = int(((a / h) * len(self.sons)))
			if s < 0:
				s = 0
			elif s >= len(self.sons):
				s = len(self.sons) - 1
			print(s)
			c = channels[i]
			c.stop()
			# c.play(self.sons[random.randint(0,len(self.sons)-1)])
			c.play(self.sons[s])
			i = (i+1)%nch