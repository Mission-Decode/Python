import os, sys

print("<-----Log files cleaner (Removes old .log files appended with dates)---->")
print("Enter the path to directory that needs to be cleaned")
path = raw_input()

print("Staring to clean :"+path)

for f in os.listdir(path):
	if f.find(".log.") != -1:
		print("Removing :"+f)
		f = os.path.join(path,f)
		os.remove(f)
