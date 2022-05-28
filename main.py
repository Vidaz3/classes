# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open("./story.txt", "r") as openfile:
        read_file_content = openfile.read()
    return read_file_content
print(read_file_content("./story.txt"))

def count_words(filename):
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()
    print (split_text)
    count = {}
    for a in split_text:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1
    return count
print(count_words("./story.txt"))