str1='This is a string with single quotes.\n We are learning python'
str2="This is a string with double quotes"
str3='''This is a string with triple single quotes'''
str4="""This is a string with triple double quotes"""


'''this is a apna's college'''  # This will cause a syntax error due to the single quote in "apna's"
"this is a apna's college"  # This will work fine because double quotes are used to enclose the string
'this is a apna\'s college'  # This will also work fine because the single quote is escaped with a backslash

print(str1)