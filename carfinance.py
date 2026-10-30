# Car buying and Financing decision Terminal

# A dictionary of Cars that a user can look at
car_inventory = {
    "BMW-M3": "86,357",
    "Mercedes-CLA": "37,894",
    "Audi-A5": "53,063",
    "PoleStar-4": "44,395",
    "Volkswagen-golf": "30,646"
}
# Using a while loop so that a lot of users can be able to proceed in the program
while True:
    # Ask the user for their name, .strip() is used to remove any gaps
    name = input("Enter your name: ").strip()
    surname = input("Enter your surname or type ('quit') to exit: ").strip()
    
    while name and surname == "" or not name.isalpha() and not surname.isalpha():
        print("Invalid name and surname, please enter a valid name and surname")
        name = input("Enter your name: ").strip()
        surname = input("Enter your surname: ").strip()
    if surname == "quit".lower():
       print("Goodbye and have good day")
       break

    try:
      age = int(input("Enter your age: "))
      if age < 18 or age > 89:
         print("Sorry but you must be between the ages of 18 to 89 in order to get a car/drive")
         break
         exit()
      else:
         print("Valid age")
    except ValueError:
       print("Invalid age, please enter a valid age")
       continue
    print()
    print(f"Hello {name}-{surname}, Hope you are doing well.")
    print()
    print("If you want to proceed in buying a car from the list we have \n" \
    "we may need to see you license")

    driver_license = True
    
    confirm = input("Do you have a drivers licences ('Yes' or 'No'): ")

    while confirm == "":
        print("Invalid answer, please select yes or no")
        confirm = input("Do you have a drivers licences ('Yes' or 'No'): ")
    if confirm == 'Yes':
       print(f"Ok {name}, you are sorted we can proceed")
    elif confirm == 'No':
       print(f"Unfortunatley without a driver licences {name} we cannot proceed with talks.")
       break
    print()
    print("------Car List------")
    print()
    print("So here is our list of cars we have in display")
    print(car_inventory)
    print()
    print("Before we proceed I will need to ask if you would like to pay monthly or pay the upfront and your budget, so that we \n" \
    "can find the right car for you")

    payChoice = input("Please select either ('Monthly' or 'Upfront'): ").strip()

    while payChoice == "" and payChoice not in ["Monthly", "Upfront"]:
        print("You have not selected a valid pay choice, please select either 'Monthly' or 'Upfront'.")
        payChoice = input("Please select either ('Monthly' or 'Upfront'): ").strip()
        print("Valid Choice")
    if payChoice == "Monthly":
        print("You will be asked for your budget")
        while True:
            try:
                budget_cost = int(input("Please tell me what your budget is: "))
                if budget_cost < 2500:
                    print("Sorry but for the cars we have here this budget is too low \n"
                          "come back next time if you have a greater budget.")
                    break
                elif budget_cost > 10000:
                    print("I would likely recommend the upfront cost were you can buy the car without paying monthly for it\n" \
                    "but if you dont want to then it is okay")
                    break
                elif budget_cost >= 2500:
                    print("That budget is sensible, therefore we can proceed with \n"
                          "talks")
                    break
            except ValueError:
                print("Invalid budget amount, please type in a value.")
                continue

    elif payChoice == "Upfront":
        print("You will pay for the car in full cost")
        while True:
            try:
                upfront_cost = int(input("Please tell me what your budget is for the upfront cost: "))
                if upfront_cost < 30646:
                    print("Sorry but this budget for the upfront cost is too \n"
                          "low for the cars we have, better luck next time")
                    break
                elif upfront_cost >= 30646:
                    print("That is a valid upfront cost therefore we can proceed \n"
                          "with talks.")
                    break
            except ValueError:
                print("Invalid budget amount, please type in a value.")
                continue

    print(f"Ok {name}, your {payChoice} plan has been confirmed, now you can view the cars we have") 
    print()
    print("Here is the list of cars we have:")
    print()

    for car in car_inventory.items():
        print(car)
    print()
    print(f"With you {payChoice} plan please select a car that will suit your plan")

    selection = input("Select a car choice from the list: ")

    car_list = ["BMW-M3", "Mercedes-CLA", "Audi-A5", "Polestar-4", "Volkswagen-Golf"]


    while selection not in car_list and selection == "":
        print("That is not a valid car type, please select a car from the list")
        selection = input("Select a car choice from the list: ")
    if payChoice == "Monthly" and budget_cost >= 2553 and budget_cost <= 3157:
        print(f"For your {payChoice} plan, you can be able to buy the mercedes-CLA or the Volkswagen-golf and not the {selection} unfortunately")
    elif payChoice == "Monthly" and budget_cost > 10000:
        print(f"For your {payChoice} plan, you can buy any car you want so your {selection} is accepted")
    elif payChoice == "Upfront" and upfront_cost >= 30646:
        print(f"For your {payChoice} plan, you can be able to buy any car you want, so the {selection} is suitable for you.")

    try: 
     if payChoice == "Monthly":
      print(f"Ok now your {selection} is now sorted, we just have to discuss how many years you would like to buy the car")
      years = int(input("Please select a number up to 6 on how long you would like to have the car: "))
      while years > 6:
        print("The years has to be less than or equal to 6, please select a number from 1-6")
        years = int(input("Please select a number up to 6 on how long you would like to have the car: "))
    except ValueError:
        print("Invalid value, please insert a valid value")
    else:
        print("Valid amount, your car is now sorted")

    if payChoice == "Upfront":
        print(f"As you will be purchasing the {selection} you will get to keep it for as long as you like.")

    # Assuming 'selection' holds the car name and 'car_inventory' is your dictionary
    raw_price = car_inventory[selection]
    clean_price = float(raw_price.replace(",", ""))

    if payChoice == "Upfront":
      print()
      print("=" * 40)
      print("CAR SUMMARY")
      print("=" * 40)
      print()
      print(f"{name}-{surname}, {age}")
      print()
      print(f"Has drivers license - {confirm}")
      print()
      print(f"Pay choice - {payChoice}")
      print()
      print(f"Car-Choice: {selection}")
      print()
      print(f"Upfront Price: £{clean_price:,.2f}")
    elif payChoice == "Monthly":
  # Assuming 'years' is the variable where you stored their chosen loan length
      total_months = years * 12
      monthly_price = clean_price / total_months
      print()
      print("=" * 40)
      print("CAR SUMMARY")
      print("=" * 40)
      print()
      print(f"{name}-{surname}, {age}")
      print()
      print(f"Has drivers license - {confirm}")
      print()
      print(f"Pay choice - {payChoice}")
      print()
      print(f"Car-Choice: {selection}")
      print()
      print(
      f"Monthly Payment: £{monthly_price:,.2f} per month for {years}"
      " year(s)"
  )
