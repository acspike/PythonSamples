import random

def get_number(minimum, maximum, tries=3, recursion=0):
    if recursion >= tries:
        print "I won't play with you, if you can't type a number!"
        raise SystemExit
    try:
        return int(raw_input())
    except:
        print "That's not a number!"
        return get_number(minimum, maximum, tries, recursion + 1)

def guess(minimum, maximum, right_answer, tries=4, recursion=0):
    if recursion >= tries:
        return False

    print 'Guess:'    
    my_guess = get_number(minimum, maximum)
    if my_guess == right_answer:
        return True
    elif my_guess > right_answer:
        print "Too high!"
    elif my_guess < right_answer:
        print "Too low!"

    return guess(minimum, maximum, right_answer, tries, recursion + 1)

minimum = 1
maximum = 10
num = random.randint(minimum, maximum)

print 'I\'ve picked a number between %s and %s.' % (minimum, maximum)
try:
    if guess(minimum, maximum, num):
        print 'You rock!!!!!!!!!!'
        print "My number was indeed %s." % num
    else:
        print "You lose! My number was %s." % num
except SystemExit:
    pass
