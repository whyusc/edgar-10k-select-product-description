import os
import re

text = """ ITEM 1 First match

ITEM 2.


 2321ITEMS 1.2112
    AND 2.  
BUSINESS AND PROPERTIES

ITEM 1A.
ITEM 1 Second match

ITEM 2.

ITEM 1 Third match

ITEM 2. """


# path from where to get the txt files
saved_path = "E:/Thesis stuff/10k abbot/python/10ktxt/"

#path to where to save the txt
selected_path = "E:/Thesis stuff/10k abbot/python/Multiple 10k/10k_select/"

#path for 10ks with ITEM1
item1_path = "E:/Thesis stuff/10k abbot/python/10kcap/"

list_txt = os.listdir(selected_path)

def allindices(text, sub, listindex=[]):
    i = text.find(sub)
    while i >= 0:
        listindex.append(i)
        i = text.find(sub, i+1)
    return listindex


item1_begin = 'ITEM 1.'
item1a = 'ITEM 1A.'
item2_begin = 'ITEM 2.'
item3_begin = 'ITEM 3.'

counter1 = 0
counter2 = 0
counter3 = 0

for text in list_txt:
    file_path = selected_path + text #the path must be united with each item from the list
    file = open(file_path, "r+", encoding="utf-8") #opens the txt document and encodes it with utf-8
    file_read = file.read() #reads the opened file
    begin = allindices(file_read, item1_begin, listindex=[])
    end = allindices(file_read, item2_begin, listindex=[])
    # try to see if the index returns errors
    # if the index returns errors, print to console, count and continue the code further
    try:
        save_txt = file_read[begin[0]:end[0]].strip()
    except IndexError:
        print("Error in 1 " + text)
        counter1 += 1
        #print("error in 1 " + text)
        continue

    # if the above try function returns no errors, then continue to this:
    if len(save_txt) >= 2000:
        saved_file = open(item1_path + text, "w+", encoding="utf-8")  # save the file with the complete names
        saved_file.write(save_txt)  # write to the new text files the selected text
        saved_file.close()  # close the file
        #print("1' works for " + text)
    else:

        try:
            save_txt = file_read[begin[1]:end[1]].strip()
        except IndexError:
            print("Error in 2 " + text)
            counter2 += 1
            #print("error in 2 " + text)
            continue
        if len(save_txt) >= 2000:
            saved_file = open(item1_path + text, "w+", encoding="utf-8")  # save the file with the complete names
            saved_file.write(save_txt)  # write to the new text files the selected text
            saved_file.close()  # close the file
            #print("2' works for " + text)
        else:
            print("not working " + text)
    file.close()

