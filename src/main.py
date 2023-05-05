import pygame, sys, time
from pygame.locals import *
from colors import Colors
from random import randrange

colors = Colors()


FPS        = 60
WINDOWSIZE = (750,550) # (width, height) 
REACTSIZE  = 25
MOVESPEED  = 5

pygame.init()
pygame.display.set_caption("PixelGame")
DISPLAY  = pygame.display.set_mode(WINDOWSIZE)
FPSCLOCK = pygame.time.Clock()



class PixelGame:
   def __init__(self) -> None:
      #position
      self.playerPosition = (0, 0) # (x, y)
      self.fruitPosition  = (0, 0)

      #create player & fruit React
      self.player = Rect(self.playerPosition[0], self.playerPosition[1], REACTSIZE, REACTSIZE)
      self.fruit  = Rect(self.fruitPosition[0],  self.fruitPosition[1], REACTSIZE, REACTSIZE)

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
      if pygame.Rect.colliderect(self.player, self.fruit):
         self.addFruit()


   def render(self):
      # draw player on screen
      self.player.x = self.playerPosition[0]; self.player.y = self.playerPosition[1]
      pygame.draw.rect(DISPLAY, colors.GREEN, self.player)

      # draw fruit on screen
      self.fruit.x = self.fruitPosition[0]; self.fruit.y = self.fruitPosition[1]
      pygame.draw.rect(DISPLAY, colors.RED, self.fruit)


   def run(self):
      while True:
         DISPLAY.fill(colors.BLACK) # set background color to black

         for event in pygame.event.get():
            if event.type == QUIT:
               pygame.quit()
               sys.exit()


         #TODO: refatorar
         self.movePlayer()
         self.render()

         pygame.display.update()
         FPSCLOCK.tick(FPS)




game = PixelGame()
def main():
   game.run()


if __name__ == "__main__":
   main()