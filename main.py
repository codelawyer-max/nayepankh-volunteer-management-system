import csv
import os

volunteers = []

# Load existing volunteers from CSV
def load_volunteers():
    global volunteers

    if os.path.exists("volunteers.csv"):

        with open("volunteers.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 5:
                    volunteer = {
                        "name": row[0],
                        "email": row[1],
                        "phone": row[2],
                        "city": row[3],
                        "domain": row[4]
                    }

                    volunteers.append(volunteer)


# Add Volunteer
def add_volunteer():

    print("\n===== Add Volunteer =====")

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone Number: ")
    city = input("Enter City: ")
    domain = input("Enter Interested Domain: ")

    volunteer = {
        "name": name,
        "email": email,
        "phone": phone,
        "city": city,
        "domain": domain
    }

    volunteers.append(volunteer)

    with open("volunteers.csv", "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            email,
            phone,
            city,
            domain
        ])

    print("\nVolunteer Added Successfully!")


# View Volunteers
def view_volunteers():

    print("\n===== Volunteer List =====")

    if len(volunteers) == 0:
        print("No Volunteers Found")
        return

    for i, volunteer in enumerate(volunteers, start=1):

        print("\n-------------------------")
        print("Volunteer", i)
        print("Name:", volunteer["name"])
        print("Email:", volunteer["email"])
        print("Phone:", volunteer["phone"])
        print("City:", volunteer["city"])
        print("Domain:", volunteer["domain"])


# Search Volunteer
def search_volunteer():

    search_name = input("\nEnter Volunteer Name: ")

    found = False

    for volunteer in volunteers:

        if volunteer["name"].lower() == search_name.lower():

            print("\nVolunteer Found")
            print("------------------")
            print("Name:", volunteer["name"])
            print("Email:", volunteer["email"])
            print("Phone:", volunteer["phone"])
            print("City:", volunteer["city"])
            print("Domain:", volunteer["domain"])

            found = True

    if not found:
        print("Volunteer Not Found")


# Generate Report
def generate_report():

    print("\n===== Volunteer Report =====")

    total = len(volunteers)

    print("Total Volunteers:", total)

    domain_count = {}

    for volunteer in volunteers:

        domain = volunteer["domain"]

        if domain in domain_count:
            domain_count[domain] += 1
        else:
            domain_count[domain] = 1

    print("\nVolunteers By Domain")

    for domain, count in domain_count.items():
        print(domain, ":", count)


# Main Program
load_volunteers()

while True:

    print("\n")
    print("====================================")
    print(" NayePankh Volunteer Management System ")
    print("====================================")
    print("1. Add Volunteer")
    print("2. View Volunteers")
    print("3. Search Volunteer")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("\nEnter Choice: ")

    if choice == "1":
        add_volunteer()

    elif choice == "2":
        view_volunteers()

    elif choice == "3":
        search_volunteer()

    elif choice == "4":
        generate_report()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice. Please Try Again.")