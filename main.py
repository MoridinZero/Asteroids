import sys
import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

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
	shots = pygame.sprite.Group()


	Player.containers = (updateable, drawable)
	Shot.containers = (updateable, drawable)
	Asteroid.containers = (updateable, drawable)
	AsteroidField.containers = (updateable,)

	player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, shot_group=shots)
	asteroid_field = AsteroidField()


	running = 1
	while running != 0:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = 0

		updateable.update(dt)
		for sprite in updateable:
			if isinstance(sprite, Asteroid) and sprite not in asteroids:
				asteroids.add(sprite)

		screen.fill((0, 0, 0))

		for shot in shots:
			shot.draw(screen)

		for item in asteroids:
			if item.check_collision(player):
				print("Game Over!")
				pygame.quit()
				sys.exit(0)

		for roid in asteroids:
			for shot in shots:
				if roid.check_collision(shot):
					roid.split()
					shot.kill()

		for item in drawable:
			item.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
