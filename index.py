age = input("Write your age: ")
money = input("How many cash you have: ")

if int(age) >= 18 and int(money) >= 13:
    print("You can buy beer.")
else:
    print("You haven't got enough money or you are kid")