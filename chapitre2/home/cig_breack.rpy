label cigarettebreak:
    
    scene cig
    "I take a cigarette from my pack and get my lighter."
   
    scene smoking004
    
    "I put on some music to relax. The air is cool and the night is calm. I can see the lights of the city from my balcony."
    "I have a descent view from here."
    scene smoking005
    "The sounds from the café below enliven the street. I smoke my cigarette mechanically while listening to the music."
    ""
    ""
    ""
    ""
    "Suddenly, I hear a noise."

    
    sar "Hey, I hope I'm not bothering you."
    scene smoking006
    "I look up."
    "It's my upstairs neighbor."
    scene bothered

    sar "I'm trying to sleep. Can you turn down the music? Some of us have to get up early tomorrow."
    name "Oh, sorry. I just wanted to smoke a cigarette. I wasn't going to leave the music on for long."
    sar "Turn it down or close the window."
    scene smoking007
    name"Ok, ok, got it."
    scene turningoff
    stop music
    "Fuck, I don't want to start having issues with my neighbors..."
    $ sarah_pissed = True
    "I turn off the music and go back to the balcony. I hear the sound of a window closing."
    $ cig_break_count += 1
    "I smoke for a few more minutes, trying to relax. After a few minutes i toss it, and go to the bathroom"

    jump gotobed


label cigbreak1: 
    
    scene cig
    "I take a cigarette from my pack and get my lighter."
    scene smoking004
  
    "The air is cool and the night is calm. I can see the lights of the city from my balcony."
    "I have a descent view from here."
    scene smoking005
    "The sounds from the café below enliven the street. I smoke my cigarette mechanically."
    "I don't have much to do, maybe something will come up later"
    $ cig_break_count += 1
    jump gotobed