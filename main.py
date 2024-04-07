import pygame, sys, random
# from time import sleep
# from pygame.locals import *
# from timeit import default_timer as timer

FPS = 60
pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
PURPLE = (51, 0, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 223, 0)
RED = (255,0,0)
FONT_SIZE = 34
BIG_FONT_SIZE = 50
IMAGE_SIZE = (200, 200)
IMAGE_PADDING = 10


#game variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hangman Two Game')
menu_font = pygame.font.Font('freesansbold.ttf', 32)
image = pygame.image.load("hangman1.svg")
hangman_image = pygame.transform.scale(image, IMAGE_SIZE)
guessed_letters = set()
# attempts_left = 6


# Load word list (you can replace this with your own list)
# word_list = [ "The Hulk", "Spiderman", "The Avengers", "Iron Man", "Captain America",
#         "Thor", "Loki", "Black Widow", "Hawk Eye", "The Red Skull", "Thanos",
#         "Scarlett Witch", "Vison", "Zemo", "Green Goblin", "The Jackal",
#         "Fantastic Four", "The Thing", "Silver Surfer",
#         "Guardians of the Galaxy", "Nick Fury", "Shield", "Vulture",
#         "Doctor Octopus", "Venom", "The Punisher", "Blade", "Magneto",
#         "Wolverine", "Cyclops", "Jean Grey", "Beast", "Iron Fist", "Luke Cage",
#         "Dare Devil", "Scorpion", "Black Panther", "Wakanda",
#         "Stark Enterprise", "Tony Stark", "Power man", "Abomination",
#         "Carnage", "I am Groot", "Avengers Assemble", "War Machine",
#         "Mister Fantasic", "Invisible Woman", "The Human Torch", "Venom",
#         "Scarlet Witch", "The Fantastic Four", "The Mandarin", "The Wasp",
#         "Wolverine", "Cyclops", "Jean Grey", "Beast", "Luke Cage",
#         "Dare Devil", "Sand man", "Beast", "Silver Surfer", "Captain Marvel",
#         "Venom", "Magneto", "Night Crawler", "Madame Web", "Carnage",
#         "King pin", "Doctor Octopus", "The Lizard", " She Hulk"
#         ]

categories = ["Marvel", "NBA", "Artists"]


word_dict = {
    "Marvel": [
        "The Hulk", "Spiderman", "The Avengers", "Iron Man", "Captain America",
        "Thor", "Loki", "Black Widow", "Hawk Eye", "The Red Skull", "Thanos",
        "Scarlett Witch", "Vison", "Zemo", "Green Goblin", "The Jackal",
        "Fantastic Four", "The Thing", "Silver Surfer",
        "Guardians of the Galaxy", "Nick Fury", "Shield", "Vulture",
        "Doctor Octopus", "Venom", "The Punisher", "Blade", "Magneto",
        "Wolverine", "Cyclops", "Jean Grey", "Beast", "Iron Fist", "Luke Cage",
        "Dare Devil", "Scorpion", "Black Panther", "Wakanda",
        "Stark Enterprise", "Tony Stark", "Power man", "Abomination",
        "Carnage", "I am Groot", "Avengers Assemble", "War Machine",
        "Mister Fantasic", "Invisible Woman", "The Human Torch", "Venom",
        "Scarlet Witch", "The Fantastic Four", "The Mandarin", "The Wasp",
        "Wolverine", "Cyclops", "Jean Grey", "Beast", "Luke Cage",
        "Dare Devil", "Sand man", "Beast", "Silver Surfer", "Captain Marvel",
        "Venom", "Magneto", "Night Crawler", "Madame Web", "Carnage",
        "King pin", "Doctor Octopus", "The Lizard", " She Hulk"
    ],
    "Artists": [
        "Jay Z", "Queen Latifah", "DMX", "Snoop Dogg", "Jadakiss", "J Cole",
        "Jermaine Dupri", "Alicia Keys", "John Legend", "Lil Jon", "Lil Kim",
        "Diddy", "Tupac", "Lil Wayne", "Beastie Boyz", "Ying Yang Twins",
        "Drake", "Cash Money", "Ruff Ryders", "Bad Boy Entertainment",
        "Nicki Minaj", "Bryson Tiller", "Torey Lanez", "Summer Walker",
        "Usher", "Cardi B", "DMX", "Meg The Stallion", "Chris Brown",
        "Rihanna", "The Fugees", "Aretha Franklin", "Jay Rock", "Kanye West",
        "Kendrick Lamar", "Kid Cudi", "James Brown", "Michael Jackson"
    ],
    "NBA": [
        "LeBron James", "Carmelo Anthony", "Michael Jordan", "Kobe Bryant",
        "Tim Duncan", "Kevin Garnet", "Russell Westbrook", "Pick and Roll",
        "New York Knicks", "Los angeles Lakers", " Los Angeles Clippers",
        "New Orlean Pelicans", "Charlotte Hornets", "Golden State Warriors",
        "Sacremento Kings", "Toronto Raptors", "Stephen Curry", "Kevin Durant",
        "Kyrie Irving", "Kawhi Leonard", "Boston Celtics", "Miami Heat",
        "Magic Johnson", "Houston Rockets", "Chicago Bulls",
        "Oklahoma City Thunder", "Denver Nuggets", "Dallas Mavericks",
        "Portland Trail Blazers", "Brooklyn Nets", "Jayson Tatum",
        "Jaylen Brown", "Anthony Davis", "Jimmy Butler", "James Harden",
        "Jimmy Butler", "Shaquille O'Neal", "Kyrie Irving", "Zion Williamson",
        "Ja Morant"
    ]
}
# chosen_word = random.choice(word_list).upper()





