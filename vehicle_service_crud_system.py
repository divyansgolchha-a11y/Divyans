# Simple Vehicle Service System

customers = []
mechanics = []
repair_requests = []

while True:
    print("\n Garage Management System ")
    print("1 - Customers")
    print("2 - Mechanics")
    print("3 - Repair Requests")
    print("4 - Exit")
    
    choice = input("Enter your choice: ")

    # for CUSTOMER SECTION:-
    if choice == "1":
        print("\na - Add Customer")
        print("b - View Customers")
        print("c - Edit Customer")
        print("d - Delete Customer")
        option = input("Choose an option: ")

        if option == "a":
            name = input("Customer Name: ")
            email = input("Customer Email: ")
            phone = input("Customer Phone: ")
            customers.append([len(customers) + 1, name, email, phone])
            print(" Customer Added Successfully")

        elif option == "b":
            print("\n Customer List ")
            for c in customers:
                print(f"ID: {c[0]} | Name: {c[1]} | Email: {c[2]} | Phone: {c[3]}")

        elif option == "c":
            print("\n Select Customer to Edit ")
            for c in customers:
                print(c[0], c[1])
            cid = int(input("Enter Customer ID: "))

            for c in customers:
                if c[0] == cid:
                    c[1] = input("New Name: ")
                    c[2] = input("New Email: ")
                    c[3] = input("New Phone: ")
                    print(" Customer Updated")
                    break

        elif option == "d":
            print("\n Select Customer to Delete ")
            for c in customers:
                print(c[0], c[1])
            cid = int(input("Enter Customer ID: "))

            for i in range(len(customers)):
                if customers[i][0] == cid:
                    customers.pop(i)
                    print(" Customer Deleted")
                    break

    # for MECHANIC SECTION:-
    elif choice == "2":
        print("\na - Add Mechanic")
        print("b - View Mechanics")
        print("c - Edit Mechanic")
        print("d - Delete Mechanic")
        option = input("Choose an option: ")

        if option == "a":
            name = input("Mechanic Name: ")
            skill = input("Mechanic Skill: ")
            phone = input("Mechanic Phone: ")
            mechanics.append([len(mechanics) + 1, name, skill, phone])
            print(" Mechanic Added Successfully")

        elif option == "b":
            print("\n Mechanic List ")
            for m in mechanics:
                print(f"ID: {m[0]} | Name: {m[1]} | Skill: {m[2]} | Phone: {m[3]}")

        elif option == "c":
            print("\n Select Mechanic to Edit ")
            for m in mechanics:
                print(m[0], m[1])
            mid = int(input("Enter Mechanic ID: "))

            for m in mechanics:
                if m[0] == mid:
                    m[1] = input("New Name: ")
                    m[2] = input("New Skill: ")
                    m[3] = input("New Phone: ")
                    print(" Mechanic Updated")
                    break

        elif option == "d":
            print("\n Select Mechanic to Delete ")
            for m in mechanics:
                print(m[0], m[1])
            mid = int(input("Enter Mechanic ID: "))

            for i in range(len(mechanics)):
                if mechanics[i][0] == mid:
                    mechanics.pop(i)
                    print(" Mechanic Deleted")
                    break

    # for REQUEST SECTION 
    elif choice == "3":
        print("\na - Add Repair Request")
        print("b - View Requests")
        print("c - Update Request Status")
        print("d - Delete Request")
        option = input("Choose an option: ")

        if option == "a":
            print("\nSelect Customer:")
            for c in customers:
                print(c[0], c[1])
            cid = int(input("Customer ID: "))

            car_model = input("Car Model: ")
            plate = input("Car Number Plate: ")
            work = input("Work Needed: ")

            repair_requests.append([
                len(repair_requests) + 1,
                cid,
                car_model,
                plate,
                work,
                "Pending",
                None
            ])
            print(" Repair Request Added")

        elif option == "b":
            print("\n Repair Requests ")
            for r in repair_requests:
                print(f"Request ID: {r[0]} | Car: {r[2]} | Status: {r[5]} | Mechanic Assigned: {r[6]}")

        elif option == "c":
            print("\nSelect Request to Update ")
            for r in repair_requests:
                print(r[0], r[2], r[5])
            rid = int(input("Request ID: "))

            for r in repair_requests:
                if r[0] == rid:
                    r[5] = input("New Status (Pending/Working/Done): ")
                    print("Select Mechanic:")
                    for m in mechanics:
                        print(m[0], m[1])
                    mid = input("Mechanic ID (optional): ")

                    if mid:
                        r[6] = int(mid)

                    print(" Request Updated")
                    break

        elif option == "d":
            print("\n Select Request to Delete ")
            for r in repair_requests:
                print(r[0], r[2])
            rid = int(input("Request ID: "))

            for i in range(len(repair_requests)):
                if repair_requests[i][0] == rid:
                    repair_requests.pop(i)
                    print("Request Deleted")
                    break

    elif choice == "4":
        print("Exiting Have a great day")
        break

    else:
        print("Invalid Choice Try Again.")
