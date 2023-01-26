def ViewColumn():
    with open('1.txt', 'r', encoding='utf-8') as file:
        print(*file)

def ViewRow():
    with open('2.txt', 'r', encoding='utf-8') as file:
        print(*file)