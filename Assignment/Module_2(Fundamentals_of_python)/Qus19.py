'''Write a Python program to find the first appearance of the substring 
'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the 
whole 'not'...'poor' substring with 'good'. Return the resulting string.'''


string="The weather is poor but not too bad."

sub_not=string.find("not")
sub_poor=string.find("poor")

if sub_poor != -1 and sub_not != -1 and sub_poor < sub_not:
   result = string[:sub_poor] + 'good' + string[sub_not + len('not'):]
else:
   result=string
print(result)
   

