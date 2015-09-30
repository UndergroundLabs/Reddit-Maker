#!/usr/bin/python

import argparse
import requests
import json
from pyquery import PyQuery as pq
import sys
from fake_useragent import UserAgent
from faker import Factory
import random
import string
import re

def register(session, username, password):

    '''
    Register an account on Reddit
    '''
    
    r = session.post("https://www.reddit.com/api/register/" + username, {
        'op':'reg',
        'user': username,
        'passwd': password,
        'passwd2': password,
        'email': '',
        'api_type': 'json'
    })
    
    return json.loads(r.text)['json']['errors']

def upvote(session, url):

    '''
    Upvote a Reddit thread
    '''

    resp = session.get(url)
    d = pq(resp.text)
    
    innerJS = d("#config").outerHtml()[51:-10]
    j = json.loads(innerJS)
    
    r = session.post("https://www.reddit.com/api/vote", data={
        'id': j['cur_link'],
        'dir': '1',
        'vh': j['vote_hash'],
        'r': 'trapproduction',
        'uh': j['modhash'],
        'renderstyle': 'html'
    })
    
    return (r.status_code == 200)

def comment(session, url, comment):
    
    '''
    Comment on a Reddit thread
    '''

    resp = session.get(url)
    d = pq(resp.text)

    innerJS = d("#config").outerHtml()[51:-10]
    j = json.loads(innerJS)
    
    r = session.post("https://www.reddit.com/api/comment", data={
        'thing_id': j['cur_link'],
        'text': comment,
        'r': '',
        'uh': j['modhash'],
        'renderstyle': 'html'
    })

    return (r.status_code == 200)    

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Reddit link to upvote')
    parser.add_argument('comment', help='Comment to post on reddit thread')    
    args = parser.parse_args()
    
    ua = UserAgent()
    
    # Generate fake profile data
    fake = Factory.create()
    
    # Create a valid username and password
    username = re.sub(r'\W+', '', fake.profile()['username'])
    password = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(8)])
    
    session = requests.Session()
    session.headers.update({
        'User-Agent': ua.random
    });

    # Create Account
    errors = register(session, username, password)
    
    # Check for any errors in creating the account
    if errors:
        print errors[0][1]
        sys.exit(1)

    # Attempt to upvote
    if not upvote(session, args.url):
        print "Upvote Failed!"
    
    # Attempt to leave a comment
    if not comment(session, args.url, args.comment):
        print "Comment Failed!"

    print username + ":" + password
