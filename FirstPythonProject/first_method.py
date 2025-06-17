

# indentation is key ... same indentation made "Hello World 3" are part of the method
def my_print_method():
    print('Hello World 1')
    print("Hello World 2")


    print('Hello World 3')
print('Hello World 4')


def my_print_method_params(msg):
    print(msg)


def my_print_method_ntimes(msg, nr):
    for i in range(0, nr):
        print(i, msg)


print('Hello World 0')
my_print_method()
print('Hello World 5')
my_print_method_params("Hello World folks!!!")
my_print_method_ntimes("Hi folks!!", 3)



