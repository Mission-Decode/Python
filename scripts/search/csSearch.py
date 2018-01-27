import webbrowser

print("Welcome to SearchPy: Automated Search For CS queries\n")
print("Currently search is supported for Google and StackOverFlow\n")

query = raw_input("Enter the search query: ")	

webbrowser.open_new('https://www.google.com/search?q='+query)
webbrowser.open_new('https://www.stackoverflow.com/search?q='+query)
