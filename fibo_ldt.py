#python code goes here
#python version :3 
def main():
    x=int(input("Enter the range to find fib series"))
    list=[]
    n0 = 0
    n1 = 1
    for i in range(0,x):
        n2=n0+n1
        n0 = n1
        n1 = n2
        list.append(n2)

    print(list)


if __name__=='__main__':
    main()
