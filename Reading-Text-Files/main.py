# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

contents = "Once upon a time a psychology professor walked around on a stage while teaching stress management principles to an auditorium filled with studentsAs she raised a glass of water, everyone expected they would be asked the typical glass half empty or glass half full question.Instead, with a smile on her face, the professor asked, How heavy is this glass of water I am holding?"


def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename) as f:
        contents = f.read()
        return contents


def count_words(contents):
    occur = {}
    array_list = contents.split()
    for i in array_list:
        occur[i] = contents.count(i)
    return occur


occurence = count_words(read_file_content("story.txt"))
print(occurence)
