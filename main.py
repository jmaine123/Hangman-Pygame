import pygame, sys, random
# from time import sleep
# from pygame.locals import *
# from timeit import default_timer as timer

FPS = 60
pygame.init()
pygame.mixer.init
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
PURPLE = (51, 0, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 223, 0)
RED = (255,0,0)
FONT_SIZE = 34
SMALL_FONT_SIZE = 23
BIG_FONT_SIZE = 50
IMAGE_SIZE = (200, 200)
IMAGE_PADDING = 10

print(pygame.font.get_fonts())

#game variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hangman Two Game")
menu_font = pygame.font.Font("freesansbold.ttf", 32)
title_font = pygame.font.Font("freesansbold.ttf", 52)
btn_sound = pygame.mixer.Sound("mixkit-light-spell-873.wav")
game_music = pygame.mixer.Sound("Industry And Technology.mp3")
correct_sound = pygame.mixer.Sound("game-sound-correct.wav")
wrong_sound = pygame.mixer.Sound("game-sound-wrong.wav")
cheer_sound = pygame.mixer.Sound("crowd-cheer.wav")
guessed_letters = set()
# image = pygame.image.load("hangman7.svg")
# hangman_image = pygame.transform.scale(image, IMAGE_SIZE)
# attempts_left = 6

hangman_list = []

for i in range(0,7):
    img_path = "hangman" + str(i) + ".png"
    image = pygame.image.load(img_path)
    img_scaled = pygame.transform.scale(image, IMAGE_SIZE)
    hangman_list.append(img_scaled)
    
    

    
selected_cat = "Marvel"

category_list = ["Marvel", "NBA", "Artists", "Smikle Family", "Zaya's Friends"]


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
        "Mister Fantastic", "Invisible Woman", "The Human Torch", "Venom",
        "Scarlet Witch", "The Fantastic Four", "The Mandarin", "The Wasp",
        "Wolverine", "Cyclops", "Jean Grey", "Beast", "Luke Cage",
        "Dare Devil", "Sand man", "Beast", "Silver Surfer", "Captain Marvel",
        "Venom", "Magneto", "Night Crawler", "Madame Web", "Carnage",
        "King pin", "Doctor Octopus", "The Lizard", " She Hulk", "Doctor Doom"
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
        "Ja Morant", "Scottie Pippen"
    ],
    "Smikle Family": [
        "Jermaine", "Denise", "Zaya", "Sharon", "Denise", "Carl Smikle", 
        "Naomi Brady", "Ingrid", "Twyla", "Denver", "Jose Lopez", "Roderick", "Jazmine", "Charise", "Dori",
        "Madison", "Uncle Dougie", "Samuel", "Kevin", "Franchesca", "Dozer"
        
    ],
    "Zaya's Friends": [
        "Zaya", "Bruce", "Leena", "Jose Jr", "Tommy", "Adrian", "Adam", "Leo", "Alex", "Zuri", "Zoe", "Liam",
        "Ryan", "Pino", "Charlotte", "Alihan", "Aria", "victoria", "Filippo", "Julian", "Malakai", "Daniel", "Harish"
        "Lucas", "Sahana", "Avyan", "Ellie", "Sophia", "Lillian", "Rowan", "Gianna", "Caroline", "Henry", "Drew", "Tyler"
        "Claire", "Ayaan", "Ruhaani", "Ilia", "Ethan", "Eleanor", "Liberty", "Mila", "Viveca", "Liana", "Lael", "Nikisha", "David"
        "Oona", "Marcella", "Madison", "Rosie", "Anastasia", "Zaire", "George", "Cristina"
        
    ]
}
# chosen_word = random.choice(word_list).upper()





