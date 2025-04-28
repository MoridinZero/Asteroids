import pygame

from constants import *
from player import Player

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

	running = 1
	while running != 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0

	screen.fill((0, 0, 0))
	player.draw(screen) # draw the player
	pygame.display.flip()
	dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
