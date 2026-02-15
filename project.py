def expense_tracker():
    l = []
    def save():
        with open("exp_track.txt", "w") as f:
            for y in l:
                f.write(f"{y['category']}:{y['amount']}\n")

    def clean(c):
        new = {}
        for z in l:
            if z["category"] in new:
                new[z["category"]] += z["amount"]
            else:
                new[z["category"]] = z["amount"]
        if c == "4":
            print(new)
        elif c == "6":
            search = input("Enter category to be searched:")
            if search in new:
                print(f"Expense: {new[search]}")
            elif search not in new:
                print("PLease spend anything!")
            else:
                print("Category not found")

    def lists():
        t = 0
        L = 10**10
        i = ""
        o = -10**10
        p = ""
        for v in l:
            t+=v["amount"]
            if v["amount"] < L:
                L = v["amount"]
                i = v["category"]
            if v["amount"] > o:
                o = v["amount"]
                p = v["category"]
        if c == "3":
            print("Total expense")
            print(t)
        if c == "8":
            print(f"Total expenses: {t}")
            print(f"Number of entries: {len(l)}")
            print(f"Average expense: {t/len(l):.1f}")
            print(f"Lowest expense:")
            print(f"Category: {i}")
            print(f"Amount: {L}")
        if c == "7" or c == "8":
            print("Highest Expense:")
            print(f"Category: {p}")
            print(f"Expense: {o}")
    while True:
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Category Expense")
        print("5. Delete Expense")
        print("6. Search Category")
        print("7. Highest Expense")
        print("8. Statistics")
        print("9. Exit")
        c = input("Enter your choice:")

        if c == "1":
            amo = float(input("Enter amount:"))
            cat = input("Enter category:")
            d = {"amount":amo, "category":cat}
            l.append(d)
            save()
            print("Expense added successfully!")
        elif c == "2":
            print("All Expenses:")
            for x in l:
                print(x)
        elif c == "3":
            lists()
        elif c == "4":
            print("Spending by Category:")
            clean(c)
        elif c == "5":
            for x in range(len(l)):
                print(f"{x}-{l[x]}")
            delete = int(input("Enter index to delete:"))
            l.pop(delete)
            print("Expense deleted successfully!")
            save()
        elif c == "6":
            clean(c)
        elif c == "7":
            lists()
        elif c == "8":
            lists()
        elif c == "9":
            break
expense_tracker()