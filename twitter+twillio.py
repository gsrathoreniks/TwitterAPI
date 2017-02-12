#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------

from twitter import *
from twilio.rest import TwilioRestClient
#----------------------------------------------------------------------
ACCOUNT_SID="xyz"
AUTH_TOKEN="xyz"


#-----------------------------------------------------------------------
con_key="xyz"
con_secret="xyz"
acc_key="xyz"
acc_secret="xyz"
#-----------------------------------------------------------------------
twitter = Twitter(
		auth = OAuth(acc_key, acc_secret,con_key, con_secret))
for  i in range(2):
    print("--------------------------------------------")
    if(i==0):
        print("----------------WELCOME --------------------")

print("1. Tweets by Username")
print("2. Search on Twitter")
print("3. Follows or Not")
print("4. list Following")
print("5. Publish a TWEET")
print("6. Send Text Message")
print("\nEnter your choice------>")
ch=input()

# ------------------------------------------------------------------------------------
# -----------------------tweets by username-------------------------------------------
# ------------------------------------------------------------------------------------

if(int(ch)==1):
    print("Enter @Username-::")
    user=input()
    results = twitter.statuses.user_timeline(screen_name=user)
    for status in results:
        print("(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore")))
# ------------------------------------------------------------------------------------
# ------------------------search on twitter-------------------------------------------
# ------------------------------------------------------------------------------------
if(int(ch)==2):
    print("Enter something to search-::")
    search=input()
    results = twitter.users.search(q=search)
    for user in results:
        print("@%s (%s): %s" % (user["screen_name"], user["name"], user["location"]))
# ------------------------------------------------------------------------------------
# -------------------------Follows or not---------------------------------------------
# ------------------------------------------------------------------------------------
if(int(ch)==3):
    print("Enter first Username-::")
    user1 =input()
    print("Enter second Username-::")
    user2 =input()
    result = twitter.friendships.show(source_screen_name=user1,
                                      target_screen_name=user2)

    following = result["relationship"]["target"]["following"]
    follows = result["relationship"]["target"]["followed_by"]

    print("%s following %s: %s" % (user1, user2, follows))
    print("%s following %s: %s" % (user2, user1, following))

# ------------------------------------------------------------------------------------
# ----------------------list following by username------------------------------------
# ------------------------------------------------------------------------------------
if(int(ch)==4):
    print("Enter @Username-::")
    username=input()
    query = twitter.friends.ids(screen_name=username)

    print("found %d friends" % (len(query["ids"])))

    for n in range(0, len(query["ids"]), 100):
        ids = query["ids"][n:n + 100]
    subquery = twitter.users.lookup(user_id=ids)

    for user in subquery:
        print(" [%s] %s" % ("*" if user["verified"] else " ", user["screen_name"]))
#-------------------------------------------------------------------------------------
#------------------------tweet on your profile----------------------------------------
#-------------------------------------------------------------------------------------
if(int(ch)==5):
    print("Write something to Tweet -->")
    TweetText = input()
    results = twitter.statuses.update(status=TweetText)

#-------------------------------------------------------------------------------------
#------------------------send text message--------------------------------------------
#-------------------------------------------------------------------------------------
if(int(ch)==6):
    print("Enter message to send-::")
    msg=input()
    client= TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN)
    client.messages.create(
        to="+919881029531",
        from_="+12018099435",
        body=msg
    )
# ------------------------------------------------------------------------------------
# ------------------------if choice not found-----------------------------------------
# ------------------------------------------------------------------------------------
if(int(ch)!=1 and int(ch)!=2 and int(ch)!=3 and int(ch)!=4 and int(ch)!=5 and int(ch)!=6):
    print("Entered choice in incorrect...!!!!")

# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------
