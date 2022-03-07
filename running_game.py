import pygame
import os           #used to define or obtain paths to modles/images

WIDTH, HEIGHT = 900, 500                            #Going off YouTuber Tech with Tim, https://www.youtube.com/watch?v=jO6qQDNa2UY
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Running Game!")

COLOR_BACKGROUND = (209, 237, 242)                  #Light blue pop up window

runner_model_1 = pygame.image.load(os.path.join('Images', 'penguin.png'))   #After reviewing some character ideas, I thought a penguin model would be a good starting point.
runner_model_1 = pygame.transform.scale(runner_model_1, (100, 150))

runner_model_2 = pygame.image.load(os.path.join('Images', 'kanye.png'))     #kanye is a joke example, but the code adding a second entity will be like this. Perhaps the second entity could be a bad guy.
runner_model_2 = pygame.transform.scale(runner_model_2, (100, 150))         #this entity can also represent the obstacle which the character has to navigate through.


class Player:
        def __init__(self, name):
            self.name = name
            self.score = 0
        def reveal_all(self):
            print("Your name is ", self.name, " and your score is ", self.score)

def keep_drawing():
    WIN.fill(COLOR_BACKGROUND)
    WIN.blit(runner_model_1, (15,325))  #places a penguin bottom left 
    #WIN.blit(runner_model_2, (400, 200))           
    pygame.display.update()

def main():

    #playerName = input("Hey player! Please enter your name: ")     
    #user1 = Player(playerName)
    #user1.reveal_all()

    clock = pygame.time.Clock()
    run = True

    while run:                              #starting the game loop
        clock.tick(60)                      #Control speed of the while loop. It will run 60 times per second (60 frames per second)
        for event in pygame.event.get():    #checks event done by user
            if event.type == pygame.QUIT:   #if event is quit
                run = False                 #exits game loop

        WIN.fill(COLOR_BACKGROUND)
        keep_drawing()

    pygame.quit()                               #pygame will only quit if run is false

if __name__ == "__main__":                      #if mario.py is the executable, then execute main
    main()