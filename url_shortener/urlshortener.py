import pyshorteners 
link = input("enter link")
shortener= pyshorteners.Shortener()
x = shortener.tinyurl.short(link)

print(x)