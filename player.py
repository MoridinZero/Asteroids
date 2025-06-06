from circleshape import *
from constants import *
from main import *

class Player(CircleShape):

	def __init__(self, x, y, shot_group):
		self.x = x
		self.y = y
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.postion = pygame.Vector2(x, y)
		self.shot_group = shot_group
		self.shot_timer = 0

	# in the player class
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE ]:
			self.shoot()
		self.shot_timer -= dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def shoot(self):
		if self.shot_timer <= 0:
			from shot import Shot
			direction = pygame.Vector2(0, 1).rotate(self.rotation)
			velocity = direction * PLAYER_SHOOT_SPEED
			shot = Shot(self.position.x, self.position.y, velocity)
			self.shot_group.add(shot)
			self.shot_timer = PLAYER_SHOOT_COOLDOWN


