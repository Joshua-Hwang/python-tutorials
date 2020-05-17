import os
filename = input("Please input the database to load\n> ")
data = open(os.path.join(os.path.dirname(__file__), filename))