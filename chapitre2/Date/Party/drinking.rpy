label drinking:
    if stacydate_activated == True or tracymelaniedate_done == True and sebastianjen_date_started == True:
        scene kitchenarrownobodyblur
    elif sebastianjen_date_started == True:
        scene kitchenarrownojenblur

    elif stacydate_activated == True or tracymelaniedate_done == True:
        scene kitchenarrownomelblur
    elif sebastianjen_date_started == True:
        scene kitchenarrownojenblur
    
    else:
        scene kitchenarrow
        scene kitchenarrowflou with dissolve
    
    "I grab a beer and open it."
    "I take a few sips."
    "The taste is a bit bitter at first, but I get used to it quickly."
    "I start to feel a little more relaxed."
    "I take a few more sips while watching people chat around me."
    show text "Your mind blurs slightly." at Move((0.5, 0.6), (0.5, 0.5), 10.0)
    pause 5.0
    hide text with dissolve
    $ drink_count += 1



    jump kitchenparty