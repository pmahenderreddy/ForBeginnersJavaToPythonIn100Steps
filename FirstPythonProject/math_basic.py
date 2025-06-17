def print_squares_of_numbers(nr):
    for i in range(1, nr+1):
        print (i * i)


def print_squares_of_even_numbers(nr):
    for i in range(2, nr+1, 2):
        print (i * i)


def print_numbers_revers(nr):
    for i in range(nr, 0, -1):
        print (i)


def sum_of_two(a, b):
    return a+b

def no_return_fn(msg):
    print (msg)

def with_empty_return_fn(msg):
    print(msg)
    return


num = 10;
print_squares_of_numbers( num )
print_squares_of_even_numbers( num )

num = 20;
print_numbers_revers ( num )

firstNr = 10
secondNr = 25;

total = sum_of_two(firstNr, secondNr)

print (f"{firstNr} + {secondNr} = {total}")

print()
msg = "method without return statement ... returns what?"
whats_returned = no_return_fn( msg )
print (whats_returned, "\nits type is ", type(whats_returned))

print()
msg = "method with empty return statement ... returns what?"
whats_returned = with_empty_return_fn( msg )
print (whats_returned, "\nits type is ", type(whats_returned))
