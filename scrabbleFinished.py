#Coursework - Scrabble with Pygame
#All references within the Bibliography attached to the end of my documentation
#For all basic PyGame commands: BIBLIOGRAPHY I (JENS, 2014)

import pygame, sys, time, random, enchant #importing modules needed to run code

d = enchant.Dict("en_GB") #assigning English dictionary to value 'd' to use later in code
                                #BIBLIOGRAPHY V (Kelly, 2006)

from pygame.locals import * #importing names from pygame.locals into code 

#setting colours I will use as global variables so they can be accessed in all functions
BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (169, 169, 169)
PURPLE = (128, 0, 128)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)

#assinging variables that have to be mutable and will be used in later functions
p1_cards = []
p1_points = []
p2_points = []
p2_cards = []
total_p1 = 0
total_p2 = 0
turn1 = random.randint(0, 1)
turn = 0
count = 0
gtotal1 = []
gtotal2 = []
player1 = ' '
player2 = ' '

#creating a list of co-ordinates for the squares which allow players to score extra points
#used later in code when player clicks on squares to place letters in
#if mouse position one of the co-ordinates contained in these lists, extra points scored 
coord_double = []

for x in range(410, 460):
        for y in range(420, 470):
            location = [(x, y)]
            coord_double += location
            

for x in range(470, 520):
        for y in range(360 ,410):
                location = [(x, y)]
                coord_double += location

for x in range(470, 520):
        for y in range(480, 530):
                location = [(x, y)]
                coord_double += location

for x in range(530, 580):
        for y in range(420, 270):
                location = [(x, y)]
                coord_double += location
        

coord_triple = []

for x in range(290, 340):
        for y in range(240, 290):
                location = [(x, y)]
                coord_triple += location

for x in range(290, 340):
        for y in range(600, 650):
                location = [(x, y)]
                coord_triple += location

for x in range(650, 700):
        for y in range(240, 290):
                location = [(x, y)]
                coord_triple += location

for x in range(650, 700):
        for y in range(600, 650):
                location = [(x, y)]
                coord_triple += location

coord_four = []
for x in range(170, 220):
        for y in range(120, 170):
                location = [(x, y)]
                coord_four += location

for x in range(170, 220):
        for y in range(720, 770):
                location = [(x, y)]
                coord_four += location

for x in range(770, 820):
        for y in range(720, 770):
                location = [(x, y)]
                coord_four += location

for x in range(770, 820):
        for y in range(120, 170):
                location = [(x, y)]
                coord_four += location

coord_five = []
for x in range(50, 100):
        for y in range(50):
                location = [(x, y)]
                coord_five += location

for x in range(50, 100):
        for y in range(840, 890):
                location = [(x, y)]
                coord_five += location

for x in range(890, 940):
        for y in range(50):
                location = [(x, y)]
                coord_five += location

for x in range(890, 940):
        for y in range(840, 890):
                location = [(x, y)]
                coord_five += location


#creating dictionary to store different point values
#more difficult letters to use score higher

points = {'a': 2,
          'b': 4,
          'c': 4,
          'd': 3,
          'e': 2,
          'f': 5,
          'g': 3,
          'h': 4,
          'i': 2,
          'j': 9,
          'k': 6,
          'l': 2,
          'm': 4,
          'n': 2,
          'o': 2,
          'p': 4,
          'q': 11,
          'r': 2,
          's': 2,
          't': 2,
          'u': 2,
          'v': 5,
          'w': 5,
          'x': 9,
          'y': 5,
          'z': 11}

#pool of letters that players letters will be taken from
#letters will be removed from the pool as they are given to each player 
pool = ['a', 'a', 'a', 'a', 'a', 'a',
        'b', 'b', 'b',
        'c', 'c', 'c',
        'd', 'd', 'd', 'd',
        'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e',
        'f', 'f', 'f',
        'g', 'g', 'g',
        'h', 'h',
        'i', 'i', 'i', 'i', 'i', 'i', 'i', 'i',
        'j', 'j',
        'k', 'k',
        'l', 'l', 'l',
        'm', 'm',
        'n', 'n', 'n', 'n', 'n',
        'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
        'p', 'p', 'p',
        'q', 'q',
        'r', 'r', 'r', 'r', 'r',
        's', 's', 's',
        't', 't', 't', 't', 't', 't', 't',
        'u', 'u', 'u', 'u',
        'v', 'v', 'v',
        'w', 'w',
        'x', 'x',
        'y', 'y', 'y',
        'z']


