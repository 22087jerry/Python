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
        print(f"{studio[1]:<25}{studio[2]:<4}")
    db.close() 





#main code
while True:
    user_input = input("\nWhat would you like to do. \n1. Print all game name\n2.Exit\nAwnser here: ")
    if user_input == "1":
        print_all_game()
    if user_input == "2":
        break
    else:
        print("That was not an option\n")
