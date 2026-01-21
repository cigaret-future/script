label articlework:
    
    
    scene home00
    if marion_conv_count == 0:
        "I should probably talk to my supervisor."
        show screen homescreen4
        call screen homescreen4
    if articlework_done == True:
        "I've already worked on my article today."
        show screen homescreen4
        call screen homescreen4
    scene homelaptopworking with dissolve
    
    "I sit down on my couch and open my laptop."
    
    "The document with my draft article pops up on the screen."
    "The cursor blinks at the end of a half-finished sentence, waiting for me to do something with it."

    "I take a breath, straighten my back, and force myself to focus."
    "I start typing."
    play sound keyboardtyping volume 1 loop
    "If I want Mrs. Gillberg to take me seriously, I need to make real progress on this."

    "One phrase at a time."
    
    "..."
    "with each word, I feel more confident."
    "I erase some sentences, rephrase others, and add new ideas."
    "After a while, I look at the clock."
    scene black with dissolve
    "I think I've done enough for now."
    $ articlework_done = True

    $ import random
    $ article_progress += int(renpy.random.uniform(3, 5))
    
    stop sound 
    show screen homescreen4
    call screen homescreen4
    