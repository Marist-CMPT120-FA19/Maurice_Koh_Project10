#Maurice Koh
#zhi.koh1@marist.edu
#Program that turns a curse sentence into a clean one


def main():
    #a = File that contains the censored words
    #b = File that contains the words to censor
    
    #used for editing purposes
    #a = "Cursewords.txt"
    #b = "Sentence.txt"
    a = input("Enter the name of the censored words file: ")
    b = input("Enter the name of the file to censor: ")
    
    #read file
    File = open(a ,"r")
    Censor = open(b ,"r")

    #split words
    Words = File.read().split(" ")
    words = Censor.read().split(" ")

    #cycle to to read every word in the sentence and change it to *
    for i in Words:
        for j in range(0 , len(words)):
            if i == words[j]:
                words[j] = "*" * len(i)       
        Censor = open(b , "w")
    #to make sure it does not delete the whole sentence
    for i in words:
        Censor.write(i)
        Censor.write(" ")
        
    Censor.close()
    
main()

