#   Game idea:
#   Let's build a ship without looking at it (a text-based test of patience). Also pleases RNGesus.
#   
#   
#   Randomly picked options:
#   
#   Fail risks:
#   low: 5%
#   med: 10%
#   high: 20%
#   Can only fail if above 10 points completion
#   
#   Work on         Progress        Fail chance         Fail damage
#   
#   Hull                +2              low                 -2
#   Mast                +1              low                 -1
#   Handrails           +1              high                -1
#   Windows             +1              med                 -1
#   Interiors           +1              high                -2
#   Observation post    +1              med                 -1
#   
#   Decorations         +1              low                  0
#   Sails               +2              low                 -1
#   Props               +1              high                 0
#   Paint               +3              high                -3
#   Flags               +1              low                 -1
#   Ladders and stairs  +1              low                 -2
#   
#   Furniture           +1              low                 -1
#   Doors               +1              med                 -2
#   Prepare glue        +1              low                  0
#   Ropes and cables    +2              high                -2
#   Anchor              +1              low                 -1
#   Mechanics           +2              high                -3


#   Chaos_Knight - Yesterday at 22:16
#   Exactly
#   That was the idea
#   It will slowly change over like 5-6 stages
#   "I am not interested."
#   "This seems boring, let's do something else."
#   "It's getting annoying, let's take a break."
#   "I am fed up with this."
#   Selvy - 22:18
#   12 hours later
#   "RAAAAAARRGHHH!!!!!"
#   Chaos_Knight - 22:18
#   "I am so damn done with this."
#   "Screw this crap, I am out."
#   And then your last suggestion when  the number of turns exceeds the score cap +10-20%(edited)
#   For the unlucky ones XD
#   See? This can be entertaining even if it's a mind-numbingly boring "game".
#   Selvy - 22:22
#   I s'pose so














label eck_bryce_buildashipsetup:
    
    $ eckbryceshipprogress = 0
    $ eckbryceshipoption1rng = 0
    $ eckbryceshipoption2rng = 0
    $ eckbryceshipoption3rng = 0
    $ eckbryceshiptries = 0
    $ eckbryceshipskillroll = 0
    $ eckbryceshipfluff = 0
    $ eckbryceshipgriefstage = 0
    
    $ eckbryceshipfailurecheck = 0
    $ eckbryceshipfailurecheckmod1 = 0
    $ eckbryceshipfailurecheckmod2 = 0
    $ eckbryceshipfailurecheckmod3 = 0
    $ eckbryceshiprepeatfirst = 0
    $ eckbryceshiprepeatsecond = 0
    $ eckbryceshiprepeatthird = 0
    
    $ eckbryceshipquitearly = False
    $ eckbryceshipquitmid = False
    $ eckbryceshipquitlate = False
    
    show screen eckextrainfo 
    $ eckextradisplay = 2
    
    jump eck_bryce_buildashipgame
    
