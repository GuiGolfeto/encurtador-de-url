# pip install pyshorteners
import pyshorteners

url = 'https://www.youtube.com/watch?v=vn4_-ZiphkQ&t=19s'

link = pyshorteners.Shortener()
short_url = link.tinyurl.short(url)
print(short_url)