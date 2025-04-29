import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updateable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updateable, drawable)
	Asteroid.containers = (updateable, drawable)
	AsteroidField.containers = (updateable,)

	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()


	running = 1
	while running != 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0

		updateable.update(dt)
		screen.fill((0, 0, 0))
		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
