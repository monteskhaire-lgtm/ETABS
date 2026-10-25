print("============================================================")
print("")
print("====================HELLO USER!=============================")
print("==================WELCOME TO ETABS!!!=======================")
print("")
print("============================================================")
print("")
print("")

print("KAILANGAN MO NA MAGTIPID,BOOYYYYY! MAG PAPASKO NA")
answer = input("Do you want to continue? (Press 1 if yes): ")
if answer == "1":
    print("============================================================")
    print("==================Welcome user==============================")
    print("============================================================")
    while True:
        c_user= input("Create username: ")
        if c_user == "":
            print("Username can't be empty!")
            continue
        break
    while True:
        c_pass= input("Create password: ")
        if c_pass == "":
            print("Password can't be empty!")
            continue
        break
    print(" You're all set!")



    chance= 3
    print("============================================================")
    while chance >0:
        usern= input("Enter your username: ")
        passw= input("Enter your password: ")
        if usern == c_user and passw ==c_pass:
            print("successful!!")
            print("")


            print("Note that you need to 7x your allowance if you receive it daily and /4 if monthly")
            print("=================================================================================")
            while True:
                while True:
                    try:
                        allowance =int(input("How much allowance do you receive WEEKLY: "))
                    except ValueError:
                        print("Numbers only!")
                        continue
                    if allowance <= 0:
                        print("Allowance must be greater than 0!")
                        continue
                    break

                while True:
                    try:
                        transpo = int(input("Enter how much you spend on transpo?: "))
                    except ValueError:
                        print("Numbers only!")
                        continue
                    if transpo < 0:
                        print("Transpo can't be negative!")
                        continue
                    break

                while True:
                    try:
                        savings= int(input("Enter how much do you wish to save: "))
                    except ValueError:
                        print("Numbers only!")
                        continue
                    if savings < 0:
                        print("Savings can't be negative!")
                        continue
                    break

                remaining= allowance - transpo - savings
                if remaining <= 0:
                    print("ubos na puuu! Sobra ang transpo at savings sa allowance. Againnnn.")
                    print("================================================================")
                    continue
                break

            print("you still have: ", remaining)
            print("================================================================")

            total_spent = 0
            all_expenses = []
            days_left = 7

            while days_left > 0:
                daily_amount = remaining / days_left
                print("Day", 8 - days_left, "- Today's amount:", round(daily_amount, 2))
                print("================================================================")


                day_remaining = daily_amount
                expenses = []

                while True:
                    choice = input("Type 'begin' to start spending, or 'done' if finished for today: ")
                    print("================================================================")

                    if choice == "done":
                        break

                    elif choice == "begin":
                        while True:
                            item = input("Enter the item or expense (or type 'done' to stop): ")

                            if item == "done":
                                break

                            if item == "":
                                print("Item name can't be empty!")
                                continue

                            while True:
                                try:
                                    amount = float(input("Enter the price: "))
                                except ValueError:
                                    print("Numbers only!")
                                    continue
                                if amount <= 0:
                                    print("Price must be greater than 0!")
                                    continue
                                break
                            print("================================================================")

                            if round(amount, 2) > round(day_remaining, 2):
                                print("Not enough budget for today!")
                                print("================================================================")
                                continue

                            expenses.append([item, amount])
                            all_expenses.append([8 - days_left, item, amount])
                            day_remaining =day_remaining- amount
                            if day_remaining < 0:
                                day_remaining = 0
                            print("You have", round(day_remaining, 2), "left for today")

                            if round(day_remaining, 2) == 0:
                                print("You've used up today's budget!")
                                break
                        break

                    else:
                        print("Type 'begin' or 'done' only!")
                        print("================================================================")

                spent_today = daily_amount - day_remaining
                total_spent = total_spent + spent_today
                remaining = remaining - spent_today
                days_left =days_left- 1
                print("Overall remaining for the week:", round(remaining, 2))
                print("================================================================")

            print("Week finished!")
            print("================================================================")
            print("Your expenses this week:")
            for day, name, price in all_expenses:
                print("Day", day, "-", name, ":", price)
            print("================================================================")
            print("Total spent this week:", round(total_spent, 2))
            if remaining > 0:
                print("You saved", round(remaining + savings, 2))
            else:
                print("You saved", savings)
            break


        else:
            print("Wrong Password or Username")
            chance = chance -1
            print("chance left: ", chance)

    if chance ==0:
        print("account locked")

else:
    print("=" * 60)
    print("Comeback pag kailangan mo nako. Ganyan ka naman eh")





height= 10
for i in range(1, 11):
    spaces= " " *  (height - i )
    stars = "*" * (2 * i-1)
    print(spaces + stars)
print("       |   |     ")
print(" ")
print("MERRY XMAS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("=" * 60)