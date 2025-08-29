
text = """<html><head>
"""


open_stack = []  #stack to keep opened tags




for i in range(len(text)):
    if (text[i] == '<'):
        #tag token
        if (text[i + 1] != '/'):
            #opening tag
            i += 1
            tag = "<"
            while (text [i]  != ">"): #end of the opening tag
                tag += text[i]
                i += 1
            tag += ">"
            print(tag)
            
        else:
            #closing tag 
            pass
    else:
        #text token
        pass
