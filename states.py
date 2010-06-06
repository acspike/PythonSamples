import random

# http://geography.about.com/od/lists/a/statecapitals.htm
text = '''Alabama - Montgomery
Alaska - Juneau
Arizona - Phoenix
Arkansas - Little Rock
California - Sacramento
Colorado - Denver
Connecticut - Hartford
Delaware - Dover
Florida - Tallahassee
Georgia - Atlanta
Hawaii - Honolulu
Idaho - Boise
Illinois - Springfield
Indiana - Indianapolis
Iowa - Des Moines
Kansas - Topeka
Kentucky - Frankfort
Louisiana - Baton Rouge
Maine - Augusta
Maryland - Annapolis
Massachusetts - Boston
Michigan - Lansing
Minnesota - St. Paul
Mississippi - Jackson
Missouri - Jefferson City
Montana - Helena
Nebraska - Lincoln
Nevada - Carson City
New Hampshire - Concord
New Jersey - Trenton
New Mexico - Santa Fe
New York - Albany
North Carolina - Raleigh
North Dakota - Bismarck
Ohio - Columbus
Oklahoma - Oklahoma City
Oregon - Salem
Pennsylvania - Harrisburg
Rhode Island - Providence
South Carolina - Columbia
South Dakota - Pierre
Tennessee - Nashville
Texas - Austin
Utah - Salt Lake City
Vermont - Montpelier
Virginia - Richmond
Washington - Olympia
West Virginia - Charleston
Wisconsin - Madison
Wyoming - Cheyenne'''

caps = {}
for line in text.split("\n"):
    state, capital = line.split(" - ")
    caps[state] = capital

states = caps.keys()
random.shuffle(states)

for state in states:
    print "What is the capital of %s?" % state
    correct = False
    for i in range(3):
        ans = raw_input()
        if ans == caps[state]:
            correct = True
            break
        else:
            print "Oops! :-("
    if correct:
        print "Yay!"
    else:
        print "The capital of %s is %s." % (state, caps[state])
