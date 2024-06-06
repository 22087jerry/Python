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
    print(f"ID         name                     studio_name")
    for studio in results:
        print(f"{studio[0]:<10}{studio[1]:<24}{studio[2]:<4}")
    db.close() 

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

def print_all_Genre():
    '''print all the Genre nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * from Genre;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID       genre:")
    for Genre in results:
        print(f"{Genre[0]:<10}{Genre[1]:<5}")
    db.close() 

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

def print_all_datas():
    '''print all the datas nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT  Game_ID, Release_date from Game order by Release_date desc;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all the results
    print(f"ID        Release_date")
    for games in results:
        print(f"{games[2]:<10}{games[4]:<8}")
    db.close() 







#main code
while True:
    user_input = input(
"""
What would you like to do. 
1. Print all game name. 
2. Print all game data. 
3. print all genre. 
4. print all genre according to alphabetical order A-Z.
5. print just the release date of the games
6. Exit. 
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
        break
    
    else:
        print("That was not an option\n")
