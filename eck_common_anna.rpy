label eck_common_anna:
    
    image eckcreditsan = "cg/eckcreditsan.jpg"
    image eckannaendingseenimga = "cg/eckannaendingseenimga.png"
    image eckannaendingseenimgb = "cg/eckannaendingseenimgb.png"
    image eckannaendingseenimgc = "cg/eckannaendingseenimgc.png"
    image eckannaendingseenimgd = "cg/eckannaendingseenimgd.png"
    image eckannaendingseenimge = "cg/eckannaendingseenimge.png"
    image eckannaendingseenimgf = "cg/eckannaendingseenimgf.png"
    image eckannaendingseenimgg = "cg/eckannaendingseenimgg.png"
    image eckannaendingseenimgh = "cg/eckannaendingseenimgh.png"
    image eckannaendingseenimgi = "cg/eckannaendingseenimgi.png"
    
    #(Lisa Purple-red name tag)
    #I don't need to test if the player already got an ending, those variables and achieves are taken care of after the credits

    #If's as set by Wyvernosis
    #(Adine needs to survive, needs to be on a good status with you, and you need to have the romance with Anna.)

    #annaromance
        #You can only be on good status with anna if you sleep with her and play all 4 scenes
            # $ annastatus = "good"
            # $ annascenesfinished = 4

    #Adine alive
            # $ adinedead = False

    #Adine stats
            # if adinestatus == "abandoned":

            #or
            #adinestatus = "neutral" and adinescenesfinished = 3
            #If the player uses skip they cannot get adinestatus = good in chanp3 adine scene

    
    python:
        if not persistent.eckannaendingseena:
            persistent.eckannaendingseena = "..."
            
        if not persistent.eckannaendingseenb:
            persistent.eckannaendingseenb = "..."
            
        if not persistent.eckannaendingseenc:
            persistent.eckannaendingseenc = "..."
            
        if not persistent.eckannaendingseend:
            persistent.eckannaendingseend = "..."
            
        if not persistent.eckannaendingseene:
            persistent.eckannaendingseene = "..."
            
        if not persistent.eckannaendingseenf:
            persistent.eckannaendingseenf = "..."

        if not persistent.eckannaendingseeng:
            persistent.eckannaendingseeng = "..."
            
        if not persistent.eckannaendingseenh:
            persistent.eckannaendingseenh = "..."
            
        if not persistent.eckannaendingseeni:
            persistent.eckannaendingseeni = "..."
    
    #time for the fun if's
    #Added one which checks if Adine is actually "impressed" by you. EvilChaosKnight.
    if annastatus == "good":
        if annascenesfinished == 4:
            if adinedead == False:
                if adinescenesfinished == 3:
                    if adinestatus == "good":
                        jump eck_annashappyend
                        
                    else:
                        jump eck_anna_stockcredits
                else:
                    jump eck_anna_stockcredits
            else:
                jump eck_anna_stockcredits
        else:
            jump eck_anna_stockcredits
    else:
        jump eck_anna_stockcredits


#large italic font: Times new roman size 50
#sub font: Lato light (not quite right but close enough)
#Thanks for the font info. I wonder if using gallery images for credits is frowned upon? Oh well. EvilChaosKnight.
#The beginning of the games Credits
label eck_anna_customcredits:
    $ persistent.eckannacured = True
    stop music fadeout (2.0)

    $ renpy.pause (1.2)

    $ _game_menu_screen = None

    stop sound fadeout 2.0

    play sound "mx/sweetmemories.ogg" fadein 0.5

    show extra2 at Pan ((450, 0), (540,0), 20.0)
    show eckcreditsan at right
    with dissolvemed

    $ renpy.pause (12.0)

    scene black with dissolvemed

    show extra8 at Pan ((0, 0), (-360,0), 20.0)
    show credits1 at left
    with dissolvemed

    $ renpy.pause (8.0)

    show black2 at left with dissolvemed

    show credits2 at left with dissolvemed

    $ renpy.pause (8.0)

    return

label eck_anna_customcredits2:
    $ persistent.eckannacured = True
    stop music fadeout (2.0)

    $ renpy.pause (1.2)

    $ _game_menu_screen = None

    stop sound fadeout 2.0

    play sound "mx/fragilemind.ogg" fadein 0.5

    show extra2 at Pan ((450, 0), (540,0), 20.0)
    show eckcreditsan at right
    with dissolvemed

    $ renpy.pause (12.0)

    scene black with dissolvemed

    show rezathroatslit at Pan ((500, 326), (1280,0), 20.0)
    show credits1 at left
    with dissolvemed

    $ renpy.pause (8.0)

    show black2 at left with dissolvemed

    show credits2 at left with dissolvemed

    $ renpy.pause (8.0)

    return
    

label eck_anna_stockdeathoutcome:
    
    nvl clear
    window show

    n "A few days later, she passed away quietly in her sleep."
    $ annadead = True
    n "The council held a funeral in her honor, which I didn't attend."
    n "Now that I had been with Anna until the end, I had a decision to make."
    n "I could either stay here, accept this outcome and all its consequences, or, by using the portal and Izumi's coordinates, travel back in time and return to the day of my arrival in this world."
    n "This way, I could get the chance to try again."
    n "No doubt, it would be a risk to relive this rollercoaster of emotions. After all, I would have to go through all the events and their dangers again, but maybe it would be worth it..."
    stop music fadeout 2.0
    window hide
    $ renpy.pause (2.0)
    
    if eckannacurrentending == "stock":
        jump eck_anna_midendingstock
    elif eckannacurrentending == "E":
        jump eck_anna_midendinge
    elif eckannacurrentending == "F":
        jump eck_anna_midendingf
    else:
        return
    
label eck_anna_stockcredits:
    scene black with dissolveslow
    $ renpy.pause (2.0)
    $ eckannacurrentending = "stock"
    jump eck_anna_stockdeathoutcome
    label eck_anna_midendingstock:
        play sound "fx/system.wav"
        s "Looks like you've got a default (\"bad\") good ending."
        s "Kinda defeats the whole purpose of this mod, doesn't it? Don't be shy to load a save and try again, if you wish. I won't tell anyone, promise."
        s "The requirements are pretty elaborate, though (see ReadMe for details), so you might have to start over from the beginning if you want to meet them. Either way, good luck, [player_name]!"
    
label eck_anna_stockcredits2:
    $ renpy.pause (3.0)
    $ _game_menu_screen = None
    stop sound fadeout 2.0

    #Stock credits
    play sound "mx/fragilemind.ogg" fadein 0.5

    show rezathroatslit at Pan ((500, 326), (1280,0), 20.0)
    show credits1 at left
    with dissolvemed

    $ renpy.pause (8.0)

    show black2 at left with dissolvemed
    show credits2 at left with dissolvemed

    $ renpy.pause (8.0)

    return