online_players = ["marc", "tom", "max", "seb"]

# access
print("---------------------------------------------")
print(online_players)
print("first", online_players[0])
print("last", online_players[len(online_players) - 1])

print("---------------------------------------------")
online_players[0] = "ali"
print(online_players)  # prints ['ali', 'tom', 'max', 'seb']

# insert an element in second position
print("---------------------------------------------")
online_players.insert(1, "ahmed")
print(online_players)  # prints ['ali', 'ahmed', 'tom', 'max', 'seb']

# insert two elements in third position
print("---------------------------------------------")
online_players[2:2] = ["mejdi", "helmi"]
print(online_players)  # prints ['ali', 'ahmed', 'mejdi', 'helmi', 'tom', 'max', 'seb']
# => insertion of ('mejdi', 'helmi') before 'tom'

# replace the third element by two elements (list size will increase by 1)
print("---------------------------------------------")
online_players[2:3] = ["bob", "marley"]
print(online_players)  # prints ['ali', 'ahmed', 'bob', 'marley', 'helmi', 'tom', 'max', 'seb']
# => 'mejdi' is replaced by ('bob', 'marley')

# append one element
print("---------------------------------------------")
online_players.append("crazy1")
print(online_players)  # ['ali', 'ahmed', 'bob', 'marley', 'helmi', 'tom', 'max', 'seb', 'crazy1']

# add two elements in the end
print("---------------------------------------------")
online_players.extend(["john", "jack"])
print(online_players)

print("---------------------------------------------")
del online_players[4]
print(online_players)  # ['ali', 'ahmed', 'bob', 'marley', 'tom', 'max', 'seb', 'crazy1', 'john', 'jack']
del online_players[4:6]
print(online_players)  # tom and max are gone
online_players.pop(1)
print(online_players)  # second element ('ahmed') is gone
online_players.remove("crazy1")
print(online_players)  # crazy1 is gone

print("---------------------------------------------")
del online_players[:]
print(online_players)  # list is emptied
online_players.extend(["john", "jack"])
online_players.clear()
print(online_players)  # list is empty again
