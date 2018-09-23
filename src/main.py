import pygame, sys, os
from Jogo import Jogo


def main():

	tela = inicializarTela()
	jogo = Jogo(tela)
	jogo.iniciar()


def inicializarTela():
	

	pygame.image.get_extended()
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.mixer.init()
	pygame.init()
	width,height = 960,640

	#centralizar tela
	fullscreen_sz = pygame.display.Info().current_w, pygame.display.Info().current_h
	win_pos_left = 1 + ((fullscreen_sz[0] - width) // 2)
	win_pos_top = 1 + ((fullscreen_sz[1] - height) // 2)
	os.environ['SDL_VIDEO_WINDOW_POS'] = '{0},{1}'.format(win_pos_left, win_pos_top)

	pygame.key.set_repeat(1,1)
	pygame.display.set_caption("Ping")
	tela = pygame.display.set_mode((width,height))
	#pygame.display.set_icon(pygame.image.load("mario.png"))
	return tela


main()
