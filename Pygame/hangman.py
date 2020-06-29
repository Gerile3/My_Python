import os
from string import ascii_uppercase
from random import choice

import pygame
import pygame.freetype

# Tutorial = https://www.youtube.com/watch?v=UEO1B_llDnc
# init
pygame.init()
WIDTH = 800
HEIGHT = 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman The Game")
GAME_FONT = pygame.freetype.Font("My_Python\\Pygame\\ARCADECLASSIC.TTF", 26)
WORD_FONT = pygame.freetype.SysFont("comicsans", 50)


# images
images = []
location = "My_Python\\Pygame\\Hangman Images"
for i in range(len(os.listdir(location))):
    image = pygame.image.load(location + "\\" + "hangman" + str(i) + ".png")
    images.append(image)

# variables
won = [False]
hangman_status = 0
word_list = ["PYTHON", "MONDAY", "ETHERNET", "STUDIO"]
word = choice(word_list)
guessed = ""
background_color = (255, 255, 255)  # White
run = True


# buttons
letter_coordinates = []
RADIUS = 20
GAP = 15

start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400


for j in range(len(ascii_uppercase)):
    x = start_x + GAP * 2 + ((RADIUS * 2 + GAP) * (j % 13)) - 15
    y = start_y + ((j // 13)) * (GAP + RADIUS * 2)
    letter_coordinates.append([x, y, ascii_uppercase[j], True])


def draw():
    display_word = ""
    win.fill(background_color)

    # draw word
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    WORD_FONT.render_to(win, (400, 175), display_word, (0, 0, 0))

    # draw letters
    for letter in letter_coordinates:
        x, y, char, pressed = letter
        if pressed:
            pygame.draw.rect(win, (0, 0, 0), (x, y, 30, 30), 3)
            GAME_FONT.render_to(win, (x + 8, y + 8), char, (0, 0, 0))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(background_color)
    WORD_FONT.render_to(win, (300, 200), message, (0, 0, 0))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    # loop
    global hangman_status, guessed, won, run
    clock = pygame.time.Clock()
    FPS = 60

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            # Check collision
            for ltr in letter_coordinates:
                x, y, char, pressed = ltr
                if 0 < m_x - x < 30 and 0 < m_y - y < 30 and pressed:
                    distance = (m_x - x) * (m_y - y)
                    if 0 < distance <= 900:
                        ltr[3] = False
                        guessed += char
                        if char not in word:
                            hangman_status += 1

            won = [True if i in guessed and word else False for i in word]

    draw()

    if hangman_status >= 6:
        display_message("You Lost!")
        run = False

    if all(won):
        display_message("You won!")
        run = False


if __name__ == "__main__":
    # Todo:
    # Refactoring.. like alot of it.
    # Build on class structure
    # Random words, daily words on internet
    # main menu and scores
    # add music
    while run:
        main()

    pygame.quit()
