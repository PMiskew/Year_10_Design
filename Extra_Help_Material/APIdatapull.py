#https://rapidapi.com/scorebat/api/free-football-soccer-videos

#Big Idea: modules are collects of functions that can 
#bue used in a program.  They are not included by default
import requests 
from pprint import pprint

#String - This is a variable type that is a collection of characters. 
url = "https://rapidapi.p.rapidapi.com/" 

#Dictionary - This is a data structure used to hold key:pair values
#	Data Structure - This is a ways a computer can orgaize data in a program
# 	Two data structure we have talked about include lists and dictionaries. 
headers = {
    'x-rapidapi-host': "free-football-soccer-videos.p.rapidapi.com",
    'x-rapidapi-key': "51507cb5fcmsh4a3e9775685c3f9p1e9bb3jsnb9e1628e4ed0"
    }

#This is an assignment statement.  An assignmentstatement always has a single equal sign
#You always evaluate the right hand side first and take the result and store in the variable on the left
response = requests.request("GET", url, headers=headers)

'''
We read this line from left to right

requests -> Goes into the request module
requests.request("GET", url, headers=headers) --> Go int the request module and access the request method

The function request takes three parameters
	- The first two order matters
	- The third is called a named parameter. 

requests.request("GET", url, headers=headers)

'''
print(response.text)