#!/usr/bin/env python

import webbrowser

query = raw_input("Enter the search query: ")	
webbrowser.open_new('https://www.stackoverflow.com/search?q='+query)
