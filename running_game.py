import pygame
import os  # used to define or obtain paths to modles/images

# Going off YouTuber Tech with Tim, https://www.youtube.com/watch?v=jO6qQDNa2UY
WIN_WIDTH, WIN_HEIGHT = 768, 768
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Running Game!")

COLOR_BACKGROUND = (209, 237, 242)  # Light blue pop up window

# After reviewing some character ideas, I thought a penguin model would be a good starting point.
runner_model_1 = pygame.image.load(os.path.join('Images', 'penguin.png'))
runner_model_1 = pygame.transform.scale(runner_model_1, (64, 64))

# kanye is a joke example, but the code adding a second entity will be like this. Perhaps the second entity could be a bad guy.
runner_model_2 = pygame.image.load(os.path.join('Images', 'kanye.png'))
# this entity can also represent the obstacle which the character has to navigate through.
runner_model_2 = pygame.transform.scale(runner_model_2, (100, 150))


class Player:
    def __init__(self, name, x, y, sprite, height, width):
        self.name = name
        self.x = x
        self.y = y
        self.sprite = sprite
        self.rect = pygame.Rect(x, y, width, height)

        self.score = 0

    def reveal_all(self):
        print("Your name is ", self.name, " and your score is ", self.score)


def keep_drawing(player):
    WIN.fill(COLOR_BACKGROUND)
    WIN.blit(player.sprite, (player.x, player.y))
    #WIN.blit(runner_model_2, (400, 200))
    pygame.display.update()


def main():

    player_width = 64
    player_height = 64

    player = Player("Penguin", 512, 512, runner_model_1, player_width, player_height)

    jump_up_counter = 0
    jump_down_counter = 0
    jumped = False

    #playerName = input("Hey player! Please enter your name: ")
    #user1 = Player(playerName)
    # user1.reveal_all()

    clock = pygame.time.Clock()
    run = True

    while run:  # starting the game loop
        # Control speed of the while loop. It will run 60 times per second (60 frames per second)
        clock.tick(60)
        for event in pygame.event.get():  # checks event done by user
            if event.type == pygame.QUIT:  # if event is quit
                run = False  # exits game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if jumped is False:

                        jump_up_counter = 0
                        jump_down_counter = 0
                        jumped = True

        pos = pygame.mouse.get_pos()

        pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()

        keys = pygame.key.get_pressed()

        # moving left to right logic
        if keys[pygame.K_a]:
            player.x -= 4
        elif keys[pygame.K_d]:
            player.x += 4

        WIN.fill(COLOR_BACKGROUND)
        keep_drawing(player)

        # jumping logic
        if jumped is True:
            if jump_up_counter <= 16:
                player.y -= 8
                jump_up_counter += 1
            else:
                if jump_down_counter <= 16:
                    player.y += 8
                    jump_down_counter += 1
                else:
                    jumped = False

    pygame.quit()  # pygame will only quit if run is false


if __name__ == "__main__":  # if mario.py is the executable, then execute main
    main()
