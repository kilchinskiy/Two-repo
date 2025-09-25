#Modul 4 Home work 4

def parse_input(user_input: str): #Парсер команд.
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def add_contact(args, contacts): #Додаємо контакти.
    if len(args) != 2:
        return "Invalid arguments. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts): #Зміна номеру теелефона.
    if len(args) != 2:
        return "Invalid arguments. Use: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts): #Видаає телефон за імьям.
    if len(args) != 1:
        return "Invalid arguments. Use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."


def show_all(contacts): #Виводимо контакти.
    if not contacts:
        return "No contacts saved."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!") #Витводимио на екран значення через команди.
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

#Перевірка.
if __name__ == "__main__":
    main()
#Передаємо команди у термінал.