import pygame
import random
from settings import *
from network_component import NetworkComponent
from text_input import TextInput

class Base():
	def __init__(self):
		self.screen = pygame.display.get_surface()
		self.active_components = []

		self.created_time = None
		self.created = False
		self.created_cooldown = 1000

		self.click_cooldown = 1000
		self.clicked = False
		self.clicked_time = None

		self.ip = [192, 168, 0, 1]
		self.ip_count = 0

		self.active_connection = []
		self.setup_count = 0

		self.wire = []

		self.txt = []

	"""
		self.writing_time = None
		self.write_trigger = False
		self.writing = False
		self.writing_cooldown = 1000


	def write(self, keys):
		if keys[pygame.K_t] and self.write_trigger == False:
			self.write_trigger = True
			self.writing = not self.writing
			self.writing_time = pygame.time.get_ticks()

		if self.writing:
			text = TextInput()
			new_text = text.write()
			print(new_text)
	"""

	# creating new instances of the NetworkComponent class
	def create(self, component):
		self.created = True
		self.created_time = pygame.time.get_ticks()
		mx, my = pygame.mouse.get_pos()
		self.ip_count = len(self.active_components)
		self.ip[3] = 1 + self.ip_count
		new = NetworkComponent(component, mx, my, self.active_components, self.ip)
		self.active_components.append(new)


	# regulates the amount of recieved clicks
	def cooldown(self):
		current_time = pygame.time.get_ticks()
		if self.clicked:
			if current_time - self.clicked_time >= self.click_cooldown:
				self.clicked = False

		if self.created:
			if current_time - self.created_time >= self.created_cooldown:
				self.created = False

	"""
		if self.writing:
			if current_time - self.writing_time >= self.writing_cooldown:
				self.write_trigger = False
	"""


	# gets the two instances of NetworkComponents that are supposed to be connected
	def connection_setup(self):
		if self.setup_count < 2:
			mouse = pygame.mouse.get_pressed()
			m_pos = pygame.mouse.get_pos()
			for comp in self.active_components:
				if mouse[0] and self.clicked == False and comp.rect.collidepoint(m_pos):			
					self.clicked = True
					self.clicked_time = pygame.time.get_ticks()
					self.active_connection.append(comp)
					self.setup_count += 1


	# tells each instance of NetworkComponents which other instance they are connected to
	def connect_components(self):
		self.active_connection[0].ip_connected[0] = self.active_connection[1].ip
		self.active_connection[1].ip_connected[0] = self.active_connection[0].ip
		self.txt.append(self.active_connection[0].info())
		self.txt.append(self.active_connection[1].info())
		self.wire = self.active_connection
		self.active_connection = []
		self.setup_count = 0


	# gives each instance of NetworkComponents a message they carry
	def message_generating(self):
		for comp in self.active_connection:
			generated_num = random.randint(1, 5)
			comp.message = random_messages[generated_num]


	# writes out information about an instance of NetworkComponents to screen
	def text_write(self, txt):
		pygame.font.init()
		textfont = pygame.font.SysFont("monospace", 15)
		i = 0
		for txt_list in txt:
			for item in txt_list:
				text = textfont.render(item, 1, (0,0,0))
				self.screen.blit(text, (750, 20 + 18*i))
				i += 1


	# clears text from screen
	def text_clear(self):
		self.txt = []


	# if there are components connected they exchange the messages they carry
	def message_sending(self):
		self.created = True
		self.created_time = pygame.time.get_ticks()
		for comp in self.active_components:
			for con_comp in self.active_components:
				if comp.ip == con_comp.ip_connected[0] and con_comp.ip == comp.ip_connected[0]:
					con_comp.recieved_message = comp.message
					self.txt.append(con_comp.info())


	# renders the created NetworkComponents
	def active_render(self):
		for comp in self.active_components:
			self.screen.blit(comp.icon, (comp.posx, comp.posy))

		if len(self.wire) == 2:
			pygame.draw.line(self.screen, (0,0,0), (self.wire[0].posx + (ICON_SIZE/2), self.wire[0].posy + (ICON_SIZE/2)), (self.wire[1].posx + (ICON_SIZE/2), self.wire[1].posy + (ICON_SIZE/2)))

		self.text_write(self.txt)


	# main loop
	def run(self):
		pygame.display.set_caption("Network")
		self.screen.fill((200, 200, 200))

		keys = pygame.key.get_pressed()

		if keys[pygame.K_r] and self.created == False:
			self.create(network_data["router"])
		if keys[pygame.K_p] and self.created == False:
			self.create(network_data["pc"])
		if keys[pygame.K_m] and self.created == False:
			self.message_sending()
		if keys[pygame.K_c]:
			self.text_clear()
		# self.write(keys)
		self.cooldown()
		self.active_render()
		self.connection_setup()
		if len(self.active_connection) == 2:
			self.message_generating()
			self.connect_components()