#sets the co-ordinates for where the window is opened on screen 
DISPLAY = pygame.display.set_mode((600, 700))
#opens the window onscreen and sets sizes
DISPLAY = pygame.display.set_mode((1220, 900), 0, 32)

#function to create the playing board
#creates the grid, start button and title
def create_board():
    '''creating scrabbble baord'''
    
    pygame.init() #initialises the display module used on line 185
    DISPLAY.fill(BLUE) #filling background colour blue 

    #drawing the grid using sets of co-ordinates
    #drawing individual rectangles with set spacing in between them to create grid
    x = 0
    y = 0
    for row in range(15):
        for column in range(15):
            pygame.draw.rect(DISPLAY, WHITE, (x, y, 50, 50), 5)
            x+=60
        y += 60
        x=0
  
    #drawing and filling grey circle at the centre of the board
    #one letter out of the first word placed on the board will have to be on the grey circle
    CIRCLE = pygame.draw.circle(DISPLAY, GREY, (445, 445), 25)

    #drawing start button at the side of the game board
    #BIBIOGRAPHY: II (Anon, 2013) for all text written onto pygame display
    START_BUTTON = pygame.draw.circle(DISPLAY, GREY, (1050, 200), 70) 
    font_0 = pygame.font.Font('freesansbold.ttf', 40)
    text_0 = font_0.render('START', True, PURPLE, None)
    
    textrect_0 = text_0.get_rect(center=(1050,200)) #BIBLIOGRAPHY: III (Anon, 2017)
    
    DISPLAY.blit(text_0, textrect_0) #blit funcion makes sure it shows in pygame display 


    #writing 'x2' in grid squares
    #if a player places a letter on these squares, double points 
    font_1 = pygame.font.Font('freesansbold.ttf', 30)
    text_1 = font_1.render('X2', True, PURPLE, None)
    textrect_1 = text_1.get_rect(center=(445,385))
    DISPLAY.blit(text_1, textrect_1)


    font_2 = pygame.font.Font('freesansbold.ttf', 30)
    text_2 = font_2.render('X2', True, PURPLE, None)
    textrect_2 = text_2.get_rect(center=(505,445))
    DISPLAY.blit(text_2, textrect_2)

    font_3 = pygame.font.Font('freesansbold.ttf', 30)
    text_3 = font_3.render('X2', True, PURPLE, None)
    textrect_3 = text_3.get_rect(center=(445,505))
    DISPLAY.blit(text_3, textrect_3)

    font_4 = pygame.font.Font('freesansbold.ttf', 30)
    text_4 = font_4.render('X2', True, PURPLE, None)
    textrect_4 = text_4.get_rect(center=(385,445))
    DISPLAY.blit(text_4, textrect_4)


    #writing 'x3' in grid squares
    #if a player places a letter on these squares, triple points 
    font_5 = pygame.font.Font('freesansbold.ttf', 30)
    text_5 = font_5.render('X3', True, MAGENTA, None)
    textrect_5 = text_5.get_rect(center=(265,265))
    DISPLAY.blit(text_5, textrect_5)


    font_6 = pygame.font.Font('freesansbold.ttf', 30)
    text_6 = font_6.render('X3', True, MAGENTA, None)
    textrect_6 = text_6.get_rect(center=(265,625))
    DISPLAY.blit(text_6, textrect_6)

    font_7 = pygame.font.Font('freesansbold.ttf', 30)
    text_7 = font_7.render('X3', True, MAGENTA, None)
    textrect_7 = text_7.get_rect(center=(625,265))
    DISPLAY.blit(text_7, textrect_7)

    font_8 = pygame.font.Font('freesansbold.ttf', 30)
    text_8 = font_8.render('X3', True, MAGENTA, None)
    textrect_8= text_8.get_rect(center=(625,625))
    DISPLAY.blit(text_8, textrect_8)


    #writing 'x4' in grid squares
    #if a player places a letter on these squares, points are multiplied by 4
    font_9 = pygame.font.Font('freesansbold.ttf', 30)
    text_9 = font_5.render('X4', True, ORANGE, None)
    textrect_9 = text_9.get_rect(center=(145,145))
    DISPLAY.blit(text_9, textrect_9)


    font_10 = pygame.font.Font('freesansbold.ttf', 30)
    text_10 = font_10.render('X4', True, ORANGE, None)
    textrect_10 = text_10.get_rect(center=(145,745))
    DISPLAY.blit(text_10, textrect_10)

    font_11 = pygame.font.Font('freesansbold.ttf', 30)
    text_11 = font_11.render('X4', True, ORANGE, None)
    textrect_11 = text_11.get_rect(center=(745,145))
    DISPLAY.blit(text_11, textrect_11)

    font_12 = pygame.font.Font('freesansbold.ttf', 30)
    text_12 = font_12.render('X4', True, ORANGE, None)
    textrect_12 = text_12.get_rect(center=(745,745))
    DISPLAY.blit(text_12, textrect_12)


    #writing 'x5' in grid squares
    #if a player places a letter on these squares, points are multiplied by 5
    font_13 = pygame.font.Font('freesansbold.ttf', 30)
    text_13 = font_13.render('X5', True, YELLOW, None)
    textrect_13 = text_13.get_rect(center=(25,25))
    DISPLAY.blit(text_13, textrect_13)

    font_14 = pygame.font.Font('freesansbold.ttf', 30)
    text_14 = font_14.render('X5', True, YELLOW, None)
    textrect_14 = text_14.get_rect(center=(25,865))
    DISPLAY.blit(text_14, textrect_14)

    font_15 = pygame.font.Font('freesansbold.ttf', 30)
    text_15 = font_15.render('X5', True, YELLOW, None)
    textrect_15 = text_15.get_rect(center=(865,25))
    DISPLAY.blit(text_15, textrect_15)

    font_16 = pygame.font.Font('freesansbold.ttf', 30)
    text_16 = font_16.render('X5', True, YELLOW, None)
    textrect_16 = text_16.get_rect(center=(865,865))
    DISPLAY.blit(text_16, textrect_16)

    #creating game title within window 
    #placed above the start button, side of game board 
    font_17 = pygame.font.Font('freesansbold.ttf', 29)
    text_17 = font_17.render('Welcome to Scrabble!', True, PURPLE, None)
    textrect_17 = text_17.get_rect(center=(1054,25))
    DISPLAY.blit(text_17, textrect_17)
    pygame.display.update()

