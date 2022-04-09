# PlatForm_Running_Game
Final project for CIS-4930. This final project is a platform game in which the core objective is to move the player character between points in a rendered environment.

First report / commit:
  Added foundation code for the GUI. A pop up with a fixed size exists when the program is ran, along with some basic components like a light blue background and
checking for events, including exiting the GUI.  In addition, a character module has been loaded into the GUI. This penguin model is what the player will control. Code exists
to insert a new entity. This new entity could be a bad guy, or an obstacle for the character module must overcome. All of these entitities are controlled via the game loop,
and this game loop itself is being constantly run at 60 frames per second.

Finally, a class dedicated for the user exists. It will gather the user's name, and keep track of their score.

*****CONTROLS******
a to go left
d to go right
spacebar to jump
