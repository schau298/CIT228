import pygame
from pygame.locals import *
import time
import random

size = 40
background_color = (0, 0, 0)
width=1000
height=800
class Rat:
    def __init__(self, parent_screen):
        self.block = pygame.image.load("term_project1/images/rat.png").convert()
        self.block = pygame.transform.scale(surface= self.block, size=(40, 40))
        self.parent_screen = parent_screen
        self.x = size * 3
        self.y = size * 3
    
    def draw(self):
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()
    
    def move(self):
        self.x = random.randint(1,24)*size
        self.y = random.randint(1,19)*size 

class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("term_project1/images/snakebody.png").convert()
        self.block = pygame.transform.scale(surface= self.block, size=(40, 40))
        self.x = [size]*length
        self.y = [size]*length
        self.direction = 'down'
    
    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'
    
    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'
    
    def move_down(self):
        self.direction = 'down'

    def slither(self):

        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size

        self.draw()
    
    def draw(self): 
        self.parent_screen.fill((background_color))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

class Game:

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((width,height))
        self.surface.fill((background_color))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.rat = Rat(self.surface)
        self.rat.draw()
    
    def collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True

        return False

    def play(self):
        self.snake.slither()
        self.rat.draw()
        self.show_score()
        pygame.display.flip()

    #Snake eating rat
        if self.collision(self.snake.x[0], self.snake.y[0], self.rat.x, self.rat.y):
            sound = pygame.mixer.Sound("term_project1/audio/bite.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.rat.move()
    
    #Snake Colliding with itself
        for i in range(3,self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                sound = pygame.mixer.Sound("term_project1/audio/collision.mp3")
                pygame.mixer.Sound.play(sound)
                raise "Game over"

        # Snake collides with border (Not functioning)
        #    if (self.snake.x[0], self.snake.x[0] >= width ):
        #       raise "Game over"
        #    if (self.snake.y[0],self.snake.y[0] >= height ):
        #       raise "Game over"   

    #SCORING
    def show_score(self):
        font = pygame.font.SysFont('Times New Roman', 35)
        score = font.render(f"Score: {self.snake.length}", True, (200, 200, 200))
        self.surface.blit(score, (800, 10))
 #Game over screen   
    def show_game_over(self):
        self.surface.fill(background_color)
        font = pygame.font.SysFont('Times New Roman', 25)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (252, 3, 23))
        self.surface.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter! To exit press escape!", True, (252, 3, 23))
        self.surface.blit(line2, (200, 350))
        pygame.display.flip()
#Reset the game
    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.rat = Rat(self.surface)
# Main Game Loop
    def run(self):
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
   
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right() 
            
                elif event.type == QUIT:
                    running = False
            
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()

            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()
    game.run()





