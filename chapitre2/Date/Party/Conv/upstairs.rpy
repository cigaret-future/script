label toiletparty:
    if drink_count >= 5:
        jump toiletscene
    else:
        jump toiletscene
    label toiletscene:   
        scene toiletscene
        "I enter the toilet."
        "I don't really feel like peeing, but at least now I know where it is."
        "It's a bit cramped, but at least it's clean."
        "I take a moment to gather myself before heading back to the party."
        jump upstairs
    label toiletscenebourre:
        scene drinkingpartybathroom
        ""

label partybathroom:
    if drink_count >= 5:
        scene drinkingpartybathroom
        "I enter the bathroom, feeling a bit dizzy from all the drinks."
        "Maybe I should slow down a bit."
        "I take a moment to splash some water on my face and gather myself."
        jump upstairs
    else:
        scene bathroompartyscene
        "I enter the bathroom."
        "Cool, I could come here to freshen up if I need to."
    jump upstairs