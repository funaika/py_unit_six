#Assignment Name
#Kalen Funai
#11/17/23

def readFile(fileName):
    '''
    get name of and read file
    :param fileName: name of the file
    :return: return empty list
    '''
    try:
        with open(fileName, "r") as file:                   #opens file named
            lines = file.readlines()                        #reads all lines from file and puts them in list called lines
            return lines
    except FileNotFoundError:                               #exception for is file is not found
        print("File not found.")
        return []                                           #returns list


def countLines(lines):
    '''
    count number of lines
    :param lines: use param of number of lines in file
    :return: number of lines in file
    '''
    return len(lines)                                       #calculate and return length of lines variable

def countWords(lines):
    '''
    count number of words
    :param lines: use lines to find number of words in sequence
    :return: number of words in file
    '''
    totalWords = 0                                          #set base to 0
    for line in lines:
        words = line.split()                                #splits lines into words
        totalWords += len(words)                            #keeping count of words
    return totalWords

def countCharacters(lines):
    '''
    count number of characters
    :param lines: use words to find number of characters in sequence
    :return: number of characters in file
    '''
    totalCharacters = 0
    for line in lines:
        words = line.split()                                #splits words to characters
        for word in words:
            totalCharacters += len(word)                    #keeping count of characters
    return totalCharacters

def main():
    '''
    print number of lines words and characters
    :return: return main()
    '''
    fileName = "intro_lists.py"                             #input file

    lines = readFile(fileName)                              #def lines opening and reading from input file

    if lines:                                               #if statement used for what to print and to make sure file is valid
        numLines = countLines(lines)
        numWords = countWords(lines)
        numCharacters = countCharacters(lines)

        print("Lines:", numLines)
        print("Words:", numWords)
        print("Characters:", numCharacters)
    else:                                                   #else statement used for if document is not able to be analyzed
        print("Cannot analyze.")

main()