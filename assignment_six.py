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
        with open(fileName, "r") as file:                   #
            lines = file.readlines()                        #
            return lines                                    #
    except FileNotFoundError:                               #
        print("File not found.")                            #
        return []                                           #


def countLines(lines):
    '''
    count number of lines
    :param lines: use param of number of lines in file
    :return: number of lines in file
    '''
    return len(lines)                                       #

def countWords(lines):
    '''
    count number of words
    :param lines: use lines to find number of words in sequence
    :return: number of words in file
    '''
    totalWords = 0                                          #
    for line in lines:                                      #
        words = line.split()                                #
        totalWords += len(words)                            #
    return totalWords                                       #

def countCharacters(lines):
    '''
    count number of characters
    :param lines: use words to find number of characters in sequence
    :return: number of characters in file
    '''
    totalCharacters = 0                                     #
    for line in lines:                                      #
        words = line.split()                                #
        for word in words:                                  #
            totalCharacters += len(word)                    #
    return totalCharacters                                  #

def main():
    '''
    print number of lines words and characters
    :return: return main()
    '''
    fileName = "intro_lists.py"                             #input name of file

    lines = readFile(fileName)                              #def lines in file

    if lines:
        numLines = countLines(lines)                        #get total lines
        numWords = countWords(lines)                        #get total words
        numCharacters = countCharacters(lines)              #get total characters

        print("Lines:", numLines)                           #print number of lines
        print("Words:", numWords)                           #print number of words
        print("Characters:", numCharacters)                 #print number of characters
    else:
        print("Cannot analyze.")                            #print it cannot analyze if it cannot analyze file

main()                                                      #run main function