label eck_bryce_buildashipgame:
    
    $ eckbryceshipoption1rng = renpy.random.randint(1, 6)
    $ eckbryceshipoption2rng = renpy.random.randint(1, 6)
    $ eckbryceshipoption3rng = renpy.random.randint(1, 6)
    
    $ eckdisplayvar1name = "Ship completion:"
    $ eckdisplayvar1 = eckbryceshipprogress
    $ eckdisplayvar1unit = "%"
    $ eckdisplayvar2name = "Turns taken:"
    $ eckdisplayvar2 = eckbryceshiptries
    $ eckdisplayvar2unit = ""
    
    show bryce normal with dissolve
    if eckbryceshipprogress < 100:
        if eckbryceshiptries > 150:
            m "I couldn't believe we were still working on this. At least we were about [eckbryceshipprogress]%% done."
            m "The rest of the evening was nothing but a blur in my memory. At least, by the end of it, we were finally done with that cursed ship model."
            jump eck_bryce_buildashipaftermath
            $ eckbryceshipgriefstage = 8
        elif eckbryceshiptries > 140:
            m "I could barely contain my frustrations at that point. At least we were about [eckbryceshipprogress]%% done."
            $ eckbryceshipgriefstage = 7
        elif eckbryceshiptries > 120:
            m "I could barely contain my frustrations at that point. At least we were about [eckbryceshipprogress]%% done."
            $ eckbryceshipgriefstage = 6
        elif eckbryceshiptries > 100:
            m "I felt like my patience was quickly approaching the breaking point. In a way I admired Bryce's determination to finish the model, for he looked just as enthusiastic as he was at the start. And we were [eckbryceshipprogress]%% done."
            $ eckbryceshipgriefstage = 5
        elif eckbryceshiptries > 80:
            m "The longer we worked, the more I asked myself if I had it in me to reach the finish line. We were about [eckbryceshipprogress]%% done at that moment."
            $ eckbryceshipgriefstage = 4
        elif eckbryceshiptries > 60:
            m "Tiredness and frustration had fully shown their ugly faces, yet I felt like I had to keep on going to show Bryce my support. The model was about [eckbryceshipprogress]%% completed at that moment."
            $ eckbryceshipgriefstage = 3
        elif eckbryceshiptries > 40:
            m "My initial enthusiasm was gone completely by that point. And we just were about [eckbryceshipprogress]%% done."
            $ eckbryceshipgriefstage = 2
        elif eckbryceshiptries > 20:
            m "Ship modelling turned out even less exciting than I originally anticipated. At least I had nice company, and we were about [eckbryceshipprogress]%% finished."
            $ eckbryceshipgriefstage = 1
        else:
            m "While I didn't find ship modelling particulary interesting, it felt like a new fresh experience. We had just started with [eckbryceshipprogress]%% model completion."
            
        $ eckbryceshipfluff = renpy.random.randint(1, 3)
        if eckbryceshiprepeatfirst > 3:
            $ eckbryceshipfailurecheckmod1 = 4 * (eckbryceshiprepeatfirst - 3)
            $ eckbryceshipfailurecheckmod2 = 0
            $ eckbryceshipfailurecheckmod3 = 0
        elif eckbryceshiprepeatsecond > 3:
            $ eckbryceshipfailurecheckmod1 = 0
            $ eckbryceshipfailurecheckmod2 = 4 * (eckbryceshiprepeatsecond - 3)
            $ eckbryceshipfailurecheckmod3 = 0
        elif eckbryceshiprepeatthird > 3:
            $ eckbryceshipfailurecheckmod1 = 0
            $ eckbryceshipfailurecheckmod2 = 0
            $ eckbryceshipfailurecheckmod3 = 4 * (eckbryceshiprepeatthird - 3)
        else:
            $ eckbryceshipfailurecheckmod1 = 0
            $ eckbryceshipfailurecheckmod2 = 0
            $ eckbryceshipfailurecheckmod3 = 0
        
        menu:
            "Work on the hull." if eckbryceshipoption1rng == 1:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod1
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=2
                    if eckbryceshipfluff > 2:
                        m "We carefully assembled wooden pieces into larger panels as it was shown in the manual."
                    elif eckbryceshipfluff > 1:
                        m "Slowly but certainly, we managed to make some progress with the top deck."
                    else:
                        m "After a few minutes of assembly, we installed several pieces meant to be below the water line."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=2
                    if eckbryceshipfluff > 2:
                        m "My hand slipped while we were making the hull panels, which broke a few frail wooden pieces."
                        c "Oops. Sorry."
                        Br normal "It's all good."
                    elif eckbryceshipfluff > 1:
                        m "Accidentally, Bryce put too much pressure on the deck piece while installing it, which made several other elements crack."
                        Br stern "Damn it."
                        c "Don't worry about it."
                    else:
                        m "While attaching some elements to the ship's bottom, I misaligned some details we had attached earlier."
                        c "This is frustrating."
                        Br smirk "Now you know how I feel."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst += 1
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the masts." if eckbryceshipoption1rng == 2:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod1
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        "A large mast fit perfectly into its intended position."
                    elif eckbryceshipfluff > 1:
                        "It took some time, but we managed to successfully attach the traversing beam to the main mast."
                    else:
                        "One of the smaller masts slotted in right where we needed it."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=1
                    if eckbryceshipfluff > 2:
                        "I miscalculated the amount of strength needed and broke off a piece of deck while installing the mast."
                    elif eckbryceshipfluff > 1:
                        "Bryce tried to connect two pieces of the large mast together but ended up breaking both."
                    else:
                        "I brushed my elbow against one of the masts, which easily snapped it in half."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst += 1
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the handrails." if eckbryceshipoption1rng == 3:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 4 + eckbryceshipfailurecheckmod1
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "With great precision, we added a few handrails to the ship model using schematics and provided pictures for reference."
                    elif eckbryceshipfluff > 1:
                        m "Slowly and carefully, we assembled a new section of the ornate wooden handrails. It was ready for installation."
                    else:
                        m "Another section of handrails was now in place."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=1
                    if eckbryceshipfluff > 2:
                        m "While attaching some handrails, I accidentally glued together a couple of other elements I wasn't supposed to touch."
                        c "Do you think we can just wash the glue off?"
                        Br brow "I don't think so. We'll have to redo these."
                    elif eckbryceshipfluff > 1:
                        m "The frail thin wood of the handrails didn't survive Bryce's claws and crumbled into several small fragments."
                        Br stern "My hands will never be agile enough for this."
                        c "Remember, it's not about the result, it's about the journey."
                    else:
                        m "Adding one section of handrails accidentally broke off another, setting our progress back a little."
                        c "This is some vicious circle. The more we add, the more we break."
                        Br smirk "But we're getting there, [player_name]."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst += 1
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the windows." if eckbryceshipoption1rng == 4:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 2 + eckbryceshipfailurecheckmod1
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "We easily slotted several tiny plastic window panels into their corresponding wooden frames."
                    elif eckbryceshipfluff > 1:
                        m "We installed several small framed portholes on the top deck structure according to the manual."
                    else:
                        m "Without much trouble, we easily fit larger panels into the sides of the ship's main chassis."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=1
                    if eckbryceshipfluff > 2:
                        m "Too afraid to break the window, I didn't apply enough strength, which allowed it to fall out and glue itself to another element, ruining them both."
                        c "Alright, maybe I was too careful this time."
                        Br smirk "A little force won't hurt."
                    elif eckbryceshipfluff > 1:
                        m "Bryce tried to grab another window to put it in place but instead crushed it."
                        Br brow "Damn. It's pretty hard to limit your strength just right for this stuff."
                        c "Even I have to agree, and I'm much smaller than you are."
                    else:
                        m "Pushing the element too hard without noticing, I accidentally broke it and sent its fragments inside the ship. It took us some time to extract them all."
                        c "At least we didn't add glue to it yet."
                        Br stern "Yeah."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst += 1
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the interiors." if eckbryceshipoption1rng == 5:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 4 + eckbryceshipfailurecheckmod1
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "For many long minutes, we decorated the only quarters with visible interiors, which I assumed was the captain's."
                    elif eckbryceshipfluff > 1:
                        m "Even though the cargo hold was normally closed, this ship's model actually came with a few elements to install there."
                    else:
                        m "Assembling independent furniture felt like a nice change of pace compared to the larger ship components."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=2
                    if eckbryceshipfluff > 2:
                        m "With a single awkward move, I managed to deal some heavy damage to the ship's hull and deck."
                        Br smirk "Don't feel bad, [player_name]. Without your aid, I wouldn't have been able to reach that all."
                        c "I guess so."
                    elif eckbryceshipfluff > 1:
                        m "Bryce tried to install an element in the cargo hold but ended up breaking the hatch, its frame, and several other things."
                        Br stern "I should've let you deal with this. Your hands are way more agile."
                        c "Without the right tools, it's just as hard for me."
                    else:
                        m "During the furniture assembly we used a tad too much glue, which made some elements permanently get stuck together."
                        c "Looks like we're redoing these."
                        Br stern "Yeah."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst += 1
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the observation posts." if eckbryceshipoption1rng == 6:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 2 + eckbryceshipfailurecheckmod1
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "Despite the fragile nature of some details, we had little trouble assembling a crow's nest."
                    elif eckbryceshipfluff > 1:
                        m "We carefully attached one of the observation posts on top of a larger mast."
                    else:
                        m "To make it more life-like, we spent several minutes attaching ladders and ropes to the observation post."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=1
                    if eckbryceshipfluff > 2:
                        m "With a loud crack, the crow's nest was broken, and together with it a piece of mast."
                        Br stern "We'll never finish this."
                        c "Remember, it's just an exercise in patience."
                    elif eckbryceshipfluff > 1:
                        m "Trying to fit an observation post onto a mast, I applied too much pressure and ended up holding glue-covered debris against the smooth wooden surface."
                        Br smirk "And you told me to be patient."
                        c "I'm not perfect myself, you know."
                    else:
                        m "During the assembly of the observation post, Bryce dropped it onto the desk and broke a few other things while trying to pick it up."
                        Br stern "Damn it. I'm losing my patience again."
                        c "Stay calm, we can do this."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst += 1
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
            
            # =========================================================
            
            "Work on the decorations." if eckbryceshipoption2rng == 1:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod2
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "We added some beautiful-looking carvings and decorations to the ship."
                    elif eckbryceshipfluff > 1:
                        m "Fitting the nose centerpiece turned out to be harder than we expected, and it took quite a while."
                    else:
                        m "More and more carvings were put into their righteous places."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=0
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond += 1
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the sails." if eckbryceshipoption2rng == 2:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod2
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=2
                    if eckbryceshipfluff > 2:
                        m "Soon, several larger sails were unpacked, unrolled and ready for installation."
                    elif eckbryceshipfluff > 1:
                        m "Installing the sails was tricky, but eventually we got the hang of it."
                    else:
                        m "We installed some smaller sails on the upper parts of the bigger masts, as well as the ship's front."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=1
                    if eckbryceshipfluff > 2:
                        m "While unrolling a particulary large sail, I failed to keep track of my arms and nudged the main model, breaking a few small things."
                        c "Oh. Sorry about that."
                        Br smirk "It's all good. Happens to me all the time."
                    elif eckbryceshipfluff > 1:
                        m "We were hanging a sail when Bryce lost his patience for a moment and pushed the mast too hard, breaking off a piece of the horizontal beam."
                        Br stern "Why didn't the sail fit?"
                        c "I think it got caught up on the detail we just broke."
                    else:
                        m "Too occupied with the precise installation, we didn't notice how one of us had rested their arm against the ship, crushing several small elements."
                        c "We better watch what we lean on, Bryce."
                        Br brow "Yeah."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond += 1
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the props." if eckbryceshipoption2rng == 3:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 4 + eckbryceshipfailurecheckmod2
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "We found putting together assorted tiny objects rather refreshing in how consequence-free it was."
                    elif eckbryceshipfluff > 1:
                        m "It didn't take long for us to place a few things on the deck here and there."
                    else:
                        m "While I was busy assembling the props, Bryce placed a few of the finished ones on the ship."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=0
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond += 1
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the paintjob." if eckbryceshipoption2rng == 4:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 4 + eckbryceshipfailurecheckmod2
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=3
                    if eckbryceshipfluff > 2:
                        m "Even with my agile hands, I had some problems properly applying the paint to the finer details, but my efforts paid off."
                    elif eckbryceshipfluff > 1:
                        m "Bryce and I painted several hull and deck elements without much trouble."
                    else:
                        m "We carefully applied the paint to several decorative elements on the ship."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=3
                    if eckbryceshipfluff > 2:
                        m "Only after finishing the paintjob on one of the elements, we realized there was supposed to be something else attached to it."
                        Br brow "Do you think we can glue those things together?"
                        c "No, it won't hold over the paint. We'll have to start over."
                    elif eckbryceshipfluff > 1:
                        m "Too generous with the paint, Bryce ruined a few frail details, which were now glazed, distorting their shape badly."
                        c "Don't be so impatient, Bryce."
                        Br stern "I'm trying."
                    else:
                        m "With a single clumsy brush stroke of mine, several components got smeared in paint, some of which could not be cleaned by the solvent."
                        c "Looks like we'll have to replace those."
                        Br "Yeah."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "Awkwardly moving my arm, I swiped a can of paint off the table. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "Bryce decided to try his hand at painting some fine details before we installed them. It didn't work out well."
                    else:
                        m "I asked Bryce to hold a detail for me while I colored it. Too late, I realized that his claws were leaving permanent furrows on the painted surface."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond += 1
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the flags." if eckbryceshipoption2rng == 5:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod2
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "Tying colorful flags to ropes and cables was refreshingly easy and fun."
                    elif eckbryceshipfluff > 1:
                        m "A large fabric flag was proudly hoisted on top of the tall mast."
                    else:
                        m "We tied one end of the colorful line of flags to the mast, and attached the other to the handrails at the ship's front."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=1
                    if eckbryceshipfluff > 2:
                        m "My hand slipped, and the rope used to hold the flags cut right through a couple of smaller elements."
                        c "Sorry about that."
                        Br smirk "You're still a great help."
                    elif eckbryceshipfluff > 1:
                        m "While attempting to slot in the flag, Bryce misaligned the pole and pushed it too hard, snapping the mast."
                        Br "Sorry. This flag just got on my nerves."
                        c "Calm down and try to relax."
                    else:
                        m "We tried to affix a line of colorful flags but ended up dislocating several details from earlier."
                        c "Fix one thing, and two more will break."
                        Br "We'll get there, [player_name]."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond += 1
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the ladders and stairs." if eckbryceshipoption2rng == 6:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod2
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "Slowly, we assembled a couple of ladders step by step."
                    elif eckbryceshipfluff > 1:
                        m "With no other objects in the way, we easily installed a staircase segment."
                    else:
                        m "Bryce and I attached a long ladder to one of the masts and fixed it in place with glue."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=2
                    if eckbryceshipfluff > 2:
                        m "While installing a stairs segment, we accidentally broke several smaller details nearby."
                        Br "Damn it."
                        c "It's fine."
                    elif eckbryceshipfluff > 1:
                        m "As gently as he could, Bryce tried to attach a ladder to the large mast, and snapped both."
                        Br stern "This model is not designed for my claws."
                        c "I can see that."
                    else:
                        m "I didn't secure the components well enough during the ladder assembly, which made it fall apart and crumble on the deck."
                        c "This is too tricky."
                        Br "Agreed."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond += 1
                $ eckbryceshiprepeatthird = 0
                jump eck_bryce_buildashipgame
                
            # =========================================================
            
            "Work on the furniture." if eckbryceshipoption3rng == 1:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod3
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "We found putting together assorted tiny objects rather refreshing in how consequence-free it was."
                    elif eckbryceshipfluff > 1:
                        m "It didn't take long for us to place a few things on the deck here and there."
                    else:
                        m "While I was busy assembling the props, Bryce placed a few of the finished ones on the ship."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=0
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird += 1
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the doors and hatches." if eckbryceshipoption3rng == 2:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 2 + eckbryceshipfailurecheckmod3
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "Carefully, we slotted a door into its designated frame according to the manual."
                    elif eckbryceshipfluff > 1:
                        m "We placed some of the ornate hatches on the upper deck."
                    else:
                        m "We installed several door frames and fixed them in place with glue."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=2
                    if eckbryceshipfluff > 2:
                        m "A door got stuck while I was inserting it into the frame. I tried to push it and broke off a chunk of the wall."
                        Br stern "Easy there, [player_name]."
                        c "This will take a while to fix."
                    elif eckbryceshipfluff > 1:
                        m "Bryce tried to slot in a hatch but applied too much force and caused a section of the deck to cave in."
                        Br sad "This happens all the time to me."
                        c "Don't feel bad. Remember why we are doing this, Bryce."
                    else:
                        m "I wanted to fit the doorframe into the wall, but with too much glue on it, the excess stained the walls and several smaller objects."
                        Br brow "We'll need to replace those."
                        c "I see."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird += 1
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on preparing the glue." if eckbryceshipoption3rng == 3:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod3
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "We extracted a few more tubes of glue and placed them on the table for later use."
                    elif eckbryceshipfluff > 1:
                        m "I checked the glue application tools and quickly replaced the ones that got glazed over."
                    else:
                        m "We applied some glue to several elements and got ready to install them."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=0
                    if eckbryceshipfluff > 2:
                        m "I dropped a small tube of glue on the floor and stepped on it."
                    elif eckbryceshipfluff > 1:
                        m "Bryce squeezed the tube too hard and got his hands covered in glue. The solvent helped get it off his scales, though."
                    else:
                        m "Some elements we were preparing got stuck to the table."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "I dropped a small tube of glue on the floor and stepped on it."
                    elif eckbryceshipfluff > 1:
                        m "Bryce squeezed the tube too hard and got his hands covered in glue. The solvent helped get it off his scales, though."
                    else:
                        m "Some elements we were preparing got stuck to the table."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird += 1
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the ropes and cables." if eckbryceshipoption3rng == 4:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 4 + eckbryceshipfailurecheckmod3
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=2
                    if eckbryceshipfluff > 2:
                        m "Several cables were tightly coiled up, so we had to spend some time to unreel them."
                    elif eckbryceshipfluff > 1:
                        m "We connected sails, masts and the main ship hull using the ropes and cables."
                    else:
                        m "Following the manual, we attached several ropes to the nose part of the ship."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=2
                    if eckbryceshipfluff > 2:
                        m "I pulled too hard tying up a knot and snapped off a part of the horizontal mast plank."
                        Br smirk "It doesn't require such strong fastening, [player_name]."
                        c "That's true."
                    elif eckbryceshipfluff > 1:
                        m "Bryce's fingers became entangled in a long cable, which caused him to break a handrail when he tried to free himself."
                        Br stern "Those ropes are the worst part."
                        c "I agree."
                    else:
                        m "A couple of cables crossed each other and, before we noticed, one of them pushed the other aside, causing some damage to the ship along the way."
                        Br stern "It's hard to keep track of all the ropes."
                        c "Yeah. They're like a cobweb."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird += 1
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the metallic elements." if eckbryceshipoption3rng == 5:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 1 + eckbryceshipfailurecheckmod3
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=1
                    if eckbryceshipfluff > 2:
                        m "We attached several chains to their designated places."
                    elif eckbryceshipfluff > 1:
                        m "With some fiddling, we managed to guide the chain and properly attach the anchor."
                    else:
                        m "Soon, several metal inserts and details were properly added to the ship."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=1
                    if eckbryceshipfluff > 2:
                        m "Because of my careless anchor chain pull, a couple of elements ended up misaligned."
                        Br stern "Be careful with that."
                        c "Sorry, my bad."
                    elif eckbryceshipfluff > 1:
                        m "We glued one of the metal insert panels in the wrong place, ruining a section of the hull wall in the process."
                        Br brow "This isn't right."
                        c "I think we've misread the manual."
                    else:
                        m "Tightening the chains coiled around some wooden parts, Bryce accidentally snapped several frail pieces."
                        c "Be careful there."
                        Br laugh "Easy for someone with your hands to say."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird += 1
                jump eck_bryce_buildashipgame
                
                #-----------------------------------------------------------
            "Work on the mechanical parts." if eckbryceshipoption3rng == 6:
                $ eckbryceshipskillroll = renpy.random.randint(1, 20)
                $ eckbryceshipfailurecheck = 4 + eckbryceshipfailurecheckmod3
                if eckbryceshipskillroll > eckbryceshipfailurecheck:
                    $ eckbryceshipprogress +=2
                    if eckbryceshipfluff > 2:
                        m "Slowly, through trial and error, we managed to fit a part of the rudder control system inside the ship."
                    elif eckbryceshipfluff > 1:
                        m "Soon, a rudder was installed."
                    else:
                        m "After many long minutes of careful work, I installed the steering wheel."
                    
                elif eckbryceshipprogress > 10:
                    $ eckbryceshipprogress -=3
                    if eckbryceshipfluff > 2:
                        m "Because of our poor skills, installing the control system caused severe damage to the ship's interiors."
                        c "I don't think anyone would notice, but I'm not sure if the ship will hold together."
                        Br smirk "Let's set it right, then."
                    elif eckbryceshipfluff > 1:
                        m "With a single move, I cracked both the steering wheel and the frame it was attached to."
                        Br stern "This will take a while to fix."
                        c "I know."
                    else:
                        m "Because of our poor skills, installing the control system caused severe damage to the ship's interiors."
                        c "I don't think anyone would notice, but I'm not sure if the ship will hold together."
                        Br smirk "Let's set it right, then."
                    
                else:
                    if eckbryceshipfluff > 2:
                        m "A few details somehow jumped out of the packaging and fell to the floor. Thankfully, no damage was done."
                    elif eckbryceshipfluff > 1:
                        m "While extracting some smaller elements, Bryce accidentally snapped a few of them. It wasn't a problem with the amount of spare parts we had, though."
                    else:
                        m "I started the pre-assembly of a complex element when Bryce brushed my arm with his elbow. While it didn't break anything, my progress was reset."
                        
                    
                $ eckbryceshiptries +=1
                $ eckbryceshiprepeatfirst = 0
                $ eckbryceshiprepeatsecond = 0
                $ eckbryceshiprepeatthird += 1
                jump eck_bryce_buildashipgame
                
            "RAAAAAARRGHHH!" if eckbryceshipgriefstage == 7:
                $ eckbryceshipquitlate = True
                Br stern "Hey, no need to get violent, [player_name]. Please don't break anything. We worked so hard on that model."
                c "I'm sorry, I just couldn't take it anymore."
                jump eck_bryce_buildashipaftermath
                
            "Screw this crap, I'm out." if eckbryceshipgriefstage == 6:
                $ eckbryceshipquitlate = True
                jump eck_bryce_buildashipaftermath
                
            "That's it. I'm done. I'm freaking done with this." if eckbryceshipgriefstage == 5:
                $ eckbryceshipquitlate = True
                jump eck_bryce_buildashipaftermath
                
            "I'm getting fed up with this. It's time to stop." if eckbryceshipgriefstage == 4:
                $ eckbryceshipquitmid = True
                jump eck_bryce_buildashipaftermath
                
            "Honestly, this is getting annoying. Let's take a break." if eckbryceshipgriefstage == 3:
                $ eckbryceshipquitmid = True
                jump eck_bryce_buildashipaftermath
                
            "I'm starting to get bored. Maybe we should do something else?" if eckbryceshipgriefstage == 2:
                $ eckbryceshipquitearly = True
                jump eck_bryce_buildashipaftermath
                
            "You know, this isn't very interesting." if eckbryceshipgriefstage == 1:
                $ eckbryceshipquitearly = True
                jump eck_bryce_buildashipaftermath
            
    else:
        jump eck_bryce_buildashipaftermath
    