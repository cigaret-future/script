label hangoutdirection:
    menu:
        "smoke a cigarette":
            if cig_break_count == 0:
                jump cigbreak1
            elif cig_break_count == 1 and sarahcafe_conv1_done == False:
                jump cigarettebreak
            elif cig_break_count >= 1 and sarahcafe_conv1_done == True and sacha_sarah_date_done == False:
                jump sacha_sarah_date
            elif cig_break_count >= 2 and sarahcafe_conv1_done == False :
                jump cigbreak1
            else :
                jump cigbreak1
         
        
        
        "send a text to chloe" if raver_first_conv_done == True and raver_date_done == False:
                    if raver_not_over == True:
                        jump raver_date_0
                    elif raver_first_conv_done == True and raver_not_over == False and raver_date_done == False:
                        jump raver_date_1
            
        "Go to Sarah's place" if sarah_sagain_done == True:
            jump sarahsagain
