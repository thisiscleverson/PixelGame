import pygame, sys, time
from pygame.locals import *
from colors import Colors
from random import randrange

FPS       = 60
WIDTH     = 750
HEIGHT    = 550
PIXELSIZE = 5 # width and height of pixel
FRUITSIZE = 5 # width and height of fruit

colors = Colors()

class PixelGame:
   def __init__(self, caption) -> None:
      pygame.init()
      pygame.display.set_caption(caption)
      self.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
      self.__fpsClock = pygame.time.Clock()

      self.playerx = 0
      self.playery = 0
      self.fluitx  = 0
      self.fluity  = 0

      self.createGame() # Add a player in a random place
   
   #TODO: adicionar o "__addPlay" aqui. E adicionar a geração randômica da fruta aqui também!
   def createGame(self) -> None:
      self.__addPlayer()
      self.__addFruit()

   def __addPlayer(self) -> None:
      x_position = randrange(5, WIDTH  / 2)
      y_position = randrange(5, HEIGHT / 2)

      self.playerx = x_position
      self.playery = y_position

      print(f'({self.playerx},{self.playery})') # show initial position

      self.__player(x_position,y_position) # create 


   def __addFruit(self) -> None:
      x_position = randrange(5, WIDTH  - (PIXELSIZE ** 2))
      y_position = randrange(5, HEIGHT - (PIXELSIZE ** 2))

      self.fluitx = x_position
      self.fluity = y_position

      print(f'({self.fluitx},{self.fluity})') # show initial position

      self.__fluit(40,40) # create 

   def __player(self, x_position, y_position) -> None:
      pygame.draw.rect(self.DISPLAYSURF, colors.GREEN ,(x_position,y_position, 25, 25))   

   def __fluit(self, x_position, y_position) -> None:
      pygame.draw.rect(self.DISPLAYSURF, colors.RED ,(x_position,y_position, 25, 25))


   def __moveUp(self, move_y):
      if self.playery - move_y >= 0:
         self.playery -= move_y

   def __moveDown(self, move_y):
      if self.playery + move_y < (HEIGHT - PIXELSIZE **2):     
         self.playery += move_y

   def __moveRight(self, move_x):
      if self.playerx + move_x < (WIDTH - PIXELSIZE**2):
         self.playerx += move_x 

   def __moveLeft(self, move_x):
      if self.playerx - move_x >= 0:
         self.playerx -= move_x


   def __movePlayer(self, event):
      if event.type == pygame.KEYDOWN:
         #print(f'({self.playerx},{self.playery})')
         if event.key == pygame.K_LEFT:
            self.__moveLeft(5)
         if event.key == pygame.K_RIGHT:
            self.__moveRight(5)
         if event.key == pygame.K_UP:
            self.__moveUp(5)
         if event.key == pygame.K_DOWN:
            self.__moveDown(5)

   
   def __checkForFruitCollision(self):
      #print(f'P: ({self.playerx},{self.playery}) F:({self.fluitx},{self.fluity})')
      pass

   def run(self):
      while True:
         self.DISPLAYSURF.fill(colors.BLACK) # set background on window

         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()

            
         self.__movePlayer(event)
         self.__fluit(self.fluitx, self.fluity)
         self.__player(self.playerx, self.playery)
         self.__checkForFruitCollision()

         pygame.display.update()
         self.__fpsClock.tick(FPS)


game = PixelGame('Pixel Game')

if __name__ == "__main__":
   game.run()