file = open("stop_words")
stopList = file.read().split("\n")
file.close()
# how to upload stop words and read them then 
#close
#if("what is your name ?")
# = ("aaron") raw_input("hows that pronounced")


print(" Hello ")
response = raw_input(" what is your name ?").split(" ")
for nextWord in response:
    if nextWord not in stopList:
   #response = response.replace(nextWord, "")
        print("hello" +" " +nextWord)    


#for x in stopList
    #x means every element in the list
    #print.replace(response)



response = raw_input("thats a nice name how do you pronounce that ?")
print(response)


response = raw_input( "not how it sounds then, my names Mac ")
print(response)


response = raw_input (" where are you from originally ? ")
print(response)

response = raw_input("do you want to go for a coffee ?")
print(response)

response = raw_input("so how old are you ?")
print("response")


response = raw_input(" whats your favourite colour ?")
if (response == "blue"):
    print("thats mine too")
elif(reponse == "red"):
    print("red is sick" )
    
elif(response == "yellow"):
    print ("yellows pretty cool too ")
    
else: print("all other colours suck")    