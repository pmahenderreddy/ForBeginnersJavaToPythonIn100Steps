def print_squares_of_numbers(nr):
    for i in range(1, nr+1):
        print (i * i)


def print_squares_of_even_numbers(nr):
    for i in range(2, nr+1, 2):
        print (i * i)


def print_numbers_revers(nr):
    for i in range(nr, 0, -1):
        print (i)


num = 10;
print_squares_of_numbers( num )
print_squares_of_even_numbers( num )

num = 20;
print_numbers_revers ( num )
