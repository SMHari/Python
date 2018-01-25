#python code goes here
#python version :3 
def main():
    global x, values
    list=[]
    def namec(list):
        Uppernames = [x.upper() for x in list]
        print(Uppernames)

    data = int(input("Enter the num of names u want to enter:"))
    for x in range(0, data):
        values = str(input("Enter value "+str(x+1)))

        list.append(values)
    namec(list)


if __name__ == '__main__':
    main()
