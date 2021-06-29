import pygame
from game_methods import draw_footer, create_pipe, move_pipe, draw_pipe
def main():
	pygame.init()
	screen = pygame.display.set_mode((576,710))
	pygame.display.set_caption('Flappy birds')
	clock = pygame.time.Clock()
	scale = 0.25
	bird_movement = 0

	# Backgorund
	bg_image = pygame.image.load('images/background-night.png').convert()
	bg_image = pygame.transform.scale2x(bg_image)

	# Footer
	footer_image = pygame.image.load('images/base.png').convert()
	footer_image = pygame.transform.scale2x(footer_image)

	# Bird
	bird_image = pygame.image.load('images/bird.png').convert()
	bird_image = pygame.transform.scale2x(bird_image)
	bird_rect = bird_image.get_rect(center=(100,250))

	# Pipe - to`siq
	pipe_image = pygame.image.load('images/pipe.png')
	pipe_image = pygame.transform.scale2x(pipe_image)

	list_pipe = []
	PIPEMAKER = pygame.USEREVENT
	pygame.time.set_timer(PIPEMAKER,1200)



	# game variable
	footer_x_pos = 0
	pipe_height = [250,300,350,400,450]

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					bird_movement = 0
					bird_movement -= 5
			if event.type == PIPEMAKER:
				list_pipe.extend(create_pipe(pipe_image,pipe_height))
				#print(list_pipe)
		# backgorund
		screen.blit(bg_image,(0,-350))

		# Bird
		bird_movement += scale
		bird_rect.centery += bird_movement
		screen.blit(bird_image,bird_rect)


		# Pipe - to`siqlar
		list_pipe = move_pipe(list_pipe)
		draw_pipe(screen,pipe_image,list_pipe)


		#Footer
		footer_x_pos -= 1
		draw_footer(screen,footer_image,footer_x_pos)
		if footer_x_pos <= -576:
			footer_x_pos = 0
		
		pygame.display.update()
		clock.tick(90)


if __name__ == "__main__":
	main()