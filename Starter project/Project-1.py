# funny story creation using python

import time

def get_input(word_input: str):
    user_input = input(f"Enter a {word_input}: ")
    return user_input


noun1 = get_input("noun1")
subject1 = get_input("subject1")
noun2 = get_input("noun2")
subject2 = get_input("subject2")

story = f"""
Once upon a time there was {noun1}, who was a {subject1} teacher
and his student {noun2} who was {subject2} student. 

One day they were going for PI, and they had a conversation:

{noun1}: Ei chele tmi 1st semester na?
{noun2}: Assalamu-Aalaikum sir, ji sir!
{noun1}: Walaikumasslam! tmi etw late keno ajke?
{noun2}: sorry sir, ami ghum theke uthte late kore felsi! 😭
{noun1}: lol!
{noun2}: SIR.....?
{noun1}: Class e jao!
{noun2}: Okay sir, lol too!! ☕

Happy Java day everybody!
"""

for i in story:
    print(i, end="", flush=True)
    time.sleep(0.07)