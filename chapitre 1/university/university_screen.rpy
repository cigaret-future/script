screen uniscreen:
    frame:
        imagemap:
            ground "uni1.jpg"
            hover "uni1hover.jpg"
            hotspot (1879, 713, 281, 469) action Jump("lindadate")
            hotspot (9, 1227, 221, 203) action Jump("gardenuni_start")
            


screen uniscreenempty:
    frame:
        imagemap:
            ground "uniempty.jpg"
            
            hotspot (9, 1227, 221, 203) action Jump("gardenuni_start")


screen uniscreenlindaout:
    frame:
        imagemap:
            ground "unilindaout.jpg"
            
            hotspot (9, 1227, 221, 203) action Jump("gardenuni_start")





