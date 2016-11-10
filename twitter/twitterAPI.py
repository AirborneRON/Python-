#Import required modules
import sqlite3 
import twitter, datetime

#Load in my keys and secrets from the credentials file into a list
#(array)
 
file = open("twitterCredentials.txt")
creds = file.read().split('\n')

#Create a new API wrapper, passing in my credentials one at a time


api = twitter.Api(creds[0],creds[1],creds[2],creds[3])

console = sqlite3.connect("/Users/aarondobson/Library/Application Support/Google/Chrome/Default/History")
cursor = console.cursor()
cursor.execute("SELECT * FROM urls")
rows = cursor.fetchall()
console.close()
#Find out what time it is now (in Coordinated Universal Time)

timestamp = datetime.datetime.utcnow()

#Post status update and get the response from Twitter

print(rows[-1])

lastP = rows[-1]
print lastP
print lastP[2]



response = api.PostUpdate("the last page i visited was " +  lastP[2])
#Print out response text (should be the status update if everything worked)





print("Status updated to: " + response.text)