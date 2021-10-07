import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 700, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

# button variables
RADIUS = 25
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 10) / 2)
starty = 135
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 10))
    y = starty + ((i // 10) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('consolas', 30)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('gabriola', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".jpeg")
    images.append(image)

# game variables
hangman_status = 0
words = ["IDE", "REPLIT", "PYTHON", "PYGAME","TEAMS","FRUIT","JAZZ","WEIRD","CEMETERY","HANGMAN"]
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)

def draw():
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("HANGMAN", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (200, 400))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (520, 280))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            screen = pygame.display.set_mode((700, 500))
            TPImage = pygame.image.load("imagewon.png")
            # coordinates of the image
            x = 0
            y = 0
            screen.blit(TPImage, (x, y))
            # paint screen one time
            pygame.display.flip()
            running = True
            while (running): # loop listening for end of game
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

        if hangman_status == 6:
            screen = pygame.display.set_mode((700, 500))
            WonImage = pygame.image.load("imagelost.png")
            # coordinates of the image
            x = 0
            y = 0
            screen.blit(WonImage, (x, y))
            # paint screen one time
            pygame.display.flip()
            running = True
            while (running): # loop listening for end of game
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
    
while True:
    
    main()
pygame.quit()