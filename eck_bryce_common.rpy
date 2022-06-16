label eck_common_brycemv:
    
    if persistent.adinegoodending == True:
        if persistent.havemap == True:
            jump eck_bryce_maverickmap
        else:
            return
    else:
        return
    
label eck_common_bryce:
    
    python:
        if not persistent.eckbryceendingseena:
            persistent.eckbryceendingseena = "..."
            
        if not persistent.eckbryceendingseenb:
            persistent.eckbryceendingseenb = "..."
            
        if not persistent.eckbryceendingseenc:
            persistent.eckbryceendingseenc = "..."
            
        if not persistent.eckbryceendingseend:
            persistent.eckbryceendingseend = "..."
            
        if not persistent.eckbryceendingseene:
            persistent.eckbryceendingseene = "..."
            
        if not persistent.eckbryceendingseenf:
            persistent.eckbryceendingseenf = "..."

        if not persistent.eckbryceendingseeng:
            persistent.eckbryceendingseeng = "..."
    
    
    image eckcreditsbr = "cg/eckcreditsbr.jpg"
    image eckbryceendingseenimga = "cg/eckbryceendingseenimga.png"
    image eckbryceendingseenimgb = "cg/eckbryceendingseenimgb.png"
    image eckbryceendingseenimgc = "cg/eckbryceendingseenimgc.png"
    image eckbryceendingseenimgd = "cg/eckbryceendingseenimgd.png"
    image eckbryceendingseenimge = "cg/eckbryceendingseenimge.png"
    image eckbryceendingseenimgf = "cg/eckbryceendingseenimgf.png"
    image eckbryceendingseenimgg = "cg/eckbryceendingseenimgg.png"
    
    if brycegoodending == True:
        pass
    else:
        jump eck_bryce_stockbadending
    
    if persistent.brycegoodending == True:
        if persistent.adinegoodending == True:
            if eckbrycemappassed == True:
                if sebastiansaved == True or sebastianunplayed == False:
                    jump eck_bryce_rezaencounter
                else:
                    jump eck_bryce_stockgoodending
            else:
                jump eck_bryce_stockgoodending
        else:
            jump eck_bryce_stockgoodending
    else:
        jump eck_bryce_stockgoodending
        
label eck_bryce_goodendcredits:
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    $ _game_menu_screen = None
    stop sound fadeout 2.0
    $ renpy.pause (2.0)
    
    play sound "mx/spring.ogg"
    
    $ renpy.pause (1.5)
    show extra4 at Pan((-650, 0), (-750,0), 20.0)
    show eckcreditsbr at left
    with dissolvemed
    $ renpy.pause (10.0)
    
    $ renpy.pause (1.5)
    show fireworks at Pan ((-960, 545), (-200, 350), 20)
    show credits1 at left
    with dissolvemed
    $ renpy.pause (8.0)
    show black2 at left with dissolvemed
    show credits2 at left with dissolvemed
    $ renpy.pause (8.0)
    scene black with dissolvemed
    show tripwire at Pan ( (800, 0), (1000, 608), 20.0)
    show credits3 at right
    with dissolvemed
    $ renpy.pause (8.0)
    show black2 at right with dissolvemed
    show credits4 at right with dissolvemed
    $ renpy.pause (10.0)
    scene black with dissolvemed
    show bryceback at Pan((50, 900), (-600, 208), 25.0)
    show credits5 at left
    with dissolvemed
    $ renpy.pause (10.0)
    show black2 at left with dissolvemed
    show credits6 at left with dissolvemed
    $ renpy.pause (10.0)
    scene black with dissolvemed
    show cgmeeting at Pan ((740, 608), (1240, 0), 24)
    show credits7 at right
    with dissolvemed
    
    $ renpy.pause (10.0)
    show black2 at right with dissolvemed
    show credits8 at right with dissolvemed
    $ renpy.pause (10.0)
    scene black with dissolvemed
    
    show cgbryce
    show credits9 at left
    with dissolvemed
    
    $ renpy.pause (10.0)
    show black2 at left with dissolvemed
    show credits10 at left with dissolvemed
    $ renpy.pause (10.0)
    
    scene black with dissolvemed
    scene logo with dissolvemed
    $ renpy.pause (10.5)
    scene black with dissolvemed
    stop sound fadeout 1.4
    $ renpy.pause (4.0)
    $ persistent.anygoodending = True
    $ persistent.lastendingseen = "good"
    $ persistent.endingsseen += 1
    
    jump eck_bryce_aftercredits
    
    
label eck_bryce_badendcredits:
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    $ _game_menu_screen = None
    stop sound fadeout 2.0
    $ renpy.pause (2.0)
    
    play sound "mx/mindstream.ogg"
    
    $ renpy.pause (1.5)
    show cgcombat at Pan((-450, 0), (-750,0), 20.0)
    show eckcreditsbr at left
    with dissolvemed
    $ renpy.pause (8.0)
    
    $ renpy.pause (1.5)
    show fireworks at Pan ((-960, 545), (-200, 350), 20)
    show credits1 at left
    with dissolvemed
    $ renpy.pause (8.0)
    show black2 at left with dissolvemed
    show credits2 at left with dissolvemed
    $ renpy.pause (8.0)
    scene black with dissolvemed
    show tripwire at Pan ( (800, 0), (1000, 608), 20.0)
    show credits3 at right
    with dissolvemed
    $ renpy.pause (8.0)
    show black2 at right with dissolvemed
    show credits4 at right with dissolvemed
    $ renpy.pause (8.0)
    scene black with dissolvemed
    show bryceback at Pan((50, 900), (-600, 208), 25.0)
    show credits5 at left
    with dissolvemed
    $ renpy.pause (8.0)
    show black2 at left with dissolvemed
    show credits6 at left with dissolvemed
    $ renpy.pause (8.0)
    scene black with dissolvemed
    show cgmeeting at Pan ((740, 608), (1240, 0), 24)
    show credits7 at right
    with dissolvemed
    
    $ renpy.pause (8.0)
    show black2 at right with dissolvemed
    show credits8 at right with dissolvemed
    $ renpy.pause (8.0)
    scene black with dissolvemed
    
    show cgbryce
    show credits9 at left
    with dissolvemed
    
    $ renpy.pause (8.0)
    show black2 at left with dissolvemed
    show credits10 at left with dissolvemed
    $ renpy.pause (8.0)
    
    scene black with dissolvemed
    scene logo with dissolvemed
    $ renpy.pause (8.5)
    scene black with dissolvemed
    stop sound fadeout 1.4
    $ renpy.pause (4.0)
    $ persistent.anygoodending = True
    $ persistent.lastendingseen = "good"
    $ persistent.endingsseen += 1
    $ renpy.block_rollback()
    $ _game_menu_screen = None
    jump eck_bryce_aftercredits
    
label eck_bryce_aftercredits:
    
    jump mainmenu
    # Don't ask why this line is here