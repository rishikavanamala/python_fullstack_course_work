data={0:{"product":"Rice","price":60},
          1:{"product":"Wheat Flour","price":45},
          2:{"product":"Sugar","price":40},
          3:{"product":"Milk","price":25},
          4:{"product":"Eggs (12 pcs)","price":70},
          5:{"product":"Cooking oil","price":130},
          6:{"product":"Tea powder","price":90},
          7:{"product":"Salt","price":20},
          8:{"product":"bread","price":30},
          9:{"product":"Soap","price":25}}
print("Index".ljust(7,' '),"Product".ljust(20,' '),"Price".ljust(10,' '))
for i in data:
    print(str(i).ljust(7,' '),data[i]['product'].ljust(20,' '),str(data[i]['price']).ljust(10,' '))
indexes=list(map(int,input("Enter the indexes: ").split()))
print("Bil1".center(30,'-'))
total_bill=0
for i in indexes:
    print(f'{data[i]["product"]}-${data[i]["price"]}')
    total_bill+=data[i]["price"]
    print(f"Your Bill:{total_bill}")
             