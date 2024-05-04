import question_d


while True:
    print("run till u say stop")

    table = question_d.create_multiplication_table()
    question_d.display_multiplication_table(table)

    choice = input("continue? ")
    if choice == "no":
        break
