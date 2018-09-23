from Parede import Parede

class ParedeHorizontal(Parede):

	def __init__(self,nomeImagem,x,y):
		super().__init__(nomeImagem,x,y,960,10,False)

	def colidirBola(self,bola):
		if self.centery < bola.centery:
			bola.top = self.bottom + 1
		else:
			bola.bottom = self.top - 1
		bola.velocidadeY = -bola.velocidadeY