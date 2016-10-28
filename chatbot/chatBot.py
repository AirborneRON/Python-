file = open("stop_words")
stopList = file.read().split("\n")
file.close()
# how to open up my plain text file, then create a variable to stuff the read file into 
#seperating each element of the list by the return key 
#then close



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
if (response == "aaron"):
    print("how is that pronounced if you dont mind me asking")
    #if ( response ==)
    #elif(response == "")


response = raw_input( "not how it sounds then, my names Mac btw")

#print ("line 30" + response)
if (response == "nice to meet you"):
    print("likewise")


response = raw_input (" where are you from originally ? ")
if (response == "im from cornwall originally"):
    print("oh I hear its beautiful down those parts")

#if (response == "")

response = raw_input("is there anywhere you'd want to go for a coffee down there ?")
print(response)

response = raw_input("so how old are you ?")
print("response")


response = raw_input(" whats your favourite colour ?")
if (response == "blue"):
    print("thats mine too")
elif(response == "red"):
    print("red is sick" )
    
elif(response == "yellow"):
    print ("yellows pretty cool too ")
    
else: print("all other colours suck")    