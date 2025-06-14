#!/usr/bin/env python3
# •	This Python script will read the same file (data.txt) that you previously created
# •	The read_file_string() function should return a string
# •	The read_file_list() function should return a list
# •	The read_file_list() function must remove the new-line characters from each line in the list
# •	Both functions must accept one argument which is a string object containing the name of a file
# •	The script should show the exact output as the samples
# •	The script should contain no errors

#Author Leung Wai Rene Chan 160682231 



def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name,'r')
    content = f.read()
    f.close()
    return content
 

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
#____________________________________________________________________________________________________
#USING FOR LOOP:
    # f = open(file_name,'r')
    # contents = f.readlines()
    # f.close()
    # # print(contents)
    # list_content = []
    # for item in contents:
    #     list_content.append(item.strip())
    # return list_content
 
#_____________________________________________________________________________________________________
#USING LIST:
    f = open(file_name,'r')
    contents = f.read()
    f.close()
    # print(contents)
    list_contents = contents.split('\n')
    # print(list_contents)
    # list_content = []
    # for item in contents:
    #     list_content.append(item.strip())
    length = int(len(list_contents))
    last = int(length) - 1
    # print (length)
    list_contents_no_last = []
    list_contents_no_last = list_contents[0:last]
    # print (list_contents_no_last)
    return list_contents_no_last


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
