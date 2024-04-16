import pygame, sys, random
import os, sys, ast
import pickle


#Game Settings
FPS = 60
pygame.init()
pygame.mixer.init
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
PURPLE = (51, 0, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 223, 0)
ORANGE = (255, 165, 0)
RED = (255,0,0)
FONT_SIZE = 36
SMALL_FONT_SIZE = 25
SUPER_SMALL_FONT = 20
BIG_FONT_SIZE = 50
IMAGE_SIZE = (200, 200)
IMAGE_PADDING = 10
MAIN_MENU_BTN_WIDTH = 200
MAIN_MENU_BTN_HEIGHT = 50

# print(pygame.font.get_fonts())

#game variables
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Hangman Two Game")
menu_font = pygame.font.SysFont("skia", 32)
title_font = pygame.font.SysFont("skia", 62, bold=True)
plain_font = pygame.font.SysFont("skia", FONT_SIZE, bold=True)
smaller_plain_font = pygame.font.SysFont("skia", SMALL_FONT_SIZE, bold=True)
super_small_text = pygame.font.SysFont("skia", SUPER_SMALL_FONT, bold=True)
btn_sound = pygame.mixer.Sound("mixkit-light-spell-873.wav")
game_music = pygame.mixer.Sound("Industry And Technology.mp3")
correct_sound = pygame.mixer.Sound("game-sound-correct.wav")
full_correct_sound = pygame.mixer.Sound("correct-2.wav") 
wrong_sound = pygame.mixer.Sound("game-sound-wrong.wav")
cheer_sound = pygame.mixer.Sound("crowd-cheer.wav")
crowd_booing = pygame.mixer.Sound("crowdbooing_01.wav")
guessed_letters = set()
non_letters = ["!", ".", "'", "?", ",", "&", ":"]
title_update = True

#Scoring Settings
difficulty = "Easy"
score = 0
high_score = 0
easy_add = 250
normal_add = 500
hard_add = 700


hangman_list = []

# load and add hangman images to list
for i in range(0,7):
    img_path = "hangman" + str(i) + ".png"
    image = pygame.image.load(img_path).convert()
    img_scaled = pygame.transform.scale(image, IMAGE_SIZE)
    hangman_list.append(img_scaled)
    
    


# Import words from external file that I manually added
with open("/Users/user/Desktop/Code_Games/Hangman/words.py") as f:
    data = f.read()
    word_dict = ast.literal_eval(data)
    
dict_paths = ['dc_characters.txt', 'countries.txt','capitals.txt', 'flowers.txt']


# for path in dict_paths:
#     with open(path, 'rb') as handle: 
#         dt = handle.read()
#         print(dt)
#         new_data = pickle.load(dt)
#         word_dict.update(new_data)
    

# reading data from webscraping
with open('dc_characters.txt', 'rb') as handle: 
    dc = handle.read()
    
with open('countries.txt', 'rb') as ct: 
    ctry = ct.read()

with open('capitals.txt', 'rb') as cpt: 
    cap = cpt.read()

with open('flowers.txt', 'rb') as f: 
    fl = f.read()

with open('childhood_cartoons.txt', 'rb') as cc: 
    ch = cc.read()
  
  
# reconstructing the data as dictionary 
dc_characters = pickle.loads(dc)
countries = pickle.loads(ctry)
capitals = pickle.loads(cap)
flowers = pickle.loads(fl)
cartoons = pickle.loads(ch)

# combing data from multiple sources both manual and webscraping
word_dict.update(dc_characters)
word_dict.update(countries)
word_dict.update(capitals)
word_dict.update(flowers)
word_dict.update(cartoons)

    
# print(word_dict)
category_list = word_dict.keys()
print(category_list)
    
selected_cat = "Marvel"









