import pygame
def draw_footer(screen,footer_image,footer_x_pos):
	screen.blit(footer_image,(footer_x_pos,580))
	screen.blit(footer_image,(footer_x_pos + 576,580))