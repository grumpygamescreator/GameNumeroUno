import pygame
import math, time


class Character:
	def __init__(self):
		pass

class Prop:
	def __init__(self):
		pass

class Statist:
	def __init__(self):
		pass

class Moose(Character):
	def __init__(self):
		pass


class Villager(Statist):
	def __init__(self):
		pass


class Dragon(Character):
	def __init__(self):
		pass


class Princess(Character):
	def __init__(self):
		pass


class Scene:
	def __init__(self):
		pass

class Vehicle:
	def __init__(self):
		pass



class Game:
	def __init__(self):
		pygame.init()
		self.width, self.height = 1000, 800
		self.surf = pygame.display.set_mode((self.width, self.height))
		pygame.display.set_caption("WIP")

		self.fps = 60
		self.clock = pygame.time.Clock()

	def update(self):
		pass

	def draw(self):
		self.surf.fill((0,0,0))
		pygame.display.update()

	def loop(self):
		while True:
			self.update()

			self.draw()

			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					pygame.quit()
					return

			self.clock.tick(self.fps)

if __name__ == "__main__":
	g = Game()
	g.loop()