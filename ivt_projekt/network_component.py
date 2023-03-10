import pygame
from settings import * 

class NetworkComponent():
	def __init__(self, component, posx, posy, active_components, ip):
		self.screen = pygame.display.get_surface()
		self.active_components = active_components
		self.clock = pygame.time.Clock()

		full_path = component["graphic"]
		self.icon = pygame.image.load(full_path).convert_alpha()
		self.posx = posx
		self.posy = posy
		self.rect = pygame.Rect(self.posx, self.posy, self.icon.get_width(), self.icon.get_height())

		self.ip = []
		self.get_ip(ip)

		self.ip_connected = [None]

		self.message = ""
		self.recieved_message = ""


	# converts information about instance to list
	def info(self):		
		ip_txt = f"Ip is {self.ip}"
		pos_txt = f"Position is ({self.posx}, {self.posy})"
		msg_txt = f"The message I carry is '{self.message}'"
		rec_msg_txt = f"The message I recieved is '{self.recieved_message}'"
		conn_text = f"Connected ip is {self.ip_connected}"
		return [ip_txt, pos_txt, msg_txt, rec_msg_txt, conn_text]


	# translates ip adress at creation of each instance
	def get_ip(self, ip):
		self.ip.append(ip[0])
		self.ip.append(ip[1])
		self.ip.append(ip[2])
		self.ip.append(ip[3])