class Button:
    def __init__(self, txt, color, pos):
        self.text = txt
        self.color = color
        self.pos = pos
        self.button = pygame.rect.Rect(self.pos[0], self.pos[1], 200, 50)
        self.clicked = False
        
    def draw(self):
        # menu_font = pygame.font.Font('freesansbold.ttf', 32)
        text = menu_font.render(self.text, True, BLACK)
        pygame.draw.rect(screen, self.color, self.button)
        screen.blit(text, ( self.pos[0] + 10, self.pos[1]+ 10))
    
    def checkClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.button.collidepoint(mouse_pos):
            if mouse_click[0] == 1 and self.clicked == False:
                btn_sound.play()
                self.clicked = True
                return True
        if mouse_click[0] == 0:
            self.clicked = False
    
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
        status_surface = font.render(game_status, True, WHITE)
        screen.blit(status_surface, (SCREEN_WIDTH // 2 - status_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()


    elif " __ " not in display_word:
        pygame.time.delay(2000)
        cheer_sound.play()
        # cheer_sound.fadeout(3)
        game_status = "You Won!!!"
        screen.fill(GREEN)
        font = pygame.font.Font(None, BIG_FONT_SIZE)
        status_surface = font.render(game_status, True, BLACK)
        screen.blit(status_surface, (SCREEN_WIDTH // 2 - status_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        
        

def configBoard(category):
    chosen_word = random.choice(word_dict[category]).upper()
    return chosen_word


def resetGame():
    global guessed_letters
    guessed_letters = set()
    


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
    global selected_cat
    
    while True:         
        screen.fill(YELLOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        # btn_x = 500
        # btn_y = 150
        
        marvel_btn = Button("Marvel", GREEN, (300, 50))
        marvel_btn.draw()
        nba_btn = Button("NBA", GREEN, (300, 150))
        nba_btn.draw()
        artist_btn = Button("Artists", GREEN, (300, 250))
        artist_btn.draw()
        family_btn = Button("Family", GREEN, (300, 350))
        family_btn.draw()
        zaya_friends_btn = Button("Zaya Friends", GREEN, (300, 450))
        zaya_friends_btn.draw()
        
        # btn_list = []
        
        # for cat_name in category_list:
        #     cat_btn = Button(cat_name, GREEN, (btn_x, btn_y))
        #     cat_btn.draw()
        #     btn_list.append(cat_btn)
        #     btn_y +=100
            
        pygame.display.flip()
        
        
        # for category_btn in btn_list:
        #     if category_btn.checkClicked():
        #         selected_cat = category_btn.text
        #         print(selected_cat)
        #         break

        if marvel_btn.checkClicked():
            selected_cat = "Marvel"
            break
        if artist_btn.checkClicked():
            selected_cat = "Artists"
            break
        if nba_btn.checkClicked():
            selected_cat = "NBA"
            break
        if family_btn.checkClicked():
            selected_cat = "Smikle Family"
            break
        if zaya_friends_btn.checkClicked():
            selected_cat = "Zaya's Friends"
            break
            

        
            
        
        
        
        


def mainMenu():
    
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        screen.fill(YELLOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        title_surface = title_font.render("HANGMAN", True, PURPLE)
        screen.blit(title_surface, (SCREEN_WIDTH //2 - title_surface.get_width()//2, 50))      
        
        
        menu_x = 300
        menu_y = SCREEN_HEIGHT//2
        new_game = Button("New Game", GREEN, (menu_x - 150, menu_y))
        new_game.draw()
        
        exit_btn = Button("Exit", RED, (menu_x + 200, menu_y))
        exit_btn.draw()

        pygame.display.flip()
        
        if new_game.checkClicked():
            selectCategory()
            global guessed_letters
            guessed_letters = set()
            chosen_word = configBoard(selected_cat) 
            attempts_left = 6
            playGame(chosen_word, attempts_left, selected_cat)
            pygame.time.delay(3000)
            
        if exit_btn.checkClicked():
            running = False
            pygame.quit()
            sys.exit()
            
        
            
    



def playGame(chosen_word, attempts_left, selected_cat):
    clock = pygame.time.Clock()
    running = True
    while running:   
        clock.tick(FPS)
        
        #quit game by click exit on window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        cheer_sound.fadeout(1)
            
        screen.fill(PURPLE)
        
        display_word = swapLetters(chosen_word)
        font = pygame.font.Font(None, FONT_SIZE)
        small_font = pygame.font.Font(None, SMALL_FONT_SIZE)
        text_surface = font.render(display_word, True, WHITE)
        moves_left = font.render(str(attempts_left), True, WHITE)
        cat_text = font.render(selected_cat, True, WHITE)
        menu_btn = Button("MAIN MENU", GREEN, (600, 550))
        menu_btn.rect = pygame.rect.Rect(600, 500, 100, 25)
        menu_btn.draw()
        hangman_image = hangman_list[attempts_left]
        
        if menu_btn.checkClicked():
            return False
        # screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        screen.blit(text_surface, (IMAGE_PADDING + hangman_image.get_width() + 50, SCREEN_HEIGHT / 2))
        screen.blit(hangman_image, (IMAGE_PADDING, 200))
        screen.blit(moves_left, (20,500))
        screen.blit(cat_text, (20,50))

        # Check for keyboard input
        keys = pygame.key.get_pressed()
        for key in range(pygame.K_a, pygame.K_z + 1):
            if keys[key]:
                letter = chr(key).upper()
                if letter not in guessed_letters:
                    guessed_letters.add(letter)
                    if letter not in chosen_word:
                        wrong_sound.play()
                        attempts_left -= 1
                    else:
                        correct_sound.play()
        
        drawGuessLetters(chosen_word)
                        
        # Update the display
        pygame.display.flip()

        displayGameStatus(display_word, attempts_left, chosen_word)
        
        # Check for game over conditions
        if attempts_left == 0 or " __ " not in display_word:
            pygame.time.delay(3000)
            resetGame()
            new_word = configBoard(selected_cat)
            playGame(new_word, attempts_left=6, selected_cat=selected_cat)
            # running = False



game_music.play(-1)
mainMenu()

# Wait for a moment before quitting
# pygame.time.delay(2000)

# Clean up and exit
pygame.quit()
