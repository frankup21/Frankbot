from tinydb import TinyDB, Query
from tinydb.operations import delete,increment
import random
db = TinyDB('rps_data.json')
Users = Query()
def rps(choice, user):
	rps = ["rock", "paper", "scissors"]
	emoji = ["\U0001F44A", "\U0001F91A", "\U0000270C"]
	num = random.randint(0, 2)

	result = ["We tie!", "You lose!", "You win!"]
	arrow = [" ", "->", "<-"]
	resultnum = (num - rps.index(choice)) % 3

    #create entry
	if db.contains(Users.id == user) is False:
		db.insert({"id": user, "record": [0, 0, 0]})

    #retrieve the player's record and update
	record = db.search(Users.id == user)[0]['record']
	record[resultnum] += 1
	db.update({"record": record}, Users.id == user)

    #build the message to return
	str = '''{} {} {} {}

	Your record: {} wins, {} losses, {} ties.
	'''.format(emoji[num], "\U0001F4A5", emoji[rps.index(choice)], result[resultnum], record[2], record[1], record[0])
	return str
