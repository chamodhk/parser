
text = """<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1 bold>Heading 1</h1>
    <p italic>This is a paragraph.</p>
  </body>
</html>

"""


open_stack = []  #stack to keep opened tags

class Node:
    def __init__(self, tag_name, tag_attribs):
        self.tag_name = tag_name 
        self.tag_attribs = tag_attribs
        self.children = []

    

i = 0
while i < len(text):
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
            
            j = 1
            tag_name = ""
            while j < len(tag):
                if tag[j] == " " or tag[j] == ">":
                    break 
                tag_name += tag[j]
                j += 1

            tag_attribs = ""
            while j < len(tag) and tag[j] != ">":
                tag_attribs += tag[j]
                j += 1

            # print(tag_name)
            print(tag_attribs)

            e = Node(tag_name,tag_attribs)
            open_stack.append(e)
        else:
            #closing tag 
            pass
    else:
        #text token
        pass

    i += 1
