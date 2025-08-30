from collections import deque



text = """
<html>
  <head>
    <title>Simple Test</title>
  </head>
  <body>
    <h1 bold>Welcome</h1>
    <p italic>This is the first paragraph.</p>
    <p>This is the second paragraph with <span bold>some bold text</span> inside.</p>
    <div>
      <h2>Subsection</h2>
      <p>Content inside the subsection.</p>
    </div>
  </body>
</html>



"""


open_tag_stack = [None]  #stack to keep opened tags
text_stack = [None]



Root = None

class Node:
    def __init__(self, tag_name, tag_attribs):
        self.tag_name = tag_name 
        self.tag_attribs = tag_attribs
        self.tag_content= ""
        self.children = []


    # def __str__(self):
    #     return self.tag_name

    

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
            # print(tag_attribs)

            e = Node(tag_name,tag_attribs)
            open_tag_stack.append(e)

            text_stack.append("")
        else:
            #closing tag 
            closing_tag = ""
            i+= 2
            while (text[i] != ">"):
                closing_tag += text[i]
                i += 1
                
            # print(closing_tag)
            
            opening_tag = open_tag_stack.pop()
            tag_contet = text_stack.pop()
            if opening_tag.tag_name == closing_tag:
                opening_tag.content = tag_contet
            else:
                print("tag mismatch")

            if (open_tag_stack[-1]):
                open_tag_stack[-1].children.append(opening_tag)
            else:
                Root = opening_tag


    else:
        #text token
        if (text_stack[-1]):
            text_stack[-1] += (text[i])

    i += 1



def dfs(node, depth):
    if (depth == 0):
        prefix = ""
    else:
        prefix = "|" + "-"*depth
    print(prefix + node.tag_name)
    if (node):
        depth += 1
        child_count = len(node.children)
        for i in range(child_count):
            dfs(node.children[i], depth)



node = Root



dfs(node,0)
