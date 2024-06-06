#docstring- Jerry Xie- game_genere database application 
#imports
import sqlite3

#contants and varibales
DATABASE = "gamers.db"


#funactions
def print_all_game():
    '''print all the game nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from studio;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name                 studio_name")
    for studio in results:
        print(f"{studio[1]:<20}{studio[2]:<4}")
    db.close() 

def print_all_game_data():
    '''print all the game nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Game;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"Player_ammount                Release_date")
    for game in results:
        print(f"{game[3]:<30}{game[4]:<8}")
    db.close() 

def print_all_game_genre():
    '''print all the game nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Game Genre;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name")
    for Game_Genre in results:
        print(f"{Game_Genre[]}")
    db.close() 





#main code
while True:
    user_input = input("\nWhat would you like to do. \n1. Print all game name. \n2. Print all game data. \n3. print all genre. \n4.Exit. \nAwnser here: ")
    if user_input == "1":
        print_all_game()
    elif user_input == "2":
        print_all_game_data()
    elif user_input == "3":
        print_all_game_genre()
    elif user_input == "4":
        break
    
    else:
        print("That was not an option\n")
