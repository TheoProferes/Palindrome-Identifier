string= input("Enter your string and I'll tell you if  its a palindrome")
string=string.upper()
newlist=[]
for count in range(len(string)):
    letter=len(string)-(count)
    newlist.append(string[letter-1])
newstring=""
newstring= newstring.join(newlist)
print(newstring)
if newstring==string:
    print("It is a palindrome")
else:
    print("It is not a plaindrome")
