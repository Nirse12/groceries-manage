from Groceries import Groceries
import json, os, datetime, ast



def add_item(groc, item, amount):
    for k in groc.items.keys():
        if item in k:
            groc.items[item] = int(groc.items[item]) + amount
            groc.total_price += groc.getPrice(amount)
            return
    groc.addItem(item, amount)


def remove_item(groc, item, amount=0):
    for k in groc.items.keys():
        if item in k:
            if not amount:
                groc.items.pop(item)
                return
            else:
                groc.items[item] = int(groc.items[item]) - amount
                groc.total_price -= groc.getPrice(amount)
                return
    print("Item does not exist")


def getTrace():
    jsond = list()
    if os.path.getsize("trace.log"):
        with open ("trace.log") as log:
            jsond = json.load(log)

    return jsond


def deleteData():
    return list()


def updateGrocList(groc, new_data):
    groc.items           = new_data['items']
    groc.itemPrice       = new_data['itemPrice']
    groc.amount          = new_data['amount']
    groc.total_price     = new_data['total_price']
    groc.time            = new_data['time']


def loadOldList(groc, exist_json):
    if not len(exist_json):
        return 
    print ("Choose by date:\n")
    for i, g in enumerate(exist_json):
        print("{}: {}\n".format(i, g['time']))
    sel = int(input ("\n"))
    print(json.dumps(exist_json[sel], indent=4))
    curr_data = ast.literal_eval(json.dumps(exist_json[sel]))
    updateGrocList(groc, curr_data)


def main():
    final_list = dict()
    delete = False
    g1 = Groceries()
    exist_json = getTrace()
    choise = input("\n1. Create a new list\
        \n2. Load an existing list\n")
    if choise == "2" and len(exist_json):
        loadOldList(g1, exist_json)
        
    while True:
        g1.time = str(datetime.datetime.now())
        curr_data = (ast.literal_eval(json.dumps(g1.__dict__)))
        choise  = input("1. Add product\n2. Remove product\nPress enter to save the list\n")
        if not choise: 
            final_list['items']       = curr_data['items']
            final_list['total_price'] = curr_data['total_price']
            with open ("trace.log", "w") as log:
                json.dump(exist_json, log, indent=4, sort_keys=True)
            with open ("list.txt", "w") as log:
                json.dump(final_list, log, indent=4, sort_keys=True)
            break 

        item = input("Enter product name\n")
        amount = int(input("How many pieces?\n"))

        if choise == "1":
            add_item(g1, item, amount)

        if choise == "2":
            remove_item(g1, item, amount)

        exist_json.append(ast.literal_eval(json.dumps(g1.__dict__)))
        if delete:
            exist_json = deleteData()
        print(json.dumps(ast.literal_eval(json.dumps(g1.__dict__['items'])), indent=4))
        print("Total price is {}".format(json.dumps(ast.literal_eval(json.dumps(g1.__dict__['total_price'])), indent=4)))

if __name__ == main():
    main()