class Button:
    def __init__(self, txt, color, pos):
        self.text = txt
        self.color = color
        self.pos = pos
        self.button = pygame.rect.Rect(self.pos[0], self.pos[1], 200, 50)
        
        
    def draw(self):
        # menu_font = pygame.font.Font('freesansbold.ttf', 32)
        text = menu_font.render(self.text, True, BLACK)
        pygame.draw.rect(screen, self.color, self.button)
        screen.blit(text, ( self.pos[0] + 10, self.pos[1]+ 10))
    
    def checkClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.button.collidepoint(mouse_pos) and mouse_click[0]:
            return True
    
    def isHoveredOver(self, color):
        mouse_pos = pygame.mouse.get_pos()
        over = self.button.collidepoint(mouse_pos)
            


def displayGameStatus(display_word, attempts_left, chosen_word):
    losing_text_options = ["Nice Try!!!", "Oh Sorry!!!", "Oh So Close!!!", "Try again", "Loser!!!!!"]
    chosen_losing_text = random.choice(losing_text_options).upper()
    if attempts_left == 0:
        pygame.time.delay(2000)
        screen.fill("Black")
        game_status= chosen_losing_text + " the word was " + chosen_word
        font = pygame.font.Font(None, BIG_FONT_SIZE)
        status_surface = font.render(game_status, True, PURPLE)
        screen.blit(status_surface, (SCREEN_WIDTH // 2 - status_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()


    elif " __ " not in display_word:
        pygame.time.delay(2000)
        game_status = "You Won!!!"
        screen.fill(GREEN)
        font = pygame.font.Font(None, BIG_FONT_SIZE)
        status_surface = font.render(game_status, True, BLACK)
        screen.blit(status_surface, (SCREEN_WIDTH // 2 - status_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        
        

def configBoard(category):
    chosen_word = random.choice(word_dict[category]).upper()
    return chosen_word


def swapLetters(chosen_word):
    board = []
    for letter in chosen_word:
        if letter in guessed_letters:
            board.append(letter + " ")
        elif letter == " ":
            board.append("    ")
        else:
            board.append(" __ ")
    return "".join(board)


def drawGuessLetters(chosen_word):
    font = pygame.font.Font(None, FONT_SIZE)
    guessed_msg = font.render("Guessed Letters: ", True, WHITE)
    screen.blit(guessed_msg, (0, 550))
    first_ltr_x = guessed_msg.get_width() + 10
    for ltr in guessed_letters:
        if ltr in chosen_word:
            ltr_surface = font.render(ltr, True, GREEN)
        else:
            ltr_surface = font.render(ltr, True, RED)
        screen.blit(ltr_surface, (first_ltr_x, 550))
        
        first_ltr_x+= 30
        

def selectCategory():
    selected = False
    
    while selected == False:         
        screen.fill(YELLOW)
        firstbtn_x = 300
        firstbtn_y = 100
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        marvel_btn = Button("Marvel", GREEN, (300, 100))
        marvel_btn.draw()
        nba_btn = Button("NBA", GREEN, (300, 200))
        nba_btn.draw()
        artists_btn = Button("Artists", GREEN, (300, 300))
        artists_btn.draw()
        
        
        pygame.display.update()
            
        
        
        
        


def mainMenu():
    
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.fill(YELLOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        menu_x = 300
        menu_y = SCREEN_HEIGHT//2
        new_game = Button("New Game", GREEN, (menu_x, menu_y))
        new_game.draw()
        
        exit_btn = Button("Exit", RED, (menu_x, menu_y + 100))
        exit_btn.draw()
        # menu_btn = pygame.draw.rect(screen, GREEN, [menu_x, menu_y, 200, 50])
        # screen.blit(text, (menu_x + 10, menu_y + 10))
        # start_game = False
        pygame.display.flip()
        
        if new_game.checkClicked():
            selectCategory()
            global guessed_letters
            guessed_letters = set()
            chosen_word = configBoard("NBA") 
            attempts_left = 6
            playGame(chosen_word, attempts_left)
            pygame.time.delay(3000)
        if exit_btn.checkClicked():
            running = False
            pygame.quit()
            
        
            
    



def playGame(chosen_word, attempts_left):
    clock = pygame.time.Clock()
    running = True
    while running:   
        clock.tick(FPS)
        
        #quit game by click exit on window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        
            
        screen.fill(PURPLE)
        # Draw the word with underscores for unguessed letters
        # display_word = "".join([letter + " " if letter in guessed_letters else " __ " for letter in chosen_word])
        display_word = swapLetters(chosen_word)
        font = pygame.font.Font(None, FONT_SIZE)
        text_surface = font.render(display_word, True, WHITE)
        moves_left = font.render(str(attempts_left), True, WHITE)
        # screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        screen.blit(text_surface, (IMAGE_PADDING + hangman_image.get_width() + 50, SCREEN_HEIGHT / 2))
        screen.blit(hangman_image, (IMAGE_PADDING, 200))
        screen.blit(moves_left, (20,500))

        # Check for keyboard input
        keys = pygame.key.get_pressed()
        for key in range(pygame.K_a, pygame.K_z + 1):
            if keys[key]:
                letter = chr(key).upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter not in chosen_word:
                        attempts_left -= 1
        
        drawGuessLetters(chosen_word)
                        
        # Update the display
        pygame.display.flip()

        displayGameStatus(display_word, attempts_left, chosen_word)
        
        # Check for game over conditions
        if attempts_left == 0 or " __ " not in display_word:
            running = False


mainMenu()
# playGame()
# selectCategory()

# Wait for a moment before quitting
pygame.time.delay(2000)

# Clean up and exit
pygame.quit()
