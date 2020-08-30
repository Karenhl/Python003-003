file1 = open('a.txt', encoding='utf8')

try:
    data = file1.read()
    print(data)
finally:
    file1.close()


with open('a.txt', encoding='utf8') as f:
    data = f.read()
    print(data)