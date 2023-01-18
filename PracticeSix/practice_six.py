def get_positive_int_from_console(text):
    while True:
        try:
            res = int(input(text))
            if res > -1:
                break
        except:
            print("only number")
    return res


def file_open():
    res = []
    with open("phonebook.txt", "r", encoding="utf8") as file:
        res = file.read().strip().split("\n")
    return res


def write_file(contacts):
    contacts = f"{','.join(contacts)}'\n'"
    with open("phonebook.txt", "a", encoding="utf8") as datafile:
        try:
            datafile.write(contacts)
            print("write success!")
        except:
            print("write error!!!")


def show_contact(contacts):
    list_contacts = contacts.split(",")
    template = f"""
First:{list_contacts[0]}
Last:{list_contacts[1]}
Middle:{list_contacts[2]}
Phone:{list_contacts[3]}"""
    print(template)


def show_all_contacts():
    file = file_open()
    for contact in file:
        show_contact(contact)


def search_contact():
    while True:
        search = input("""
Press Enter for search or input 1 for Exit 
Input for search: """)
        if search == "1":
            break
        res = []
        file = file_open()
        for data in file:
            res.append(data.strip("\n"))
        result = [item for item in res if search in item]
        for contact in result:
            show_contact(contact)


def add_contact():
    while True:
        input("""
For exit press Enter
Input V""")
        first_name = input("First Name: ")
        if "" in first_name:
            break
        last_name = input("Last Name: ")
        middle_name = input("Middle Name: ")
        phone_number = input("Phone number: ")
        contacts = [first_name, last_name, middle_name, phone_number]
        write_file(contacts)


def del_contact():
    pass


def change_number():
    pass


def selection():
    while True:
        print("""
1 - Show all contacts
2 - Search contact(s)
3 - Add contact
4 - Delete contact
5 - Change number

0 - Exit""")
        sel = get_positive_int_from_console("input:")
        if sel == 1:
            show_all_contacts()
        elif sel == 2:
            search_contact()
        elif sel == 3:
            add_contact()
        elif sel == 4:
            del_contact()
        elif sel == 5:
            change_number()
        elif sel == 0:
            break
        else:
            print("wrong number")


selection()
