label quickgotobed:
    if party_started == True:
        jump partydate
    $ quickbed = True
    jump textdirection