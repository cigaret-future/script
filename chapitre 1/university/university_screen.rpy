screen uniscreen:
    frame:
        imagemap:
            ground "uni1.jpg"
            hover "uni1hover.jpg"
            hotspot (1879, 713, 281, 469) action Jump("lindadate")
            hotspot (60, 1149, 337, 261) action Jump("gardenuni_start")
            


screen uniscreenempty:
    frame:
        imagemap:
            ground "uniempty.png"
            hover "uniemptyhover.png"
            hotspot (27, 1189, 309, 233) action Jump("gardenuni_start")


screen uniscreenlindaout:
    frame:
        imagemap:
            ground "unilindaout.png"
            hover "unilindaouthover.png"
            hotspot (60, 1149, 337, 261) action Jump("gardenuni_start")





