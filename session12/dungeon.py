player = {
    "x": 2,
    "y": 3,
 }

key = {
    "x": 0,
    "y": 1,
    "name": "K"
}
exit_door = {
    "x": 2,
    "y": 0,
}
bien = 0
new_x = 0
new_y = 0
while True:
    for y in range(4):
        for x in range(4):
            if player["x"] == x and player["y"] == y:
                print("P ", end="")
            elif key["x"] == x and key["y"] == y:
                print(key["name"], end=" ")
            elif exit_door["x"] == x and exit_door["y"] == y:
                print("E ", end="")
            else:
                print("- ", end="")
        print("")            

    move = input("Which way? (w, a, s, d): ")
    move.lower()

    if move == "w":
        player["y"] = player["y"]-1
    if move == "a":
        player["x"] = player["x"]-1
    if move == "s":
        player["y"] = player["y"]+1
    if move == "d":
        player["x"] = player["x"]+1    

    if player ["x"] == key["x"] and player["y"] == key["y"]:
        print("You have obtained the key")
        key["name"] = "-"
        bien = 1
    if player ["x"] == exit_door["x"] and player["y"] == exit_door["y"]:
        if bien == 0:
            print("You can't exit, please acquire the key(s) first")
            if move == "w":
                player["y"] = player["y"]+1
            if move == "a":
                player["x"] = player["x"]+1
            if move == "s":
                player["y"] = player["y"]-1
            if move == "d":
                player["x"] = player["x"]-1
        else: 
            print("Congrats, you’ve just escaped the dungeon")
            exit()


