import pygame, sys, time
from pygame.locals import *
from colors import Colors
from random import randrange

FPS       = 60
WIDTH     = 750
HEIGHT    = 550
PIXELSIZE = 25 # width and height of pixel
FRUITSIZE = 25 # width and height of fruit]
MOVESPEED = 5

colors = Colors()

class PixelGame:
   def __init__(self, caption) -> None:
      pygame.init()
      pygame.display.set_caption(caption)
      self.DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
      self.__fpsClock = pygame.time.Clock()


      self.playerX = 0
      self.playerY = 0

      self.fruitX  = 0
      self.fruitY  = 0

      self.createGame() # Add a player and fruit in a random place
   
   def createGame(self) -> None:
      self.__addPlayer()
      #self.__addFruit()

   def __addPlayer(self) -> None:
      self.playerX = randrange(5, WIDTH  / 2)
      self.playerY = randrange(5, HEIGHT / 2)
      self.__player(x=self.playerX, y=self.playerY)

   def __player(self,x, y) -> None:
      self.player = Rect(x, y, PIXELSIZE, PIXELSIZE) 
      pygame.draw.rect(self.DISPLAYSURF, colors.GREEN, self.player)   

   
   def __addFruit(self) -> None:
      self.fruitX = randrange(5, WIDTH  - FRUITSIZE)
      self.fruitY = randrange(5, HEIGHT - FRUITSIZE)
      self.__player(x=self.fruitX, y=self.fruitY)

   def __fruit(self,x, y) -> None:
      self.fruit = Rect(x, y, PIXELSIZE, PIXELSIZE) 
      pygame.draw.rect(self.DISPLAYSURF, colors.RED, self.fruit)



   def __moveUp(self, moveValue):
      if self.playerY - moveValue > 0:
         self.playerY -= moveValue

   def __moveDown(self, moveValue):
      if self.playerY + moveValue < (HEIGHT - PIXELSIZE):
         self.playerY += moveValue
   
   def __moveRight(self, moveValues):
      if self.playerX + moveValues  < (WIDTH - PIXELSIZE):
         self.playerX += moveValues
   
   def __moveLeft(self, moveValues):
      if self.playerX - moveValues > 0:
         self.playerX -= moveValues


   def __movePlayer(self,event):
      keyPressed = pygame.key.get_pressed() # Listener keys of keyboard

      if keyPressed[pygame.K_LEFT]:
         self.__moveLeft(MOVESPEED)
      if keyPressed[pygame.K_RIGHT]:
         self.__moveRight(MOVESPEED)
      if keyPressed[pygame.K_UP]:
         self.__moveUp(MOVESPEED)
      if keyPressed[pygame.K_DOWN]:
         self.__moveDown(MOVESPEED)

   def __checkForFruitCollision(self):
      if pygame.Rect.colliderect(self.player, self.fruit):
         self.__addFruit()
   

   def run(self):
      while True:
         self.DISPLAYSURF.fill(colors.BLACK) # set background on window

         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()

         self.__movePlayer(event)

         self.__player(x=self.playerX, y=self.playerY)
         self.__fruit(x=self.fruitX, y=self.fruitY)

         self.__checkForFruitCollision()

         pygame.display.update()
         self.__fpsClock.tick(FPS)


game = PixelGame('Pixel Game')

if __name__ == "__main__":
   game.run()