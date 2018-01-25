#python code goes here
#python version :3 
def main():
    name_list=[]
    n=int(input("Enter the number of names to enter:"))
    print("Enter the names one by one")
    for i in range(0,n):
        names=input().lower()
        final_names=names[0].upper()+names[1:]
        #print(final_names)
        name_list.append(final_names)
    print(name_list)

if __name__=='__main__':
    main()
