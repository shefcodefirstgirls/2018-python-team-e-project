import praw
import pprint

reddit = praw.Reddit(client_id='07ExaDCVmWyyHA',
                     client_secret='lKmGTXaquPyZc2CttdmoGYrUYlI',
                     user_agent='jedy2468')

print(reddit.read_only) 
print(reddit.subreddit('vegan').description)
for submission in reddit.subreddit('vegan').hot(limit=1):
    print(submission.title)
    print(submission.url)

<a href="https://www.facebook.com/TaiwanVegHound"> <img src="facebook-box.png"></a> 
<a href="https://www.instagram.com/vegan_taiwan"> <img src="instagram.png"></a>


    #pprint.pprint(vars(submission))