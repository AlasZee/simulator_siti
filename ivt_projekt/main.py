import pygame, sys
from settings import *
from base import Base

class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption("Network")
		self.clock = pygame.time.Clock()
		self.base = Base()

	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				
			self.screen.fill("black")
			self.base.run()
			pygame.display.update()
			self.clock.tick(FPS)


if __name__ == "__main__":
	game = Game()
	game.run()