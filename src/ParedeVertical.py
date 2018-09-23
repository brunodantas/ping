from Parede import Parede

class ParedeVertical(Parede):

	def __init__(self,nomeImagem,x,y,w,h,white):
		super().__init__(nomeImagem,x,y,w,h,white)

	def colidirBola(self,bola):
		if self.centerx < bola.centerx:
			bola.left = self.right + 1
		else:
			bola.right = self.left - 1
		bola.velocidadeX = -bola.velocidadeX