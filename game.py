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
    for studio in results:
        print(f"{studio[1]:<25}{studio[2]:<4}")
    db.close() 





#main code
print_all_game()
