import pyautogui
import random
import time

mylist = [
    "David proudly graduated from high school top of his class at age 97.",
    "He decided to count all the sand on the beach as a hobby.",
    "It must be easy to commit crimes as a snake because you don't have to worry about leaving fingerprints.",
    "Nothing seemed out of place except the washing machine in the bar.",
    "She felt that chill that makes the hairs on the back of your neck when he walked into the room",
    "Art doesnt have to be intentional.",
    "If any cop asks you where you were, just say you were visiting Kansas.",
    "A suit of armor provides excellent sun protection on hot days.",
    "While on the first date he accidentally hit his head on the beam.",
    "You should never take advice from someone who thinks red paint dries quicker than blue paint.",
    "At that moment I was the most fearsome weasel in the entire swamp.",
    "On a scale from one to ten, what's your favorite flavor of random grammar?",
    "Charles ate the french fries knowing they would be his last meal.",
    "The near-death experience brought new ideas to light.",
    "Giving directions that the mountains are to the west only works when you can see them.",
    "He looked behind the door and didn't like what he saw.",
    "She was too short to see over the fence.",
    "UHaul trucks bring back bad memories for us.",
    "The door swung open to reveal pink giraffes and red elephants.",
    "Blue sounded too cold at the time and yet it seemed to work for gin.",
]

# print(random.choice(mylist))

time.sleep(5)
while True:
    a = random.choice(mylist)
    pyautogui.write(a, interval=0.10)
    pyautogui.PAUSE = 1
    pyautogui.press('enter')

