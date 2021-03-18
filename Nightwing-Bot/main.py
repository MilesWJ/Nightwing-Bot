import praw
import random
import time

reddit = praw.Reddit(
    client_id="3D8wQy3XcNc0SQ",
    client_secret="KGA6GZyJrmfsXcqtAq8GJzVPlkVxfQ",
    user_agent="<<console:Nightwing-Bot>>",
    username="Nightwing-Bot",
    password="MilesWJames062704"
)

quotes = ["The Batman taught me, guided me, trained me. What I am I owe to him. What more can I say? And Superman. I grew up in your shadow, too. You taught me honor, selflessness, and the true meaning of the word 'hero.' … I'm the sum of so many people who have influenced me, shaped my thinking, and given me love. Mom and Dad, you were the first … what you gave me will never leave. It's forever locked in my heart and in my soul. Batman, you took in a young, frightened boy. And you showed him how to become a good man. Kory, it's so funny. I spent the better part of last year fighting to forget what made me me. I almost alienated everyone, but you stuck by me and I love you for that. I gave up being Robin because that tied me to Batman. But now I become someone new who commemorates all those who made me someone special.", "Hard to imagine me without the Titans, either. I think the Titans helped define me. I was always the bottom half of Batman and … Now I'm Nightwing, myself. No junior partner. Whatever I do from now on is my choice. It's scary sometimes. But it's always a lot easier to let others tell you what to do. Don't quite feel like an adult yet, but I think I've grown up … I certainly don't make decisions rashly anymore. And I wouldn't quit college today just to rebel against Bruce. Fortunately, some mistakes can be fixed… Yeah, I'm grown up, but I still don't know what I'm going to do when I'm really grown up…. Doctor, lawyer, indian chief? They all sound good to me. What do I do when I take off my costume? If I were Batman, I'd become Bruce Wayne, professional cypher. I think he'd give up being Bruce in a second if he thought Batman could go out during the day. I can't. I need my normal life. Bats need the night. Robins need light.",
          "You molded me and taught me, Bruce. For years, I lived under the shadow of The Batman. I wanted to get away, to be my own man. Yet, when I chose a costume and a name, they reflected you. You're a part of me, Bruce. I can't deny it. And I don't want to any longer. I just wanted you to know that. That, and one other thing -- I'm proud to have been Robin.", "Parents, friends and lovers, you taught me, helped me, nursed me and cared for me…. Nightwing's got his act together. He's still going to do what he can to keep the world from spinning into chaos … but Dick Grayson needs some time to figure out what he wants. I want you to be proud of me, but even more importantly -- I want to be proud of myself. It may be a couple of days or weeks or even months, but I'll see you guys soon. Till then -- I love you.", "Try to understand our position here, Batman. You began training to be a hero as a young adult. For me and a lot of the other Titans -- like Vic -- that training shaped and influenced most of our childhood. Unlike the JLA, the Titans aren't just about a promise to the world -- it's also about a promise to each other … to ourselves. We swore on our childhood nightmares that we'd be there for one another. If I don't honor that I don't honor who I am.", "And I'm unique in this family, a talker among writers. Alfred's got his journal. You've got your files. Babs keeps an account of everything. While I've only ever recorded a message like this once before... the first time.", "Alfred always had faith that the dynamic duo could survive anything. Except maybe each other.", "Sometimes I'm surprised I can even stand on a high ledge after what happened to the Flying Graysons. Boss Zucco could have sabatoged Haly's Circus any number of ways to drive down business and get his protection money. Instead he gave the crowd that night a show they'll never forget. I know I won't. When my mom and dad died, attendance actually went up.", "What I've gotten is the realization that you did the best you could with what you had. You weren't a perfect father but that's okay because -- probably nobody's a perfect father. No family's perfect, either. I was lucky. I was privileged. Not because of the big house and the money, but because you gave me a lot of yourself. You taught me, you showed me, you encouraged me -- you never lied to me and you never demanded that I be anything I'm not. I didn't imitate you because you insisted that I do so, but because I wanted to. Of all the men I knew, you were most worthy of imitation.", "I've got one more thing to say. You and Alfred gave me a home and you gave me what we don't mention. The L word. You were the best family I could have had. Thanks.", "I've always taken it for granted that I'm fighting the good fight, I guess mostly due to my faith in Batman. But I have to admit, up here on the urban highwire, I take a lot of liberties. I tell myself they're all justified, but isn't that what everybody tells themselves? Does anybody wake up thinking, 'Today, I'm going to cross the line'?"]


def post():
    while True:
        ask = str(input("\nEnter the subreddit name: "))
        subreddit = reddit.subreddit(ask)
        print(f"Searching for {ask} subreddit...")

        try:
            for post in subreddit.hot(limit=10):
                for comment in post.comments:
                    if hasattr(comment, "body"):
                        comment_lower = comment.body.lower()
                        if "nightwing" in comment_lower:
                            random_index = random.randint(0, len(quotes) - 1)
                            comment.reply(quotes[random_index])
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
