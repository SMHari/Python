
def main():
    #s=input()
    s,num=(input()).split(" ")
    num=int(num)
    def Exploder(string, n):
        print(string*n)

    def Myfun(string,Exploder,n):
        Exploder(string,n)

    Myfun(s,Exploder,num)

if __name__=='__main__':
    main()

