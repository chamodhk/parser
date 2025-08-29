
import re
text = """

<html>
<head>
    <title> my first parser </title>
</head>
<body> This is H1 </body>
</html>

"""

opening = '^<[a-z]'
closing = '^</'
text = text.split()


class Elemenet:
    def __init__(self, tag, content):
        self.tag = tag 
        self.content = content
        self.children = []


content = ""
opening_stack = []
closing_stack = []
elements = []
for tag in text:
    if re.match(opening, tag):
        # print(tag, 'opening')
        opening_stack.append(tag)
    elif re.match(closing, tag):
        # print(tag, 'closing')
        el = Elemenet(opening_stack.pop(), content)
        content = ""
        elements.append(el)
        
    else:
        content = content + tag +  " "
# print(text)

for e in elements:
    print(e.content)
        