class Button:
    def __init__(self, txt, color, pos, width, height):
        self.text = txt
        self.text_surf = menu_font.render(self.text, True, PURPLE)
        self.color = color
        self.display_color = self.color
        self.hover_color = WHITE
        self.pos = pos
        self.height = height
        self.width = width
        self.button = pygame.rect.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.text_rect = self.text_surf.get_rect(center = self.button.center)
        self.border_rect = pygame.rect.Rect(self.pos[0] - 2, self.pos[1] - 2, self.width + 4, self.height + 4)
        self.clicked = False
        
    def draw(self):
        # border_rect = pygame.rect.Rect(self.pos[0] - 2, self.pos[1] - 2, self.width + 4, self.height + 4)
        pygame.draw.rect(screen, PURPLE, self.border_rect, border_radius=15)
        pygame.draw.rect(screen, self.display_color, self.button, border_radius=15)
        screen.blit(self.text_surf, self.text_rect)
    
    def checkClicked(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.button.collidepoint(mouse_pos):
            self.display_color = self.hover_color
            if mouse_click[0] == 1 and self.clicked == False:
                # print("click")
                btn_sound.play()
                self.clicked = True
                return True
        if mouse_click[0] == 0:
            self.display_color = self.color
            self.clicked = False
    
    def isHoveredOver(self, color):
        mouse_pos = pygame.mouse.get_pos()
        over = self.button.collidepoint(mouse_pos)
        
        
        
            


def displayGameStatus(display_word, attempts_left, chosen_word):
    global high_score
    global score
    losing_text_options = ["Nice Try!!!", "Oh Sorry!!!", "Oh So Close!!!", "Try again", "Loser!!!!!"]
    chosen_losing_text = random.choice(losing_text_options).upper()
    if attempts_left == 0:
        pygame.time.delay(3000)
        crowd_booing.play()
        screen.fill("Black")
        score = 0
        if score > high_score:
            high_score = score
    
        game_status= chosen_losing_text + " the word was " + chosen_word
        font = pygame.font.Font(None, BIG_FONT_SIZE)
        status_surface = font.render(game_status, True, WHITE)
        screen.blit(status_surface, (SCREEN_WIDTH // 2 - status_surface.get_width() // 2, SCREEN_HEIGHT / 2))        
        pygame.display.flip()



    elif " __ " not in display_word:
        full_correct_sound.play()
        pygame.time.delay(3000)
        cheer_sound.play()
        game_status = "You Won!!!"
        handleScore()
        screen.fill(GREEN)
        font = pygame.font.Font(None, BIG_FONT_SIZE)
        status_surface = font.render(game_status, True, BLACK)
        screen.blit(status_surface, (SCREEN_WIDTH // 2 - status_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        pygame.display.flip()
        
 
 
def handleScore():
    global score
    if difficulty == "Easy":
        score+= easy_add
    elif difficulty == "Normal":
        score+= normal_add
    else:
        score+= hard_add
        
        
        
def drawscore():
    if score > high_score:
        score_color = GREEN
    else:
        score_color = WHITE
    
    display_score = smaller_plain_font.render(f'Score: {score}', True, score_color)
    display_high_score = smaller_plain_font.render(f'High Score: {high_score}', True, GREEN)
    screen.blit(display_score, (800, 100))
    screen.blit(display_high_score, (500, 100))
 
 
  
  
        

def configBoard(category):
    chosen_word = random.choice(word_dict[category]).upper()
    return chosen_word


def resetGame():
    global guessed_letters
    guessed_letters = set()
    score = 0
    difficulty = "Easy"

    


def swapLetters(chosen_word):
    board = []
    for letter in chosen_word:
        if letter in guessed_letters or letter in non_letters:
            board.append(letter + " ")
        elif letter == " ":
            board.append("    ")
        else:
            board.append(" __ ")
    return "".join(board)



def draw_hangman_title():
    hangman_titles = ["_ _ _ _ _ _ _", "_ _ _ G _ _ _", "_ _ _ G M _ _","_ _ N G M _ N", "_ A N G M A N", "H A N G M A N"]
    
    global title_update
    
    while title_update:
        for title in hangman_titles:
            screen.fill(YELLOW)
            title_surf = title_font.render(title, True, PURPLE)
            screen.blit(title_surf, (SCREEN_WIDTH //2 - title_surf.get_width()//2, 50)) 
            correct_sound.play()       
            pygame.display.update()
            pygame.time.wait(500)
            
            if title == "H A N G M A N":
                full_correct_sound.play()
                title_update = False
    




def drawGuessLetters(chosen_word):
    font = pygame.font.Font(None, FONT_SIZE)
    guessed_msg = plain_font.render("Guessed Letters: ", True, WHITE)
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
    global difficulty
    
    while True:         
        screen.fill(YELLOW)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        # btn_x = 500
        # btn_y = 150
        
        # All buttons on the category page
        select_msg = plain_font.render("SELECT A CATEGORY BELOW", True, PURPLE )
        screen.blit(select_msg, (250, 30))
        
        first_column = 100
        second_column = 400
        third_column = 600
        first_row = 200
        second_row = first_row + 100
        third_row = second_row + 100
        fourth_row = third_row + 100
        fifth_row = fourth_row + 100
        
        marvel_btn = Button("Marvel", GREEN, (second_column, first_row), 120, 50)
        marvel_btn.draw()
        nba_btn = Button("NBA", ORANGE, (second_column, second_row), 100, 50)
        nba_btn.draw()
        artist_btn = Button("Artists", ORANGE, (second_column, third_row), 120, 50)
        artist_btn.draw()
        family_btn = Button("Family", GREEN, (second_column, fourth_row), 120, 50)
        family_btn.draw()
        cereal_btn = Button("Cereal", GREEN, (second_column, fifth_row), 120, 50)
        cereal_btn.draw()
        zaya_friends_btn = Button("Zaya Friends", GREEN, (third_column, fourth_row), 200, 50)
        zaya_friends_btn.draw()
        grandma_btn = Button("Grandma's Phrases", RED, (third_column, first_row), 300, 50)
        grandma_btn.draw()
        capitals_btn = Button("Capitals and States", RED, (third_column, second_row), 300, 50)
        capitals_btn.draw()
        childhood_cartoons_btn = Button("Childhood Cartoons", RED, (third_column, third_row), 300, 50)
        childhood_cartoons_btn.draw()
        fruit_btn = Button("Fruits", GREEN, (first_column, first_row), 100, 50)
        fruit_btn.draw()
        dc_btn = Button("DC Comics", RED, (first_column, second_row), 180, 50)
        dc_btn.draw()
        country_btn = Button("Countries", RED, (first_column, third_row), 180, 50)
        country_btn.draw()
        flowers_btn = Button("Flowers", ORANGE, (first_column, fourth_row), 150, 50)
        flowers_btn.draw()
        
        # btn_list = []
        
        # for cat_name in category_list:
        #     cat_btn = Button(cat_name, GREEN, (btn_x, btn_y), 200, 50)
        #     cat_btn.draw()
        #     btn_list.append(cat_btn)
        #     btn_y +=100
            
        # for category_btn in btn_list:
        #     if category_btn.checkClicked():
        #         selected_cat = category_btn.text
        #         print(selected_cat)
        #         break
        pygame.display.flip()
        
        

        if marvel_btn.checkClicked():
            selected_cat = "Marvel"
            difficulty = "Easy"
            return selected_cat
        if artist_btn.checkClicked():
            selected_cat = "Artists"
            difficulty = "Normal"
            return selected_cat
        if nba_btn.checkClicked():
            selected_cat = "NBA"
            difficulty = "Normal"
            return selected_cat
        if family_btn.checkClicked():
            difficulty = "Easy"
            selected_cat = "Smikle Family"
            return selected_cat
        if zaya_friends_btn.checkClicked():
            selected_cat = "Zaya's Friends"
            return selected_cat
        if grandma_btn.checkClicked():
            selected_cat = "Grandma's Phrases"
            difficulty = "Hard"
            return selected_cat
        if fruit_btn.checkClicked():
            selected_cat = "Fruits"
            difficulty = "Easy"
            return selected_cat
        if dc_btn.checkClicked():
            selected_cat = "DC Comics"
            difficulty = "Hard"
            return selected_cat
        if country_btn.checkClicked():
            selected_cat = "Countries"
            difficulty = "Hard"
            return selected_cat
        if capitals_btn.checkClicked():
            selected_cat = "Capitals"
            difficulty = "Hard"
            return selected_cat
        if flowers_btn.checkClicked():
            selected_cat = "Flowers"
            difficulty = "Normal"
            return selected_cat
        if childhood_cartoons_btn.checkClicked():
            selected_cat = "Childhood Cartoons"
            difficulty = "Hard"
            return selected_cat
        if cereal_btn.checkClicked():
            selected_cat = "Cereal"
            difficulty = "Easy"
            return selected_cat

        
            
        
        
        
        


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
                
        
        #draw main title letter by letter animaton
        
        draw_hangman_title()      
        
        title_surface = title_font.render("H A N G M A N", True, PURPLE)
        screen.blit(title_surface, (SCREEN_WIDTH //2 - title_surface.get_width()//2, 50))
        
        menu_x = 250
        menu_y = SCREEN_HEIGHT//2
        new_game = Button("New Game", GREEN, (menu_x, menu_y), 175, 50)
        new_game.draw()
        
        exit_btn = Button("Quit", RED, (menu_x + 370, menu_y), 175, 50)
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
    global guessed_letters
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

        if len(chosen_word) > 20: 
            text_surface = super_small_text.render(display_word, True, WHITE)
        elif len(chosen_word) > 10:
            text_surface = smaller_plain_font.render(display_word, True, WHITE)
        else:
            text_surface = plain_font.render(display_word, True, WHITE)

        moves_left = smaller_plain_font.render(f'Attempts Left: {attempts_left}', True, WHITE)
        cat_text = plain_font.render(selected_cat, True, WHITE)
        menu_btn = Button("MAIN MENU", GREEN, (800, 10), 200, 50)
        # menu_btn.rect = pygame.rect.Rect(600, 500, 100, 25)
        menu_btn.draw()
        hangman_image = hangman_list[attempts_left]
        
        if menu_btn.checkClicked():
            global title_update
            title_update = True
            return False
        # screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, SCREEN_HEIGHT / 2))
        screen.blit(text_surface, (IMAGE_PADDING + hangman_image.get_width() + 50, SCREEN_HEIGHT / 2))
        screen.blit(hangman_image, (IMAGE_PADDING, 200))
        screen.blit(moves_left, (10,500))
        screen.blit(cat_text, (20,50))
        
        
        # Change category during game. Not working
        new_cat_btn = Button("Change Category", GREEN, (450, 10), 300, 50)
        if len(guessed_letters) == 0:
            new_cat_btn.draw() 
        if new_cat_btn.checkClicked():
            new_cat = selectCategory()
            print(selected_cat)
            attempts_left = 6
            new_chosen_word = configBoard(new_cat)
            guessed_letters = set()
            playGame(new_chosen_word, attempts_left, new_cat)
        
        
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
        drawscore()
                        
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
