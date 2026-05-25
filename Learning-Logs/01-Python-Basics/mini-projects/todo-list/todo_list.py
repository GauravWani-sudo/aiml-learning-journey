tasks = []

while True:
    print("1.add task")
    print("2.view tasks")
    print("3.remove task")
    print("4.exit")

    choice = input("enter choice: ")

    if choice == "1":
        task = input("enter task: ")

        tasks.append(task)

    elif choice == "2":
        for task in tasks:
            print(task)

    elif choice == "3":
        task = input("enter task to remove: ")

        if task in tasks:
            tasks.remove(task)

    elif choice == "4":
        break