#function opening the instructions text file
#displays the text file in pygame window
    
#BIBLIOGRAPHY: VI (Dawson, 2010)
def display_instructions():
        '''Opening Instructions File'''
        text_file = open('scrabbleinstruct.txt', 'r') #opening text file
        x = 450
        y = 430
        SQUARE = pygame.draw.rect(DISPLAY, GREY, (15, 410, 870, 300)) #drawing and filling rectangle to put text on top  
        for line in text_file:
                font_18 = pygame.font.Font('freesansbold.ttf', 15)
                text_18 = font_18.render(line, True, BLACK, None)
                textrect_18 = text_18.get_rect(center=(x,y))
                DISPLAY.blit(text_18, textrect_18)
                pygame.display.update()#updating pygame display so text file and rectangle shown on screen 
                y += 20 #changing y coordinate so that lines in text file printed on seperate lines 
        
        text_file.close()
        time.sleep(20) #allowing the instructions and rectangle to be shown for 20 seconds
                        #BIBLIOGRAPHY: VII (Tyler, no date)
        
        create_board() #after 20 seconds, create_board() function called to remove instructions and go back to start board 

#function caluclating winner
#function congratulating winner
#function writing winner to scoreboard 
def end_game(count, total_p1, total_p2, player1, player2, gtotal1, gtotal2):
        print('The 7 rounds have finished, lets calculate a winner!')

        #sum of players overall points
        #can find highest score
        a = sum(gtotal1)  
        b = sum(gtotal2) 


        #comparing scores and calculating winner
        #printing winnner and thier score
        if a > b: 
                print('player 1 wins scoring', a ,'! Lets add your score to the scoreboard')
                file = open('scoreboard.txt', 'a')  #opening text file
                                                        #BIBLIOGRAPHY: X (Anon, 2009)
                
                initials = str(input('Enter your inititals: '))
                file.write(initials)  #writing winners initials to text file 
                file.write('\n')  #creating a new line for the next winner so that initials printed on seperate lines
                file.close()  #closing file
                
        if b > a:
                print('player2 wins scoring', b ,'! Lets add your score to the scoreboard')  
                file = open('scoreboard.txt', 'a')
                initials = str(input('Enter your inititals: '))
                file.write(initials)
                file.write('\n')
                file.close()
        if a == b:
                print('It is a draw! No one gets onto the scoreboard today.')

        #allows players to see the scoreboard
        #the scoreboard text file will have initials of all winners       
        view = input('Do you want to see the scoreboard? (y/n)')
        if view == 'y':
                file = open('scoreboard.txt', 'r')
                read = file.read()
                print(read)
                file.close()
                input('press enter to quit:')
                sys.exit() #BIBLIOGRAPHY: IX (Anon 2014)
        else:
                input('Press enter to quit:')
                sys.exit()
                      

