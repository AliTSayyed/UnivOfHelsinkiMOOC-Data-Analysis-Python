#!/usr/bin/env python3


def triple(x):        
        return x*3
    
    
def square(x):
        return x**2

def main():
    pass

    for value in range(1, 11):
        triple_value = triple(value)
        square_value = square(value)
        if square_value > triple_value:
            break
        print(f"triple({value})=={triple_value} square({value})=={square_value}")

        
        
    

if __name__ == "__main__":
    main()
