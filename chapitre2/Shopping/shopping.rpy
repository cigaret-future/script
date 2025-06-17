label shop:
    if groceries >= 1:
        show map1
        "I already have everything I need."
        
        jump map3
    elif groceries <= 0:
        scene store 
        "I walk into the store."
        "Looking at the prices on the shelves."
        "I pick my items, trying to keep my budget in mind. "
        $ groceries = 4
        $ money -= 50
        show text "-100$" at Move((0.5, 0.6), (0.5, 0.5), 2.0) 
        hide text with dissolve
                
        "I pay for my groceries and leave the store."
        jump map3