#function for the start of the game
#receives players names and decides who gets the first turn 
def start():
    '''user presses start, terminal asks for player name'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  #detecting if mouse button pressed
                                                            # BIBLIOGRAPHY: IV (Anon, 2012)
                                                            
                x, y = pygame.mouse.get_pos()  #getting mouse co-ordinates 
                if x in range (980, 1120, 1) and y in range(130, 270, 1):

                        START_BUTTON = pygame.draw.circle(DISPLAY, BLUE, (1050, 200), 70) #drawing over the start button once it has been pressed 
                        pygame.display.update() #updating display so it looks like the start button has been removed
                        
                        player1 = str(input('Player 1 name: ')) #getting players names 
                        player2 = str(input('Player 2 name: '))
                        
                        turn1 = random.randint(0, 1) #using the random module to randomly choose who gets the first turn 
                        if turn1 == 0:
                                print(player1 , 'gets the first turn!')
                                font_18 = pygame.font.Font('freesansbold.ttf', 30)
                                text_18 = font_18.render('Player 1:', True, PURPLE, None)
                                textrect_18 = text_18.get_rect(center=(1050,200))
                                DISPLAY.blit(text_18, textrect_18) #writing 'player 1:' onto the pygame display so names can be displayed next to them 

                                font_19 = pygame.font.Font('freesansbold.ttf', 30)
                                text_19 = font_19.render('Player 2:', True, PURPLE, None)
                                textrect_19 = text_19.get_rect(center=(1050,300))
                                DISPLAY.blit(text_19, textrect_19)
                                pygame.display.update() #updates display so that 'player 1:' and 'player2:' are displayed in pygame window 

                                name1 = str(player1)#converting inputted names into strings that can be used within the .render function
                                name2 = str(player2)
                                font_20 = pygame.font.Font('freesansbold.ttf', 30)
                                text_20 = font_20.render(name1, True, PURPLE, None)
                                textrect_20 = text_20.get_rect(center=(1150,200))
                                DISPLAY.blit(text_20, textrect_20) #writing player 1's name next to 'player 1:' in the pygame window

                                font_21 = pygame.font.Font('freesansbold.ttf', 30)
                                text_21 = font_21.render(name2, True, PURPLE, None)
                                textrect_21 = text_21.get_rect(center=(1150,300))
                                DISPLAY.blit(text_21, textrect_21) #writing player 2's name next to 'player 2:' in the pygame window
                                pygame.display.update() #updates window 
                                turn == p1_turn(p1_cards, p1_points, points, total_p1, pool, gtotal1) #setting the first turn to player 1 by
                                                                                                        #calling p1_turn() function

                        elif turn1 == 1:
                                print(player2 , 'gets the first turn!')
                                font_18 = pygame.font.Font('freesansbold.ttf', 30)
                                text_18 = font_18.render('Player 1:', True, PURPLE, None)
                                textrect_18 = text_18.get_rect(center=(1050,200))
                                DISPLAY.blit(text_18, textrect_18) 

                                font_19 = pygame.font.Font('freesansbold.ttf', 30)
                                text_19 = font_19.render('Player 2:', True, PURPLE, None)
                                textrect_19 = text_19.get_rect(center=(1050,300))
                                DISPLAY.blit(text_19, textrect_19)
                                pygame.display.update()

                                name1 = str(player1)
                                name2 = str(player2)
                                font_20 = pygame.font.Font('freesansbold.ttf', 30)
                                text_20 = font_20.render(name1, True, PURPLE, None)
                                textrect_20 = text_20.get_rect(center=(1150,200))
                                DISPLAY.blit(text_20, textrect_20)

                                font_21 = pygame.font.Font('freesansbold.ttf', 30)
                                text_21 = font_21.render(name2, True, PURPLE, None)
                                textrect_21 = text_21.get_rect(center=(1150,300))
                                DISPLAY.blit(text_21, textrect_21)
                                pygame.display.update()
                                turn == p2_turn(p2_cards, p2_points, points, total_p2, pool, gtotal2, player1) #setting the first turn to player 2 by
                                                                                                                #calling p2_turn() function
                                        

                        
                        return player1, player2, turn #returning the values so that they can be accessed within other functions 

                        
                            
                    
                    

#function dealing first letters
#gives each player 7 random letters each
#at the start of the game 
def first_tiles():
    '''giving players first tiles'''

    for i in range(7):#using the range function to give each player 7 letters 
        p2_card = random.choice(pool) #randomly chosen letters from the pool
        pool.remove(p2_card) #letter given to player2, removed from the pool
        p2_cards.extend([p2_card]) #letter given to player2 added to their list of letters
        p1_card = random.choice(pool)
        pool.remove(p1_card)#letter given to player1, removed from the pool
        p1_cards.extend([p1_card])#letter given to player1, added to their list of letters
        
    
    return p1_cards, p2_cards #returning values so they can be accessed within other functions
    
    

            
    

#function for player 1's turn
#allows them to see their letters, choose a word, or miss a go if they cannot go 
def p1_turn(p1_cards, p1_points, points, total_p1, pool, gtotal1): #accessing all the variables the function needs
    '''Player 1 turn'''
    
    print(p1_cards) #displaying the letters 
    answer = ''
    length = int(input('Player 1: how many letters is your word? (If you cannot go press 0)')) #asking user to input how many letters their word is 
    if length == 0: #if they cannot go they press 0
        print('Okay, we will move on, you will score 0 and gain 1 extra tile to help with your next go') 
        p1_card1 = random.choice(pool) #randomly chooses 1 extra letter from the pool
        pool.remove(p1_card1) #removes this letter from the pool
        p1_cards.append(p1_card1) #adds this letter to players list of letters

    
    
    for i in range(length): #using the range function to repeat question as many times as the legnth of the players word
             letter = input('Enter your letter: (If you cannot go press 0) ') #asks user to input each individual letter of the word 
             if letter == '0': #still gives user the option to skip their turn if they realise they cannot make a word afterall 
                     print('okay, we will move on and you score 0')

             else:
                     P = points[letter] #retrieves point value for each letter entered from the dictionary 'points'
                     p1_points.append(P) #adds this point value to the list 'p1_points'
                     answer += letter #the letter is added to a string which creates the chosen word 

                    
             if letter not in p1_cards: #if player enters a letter that is not in their list of letters their turn is skipped 
                     print('your letter is not valid, your turn will now be skipped.')
                     p2_turn(p2_cards, p2_points, points, total_p2, pool, gtotal2, player1) #changing turns 

    if answer != '':
            if d.check(answer): #checking answer is in the english dictionary 
                    print('Yay your word is valid!')
                    ans_sum = sum(p1_points) #sum of 'p1|_points' to give points for this word choice before putting on board
                    total_p1 += ans_sum #adding the amount of points for the word choice to the total amount of points for player 1 so far
                    print('You can now click on the board where to place each letter')

                    split_answer = list(answer) #splitting answer into a list so letters can be individually placed on the board
                    i = 0
                    while i in range(len(split_answer)):
                            while True:
                                    for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN: #getting mouse position
                                                    x1, y1 = pygame.mouse.get_pos() #assigning mouse position co-ordinates to x1, y1
                                                    font_22 = pygame.font.Font('freesansbold.ttf', 50)
                                                    text_22 = font_22.render(split_answer[i], True, BLACK, None)
                                                    textrect_22 = text_22.get_rect(center=((x1), y1)) #placing the letter at the co-ordinates x1, y1
                                                    DISPLAY.blit(text_22, textrect_22)
                                                    pygame.display.update() #updating display to show letter on screen
                                                    i += 1 #iterating through the list of letters, moving onto the next letter


                                                
                                                    #testing if the mouse co-ordinates are within the list of co-ordinates for extra points  
                                                    if (x1, y1) in coord_double:
                                                            total_p1 += (ans_sum * 2)
                                                    elif (x1, y1) in coord_triple:
                                                            total_p1 += (ans_sum * 3)
                                                    elif (x1, y1) in coord_four:
                                                            total_p1 += (ans_sum * 4)
                                                    elif (x1, y1) in coord_five:
                                                            total_p1 += (ans_sum * 5)
                                                    if i in range(len(split_answer)):
                                                            print('Press your next square: ') #telling player from the command line to keep pressing the next square
                                                                                                    #until all the letters have been placed on the board

                                                    else:
                                                            print('Now we switch turns!') 
                                                            print('You scored:', total_p1) #telling player total score for their word after placing on the board
                                                            gtotal1.append(total_p1) #adding this total score to a list which will be used to calculate the winner
                                                            total_p1 == 0 #resetting the variable to 0 at the end of the turn so points for the next word can be calculated correctly
                                                            print('You used', length ,'tiles, so you will now be given', length ,'more')
                                        

                                                            for i in range(length): #giving player as many more letters as they used up
                                                                    p1_card1 = random.choice(pool)
                                                                    pool.remove(p1_card1)
                                                                    p1_cards.append(p1_card1)
                                            

                                        
                                                            for i in split_answer:
                                                                    p1_cards.remove(i) #removing the letters that were used in the answer from the players list of letters

                                                            print(p1_cards) #printing their remaining cards   
                                                            p1_points = [0] #resetting variable to 0 at the end of the turn so points for the next word are caluclated correctly
                                                            p2_turn(p2_cards, p2_points, points, total_p2, pool, gtotal2, player1) #moving onto the next turn
                                             
            else:
                    print('Your word is not valid. You will now score 0.') #if the word is not in the english dictionary the letters cannot be placed on the board
                    p2_turn(p2_cards, p2_points, points, total_p2, pool, gtotal2, player1) #moving on to the next turn 

    
    
    p1_points = [0] #still resetting the variable to 0 so points for next word are calculated correctly 
    p2_turn(p2_cards, p2_points, points, total_p2, pool, gtotal2, player1) #moving on to the next turn 
     
    return answer, p1_cards, p1_points, total_p1, pool, length, gtotal1 #returning values so that they can be used in other functions and when it is player1's turn again 
    
    pygame.display.update()
    


#function for player 2's turn
#allows them to see their letters, choose a word, or miss a go if they cannot go
#same as p1_turn except includes the counter for each round
def p2_turn(p2_cards, p2_points, points, total_p2, pool, gtotal2, player1):  
    '''Player 2 turn'''
     
    print(p2_cards)
    global count #accessing the count variable that was assigned outside of this function, 'global' command used so it can be changed
                    #BIBLIOGRAPHY: VIII (Anon, 2012)
    
    count += 1 #adding 1 to the count each time player 2 goes to keep track of rounds
    if count == 8: #finishing the game when the number of rounds == 8 instead of 7, if count == 7 was used there would only be 6 rounds
            print('Game finished.')
            end_game(count, total_p1, total_p2, player1, player2, gtotal1, gtotal2) #changing to the end_game() function to finish the game
        
            

    #code the same as p1_turn() function        
    answer = ''
    length = int(input('Player 2: how many letters is your word?')) 
    if length == 0:
        print('Okay, we will move on, you will score 0 and gain 1 extra tile to help with your next go')
        print(count)
        p2_card1 = random.choice(pool)
        pool.remove(p2_card1)
        p2_cards.append(p2_card1)
        p1_turn(p1_cards, p1_points, points, total_p1, pool, gtotal1)
        
    
    
    for i in range(length):
            letter = input('Enter your letter: (Remember if you cannot go press 0) ')
            if letter == '0':
                    print('okay, we will move on and you score 0')
                    
            else:
                    P = points[letter]
                    p2_points.append(P)
                    answer += letter
            if letter not in p2_cards:
                    print('your letter is not valid, your turn will now be skipped.')
                    p1_turn(p1_cards, p1_points, points, total_p1, pool, gtotal1)
    
                
        
    if answer != '':
        if d.check(answer):
            print('Yay your word is valid!')
            ans_sum = sum(p2_points)
            total_p2 += ans_sum

            
            print('You can now click on the board where to place each letter')
            
            split_answer = list(answer)
            i = 0
            while i in range(len(split_answer)):
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            x2, y2 = pygame.mouse.get_pos()
                            font_22 = pygame.font.Font('freesansbold.ttf', 50)
                            text_22 = font_22.render(split_answer[i], True, BLACK, None)
                            textrect_22 = text_22.get_rect(center=((x2), y2))
                            DISPLAY.blit(text_22, textrect_22)
                            pygame.display.update()
                            i += 1
                            
                            if (x2, y2) in coord_double:
                                    total_p2 += (ans_sum * 2)
                            elif (x2, y2) in coord_triple:
                                    total_p2 += (ans_sum *3)
                            elif (x2, y2) in coord_four:
                                    total_p2 += (ans_sum * 4)
                            elif (x2, y2) in coord_five:
                                    total_p2 += (ans_sum * 5)
                            
                            if i in range(len(split_answer)):
                                print('Press your next square: ')
                            else:
                                print('Now we switch turns!')
                                
                                
                                
                                print('You scored: ', total_p2)
                                gtotal2.append(total_p2)
                        
                                total_p2 == 0
                                print('You used', length ,'tiles, so you will now be given', length ,'more')
                                

                                for i in range(length):
                                    p2_card1 = random.choice(pool)
                                    pool.remove(p2_card1)
                                    p2_cards.append(p2_card1)  

                                
                                for i in split_answer:
                                    p2_cards.remove(i)
                                    
                                   
                                print(p2_cards)
                                p2_points = [0]
                                p1_turn(p1_cards, p1_points, points, total_p1, pool, gtotal1)
                                

        else:
                print('Your word is not valid. You will now score 0.')
                

            
    
    p2_points = [0]
    p1_turn(p1_cards, p1_points, points, total_p1, pool, gtotal1)

    return answer, p2_cards, p2_points, total_p2, pool, length, gtotal2, count
    pygame.display.update()
    
   
#main function calling all other functions
def main():
        
    #setting title of pygame display window   
    pygame.display.set_caption('scrabble') 
    
    #defining varibales
    x, y = pygame.mouse.get_pos() 
    total_p1 = 0
    total_p2 = 0
    
    
    #calling the functions in the order they will be used 
    create_board()
    display_instructions()
    first_tiles()
    start()
    p1_turn(p1_cards, p1_points, points, total_p1, pool, gtotal1)
    p2_turn(p2_cards, p2_points, points, total_p2, pool, gtotal2, player1)
    end_game(count, total_p1, total_p2, player1, player2, gtotal1, gtotal2)


    while True: #lets the players quit the pygame window 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #function within pygame to quit window
                sys.exit() #exits program
            
main() #calls the main function, which contains all other functions
        #starts the program

