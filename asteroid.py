from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
	containers = None


	def __init__(self, x, y, radius):
		if not Asteroid.containers:
			raise ValueError("Asteroid.containers must be set before creating an Asteroid")

		pygame.sprite.Sprite.__init__(self, *Asteroid.containers)
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
