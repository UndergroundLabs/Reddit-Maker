Reddit Maker
============

This script will create an account on Reddit, and attempt to upvote, and comment on a Reddit thread.

I created this script to test if I could mass create accounts from different IP addresses and use them to artifically manipulate upvotes.

I have now released it purely for others to learn from.

Installation
------------

Please ensure you have the following Python packages installed

    pip install requests
    pip install pyquery
    pip install fake_useragent
    pip install faker

Clone the repo

    git clone ...

Usage
-----

Navigate to the directory

    cd reddit-maker

Run

    ./reddit-maker.py URL_TO_REDDIT_THREAD COMMENT_TO_POST

Example

    ./reddit-maker.py https://www.reddit.com/r/linux/comments/3mz1db/amazon_instant_video_now_works_in_linux/ "This cool!"

How It Works
------------

+ Generate fake profile information.
+ Create an account on Reddit
+ Upvote a thread
+ Comment on a thread

If any errors happen along the way the script will terminate and report the error.

Once the script has finished running successfuly it will return the username and password of the newly registered account.
