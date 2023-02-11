
import re
import nltk
from nltk.tokenize import RegexpTokenizer


def tokenize(text):

    pattern = r'[\w]+|[\:]+|[\d]+[\w]+|[\:\;]+[\w]+|[\|]+|[\,]++|[\[\]]+|[\:\;]+|\([\(\)\;]+\)|[\w]+' 
    tokenizer = RegexpTokenizer(pattern, gaps=False)
    tokens = tokenizer.tokenize(text)
    u_tokens = []

    for index in range(0, len(tokens)):
        
        if tokens[index] == "[[":
            u_tokens.append("[")
            u_tokens.append("[")
        elif tokens[index] == "]]":
            u_tokens.append("]")
            u_tokens.append("]")
        else:
            u_tokens.append(tokens[index])

    return u_tokens


def castInteger(tokens): 

    for index in range (0, len(tokens)):
        
        try:
            token = int(tokens[index])
            tokens[index] = token
        except:
            pass

    return tokens