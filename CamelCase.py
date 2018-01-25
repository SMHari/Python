#python code goes here
#python version :3 
def main():
    input_word = input("Enter a string \n").lower()
    words = input_word.split(' ')
    capitalized = []
    for word in words:
        final_words = word[0].upper() + word[1:]
        capitalized.append(final_words)
    output = ' '.join(capitalized)
    print (output) 

if __name__=='__main__':
    main()
