# coding: utf-8
#!/usr/bin/python

import praw
import webbrowser
from operator import itemgetter

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("hiphopheads")

submissions = []

for submission in subreddit.hot(limit=100):
    if "FRESH" in submission.title.upper() and submission.score > 100:
        submissions.append([submission.score, submission.title,
        submission.permalink])

submissions = sorted(submissions, key=itemgetter(0), reverse=True)

print "\n\n"

for s in submissions:
    print (str(submissions.index(s) + 1) + "." + "\t" + str(s[0])
           + "\t" + s[1].encode('utf-8'))

print "\n"

lnk = input("Which link do you want to open? ")

try:
    webbrowser.open_new_tab("https://reddit.com" + submissions[lnk - 1][2])
except:
    print "error"
