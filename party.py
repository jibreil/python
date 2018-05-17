## Simple python party thingo
## Jibreil, May 2018

from time import sleep

sleep(1)
print("\n ~~ Welcome to the digital invitation system for my Python Party ~~")
sleep(1)

print("\n ~ Here's some information about the party")
sleep(1)

print("\n\t ~ Date: Janurary 17th")
sleep(1)

print("\n\t ~ Time: 6:30 PM")
sleep(1)

print("\n\t ~ Location: 123 Sesame Street")
sleep(1)

name = input("\n ~ What is your name? ")
sleep(0.5)

print("\n\t ~ Thanks for answering " + name + ".")
sleep(1)

bring = input("\n ~ Will you be bringing anything? (Yes/No): ")
sleep(0.5)

if bring == "Yes":
    bringing = input("\n\t ~ What will you be bringing? ")
    sleep(0.5)
    print("\n\t ~ Thank you " + name + ".")
    sleep(1)
if bring == "No":
    print("\n\t ~ That's okay, " + name + ".")
    sleep(1)

print("\n ~ Here is a summary of the party for you " + name + ".")
sleep(1)

print("\n\t ~ Date: Janurary 17th")
sleep(1)

print("\n\t ~ Time: 6:30 PM.")
sleep(1)

print("\n\t ~ Location: 123 Sesame Street")
sleep(1)

print("\n\t ~ You said you will be bringing " + bringing + ".")
sleep(1)

confirmation = input("\n ~ Is this all correct? (Yes/No): ")
sleep(0.5)

if confirmation == "Yes":
    sleep(1)
    print("\n\t ~ Great! Can't wait to see you there " + name + ".")
    sleep(1)
    quit()
if confirmation == "No":
    sleep(1)
    print("\n\t ~ That's too bad," + name + ".")
    sleep(1)
    quit()
