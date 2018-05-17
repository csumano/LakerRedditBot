import praw
import time

def bot_login():
    print("Loging in...")
    lb = praw.Reddit(user_agent='LakerBot v0.1', client_id='8pjabuPyk3Y-EA',
                  client_secret='QRHaLpZnXHq4j4lQyfIbM2lDGmw',username='OswegoBot', password='lilpumpave')
    print("Succesful login")
    return lb


def run_bot(lb):
    print("Getting Comments")
    for comment in lb.subreddit('test').comments(limit=25):
        if "Oswego" in comment.body:
            print("Found string \"Oswego\"!")
            comment.reply("Go lakers!!")
            print("Replied to " + " " + comment.id)


    print("Sleeping...")
    time.sleep(10)
    print("Ready!")


lb = bot_login()

while True:
    run_bot(lb)
