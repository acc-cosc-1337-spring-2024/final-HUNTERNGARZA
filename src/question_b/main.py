import question_b


while True:
    print("your menu")
    print(" 1-Display stock purchase history")
    print("2-Exit")
    user_choice = input("Choice? ")
    if user_choice == "1":
        question_b.stock_purchase_history()
    else:
        break
