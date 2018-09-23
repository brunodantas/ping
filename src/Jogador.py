from ParedeVertical import ParedeVertical
from Bola import Bola
import random
import math

class Jogador(ParedeVertical):
	def __init__(self,x,y):
		super().__init__("src/g/ping_pong_8bit_player_glowy.png",x,y,20,640/4,True)
		self.velocidade = 500 #pixels/segundo


	def mover(self,cima,segundos):
		vel = self.velocidade
		if cima:
			vel = -vel
		self.move_ip(0,int(vel*segundos))

	def colidirBola(self,bola):
		super().colidirBola(bola)
		# bola.velocidadeX += 10
		# diferencaY = self.centery - bola.centery
		# if diferencaY < self.height/3:
		# 	if bola.velocidadeY >= 0:
		# 		bola.velocidadeY = -bola.velocidadeY - random.randint(0,10) 
		# 	else:
		# 		bola.velocidadeY -= random.randint(0,10)
		# elif diferencaY > 2*self.height/3:
		# 	if bola.velocidadeY <= 0:
		# 		bola.velocidadeY = -bola.velocidadeY + random.randint(0,10)
		# 	else:
		# 		bola.velocidadeY += random.randint(0,10)

		# bola.velocidadeY -= diferencaY*5 + 10*random.randint(-1,1)

		# if abs(bola.velocidadeY) < 70:
		# 	if bola.velocidadeY==0:
		# 		bola.velocidadeY += 40
		# 	bola.velocidadeY *= 20*(bola.velocidadeY/abs(bola.velocidadeY))
		# 	if abs(bola.velocidadeY) < 70:
		# 		bola.velocidadeY += 20*(bola.velocidadeY/abs(bola.velocidadeY))

		# veloc = bola.velocidadeX + random.randint(-30,10)
		# veloc2 = -bola.velocidadeY + random.randint(-30,30)
		# novaBola = Bola(bola.left+1,bola.top+1,veloc,veloc2)

		bola.left = self.right
		bola.velocidadeX += 30
		v = bola.velocidadeX + bola.velocidadeY
		bola.velocidadeY += bola.centery - self.centery
		if abs(bola.velocidadeY) < 30:
			if bola.velocidadeY < 0:
				bola.velocidadeY += -30
			else:
				bola.velocidadeY += 30
		# if diferencaY < self.height/3:
		# 	if bola.velocidadeY >= 0:
		# 		bola.velocidadeY = -bola.velocidadeY - random.randint(0,10) 
		# 	else:
		# 		bola.velocidadeY -= random.randint(0,10)
		# elif diferencaY > 2*self.height/3:
		# 	if bola.velocidadeY <= 0:
		# 		bola.velocidadeY = -bola.velocidadeY + random.randint(0,10)
		# 	else:
		# 		bola.velocidadeY += random.randint(0,10)

		# bola.velocidadeY -= diferencaY*5 + 10*random.randint(-1,1)

		# if abs(bola.velocidadeY) < 70:
		# 	if bola.velocidadeY==0:
		# 		bola.velocidadeY += 40
		# 	bola.velocidadeY *= 20*(bola.velocidadeY/abs(bola.velocidadeY))
		# 	if abs(bola.velocidadeY) < 70:
		# 		bola.velocidadeY += 20*(bola.velocidadeY/abs(bola.velocidadeY))

		veloc = abs(bola.velocidadeY)
		if veloc < 40:
			veloc += 40
		r = random.randint(0,1)
		if r:
			veloc2 = bola.velocidadeX
		else:
			veloc2 = -bola.velocidadeX
		novaBola = Bola(bola.left,bola.top,veloc,veloc2)
		return novaBola