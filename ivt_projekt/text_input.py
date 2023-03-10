import pygame
from settings import *

class TextInput():
	def __init__(self):
		self.screen = pygame.display.get_surface()
		self.clock = pygame.time.Clock()


	def write(self):
		text_input = pygame.Rect(100, 100, 200, 30)
		active = False
		text = ""
		font = pygame.font.Font(None, 20)
		running = True

		pygame.display.set_caption("Test")
		while running:
			self.screen.fill((200, 200, 200))
			pygame.draw.rect(self.screen, (0, 0, 0), text_input, 2)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if text_input.collidepoint(event.pos):
						active = True
					else:
						active = False
				if event.type == pygame.KEYDOWN:
					if active:
						if event.key == pygame.K_BACKSPACE:
							text = text[:-1]
						else:
							text += event.unicode
					else:
						if event.key == pygame.K_KP_ENTER:
							return text
							break
						if event.key == pygame.K_ESCAPE:
							running = False

			text_surface = font.render(text, True, (255, 0, 0))
			self.screen.blit(text_surface, (text_input.x + 5, text_input.y + 5))
			self.ip = text
			return text
			pygame.display.update()
			self.clock.tick(FPS)