# runtime-error

while True:
    i = int(input("Enter first Value: "))
    j = int(input("Enter second Value:  "))
    
    try:
        print(f"{i} / {j} : {i/j}")
    except ZeroDivisionError: 
        print("Hey! Are you mad!😡")
    except NameError:
        print("Hey! Variable is Not There!😢")
    except ValueError:
        print("Hello Mr. Value Error occured.💥")
    else:
        print("Yeah All RIght Input.✅")
    finally:
        if (not int(input("'1' for continue/ '0' for exit: "))):
            break
    

try:
    print(int("hello"))
except Exception as error:
    # print("Hello Dude, X is not there😢")
    print(error)
    
        
