def generateDocument(characters, document):

    if document == "":
        return True

    else:
        char_freq = {}
        doc_freq = {}
        
        for c in characters:
            if c not in char_freq:
                char_freq[c] = 1
            else:
                char_freq[c] += 1
        
        for d in document:
            if d not in doc_freq:
                doc_freq[d] = 1
            else:
                doc_freq[d] += 1

        print(doc_freq)
        print(char_freq)
        
        for key in doc_freq.keys():
            if (key not in char_freq) or (doc_freq[key] > char_freq[key]):
                return False
        return True