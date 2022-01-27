import json


def add(book: list[dict]) -> list[dict]:
    name: str = input('Enter name')
    surname: str = input('Enter surname')
    number: str = input('Enter number')
    city: str = input('Enter city')
    new: dict = {
        'name': name,
        'number': number,
        'surname': surname,
        'city': city
    }
    book.append(new)
    with open('js_file.json', 'w') as file:
        json.dump(book, file, indent=4)
    return book


def renew(book: list[dict]) -> list[dict]:
    name: str = input('Enter new name')
    surname: str = input('Enter new surname')
    number: str = input('Enter new number')
    city: str = input('Enter new city')
    new: dict = {
        'name': name,
        'number': number,
        'surname': surname,
        'city': city
    }
    book.append(new)
    with open('js_file.json', 'w') as file:
        json.dump(book, file, indent=4)
    return book


def search(book: list[dict]) -> None:
    ent: str = input('What is search?:[N]ame,[S]urname,[P]hone number,[C]ity,[E]xit').lower()
    if ent == 'n':
        name: str = input('Enter name').capitalize()
        for contakt in book:
            if contakt['name'] == name:
                print(contakt)
                option: str = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 's':
        surname: str = input('Enter surname').capitalize()
        for contakt in book:
            if contakt['surname'] == surname:
                print(contakt)
                option = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 'p':
        number: str = input('Enter number')
        for contakt in book:
            if contakt['number'] == number:
                print(contakt)
                option = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 'c':
        city: str = input('Enter city').capitalize()
        for contakt in book:
            if contakt['city'] == city:
                print(contakt)
                option = input('Enter option: [R]enew, [D]elete,[E]xit').lower()
                if option == 'r':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    renew(book)
                if option == 'e':
                    break
                if option == 'd':
                    del contakt
                    with open('js_file.json', 'w') as js_file:
                        json.dump(book, js_file, indent=4)
                    with open('js_file.json', 'r') as js_file:
                        json.load(js_file)
                        print(js_file)
    elif ent == 'e':
        exit()


if __name__ == '__main__':

    book: list[dict] = [{'name': 'Ivan', 'surname': 'Prokopenko', 'number': '+6475896743', 'city': 'Kyiv'}]
    with open('js_file.json', 'w') as file:
        json.dump(book, file, indent=4)
    while True:
        option: str = input('Enter option: [A]dd;[S]earch;[Q]uit ').lower()
        if option == 'a':
            add(book)
            with open('js_file.json', 'r') as file:
                a = json.load(file)
                print(a)
        elif option == 's':
            search(book)
        elif option == 'q':
            exit()
