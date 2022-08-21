# Importing Pygame Module as pg
import pygame as pg
import os
import sys

# Initializing Pygame
pg.init()

# Declaring width & height
(width, height) = (430, 700)

# Declaring Colors
black = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


# Declaring Font
font = pg.font.Font('freesansbold.ttf', 32)

# Setting up the color & size
screen = pg.display.set_mode((width, height))
pg.display.set_caption('Main Menu')
screen.fill(black)

# "Main Menu" Text
text = font.render('MAIN MENU', True, white)
textRect = text.get_rect(center=(width / 2, height / 7))

# Loading Button Images
b1 = pg.image.load('button2.jpeg').convert_alpha()

# Button Class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y)
        self.clicked = False

    def draw(self):

        action = False

        # Mouse Position
        mouse_pos = pg.mouse.get_pos()

        # Check Mouseover & Clicked condition
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # For Displaying The Button
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# Creating Buttons
button1 = Button(width / 4.5, height / 4, b1, 0.38)
button2 = Button(width / 1.7, height / 4, b1, 0.38)
button3 = Button(width / 4.5, height / 2.4, b1, 0.38)
button4 = Button(width / 1.7, height / 2.4, b1, 0.38)
button5 = Button(width / 4.5, height / 1.7, b1, 0.38)
button6 = Button(width / 1.7, height / 1.7, b1, 0.38)


# Main Loop
running = True
while running:

    screen.blit(text, textRect)

    if button1.draw():
        #print("Game 1")
        exec(open("main.py").read())
    if button2.draw():
        print("Game 2")
    if button3.draw():
        print("Game 3")
    if button4.draw():
        print("Game 4")
    if button5.draw():
        print("Game 5")
    if button6.draw():
        print("Game 6")

    for event in pg.event.get():
        if event.type == pg.QUIT: 
            running = False

    pg.display.update()
    pg.display.flip()

pg.quit()