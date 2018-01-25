def main():
    job = "Programmer"
    print (job)
    count_r=job.count("r")
    print("no of r:{0}".format(count_r))
    pos_g=job.find("g")
    print("position of g:{0}".format(pos_g+1))
    mreplace_y=job.replace("m","Y")
    print("Replacing m with Y:{0}".format(mreplace_y))


if __name__=='__main__':
    main()
