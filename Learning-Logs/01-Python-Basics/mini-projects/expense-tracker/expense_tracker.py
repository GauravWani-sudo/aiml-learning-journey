expenses = []

while True:
    print("1.add")
    print("2.view")
    print("3.total")
    print("4.exit")

    choice = input("enter choice: ")

    if choice == "1":
        name = input("expense name: ")
        amount = float(input("amount: "))

        expenses.append((name, amount))

    elif choice == "2":
        for expense in expenses:
            print(expense)

    elif choice == "3":
        total = sum(amount for name, amount in expenses)

        print(total)

    elif choice == "4":
        break