default linda_3rd_conv_done = False
default linda_4rd_con_done = False

label lindadate:
    if linda_1st_conv_done == False:
        jump linda1

    if linda_2nd_conv_done == False:
        jump linda2
    
    elif linda_3rd_conv_done == False:
        jump linda3

    elif linda_4rd_con_done == False:
        jump linda4