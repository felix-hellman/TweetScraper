from html.parser import HTMLParser
import sys

import fileinput

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    start = False
    def handle_starttag(self, tag, attrs):
        if('p' in tag):
            for attribute in attrs:
                if('class' in attribute[0]):
                    if('TweetTextSize TweetTextSize--normal js-tweet-text tweet-text' in attribute[1]):
                        self.start = True

    def handle_endtag(self, tag):
        if('p' in tag):
            if(self.start is True):
                self.start = False
                print()
            

    def handle_data(self, data):
        if(self.start is True):
            if(len(data) > 1):
                sys.stdout.write(data)
                sys.stdout.write(' ')

parser = MyHTMLParser()

for line in fileinput.input():
    parser.feed(line)
