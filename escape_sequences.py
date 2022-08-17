"escape secquences"
# print("hello\anikth") #hellonikth. by keeping one back word slash the(a) will not come. if we want to print the full  use  this method
# print("hello\\anikth") #hello\anikth. mostly this method is used by keeping two types back word slach we can print this.
# print("hello\a arun") #helloarun. this can be also used. we can keep space also.

# print("hello\barun") #hellarun. \b is used to remove the one charater from the back side if their is space also it will get removed.
# print("hello \barun") #helloarun. in this we gave one space now it has been removed.
# print("hello  \barun") #hello arun. in this case we gave 2 spaces one space has been removed.

"\c,\d,\e" "for this 3 charaters it has no meaning it will be woring properly only"
# print("hello\camera") #hello\camera
# print("hello\dog") #hello\dog
# print("hello\elephanat") #hello\elephanat

"\f" #\f which means new line or next line to print the statement.
# print("hello\frohan\fhow are you") #the out will be first line hello next line rohan and last line how are you.
# print("hello\\fun") # hello\fun. with this we will getting the statement in one line only if we put 2 back slash.

"\g,\h,\i,\j,\k,\l,\m" "for this all dont have any meaning it will run perfectly"
# print("hello\gun") #hello\gun
# print("hello\hat") #hello\hat
# print("hello\ironman") #hello\ironman
# print("hello\jack") #hello\jack
# print("hello\kiran") #hello\kiran
# print("hello\mango") #hello\mango

"\n" "which is used for the next or new line if we print in one line with usig the \n we can use \\ 2 times back slash."
# print("hello\nrohan\nkuamr") #first line hello 2nd line rohan 3rd line kumar
# print("hello\\naresh") #hello\naresh. this will print in one line only.

"\o,\p,\q" "for this it has no meaning"
# print("hello\ohan") #hello\ohan
# print("hello\paint") #hello\paint
# print("hello\queen") #hello\queen

"\r" #carrage return when we have left side few charaters and right side more then it will print right side on charaters.
# print("hello\rrohankumar") #rohankumar. coz the right side it has more chraters so it has printed only right side one only.
# print("hello\ranna") #annao . the left side we have more and right side less so the right side we have 4 and left 5 chraters so from the left side 4chraters will get erased and it will print first left side 4 charaters and reamaning 1 charater of left side aganin it will print i,e. "o"

"\t" "which means tab"
# print("\thello") #        hello. if we keep \t at starting we will get 8 spaces.
# print("hello\trohan") #hello   rohan. if we kepp in middle we will get 3 spaces.
# print("hello   rohan") #hello   rohan. the above line and this line is same.
# print("hello \trohan") #hello   rohan. same if we keep space and write \t we will get same 3 spaces only.
# print("hellorohan\t") #hellorohan. if we keep \t at last it has no use.
# print("hello\t rohan") #hello    rohan. if we keep space after \t then it will count that space and give us 4 spaces
# print("hello    rohan") #hello    rohan.

# "\u" "which means unicode"
# print("hello\umberala") #syntax error: unicode
# print("hello\\umberala") #hello\umberala

"\v" "which means new or next line"
# print("hello\vrohan") #first line hello and next line rohan

"\w" "\w which has no meaning it will work properly"
# print("hello\war") #hello\war

# "\x" "which means unicode"
# print("hello\xrohan") #unicode
# print("hello\\xrohan") #hello\xrohan

"\y, \z" "which has no meaning it will properly."
"the above one  all in lower case which means"

"in the upper case U&N this two only have the problem it give us as unicode"

# "\u it will take 4 charaters only and the output will be printed in blac and white. till 0001 to 0006"
print("\u0001")
# print("\u0002")
# print("\u0003")
# print("\u0004")
# print("\u0005")
# print("\u0006")

# "\u 0007 to 0009 it will give blank line" 
# print("\u0007")
# print("\u0008")  
# print("\u0009")

"colout emoji"
# print("\U0001f601")
# print("\U0001f602")
# print("\U0001f604")
# print("\U0001f605")

import emoji