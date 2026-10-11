# Gym membership and booking system

while True:

    name = input("Enter your fullname (or type 'quit' to exit): ").strip()

    if name.lower() == 'quit':
            print("Goodbye and enjoy your day")
            break 


    while not name.replace(" ", "").isalpha() or len(name) == 0:
        print("You have typed in an invalid fullname.\n please ensure you have typed in your fullname in the correct format")
        name = input("Enter your fullname (or type 'quit' to exit): ").strip()

  
    cap_name = name.capitalize()

    print(f"Hello {cap_name} and welcome \n")
 
    try: 
       age = int(input("Enter your age "))
    except ValueError:
         print("Invalid age entered: ")
         age = 0
    if age >= 16 and age <= 22:
          print("You will recieve a discount for any of our memberships")
    elif age <= 0 or age <= 15:
         print("Sorry but you are too young to sign up for this programe.")
         break
    elif age >= 70 or age >= 100:
         print("You are too old to sign up for this programe.")
         break
    
    
    
    
    print()

    try:
        membership = int(input("How many guest passes or personal training sessions \n" \
                                "do you wish to add to this programe: "))
    except ValueError:
        print("Invalid number enterd. Please try again")
        int(input("How many guest passes or personal training sessions \n" \
                                "do you wish to add to this programe: "))
        membership = 0
    while membership > 7 or membership <= 0:
         print("This is an invalid amount  \n " \
               "please ensure you have maximum 5. ")
         int(input("How many guest passes or personal training sessions \n" \
                                "do you wish to add to this programe: "))
    if  membership > 0 and membership <= 5:
         print("Valid amount")

    standard = 34.64 
    standard = float(standard)
    monthly = standard / 3
    discount = monthly / 2

    vip = 65.91 
    vip = float(vip)
    monthly1 = vip / 3
    discount1 = monthly1 / 2
    

    options = input("Choose between two membership tiers - standard or vip : ").strip()

    if options == "standard" and age <= 70 and age >= 23:
         print("You have chosen the standard membership. \n" \
               "So your monthly price for this will be 11.55 per month." \
               "By the end of the 3 months you will have to renew your membership.")
    elif options == "vip" and age <= 70 and age >= 23:
         print("You have chosen the vip membership. \n" \
              "So your monthly price for this will be 21.97 per month.\n" \
              "By the end of the 3 months you will have to renew your membership.")
    elif options == "standard" and age >= 15 and age <= 22:
         print("You have chosen the standard option, \n" \
         "therefore you have recieved a discount so you will \n" \
         "pay 5.77 per month for 3 months and at the end of the 3 months\n" \
         "you will have to renew your membership")
    elif options == "vip" and age >= 15 and age <= 22:
         print("You have chosen the vip option, \n" \
         "therefore you have recieved a discount so you will \n" \
         "pay 10.98 per month for 3 months and at the end of the 3 months\n" \
         "you will have to renew your membership")

    print("=" * 40)
    print("Gym membership summary")
    print("=" * 40)

    print(f"Name - {cap_name}")
    print()
    print(f"Age - {age}")
    print()
    print(f"Membership - {options}")
    print()
    if options == "standard" and age >= 15 and age <= 22:
         print(f"price - £{round(discount, 2)}")
    elif options == "vip" and age >= 15 and age <= 22:
         print(f"price - £{round(discount1, 2)}")
    elif options == "standard" and age <= 70 and age >= 23:
         print(f"price - £{round(monthly, 2)}")
    elif options == "vip" and age <= 70 and age >= 23:
         print(f"price - £{round(monthly1, 2)}")
    print()
    print(f"personal training sessions - {membership}")



     

