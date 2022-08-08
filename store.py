import qrcode

def menu():
    global choice
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Search")
    print("5. List")
    print("6. QR")
    print("7. Shop")
    print("0. Exit")
    choice = input("Menu: ")

def list():
    print('\033[1;31m Code \tQT \t Name \t $')
    for i in range(len(products)):
        print('\033[0m', products[i]['id'], end='\t')
        print(products[i]['count'], end='\t')
        print(products[i]['name'], end='\t')
        print(products[i]['price'], end='\t \n')

def add():
    name = input("Name: ")
    price = input("$: ")
    count = int(input("QT: "))
    id = int(input("Code: "))
    if find(name) == -1:
        products.append({'id': id, 'name': name, 'price': price, 'count': count})
        print("SUCCEED")
    else:
        print("Already exist")

def edit():
    key = input("Name or Code:")
    i = find(key)
    if i != -1:
        name = input("New name ('-' for skip): ")
        if name != '-': products[i]['name'] = name
        count = input("New QT ('-' for skip): ")
        if count != '-': products[i]['count'] = int(count)
        price = input("New $ ('-' for skip): ")
        if price != '-': products[i]['price'] = float(price)
        print("SUCCEED")
    else:
        print("Not Found")

def delete():
    key = input("Name or Code:")
    i = find(key)
    if i != -1:
        while True:
            print("Are you sure you want to delete", products[i]['name'], "? (y/n)")
            temp = input()
            if temp in ['y', 'n']: break
        if temp == 'y':
            products.remove(products[i])
            print("SUCCEED")
    else:
        print("Not Found")

def search():
    key = input("Name or Code:")
    i = find(key)
    if i != -1:
        print('\033[1;31m Code \tQT \t Name \t $')
        print('\033[0m', products[i]['id'], end='\t')
        print(products[i]['count'], end='\t')
        print(products[i]['name'], end='\t')
        print(products[i]['price'], end='\t \n')
    else:
        print("Not Found")

def qr():
    key = input("Name or Code:")
    i = find(key)
    if i != -1:
        info = products[i]['id'] + ' ' + products[i]['name'] + ' $' + str(products[i]['price']) + ' x' \
               + str(products[i]['count'])
        print(info)
        img = qrcode.make(info)
        qrcode_name = products[i]['name'] + '.png'
        img.save(qrcode_name)
    else:
        print("Not Found")

def shop():
    final_price = 0
    basket = []
    while True:
        key = input("Product code ('-' to end): ")
        if key != '-':
            i = find(key)
            if i != -1:
                qt_shop = int(input("Quantity: "))
                if qt_shop > products[i]['count']:
                    print("Out of stock")
                else:
                    new_dict = {}
                    products[i]['count'] -= qt_shop
                    new_dict['name'] = products[i]['name']
                    new_dict['price'] = qt_shop * products[i]['price']
                    final_price += new_dict['price']
                    basket.append(new_dict)
            else:
                print("Not found")
        else:
            break
    for i in range(len(basket)):
        print(basket[i]['name'], '\t', basket[i]['price'])
    print(final_price)

def save_and_exit():
    new_file = open('database.txt', 'w')
    new_text = ''
    for i in range(len(products)):
        new_text += products[i]['id'] + ','
        new_text += products[i]['name'] + ','
        new_text += str(products[i]['price']) + ','
        new_text += str(products[i]['count'])
        if i < len(products)-1: new_text += '\n'
    new_data = new_file.write(new_text)
    exit()

def find(key):
    found = False
    for i in range(len(products)):
        if key in [products[i]['name'], products[i]['id']]:
            found = True
            break
    if found:
        return i
    else:
        return -1


file = open('database.txt', 'r')
data = file.read()
product_list = data.split('\n')
products = []

for i in range(len(product_list)):
    product_list_info = product_list[i].split(',')
    mydict = {'id': product_list_info[0], 'name': product_list_info[1], 'price': float(product_list_info[2]),
              'count': int(product_list_info[3])}
    products.append(mydict)

choice = 0
while True:
    menu()
    if choice == '1': add()
    if choice == '2': edit()
    if choice == '3': delete()
    if choice == '4': search()
    if choice == '5': list()
    if choice == '6': qr()
    if choice == '7': shop()
    if choice == '0': save_and_exit()
