import pygame
from game_methods import draw_footer
def main():
	pygame.init()
	screen = pygame.display.set_mode((576,710))
	pygame.display.set_caption('Flappy birds')
	bg_image = pygame.image.load('images/background-night.png')
	bg_image = pygame.transform.scale2x(bg_image)

	footer_image = pygame.image.load('images/base.png')
	footer_image = pygame.transform.scale2x(footer_image)


	# game variable
	footer_x_pos = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		screen.blit(bg_image,(0,-350))

		footer_x_pos -= 1
		draw_footer(screen,footer_image,footer_x_pos)
		if footer_x_pos <= -576:
			footer_x_pos = 0
		
		pygame.display.update()


if __name__ == "__main__":
	main()