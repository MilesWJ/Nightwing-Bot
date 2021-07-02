import praw
import random
import time

reddit = praw.Reddit(
    client_id="REDACTED",
    client_secret="REDACTED",
    user_agent="REDACTED",
    username="REDACTED",
    password="REDACTED"
)


def get_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.read().splitlines()
        return random.choice(quotes)


def post():
    while True:
        ask = str(input("\nEnter the subreddit name: "))
        subreddit = reddit.subreddit(ask)
        print(f"Searching for {ask} subreddit...")

        try:
            print(f"Subreddit r/{ask} found.")
            for post in subreddit.hot(limit=10):
                for comment in post.comments:
                    if hasattr(comment, "body"):
                        comment_lower = comment.body.lower()
                        if "nightwing" in comment_lower:
                            print("Replying to a post...")
                            quote = get_quote()
                            comment.reply(quote)
                            print("Reply sent.")
                            time.sleep(900)
            break

        except:
            print(f"\nNo subreddit found for {ask}.")
            continue


def main():
    while True:
        ask = str(input(
            "\nWould you like to run the Nightwing Bot? [Yes or No]: ")).lower()
        if "yes" in ask:
            post()
            break
        elif "no" in ask:
            print("\nMayer another time...")
            break
        else:
            print(f"Invalid response; {ask}. [Yes or No]")
            continue


main()
