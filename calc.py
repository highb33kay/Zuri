x = int(input("what is x: "))
y = int(input("what is y: "))

def cal(x,y):
    print('''
          reply + for addition
          reply - fro subtraction
          reply / for division
          reply * for multiplication
          ''')
    s = input("what do you want to do:")
    
    if s == "+":
        a = x + y
        print(a)
    elif s == "-":
        a = x - y
        print(a)
    elif s == "/":
        a = x / y
        print(a)
    elif s == "*":
        a = x * y
        print(a)
    else:
        pass    

cal(x,y)