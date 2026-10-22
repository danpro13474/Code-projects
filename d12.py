# Gaming arcade

print("--------WELCOME TO THE TERMINAL GAMING ARCADE--------")



while True:

    name = input("Please enter your name or type ('quit') to exit: ")
    surname = input("Please enter you surname: ")
    
    if name == "quit":
        print("Goodbye and enjoy your day")
        break
    
    while name == "":
            print("You have not typed in anything," \
            "please ensure you have typed in your name")
            name = input("Please enter your name or type ('quit') to exit: ")
    while not name.isalpha():
            print("Your name cannot contain any symbols or numbers /n" \
            "please try again")
            name = input("Please enter your name or type ('quit') to exit: ")

    while surname == "":
         print("You have not typed in anything, \n" \
         "please ensure you have typed in your surname")
         surname = input("Please enter you surname: ") 
    while not surname.isalpha():
         print("Your surname cannot contain any symbols or numbers \n" \
         "please try again")
         surname = input("Please enter you surname: ")
             
              

    print()
    print(f"Hello and greetings {name}{surname}")
    print()
    try:
      age = int(input("Please enter your age: "))
    except ValueError:
        print("Age not valid, you have not typed in anything")
        age = int(input("Please enter your age: "))
    if age <= 6:
        print("You are too young to enter this arcade")
        break
    while age > 100:
         print("Invalid age")
         age = int(input("Please enter your age: "))
         print()
    choice = {
        "Virtual Reality": "16-24+ - 2 hours",
        "Retro Gaming": "5-16+ - 2 hours 30mins",
        "Racing Simulator": "5-18+ - 3 hours",
        "Bowling": "9-18+ - 1 hour 30mins"
        ""
    }

    details = [f"{name}, {age}"]
    print()
    print(details)
    print()
    print("Here is a list of games we have in our Arcade")
    print()
    print(choice)
    print()
    
    zone = input("Please select a choice: ")
    print()

    if zone == "Virtual Reality":
         print("Valid choice")
    elif zone == "Retro Gaming":
         print("Valid choice")
    elif  zone == "Racing Simulator":
         print("Valid choice")
    elif zone  == "Bowling":
         print("Valid choice")
    else:
         print("Invalid choice, please try again")
     
         
    print()
    confirm = int(input("Please confirm your age: "))
    print()

    if zone == "Virtual Reality" and confirm >= 16:
         hours = 2
         mins = 0
         print("You are eligible to participate in the Virtual Reality arcade")
    elif zone == "Retro Gaming" and confirm >= 5:
     hours = 2
     mins = 30
     print("You are eligible to participate in the Retro gaming arcade")
    elif zone == "Racing Simulator" and confirm >= 5:
          hours = 3
          mins = 0
          print("You are eligible to participate in the Racing Simulator")
    elif zone == "Bowling" and confirm >= 9:
          hours = 1
          mins = 30
          print("You are eligible to participate in the Bowling arcade")
    else:
          print("Sorry but you are too young to attend this type of arcade")
          input("Please select a different choice: ")
          print()
          confirm = int(input("Please confirm your age: "))
          print()
          

    print()
    pass1 = input("Please select a pass that you would like ('Standard or Vip'): ")
    print()

    Standard = 25
    Standard = float(Standard)

    Vip = 44
    Vip = float(Vip)

    if pass1 == "Standard" and age >= 16:
         print("You have a standard ticket and will pay a full price")
    elif pass1 == "Standard" and age < 10 and age >= 5:
         print("You have a standard ticket alongside a discount so you \n" \
         "will pay half the price")
         discount1 = Standard / 2   
    elif pass1 == "Vip" and age >= 16:
         print("You have a vip ticket and will pay a full price")
    elif pass1 == "Vip" and age < 10 and age >= 5:
         print("You have a vip ticket alongside a discount so you \n" \
         "will pay half the price")
         discount2 = Vip / 2
     
    print()
    price = float(input("Please tell me the price of the ticket: "))
    print()
    print("--------------CHECKPOINT--------------")
    print()
    def session():
         print(f"Your ticket: {name}, {surname}, {age}, {pass1}, £{price}, {zone}, {hours}hrs and {mins}mins")
    session()
    print()
    print("--------------CHECKPOINT--------------")
 

   