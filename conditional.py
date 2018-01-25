def main():
    age=(int(input("Enter your age:")))
    if(age>=20 and age<=110):
        print("eligible")
    elif(age>=0 and age<20):
        print("not eligible")
    else:
        print("Enter valid age!")


if __name__=='__main__':
    main()
