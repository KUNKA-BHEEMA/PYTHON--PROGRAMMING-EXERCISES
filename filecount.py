'''
program to count number of words, characters, and lines
in a file.
we are passing the file name as a argument on which we have 
to perform above said.
Any file name which is present in the same directory with
its extension can be given.
Here I have given filecontent.txt
Make sure that file is stored in location where python software installed

'''
def countWords(fileName):
    numwords = 0
    numchars = 0
    numlines = 0

    with open(fileName, 'r') as file:
        for line in file:
            wordlist = line.split()
            numlines += 1
            numwords += len(wordlist)
            numchars += len(line)

    print ("Words: ", numwords)
    print ("Lines: ", numlines)
    print ("Characters: ", numchars)

if __name__ == '__main__':
    countWords('filecontent.txt')






