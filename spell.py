import pyTTS
tts = pyTTS.Create()

words = ['leopard', 'tiger', 'panther', 'bozo']

num_right = 0

for word in words:
    tts.Speak("Please spell %s" % word)
    userword = raw_input()
    if userword == word:
        tts.Speak('Correct!')
        num_right += 1
    else:
        tts.Speak("Oh, sorry! It's %s." % word)
        for i in word:
            tts.Speak(i)

tts.Speak("You got %s out of %s!" % (num_right,len(words)))
