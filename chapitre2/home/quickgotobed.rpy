label quickgotobed:
    stop background fadeout 0.5
    stop music fadeout 0.5
    if party_started == True:
        jump partydate
    $ quickbed = True
    jump textdirection