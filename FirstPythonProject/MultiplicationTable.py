
## overloading is not possible
## it overrides the previous implementation
# def print_multiplication_tables (table, start, end):
#     for i in range(start, end+1):
#         #print (table, "X" , i, "=", table * i)
#         print(f"{table} X {i} = {table * i}")

def print_multiplication_tables (table=1, start=1, end=10):
    for i in range(start, end+1):
        #print (table, "X" , i, "=", table * i)
        print(f"{table} X {i} = {table * i}")

print_multiplication_tables (10, 1, 5)
print_multiplication_tables (10, 6)
print_multiplication_tables (10)
print_multiplication_tables ()


