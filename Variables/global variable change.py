count  = 10 

def my_function():
    global count
    count = count + 5

my_function()
print(count)