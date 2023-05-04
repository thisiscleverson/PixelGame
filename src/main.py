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
      self.__fpsClock  = pygame.time.Clock()
      self.font        = pygame.font.Font('./assets/fonts/montserrat.ttf',32)

      self.playerX = 0
      self.playerY = 0

      self.fruitX  = 0
      self.fruitY  = 0

      #TODO: refatorar as variaveis de point, _milles, time
      self.point   = 0
      self._milles = self.milles()
      self.time    = 30

      self.createGame() # Add a player and fruit in a random place
   
   def createGame(self) -> None:
      self.addPlayer()
      self.addFruit()


   def addPlayer(self) -> None:
      self.playerX = randrange(5, WIDTH  / 2)
      self.playerY = randrange(5, HEIGHT / 2)
      self.player(x=self.playerX, y=self.playerY)

   def player(self,x, y) -> None:
      self._player = Rect(x, y, PIXELSIZE, PIXELSIZE) 
      pygame.draw.rect(self.DISPLAYSURF, colors.GREEN, self._player)   
   
   def addFruit(self) -> None:
      self.fruitX = randrange(5, WIDTH  - FRUITSIZE)
      self.fruitY = randrange(5, HEIGHT - FRUITSIZE)
      self.fruit(x=self.fruitX, y=self.fruitY)

   def fruit(self,x, y) -> None: # TODO: refatorar
      self._fruit = Rect(x, y, PIXELSIZE, PIXELSIZE) 
      pygame.draw.rect(self.DISPLAYSURF, colors.RED, self._fruit)


   def moveUp(self, moveValue):
      if self.playerY - moveValue > 0:
         self.playerY -= moveValue

   def moveDown(self, moveValue):
      if self.playerY + moveValue < (HEIGHT - PIXELSIZE):
         self.playerY += moveValue
   
   def moveRight(self, moveValues):
      if self.playerX + moveValues  < (WIDTH - PIXELSIZE):
         self.playerX += moveValues
   
   def moveLeft(self, moveValues):
      if self.playerX - moveValues > 0:
         self.playerX -= moveValues

   def movePlayer(self):
      keyPressed = pygame.key.get_pressed() # Listener keys of keyboard

      if keyPressed[pygame.K_LEFT]:
         self.moveLeft(MOVESPEED)
      if keyPressed[pygame.K_RIGHT]:
         self.moveRight(MOVESPEED)
      if keyPressed[pygame.K_UP]:
         self.moveUp(MOVESPEED)
      if keyPressed[pygame.K_DOWN]:
         self.moveDown(MOVESPEED)


   def checkForFruitCollision(self):
      if pygame.Rect.colliderect(self._player, self._fruit):
         self.time    += 2
         self.point   += 1
         self.addFruit()


   def milles(self) -> int:
      return int(round(time.time() * 1000))

   #TODO: refatorar o timer
   def timer(self,value) -> int: 
      time = self.time
      if (self.milles() - self._milles) > 1000: 
         if time - value >= 0:
            time -= value
            self.time = time     
         self._milles = self.milles()

      return time
   
   
   def showPointAndTime(self):
      textRender = self.font.render(f'Point: {self.point} | Time: {self.time}',True, colors.ORANGE) # text | antialias | color

      textRectObj = textRender.get_rect()
      textRectObj.center = ((WIDTH / 2), 25) # set position 

      self.DISPLAYSURF.blit(textRender, textRectObj)


   def showGameOver(self):
      self.DISPLAYSURF.fill(colors.BLACK)
      textRender = self.font.render("Gamer Over!",True, colors.RED) # text | antialias | color

      textRectObj = textRender.get_rect()
      textRectObj.center = ((WIDTH / 2), HEIGHT / 2) # set position 

      self.DISPLAYSURF.blit(textRender, textRectObj)


   def run(self):
      while True:
         self.DISPLAYSURF.fill(colors.BLACK) # set background on window

         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()

         self.movePlayer()

         self.player( x=self.playerX,  y=self.playerY)
         self.fruit(  x=self.fruitX,   y=self.fruitY)

         self.checkForFruitCollision()
         

         if self.timer(1) == 0:
            self.showGameOver()
         else: 
            self.showPointAndTime()

         pygame.display.update()
         self.__fpsClock.tick(FPS)


game = PixelGame('Pixel Game')

if __name__ == "__main__":
   game.run()