from ElementoJogo import ElementoJogo
from abc import ABCMeta, abstractmethod

class Parede(ElementoJogo):
    #classe abstrata
    __metaclass__ = ABCMeta

    def __init__(self,nomeImagem,x,y,w,h,white):
    	super().__init__(nomeImagem,x,y,w,h,white)

    @abstractmethod
    def colidirBola(self, bola):
        raise NotImplementedError
