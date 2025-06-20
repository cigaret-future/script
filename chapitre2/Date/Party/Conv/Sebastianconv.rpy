label sebastianconv:
    seb "Hey, [player]!"
    name "Hey there..."
    seb "How's it going?"
    name "I'm good, just walking around a bit."
    seb "Nice, you seem like a pretty chill guy."
    seb "It's good to see."
    name "Yeah, sure."
    seb "Want to grab a drink?"
    name "Yeah, sounds good."
    seb "Here you go."
    "I take the beer Sebastian hands me and take a sip."
    $ drink_count += 1
    show text "Your mind feels a bit fuzzy." at Move((0.5, 0.6), (0.5, 0.5), 10.0)
    pause 5.0
    hide text with dissolve
    seb "So, what do you do?"
    name "Uh, I'm a student. I'm doing a master's in art history."
    seb "That's cool, I'm really interested in that field."
    seb "I've always been fascinated by art and its impact on society."