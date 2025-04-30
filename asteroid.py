from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random


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

	def split(self):
		random_angle = random.uniform(20, 50)
		self.kill()

		if self.radius <= ASTEROID_MIN_RADIUS:
			return

		new_vel_one = self.velocity.rotate(random_angle)
		new_vel_two = self.velocity.rotate(-random_angle)

		new_size = self.radius - ASTEROID_MIN_RADIUS

		kiddy_roid_one = Asteroid(self.position.x, self.position.y, new_size)
		kiddy_roid_two = Asteroid(self.position.x, self.position.y, new_size)

		kiddy_roid_one.velocity = new_vel_one * 1.2
		kiddy_roid_two.velocity = new_vel_two * 1.2
