# initialising variables and lists used
items = []
itemCount = 0
# defing a list of possible commands
possibleCommands = ["help", "add item", "delete item", "quit", "list items"]
# printing welcome message along with all possible commands
print("Welcome to the best Item Management System!")
print("Please entera command, possible commands:", possibleCommands)

# starting a while loop to iterate through commands
while True:
    # converting entered command to lower case
    command = input("Please enter command: ").lower()

    # checking if command is equal to "quit"
    if command == possibleCommands[3]:
        # Displaying "bye" message and closing program

        # ACTIVITY HERE
        # print goodbye message

        print("")
        exit()

    # checking if command is equal to "help"
    elif command == possibleCommands[0]:
        # printing all supported commands
        print("Possible Commands:", possibleCommands)
        print("")

    # checking if command is equal to "list items"
    elif command == possibleCommands[4]:
        # running sql query to retrive item list
        print("List of items (ItemID, Item Name, Item Price, Item Description):")
        print(*items, sep = "\n")

    # checking if command is equal to "add item"
    elif command == possibleCommands[1]:
        # taking new item name as input
        NewItemName = input("Please enter new item name: ")
        NewItemPrice = input("Please enter new item price: ")
        NewItemDescription = input("Please enter new item description: ")

        # ACTIVITY HERE
        # insert add item command here to append to items list (itemCount, NewItemName, NewItemPrice, NewItemDescription)


        itemCount += 1

        print("Updated list of items (ItemID, Item Name, Item Price, Item Description):")
        print(*items, sep = "\n")

    # checking if command is equal to "delete item"
    elif command == possibleCommands[2]:
        # running sql query to retrive item list to allow user to choose which item to delete
        print("List of items (ItemID, Item Name, Item Price, Item Description):")
        print(*items, sep = "\n")
        # taking item ID as input to delete item
        deleteItem = input("Please enter Item ID to delete: ")

        # ACTIVITY HERE
        # insert delete item command here to pop items from items list. remember to convert "deleteItem" to an integer


        for item in items:
            if item[0] != 0:
                item[0] = item[0] - 1
        # printing notification message
        print("Item number: " + deleteItem + " has been deleted!")
        print("")
        
    # If no valid commands are entered
    else:
        # Error message, for invalid command
        # printing all supported commands

        # ACTIVITY HERE
        # print error message here and all possible commands (use seperate print statements)
        
        print("")
