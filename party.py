## simple python party thing
## jibreil, may 2018

from time import sleep

sleep(1)
print("\n~~ Welcome to the digital invitation system for my Python Party ~~")
sleep(1)

print("\n~ Here's some information about the party")
sleep(1)

print("\n\t~ Date: Janurary 17th")
sleep(1)

print("\n\t~ Time: 6:30 PM")
sleep(1)

print("\n\t~ Location: 123 Sesame Street")
sleep(1)

name = str(input("\n~ What is your name?"))
sleep(0.5)

print("\n\t~ Thanks for answering " + name + ".")
sleep(1)

bring = str(
    input("\n~ Will you be bringing anything? (Please answer yes or no):"))
bring = bring.casefold()
sleep(0.5)

if bring == "yes":
    bringing = str(input("\n\t~ What will you be bringing?"))
    bringing = bringing.casefold()
    sleep(0.5)
    print("\n\t~ Thank you " + name + ".")
    sleep(1)
if bring == "no":
    print("\n\t~ That's okay, " + name + ".")
    bringing = str("nothing")
    sleep(1)

print("\n~ Here is a summary of the party for you " + name + ".")
sleep(1)

print("\n\t~ Date: Janurary 17th")
sleep(1)

print("\n\t~ Time: 6:30 PM.")
sleep(1)

print("\n\t~ Location: 123 Sesame Street")
sleep(1)

print("\n\t~ You said you will be bringing " + bringing + ".")
sleep(1)

confirmation = str(
    input("\n~ Is this all correct? (Please answer yes or no):"))
confirmation = confirmation.casefold()
sleep(0.5)

if confirmation == "yes":
    sleep(1)
    print("\n\t~ Great! Can't wait to see you there " + name + ".")
    sleep(1)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    quit()
if confirmation == "no":
    sleep(1)
    print("\n\t~ That's too bad," + name + ".")
    sleep(1)
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    quit()
