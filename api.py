import praw
#import pprint

reddit = praw.Reddit(client_id='07ExaDCVmWyyHA',
                     client_secret='lKmGTXaquPyZc2CttdmoGYrUYlI',
                     user_agent='jedy2468')

#print(reddit.read_only) 




def get_title(sub):
    submissions=reddit.subreddit(sub).hot(limit=10)
    title=[]
    for submission in submissions:
    	title.append(submission.title)
    return (title)

def get_url(sub):
    submissions=reddit.subreddit(sub).hot(limit=10)
    url=[]
    for submission in submissions:
        url.append(submission.url)
    return (url)




	    
#print (getreddit("vegangifrecipes"))

    

    #print (submission.selftext)
    #for comment in submission.comments:
    	
    
    #pprint.pprint(vars(submission))
    #print (dir(submission))




    