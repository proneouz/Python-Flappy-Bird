import pygame, random
def draw_footer(screen,footer_image,footer_x_pos):
	screen.blit(footer_image,(footer_x_pos,580))
	screen.blit(footer_image,(footer_x_pos + 576,580))
def create_pipe(pipe_image,pipe_height):
	rand_pipe_y = random.choice(pipe_height)
	bottom_pipe = pipe_image.get_rect(midtop=(650,rand_pipe_y))
	top_pipe = pipe_image.get_rect(midbottom=(650,rand_pipe_y-180))
	return bottom_pipe,top_pipe
def move_pipe(pipes):
	for pipe in pipes:
		pipe.centerx -= 5
	return  pipes
def draw_pipe(screen,pipe_image,pipes):
	for pipe in pipes:
		if pipe.centery >= 100:
			screen.blit(pipe_image,pipe)
		else:
			flip_pipe = pygame.transform.flip(pipe_image,False,True)
			screen.blit(flip_pipe,pipe)