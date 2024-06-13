#docstring- Jerry Xie- game_genere database application 
#imports
import sqlite3

#contants and varibales
DATABASE = "gamers.db"
users = {'Jerry': 'weka1111'}


#funactions
#login system


def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        
        if username in users and users[username] == password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again buddy.")

# Example usage
login()

#prints all game and studio
def print_all_game():
    '''print all the game nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from studio;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID        name                    studio_name")
    for studio in results:
        print(f"{studio[0]:<10}{studio[1]:<24}{studio[2]:<4}")
    db.close() 
    input('Press Enter to Continue ... ')
#Print all game data
def print_all_data():
    '''print all the data nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Game;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID        Player_ammount                Release_date")
    for game in results:
        print(f"{game[2]:<10}{game[3]:<30}{game[4]:<8}")
    db.close() 
    input('Press Enter to Continue ... ')
#Print all genre
def print_all_Genre():
    '''print all the Genre nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Genre;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID        genre:")
    for Genre in results:
        print(f"{Genre[0]:<10}{Genre[1]:<5}")
    db.close() 
    input('Press Enter to Continue ... ')
#print all genre from a-z
def print_all_Genres():
    '''print all the Genres nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Genre order by Name asc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID                  Genre:")
    for Genres in results:
     print(f"{Genres[0]:<20}{Genres[1]:<5}")
    db.close() 
    input('Press Enter to Continue ... ')
#print all data and order by release dates desc
def print_all_datas():
    '''print all the datas nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Game order by Release_date desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID          Player ammount        Release date")
    for games in results:
        print(f"{games[2]:<12}{games[3]:<22}{games[4]:<5}")
    db.close() 
    input('Press Enter to Continue ... ')
#print all game and studio order by name desc
def print_all_gamess():
    '''print all the gamess nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from studio order by name desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID         name                     studio_name")
    for studio in results:
        print(f"{studio[0]:<10}{studio[1]:<24}{studio[2]:<4}")
    db.close() 
    input('Press Enter to Continue ... ')

                     







#main code
while True:
    user_input = input(
"""
What would you like to do. 
1. Print all game and studio name. 
2. Print all game data. 
3. Print all genre. 
4. Print all genre according to alphabetical order A-Z.
5. Print all game data from 30-1 by release date.
6. Print all game and studio name order from Z-A.
7. All game description.
8. Exit. 
""")
    
    if user_input == "1":
        print_all_game()
    elif user_input == "2":
        print_all_data()
    elif user_input == "3":
        print_all_Genre()
    elif user_input == "4":
        print_all_Genres()
    elif user_input == "5":
        print_all_datas()
    elif user_input == "6":
        print_all_gamess()
    elif user_input == "7":
     input(
    """
    a. Valorant: an online multiplayer computer game, 
    produced by Riot Games. It is a first-person shooter game, 
    consisting of two teams of five, where one team attacks and the other defends. 
    Players control characters known as 'agents', who all have different abilities to use during gameplay.

    b. NBA 2K24: Packed with pure, authentic hoops action, 
    NBA 2K24 boasts a variety of single-player and multiplayer game modes for you to immerse yourself in. 
    Realize your NBA dreams in MyCAREER, assemble a dream team of your favorite players in MyTEAM, 
    put on your General Manager cap in MyNBA, and play as today's stars in Play Now.

    c. Cyberpunk 2077:  In Night City, 
    a mercenary known as V navigates a dystopian society in which the line between humanity and technology becomes blurred. 
    In 2077, America is in pieces. Megacorps control life in all its aspects from the top floors of their sky-high fortresses.
    
    d. Stardew Valley: open-ended, allowing players to grow crops, 
    raise livestock, fish, cook, mine, forage, and socialize with the townspeople, 
    including the ability to marry and have children. 
    It allows up to eight players to play online together. 
    Barone solely developed Stardew Valley for over four and a half years.

    e. Poppy playtime: A horror video game where the player controls a former employee of toy-making company named Playtime Co., 
    who returns to the company's abandoned toy factory after its staff mysteriously disappeared 10 years earlier.

    f. Tetris:  players complete lines by moving differently shaped pieces (tetrominoes), which descend onto the playing field. 
    The completed lines disappear and grant the player points, and the player can proceed to fill the vacated spaces.

    g. Minecraft: a game made up of blocks, creatures, and community. You can survive the night or build a 
    work of art – the choice is all yours. 
    But if the thought of exploring a vast new world all on your own feels overwhelming, then fear not!

    h. Roblox: an online game platform and game creation system developed by Roblox Corporation
      that allows users to program and play games created by themselves or other users.

    i. Spiderman 2: Peter Parker is beset with troubles in his failing personal life as he battles a 
    former brilliant scientist named Otto Octavius. 
    Peter Parker is beset with troubles in his failing personal life as he battles a former brilliant scientist named Otto Octavius.

    j. AdVenture Capitalist: The goal of the game is to manage a mock communist state and 
    become more powerful by buying different productions that produce resources. 
    Specifically, there are five industries that all act as a different currency: Potato, Land, Ore, Military, and Placebo.

    
    7. EXIT
    """)  
    
    
    elif user_input == "8":
            break
    else:
      print("That was not an option\n")


