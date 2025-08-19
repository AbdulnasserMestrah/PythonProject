def count_words(paragraph):
    # convert the text to lowercase beacuse its insensitive
    paragraph = paragraph.lower()

    for punctuation in [".",",","!","?"]:
        paragraph = paragraph.replace(punctuation,"")
    
        # in this part it splits it to a list
        words = paragraph.split()

        # create a dictionary to count the words
        word_count= {}

        for word in words:
            # if it's previously in the list add the counter
            if word in word_count:
                word_count[word]+=1
            # if not add it with a counter equals 1     
            else:
                word_count[word] = 1

        return word_count
    

text = "Ai is the future. The future is now "
print (count_words(text))


        

