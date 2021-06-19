#! /usr/bin/env python3


def test():
    n = 10
    m = 10
    rows, cols = (n, m)


    Outp = []
    for i in range(m): 
        row = []
        for j in range(n):  
            num = 0
            row.append(num)  
        Outp.append(row)  
    
    Outp[0][9]= 9
    print(Outp)



if __name__ == "__main__":
    test()