#write functions here, don't add input('') statements here!


def create_multiplication_table():
    table = []

    for i in range(1, 6):
        for j in range(1, 11):
            table.append(i*j)

    return table


def display_multiplication_table(table):

    count = 10

    for i in table:
        if i % count == 0:
            print(i)
            count += 10
        else:
            print(i, end=" ")
