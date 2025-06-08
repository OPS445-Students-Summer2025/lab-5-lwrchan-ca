#!/usr/bin/env python3
#lab5b.py
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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name,'a')
    f.write(string_of_lines)
    f.close


def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    
    f.close


def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    # i.	Takes two arguments: Both are files path-names (which happen to be strings)
    # ii.	Reads all data from first file(Argument 1), and writes all lines into second file(Argument 2) adding line numbers
    # iii.	Line numbers should be added to the beginning of each line with a colon next to them(see sample output below for reference)
    # iv.	Hint: Use an extra variable for the line number

    original_list = read_file_list(file_name_read)
    # print (original_list)
    f = open(file_name_write, 'w')  #to empty the file_name_write before it starts appending in the below codes
    f.close()
    f = open(file_name_write, 'a')
    count = 0
    for line in original_list:
        # line_item = original_list[count]
        # f.write(str(count+1)+":"+ line_item+"\n")
        f.write(str(count+1) + ":"+ line + "\n")
        count = count + 1
    f.close()





if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
 
    write_file_list(file2, list1)
    print(read_file_string(file2))
 
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

