#!/usr/bin/python3
def text_indentation(text):
    """
    function that prints a text with 2 new lines after each of these characters: ., ? and :
    """
    characters =['.','?',':']
    new_string=''
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        if i in characters:
            i+="\n"
        new_string += i
    print(new_string)