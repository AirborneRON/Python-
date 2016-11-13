file = open("stop_words")
stopList = file.read().split("\n")
file.close()
# how to open up my plain text file, then create a variable to stuff the read file into 
#seperating each element of the list by the return key 
#then close

# all responses should start with a space before typing

print(" Hello ")    
response = raw_input(" what is your name ?")
words = response.split(" ")
for nextWord in words:
    if nextWord not in stopList:
        response = response.replace(nextWord, "")
        print("Well hello" +" " +nextWord)
        
#because of how my stopList was formatted ive had to use the split function which has conflicted
#with the String  
        
#print ("line 21" + nextWord)        
response = raw_input ("how lovely to meet you")

if (response == "my names aaron"):
    print("how is that pronounced if you dont mind me asking ? ")
    


response = raw_input( " Interesting name btw, my names Mac")
if (response == " nice to meet you"):
    print("likewise")


response = raw_input (" where are you from originally ? ")
if (response == "im from cornwall originally"):
    print("oh I hear its beautiful down those parts")

#if (response == "")

response = raw_input("is there anywhere you'd want to go for a coffee there ?")
if (response == " yes"):
    print("Great I look forward to it")
elif(response == " no"):
    print("sod you then" + " i'll go by myself")

response = raw_input("anyways, so how old are you ?")
if (response == " 18"):
    print(" not as old as me then ")
elif (response == " 23"):
    print("same age as me then")



response = raw_input(" whats your favourite colour ?")
if (response == "blue"):
    print("thats mine too")
elif(response == "red"):
    print("red is sick" + " but unfortunetly we must end this conversation" )
    
elif(response == "yellow"):
    print ("yellows pretty cool too " + " anyways i really must be off TTFN")
    
else: print("im not a fan of that colour" + "and on that note good day to you sir")    
