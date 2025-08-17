screen uniscreenlindaout2:
    frame:
        imagemap:
            ground "unilindaout.png"
            
            hotspot (39, 1202, 288, 225) action Jump("gardenuni_start2")




screen uniscreen2:
    if linda_conv_done == False and linda_4th_conv_done== False:
        frame:
            imagemap:
                ground "uni1.jpg"
                hover "uni1hover.jpg"
                hotspot (1879, 713, 281, 469) action Jump("lindadate")
                hotspot (52, 1150, 324, 262) action Jump("gardenuni_start2")
                
    elif linda_conv_done == True:
        frame:
            imagemap:
                ground "unilindaout.png"
                hover "unilindaouthover.png"
                hotspot (39, 1202, 288, 225) action Jump("gardenuni_start2")
    elif linda_conv_done == False and linda_4th_conv_done == True :
            frame:
                imagemap:
                    ground "unilindaout.png"
                    
                    hotspot (9, 1227, 221, 203) action Jump("gardenuni_start2")