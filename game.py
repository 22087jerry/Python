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
    print(f"name                          studio_name")
    for studio in results:
        print(f"{studio[1]:<25}{studio[2]:<4}")
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

def print_all_Genre():
    '''print all the game nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Genre;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"name")
    for Genre in results:
        print(f"{Genre[1]}")
    db.close() 





#main code
while True:
    user_input = input(
"""
What would you like to do. 
1. Print all game name. 
2. Print all game data. 
3. print all genre. 
4. Exit. 
""")
    if user_input == "1":
        print_all_game()
    elif user_input == "2":
        print_all_game_data()
    elif user_input == "3":
        print_all_Genre()
    elif user_input == "4":
        break
    
    else:
        print("That was not an option\n")
