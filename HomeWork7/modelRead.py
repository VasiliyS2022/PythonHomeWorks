def ViewColumn():
    with open('1.txt', 'r') as file:
        print(*file)

def ViewRow():
    with open('2.txt', 'r') as file:
        print(*file)