import pygame
from abc import ABCMeta, abstractmethod

class ElementoJogo(pygame.rect.Rect):
    #classe abstrata
    __metaclass__ = ABCMeta

    def __init__(self,nomeImagem,x,y,w,h,white):
    	# superficie = pygame.image.load(nomeImagem).convert_alpha()
    	self.superficie = pygame.Surface((w,h))
    	# self.superficie = pygame.transform.scale(superficie,(2*superficie.get_width(),2*superficie.get_height()))
    	if white:
    		c = (255,255,255)
    	else:
    		c = (0,0,0)
    	self.superficie.fill(c)
    	r = self.superficie.get_rect()
    	super().__init__(x+2,y+2,r.width-4,r.height-4)