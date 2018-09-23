from ElementoJogo import ElementoJogo

class Bola(ElementoJogo):
	def __init__(self,x,y,velocidadeX,velocidadeY):
		super().__init__("src/g/ping_pong_8bit_ball.png",x,y,16,16,True)
		self.velocidadeX = velocidadeX #pixels/segundo
		self.velocidadeY = velocidadeY


	def mover(self,segundos):
		self.move_ip(int(self.velocidadeX*segundos),int(self.velocidadeY*segundos))