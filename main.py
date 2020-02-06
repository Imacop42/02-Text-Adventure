import sys, os, json
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


game_file = 'document.json'
item_file = 'items.json'
inventory = []



def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)

def check_inventory(item):
    for i in inventory:
        if i == item:
            return True
        return False



def render(game,items,current):
    c = game[current]
    print("\n\n" + c["name"])
    print("\n\n "+ c["desc"])
  
    # Display any items
    for item in c["items"]:
        if not check_inventory(item["item"]):
            print(item["desc"])
    
    #display item information
    for i in inventory:
        if i in items:
            if current in items[i]["exits"]:
                print(items[i]["exits"][current])






def get_input():
    response = input("\nWhat would you like to do? ")
    response = response.upper().strip()
    return response



def update(game,items,current,response):
    #inventory check command
    if response == "INVENTORY":
        print("You are carrying: ")
        if len(inventory) == 0:
            print("Nothing")
        else:
            for i in inventory:
                print(i.lower())
        return current

    #movement command
    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]

    #pick up command
    for item in c["items"]:
        if response == "GET " + item["item"] and not check_inventory(item["item"]):
            print(item["take"])
            inventory.append(item["item"])
            return current
        if response == "PICK UP " + item["item"] and not check_inventory(item["item"]):
            print(item["take"])
            inventory.append(item["item"])
            return current
        if response == "TAKE " + item["item"] and not check_inventory(item["item"]):
            print(item["take"])
            inventory.append(item["item"])
            return current
    
    #actions for items
    for i in inventory:
        if i in items:
            for action in items[i]["actions"]:
                if response == action + " " + i:
                    print(items[i]["actions"][action])
                    return current       

    return current




# MAIN GAME FUNCTION
def main():
    current = 'FIELD'  #START
    end_game = ['END']  #ENDGAME AREAS

    (game,items) = load_files()




    while True:
        render(game,items,current)
        response = get_input()

        if response == "QUIT":
            break

        current = update(game,items,current,response)
    
    print("Thanks for playing!")
    


     













if __name__ == '__main__':
	main()