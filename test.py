from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import urllib2
import os,sys
from pytube import YouTube
from pytube import utils
from pytube.utils import print_status, FullPaths

# Html Parser Class
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        for attr in attrs:
            if attr[0]=='href' :
                links.append(attr[1])
    def handle_entityref(self, name):
        c = chr(name2codepoint[name])

links = []
parser = MyHTMLParser()
#f = urllib2.urlopen('http://www.codenewbie.org/podcast')
#f = urllib2.urlopen('https://www.youtube.com/watch?v=8r1c0a8cL6s&list=PLB9B5308D24A6061D')
f = urllib2.urlopen('https://www.youtube.com/watch?v=UzxYlbK2c7E&list=PLA89DCFA6ADACE599')
parser.feed(f.read())
fp = open("download_links.txt","w+")
fp.close()
for i in list(set(links)):
    fp = open("download_links.txt", "a")
    if 'watch' in i and '&index' in i:
        try:            
            download_command = "https://www.youtube.com"+i
            yt = YouTube(str(download_command))
            print(yt.filename)
            print(yt.filter('mp4')[-1])
#            video =  yt.get('mp4', '720p')
            video = yt.get('mp4', '360p')
#            video.download('')
            
            video.download(path='download_videos/', on_progress=print_status)
            fp.write(str(download_command))
            fp.write("\n")
            fp.close()
        except :
            print str(download_command)
            print "Error in downloading"       

print "The Task is completed :-)"

