import webbrowser

print("Welcome to SearchPy: Automated Search For CS queries,Currently search is supported for Google and StackOverFlow")
print("Usage Options:")
print("-g : Append -g at the end of the search query for google only search")

query = raw_input("Enter the search query: ")	
option = query[-2:]
query = query.replace('-g','')
if option=="-g":
	webbrowser.open_new('https://www.google.com/search?q='+query)
else:
	webbrowser.open_new('https://www.google.com/search?q='+query)
	webbrowser.open_new('https://www.stackoverflow.com/search?q='+query)