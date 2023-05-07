import pygame, sys, time
from pygame.locals import *
from colors import Colors
from random import randrange

colors = Colors()


FPS        = 60
WINDOWSIZE = (750,550) # (width, height) 
REACTSIZE  = 25
MOVESPEED  = 5
ADD_TIME   = 2


pygame.init()
pygame.display.set_caption("PixelGame")
DISPLAY  = pygame.display.set_mode(WINDOWSIZE)
FPSCLOCK = pygame.time.Clock()
FONT     = pygame.font.Font('./assets/fonts/DarumadropOne.ttf', 32)

global Time; Time   = 10
global Point; Point = 0

class PixelGame:
   def __init__(self) -> None:
      #position
      self.playerPosition = (0, 0) # (x, y)
      self.fruitPosition  = (0, 0) # (x, y)

      #create player & fruit React
      self.player = Rect(self.playerPosition[0], self.playerPosition[1], REACTSIZE, REACTSIZE)
      self.fruit  = Rect(self.fruitPosition[0],  self.fruitPosition[1],  REACTSIZE, REACTSIZE)

      #timer config
      self.cache_millis = self.millis()

      #start game:
      self.createGame()


   def createGame(self):
      self.addPlayer()
      self.addFruit()

   def addPlayer(self):
      playerX = randrange(5, WINDOWSIZE[0]  / 2)
      playerY = randrange(5, WINDOWSIZE[1] / 2)
      self.playerPosition = (playerX, playerY)
   
   def addFruit(self):
      fruitX = randrange(5, WINDOWSIZE[0] - REACTSIZE)
      fruitY = randrange(5, WINDOWSIZE[1] - REACTSIZE)
      self.fruitPosition = (fruitX, fruitY)

   def movePlayer(self):
      def moveUp(moveValue):
         if self.playerPosition[1] - moveValue > 0:
            positionX, positionY = self.playerPosition[0], (self.playerPosition[1] - moveValue)
            self.playerPosition  = (positionX, positionY)

      def moveDown(moveValue):
         if self.playerPosition[1] + moveValue < (WINDOWSIZE[1] - REACTSIZE):
            positionX, positionY = self.playerPosition[0], (self.playerPosition[1] + moveValue)
            self.playerPosition  = (positionX, positionY)
      
      def moveRight(moveValue):
         if self.playerPosition[0] + moveValue  < (WINDOWSIZE[0] - REACTSIZE):
            positionX, positionY = (self.playerPosition[0] + moveValue), self.playerPosition[1]
            self.playerPosition  = (positionX, positionY)
      
      def moveLeft(moveValue):
         if self.playerPosition[0] - moveValue > 0:
            positionX, positionY = (self.playerPosition[0] - moveValue), self.playerPosition[1]
            self.playerPosition  = (positionX, positionY)

      #############################################
      #TODO: refatorar
      keyPressed = pygame.key.get_pressed() 
      
      if keyPressed[pygame.K_LEFT]:
         moveLeft(MOVESPEED)
      if keyPressed[pygame.K_RIGHT]:
         moveRight(MOVESPEED)
      if keyPressed[pygame.K_UP]:
         moveUp(MOVESPEED)
      if keyPressed[pygame.K_DOWN]:
         moveDown(MOVESPEED)

      self.checkForFruitCollision()


   def checkForFruitCollision(self):
      global Point, Time
      if pygame.Rect.colliderect(self.player, self.fruit):
         Point += 1
         Time  += 2
         self.addFruit()
         self.cache_millis = self.millis()


   def showPointAndTime(self):
      global Point,Time
      
      textRender = FONT.render(f'Point: {Point} | Time: {Time}',True, colors.WHITE)
      textRectObj = textRender.get_rect()
      textRectObj.center = ((WINDOWSIZE[0] / 2), 25) # set position 

      DISPLAY.blit(textRender, textRectObj)
   
   
   
   def gameOverMessage(self):
      textRender = FONT.render('Game Over', True, colors.WHITE)
      textRectObj = textRender.get_rect()
      textRectObj.center = ((WINDOWSIZE[0] / 2), (WINDOWSIZE[1] / 2)) # set position 

      DISPLAY.blit(textRender, textRectObj)


   def millis(self):
      return int(round(time.time() * 1000))

   def timer(self, time, decrement_value=1) -> int:
      if time - decrement_value >= 0:
         if (self.millis() - self.cache_millis) > 1000: # delay of 1 seconds
            time -= decrement_value
            self.cache_millis = self.millis()
      return time
      


   def render(self):
      # draw player on screen
      self.player.x = self.playerPosition[0]; self.player.y = self.playerPosition[1]
      pygame.draw.rect(DISPLAY, colors.GREEN, self.player)

      # draw fruit on screen
      self.fruit.x = self.fruitPosition[0]; self.fruit.y = self.fruitPosition[1]
      pygame.draw.rect(DISPLAY, colors.RED, self.fruit)


   def run(self):
      global Time
      while True:
         DISPLAY.fill(colors.BLACK) # set background color to black

         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()

         Time = self.timer(Time)
         if Time != 0:
            self.movePlayer()
            self.showPointAndTime()
            self.render()
         else:
            self.gameOverMessage()
         
         pygame.display.update()
         FPSCLOCK.tick(FPS)




game = PixelGame()
def main():
   game.run()


if __name__ == "__main__":
   main()
   