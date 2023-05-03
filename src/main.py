import pygame, sys, time
from pygame.locals import *
from colors import Colors
from random import randrange
from datetime import datetime

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
      self.font = pygame.font.Font('./assets/fonts/montserrat.ttf',32)


      self.playerX = 0
      self.playerY = 0

      self.fruitX  = 0
      self.fruitY  = 0

      self.point   = 0
      self.seconds = self.__getSeconds()
      self.time    = 10

      self.createGame() # Add a player and fruit in a random place
   
   def createGame(self) -> None:
      self.__addPlayer()
      self.__addFruit()

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
         self.time    += 2
         self.point   += 1
         self.__addFruit()

   def __getSeconds(self) -> int:
      return int(datetime.now().strftime('%S'))

   def __timer(self,value) -> int: 
      timer = self.time
      if (self.__getSeconds() - self.seconds) > 1:
         if timer - value >= 0:
            timer -= value
            self.time = timer      
         self.seconds = self.__getSeconds()

      return timer
   
   def __printPoints(self):

      textRender = self.font.render(f'Point: {self.point} | Time: {self.time}',True, colors.ORANGE) # text | antialias | color

      textRender 
      textRectObj = textRender.get_rect()
      textRectObj.center = (WIDTH / 2,25) # set position 

      self.DISPLAYSURF.blit(textRender, textRectObj)

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
         
         time = self.__timer(1)
         #print(self.__timer(1) < 0)
         if time == 0:
            print('Game Over!')
            break

         self.__printPoints()

         pygame.display.update()
         self.__fpsClock.tick(FPS)


game = PixelGame('Pixel Game')

if __name__ == "__main__":
   game.run()