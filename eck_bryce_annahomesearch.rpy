#   Cheat sheet :D
#
#   g3n3t1cs
#   st4ystr0ng
#   1753
#   15, 61, 23, 5 and 87























label eck_bryce_annabedroom:
    $ renpy.pause (2.0)
    show sebastian normal b flip at left with dissolve
    show naomi normal b at right with dissolve
    
    if eckbrycebedvisited == True:
        jump eck_bryce_annabedsearch
    else:
        pass
    
    Nm "A cozy place."
    Sb "It's a little too minimalistic and cold for me. I prefer wooden furniture rather than plastic and metal."
    Nm smile b "The computer desk is made of wood."
    Sb smile b flip "You know what I mean."
    Nm normal b "That you prefer more classic natural looks, yeah."
    c "(I could've sworn this room in particular feels familiar.)"
    c "Personally, I'd say it has a good balance of style and practicality. Reminds me a lot of how apartments used to be back on Earth."
    c "I wonder where the dresser or wardrobe is, though?"
    Nm smile b "..."
    Sb "..."
    c "Right..."
    Nm normal b "Thanks for the laugh, [player_name], but let's not stray away from our objective."
    Sb normal b flip "Yeah."
    $ eckbrycebedvisited = True
    
    label eck_bryce_annabedsearch:
        
        menu:
            "Look under the bed.":
                m "Meeting face to face with a large spider was an unpleasant surprise. Nothing else of interest."
                jump eck_bryce_annabedsearch
                
            "Search the bag.":
                m "Large and spacious, the travelling bag was completely empty. The amount of scratches and wear on it, however, suggested that it had seen the wilderness a few times."
                jump eck_bryce_annabedsearch
                
            "Check the bookshelf." if eckbrycebedbooks == False:
                $ renpy.pause (2.0)
                $ eckbrycebedbooks = True
                c "Look at all those books. I have some expertise in biology and even I can't understand what most of the titles could be about."
                Sb drop b flip "Too much science."
                Nm blank b "I know some of those terms but nothing about the subjects."
                show sebastian normal b flip with dissolve
                m "One tome after another, we skimmed through each volume and checked if something was hidden between the pages."
                Sb smile b flip "Bingo!"
                c "Got something interesting?"
                Sb normal b flip "No. Just an old lottery ticket."
                Nm shy b "I play it too sometimes. Never won anything, but I might get lucky one day."
                c "Hope always dies last."
                Nm smile b "True."
                c "What were the winning numbers, Seb?"
                Sb "15, 61, 23, 5 and 87 if you're curious. It's already redeemed, so don't count on any easy money."
                show naomi normal b with dissolve
                jump eck_bryce_annabedsearch

            "Check the bookshelf." if eckbrycebedbooks:
                m "Nothing of interest here besides the redeemed lottery ticket with winning numbers of 15, 61, 23, 5 and 87."
                jump eck_bryce_annabedsearch
                
            "Access the computer.":
                $ renpy.pause (2.0)
                if eckbryceannaarchiveopen == True:
                    show eckannacompexplorer5 with fade
                    jump eck_bryce_annacomputer4
                elif eckbrycepcopen == True:
                    show eckannacompexplorer2 with fade
                    jump eck_bryce_annacomputer2
                else:
                    show eckannacomplogon with dissolve
                    jump eck_bryce_annapclogon
                
            "Leave.":
                stop music fadeout (2.0)
                $ renpy.pause (2.0)
                scene black with dissolve
                play music "mx/martyr.ogg"
                $ renpy.pause (2.0)
                jump eck_bryce_annahomesearch

label eck_bryce_annapclogon:
    menu:
        "Enter the password.":
            $ eckanpw = renpy.input(_("Password:"), exclude='{%}', length=20)
            play sound2 "fx/keyboard.ogg"
            $ renpy.pause (3.5)
            
            if eckanpw == _("st4ystr0ng") and eckanpwtries > 0:
                s "Welcome!"
                jump eck_bryce_annacomputer
    
            elif eckanpwtries > 0:
                $ eckanpwtries -=1
                s "Wrong password. Tries left: [eckanpwtries]."
                jump eck_bryce_annapclogon
                
            else:
                m "Lockdown in effect. Please contact your administrator to reset the system."
                Sb disapproval b flip "We got locked out."
                Nm stern b "So much for exploring the files."
                jump eck_bryce_annapclogon
                
        "Shut down the computer.":
            
            $ renpy.pause (2.0)
            hide eckannacomplogon with fade
            jump eck_bryce_annabedsearch

label eck_bryce_annacomputer:
    $ eckbrycepcopen = True
    show eckannacompexplorer
    hide eckannacomplogon
    with fade
    
    c "We're in."
    Nm "Good job, [player_name]."
    Sb "She has three hard drives loaded with files, though. Navigating them all will take ages."
    c "Let's see the list of recently visited locations. That should give us some hints. And... I think this should be the work folder."
    
    hide eckannacompexplorer
    show eckannacompexplorer2 
    with fade
    
    Nm "Hm, I expected more."
    c "It's her personal home computer. Most of the mainline research data is probably stored somewhere in the production facility."
    Sb "Should we check her mail as well?"
    Nm "Don't you think we're invading her privacy enough already?"
    c "We can't access it, anyway. The network is shown to be working, but it's not responding."
    Sb "Oh well."
    c "What folder should we go for?"
    Nm "It's probably the one called \"Cure Project\"."
    Sb "Agreed. The most obvious one."
    
label eck_bryce_annacomputer2:
    menu:
        "Open the Cure Project folder." if eckbrycecureprojectfirst:
            c "Here it comes."
            hide eckannacompexplorer2
            show eckannacompexplorer3
            with fade
            
            Nm "Not a whole lot of files here. But this archive looks interesting."
            c "File size is huge, too."
            Sb "Let's see what's inside."
            $ eckbrycecureprojectfirst = False
            jump eck_bryce_annacomputer3
            
        "Open the Cure Project folder." if eckbrycecureprojectfirst == False:
            hide eckannacompexplorer2
            show eckannacompexplorer3
            jump eck_bryce_annacomputer3
            
        "Check the notes.":
            m "\"Don't forget to call the production department tomorrow about the quality of their goods. We keep getting complaints.\""
            m "\"Buy new beakers. Those idiot cops just had to trash my equipment.\""
            m "\"Call in the computer tech assistants to take a look at the faulty lab comp. The damn thing crashed twice on me.\""
            jump eck_bryce_annacomputer2
            
        "Check the scans.":
            m "Copies of standard lab reports on the official projects, including one from Reza's case. Boring and perfectly legal."
            jump eck_bryce_annacomputer2
            
        "Check the assignments.":
            m "The database contained the list of pending research as well as several smaller tasks mentioned separately. Nothing of interest, though."
            jump eck_bryce_annacomputer2
            
        "Shut down the computer.":
            hide eckannacompexplorer2 with fade
            c "We can return to it later. I want to look for something else right now."
            Nm blank b "If you say so."
            jump eck_bryce_annabedsearch
            
label eck_bryce_annacomputer3:
    $ eckdisplayvar1 = eckbryceannaclues
    menu:
        "Check the archive." if eckbryceannapcarchunchecked:
            c "Might as well."
            hide eckannacompexplorer3
            show eckannacompexplorer4
            
            Nm "I've yet to see a person who bought it."
            Sb "Wait, you own a computer, and I'm sure I've seen you use this program."
            Nm "Yes?"
            Sb "..."
            c "..."
            Nm "It's too expensive! Not to mention how hard it is to pay for things online."
            Sb "Can't blame you."
            Nm "Makes me wonder how they're making profits, though."
            $ eckbryceannapcarchunchecked = False
            
            hide eckannacompexplorer4
            show eckannacompexplorer5
            
            c "Great. Another password."
            Sb "Something has to be here."
            
            label eck_bryce_annacomputer4:
                menu:
                    "Enter the password.":
                        $ eckanpw = renpy.input(_("Password:"), exclude='{%}', length=20)
                        play sound2 "fx/keyboard.ogg"
                        $ renpy.pause (3.5)
                    
                        if eckanpw == _("g3n3t1cs"):
                            c "We're in."
                            jump eck_bryce_annaarchives
                
                        else:
                            s "Invalid password."
                            jump eck_bryce_annacomputer4
                        
                    "Check other files":
                        hide eckannacompexplorer5
                        show eckannacompexplorer3
                        jump eck_bryce_annacomputer3
                        
                    "Leave the computer.":
                        $ eckbryceannaarchiveopen = True
                        hide eckannacompexplorer5 with fade
                        jump eck_bryce_annabedsearch
                
        "Check the archive." if eckbryceannapcarchunchecked == False and eckbryceannagotpcevidence == False:
            hide eckannacompexplorer3
            show eckannacompexplorer5
            with fade
            jump eck_bryce_annacomputer4
                
        "Check the notes." if eckbryceannapcnoteunchecked:
            Nm "That's a whole list of experiments. But they're all marked as failures. Some of those are certainly outside of the conditions for Anna's suspended sentence."
            $ eckbryceannapcnoteunchecked = False
            $ eckbryceannaclues +=1
            c "That might be debatable. Nothing here goes against the regulations from what I can see."
            Sb "Correct. But some of these require additional permissions. We'll see if Anna has them."
            jump eck_bryce_annacomputer3
            
        "Check the scan." if eckbryceannapcscanunchecked:
            c "Huh. That's my blood test results."
            $ eckbryceannapcscanunchecked = False
            Nm "90%% genetic similarity? Woah, impressive."
            Sb "I don't get it."
            Nm "It means that humans and dragons share 90%% of their genetic structure, Seb. True, we are like 60%% genetically similar to trees, but at least they come from the same planet as we do."
            Nm "[player_name] is an alien, yet only has 10%% difference in the DNA. To put things into perspective, you and I are just 5%% different."
            Sb "That is pretty curious."
            Nm "If I didn't know any better, I'd have said that [player_name] comes from our world as well."
            c "(I'm not sure I want any further development on this line of thought.)"
            $ eckbryceannaclues +=1
            c "Either way, we have another minor clue. Let's move on."
            Sb "Yeah."
            jump eck_bryce_annacomputer3
            
        "Go back.":
            c "Let's take a look at the previous folder."
            hide eckannacompexplorer3
            show eckannacompexplorer2
            
            jump eck_bryce_annacomputer2
            
        "Shut down the computer.":
            hide eckannacompexplorer3 with fade
            c "We can return to it later. I want to look for something else right now."
            Nm blank b "If you say so."
            jump eck_bryce_annabedsearch
            
label eck_bryce_annaarchives:
    $ eckbryceannaclues +=10
    $ eckdisplayvar1 = eckbryceannaclues
    $ eckbryceannaarchiveopen = False
    $ eckbryceannagotpcevidence = True
    $ renpy.pause (1.5)
    scene black with dissolve
    $ renpy.pause (1.5)
    scene eckannabedroom4
    show sebastian normal b flip at left
    show naomi normal b at right
    with dissolve
    
    Nm blank b "Whoa..."
    Sb "We'll need days to review all the data here."
    Nm stern b "More like I will need weeks to sort this out. I'm the only one with a proper computer and the skills to work it, and you guys are of no help here."
    c "Hey, I'm pretty good with computers too."
    Nm smile b "Sorry. I keep forgetting that you are in the force now, [player_name]."
    c "It's alright."
    Sb smile b flip "Good work, everyone. This alone should give us enough information to bring out the truth."
    Nm blank b "But should we?"
    Nm stern b "We won't be helping anyone but hard-headed politicians and their games by doing so."
    Sb normal b flip "It's our duty, Naomi. You heard the chief."
    c "Yeah. We must do what we must do."
    Nm sad b "It just doesn't feel right to me. No matter how much I try to convince myself otherwise, I can't help but feel deeply wrong or even dirty."
    c "Maybe you could use some days off. You had to work hard while Mav and Bryce were out, and you've never got to catch a break since."
    Nm shy b "Maybe you're right."
    Nm normal b "How I miss relaxing in the waves, bathing in the warm rays of the sun, exploring the unseen depths of the ocean and not having to worry about anything but what to have for dinner."
    Nm "That was the life."
    c "Sounds like a real paradise."
    Sb smile b flip "Yeah. Going on a vacation like that could be great."
    Sb drop b flip "I'm a terrible swimmer, though."
    Nm "When we're finished with this case, I'm so going on a long holiday."
    Sb smile b flip "Can I join?"
    Nm smile b "That'd be wonderful. Everything is more fun with the right company, you know. I'll teach you how to swim."
    Sb drop b flip "I'd rather not. Water isn't kind to us runners, even after heavy training."
    Nm normal b "You'll like it, I promise. We'll get you a mask, flippers or even scuba gear if you fancy it, and go under the sea."
    Sb "But what if I get lost, panic and start drowning? I heard water is very disorienting."
    Nm smile b "That's why you have me. I'll get you to safety and provide any help you might need."
    c "Like artificial respiration mouth-to-mouth?"
    show sebastian shy b flip with dissolve
    Nm annoyed b "[player_name]!"
    c "I'm not judging."
    Nm stern b "Of course, you and Bryce have had plenty of practice already."
    c "Hey, that's low."
    Nm "So are you."
    c "Alright, alright. I'm sorry."
    show sebastian normal b flip with dissolve
    Nm shy b "..."
    Nm "Yeah. Me too."
    c "Either way, looks like Bryce, Mav and I will be the ones to do all the work while you two are having fun."
    Nm normal b "We did alright without you for a couple of weeks. I'm sure you guys won't have any problems."
    c "We'll manage."
    c "Alright, let me copy all the data on the portable carrier, and we should be done with the computer."
    
    jump eck_bryce_annabedsearch
    
label eck_bryce_annabasement:
    $ renpy.pause (2.0)
    scene eckannabasement with dissolve
    
    show sebastian normal b flip at left with dissolve
    show naomi normal b at right with dissolve
    
    $ eckbryceannabasebooksunseen = True
    $ eckbryceannabasesafefound = False
    $ eckbryceannabasesafeclosed = True
    $ eckbryceannabaseboxsunseen = True
    
    m "Behind the door we found several large shelves filled with books, dusty boxes and some plastic containers."
    Sb "That's a lot of books."
    Nm "I doubt she's a big reader. I can tell they haven't been touched for a very long time."
    c "Why was the door locked by a digital keypad, though?"
    Nm "Maybe she values the items stored here. In case of, say, thieves breaking into the main apartment, this room can provide certain extra security."
    Sb "There has to be something more to this. I don't see anything worthy of such protection so far."
    c "Only one way to find out."
    
    label eck_bryce_annabasementsearch:
        menu:
            "Check the books." if eckbryceannabasebooksunseen:
                m "Most of them turned out to be old textbooks, guides, manuals and other study materials. Some dated as far back as middle school, probably holding sentimental value."
                $ eckbryceannabasebooksunseen = False
                Nm "Let's not dig out things that have been here for years. That would only create more mess for no good reason."
                Sb "Looking at the dust and everything, none of these books were touched in the last several months, so let's leave them alone."
                jump eck_bryce_annabasementsearch
                
            "Check the boxes." if eckbryceannabaseboxsunseen:
                m "Some of them had clothing items like hats or gloves, others were filled with assorted science journals, and a few had old plastic toys and some odd installations, likely made for school fairs back in the day."
                $ eckbryceannabaseboxsunseen = False
                m "I also found what looked like an ancient gaming console, covered in cobwebs and with only a handful of cartridges."
                c "(I guess she never got into gaming.)"
                m "The next box had a bunch of framed photos with faded colors, so I decided against rummaging through them. The top picture I could clearly see showed a couple of runners with little Anna standing between them holding a bronze cup in her claws."
                Nm smile b "Aw, she's so proud and cute here."
                show naomi normal b with dissolve
                m "The final box had some old data carriers. They looked like compact disks, which became obsolete long ago on Earth. No writing on the packages was present, though."
                c "What is this?"
                Sb "Must be her movie collection from back in the day. Some of them could be illegal copies, judging by the boxes, but we aren't the copyright police."
                Nm "They've been unattended for years. I doubt they still work."
                Sb "True."
                jump eck_bryce_annabasementsearch
                
            "Check the plastic containers." if eckbryceannabasesafefound == False:
                m "They had some non-perishable foods in plastic packages and tin cans of all forms, colors and shapes."
                m "When I moved one of them, however, a whole different item caught my attention. It was a wall-mounted sealed metal wall safe with another keypad."
                Nm "That's some intense security."
                Sb "Do you think we can open it, [player_name]?"
                c "We should try. At worst, we'll just get nothing."
                $ eckbryceannabasesafefound = True
                jump eck_bryce_annabasementsearch
                
            "Check the wall safe" if eckbryceannabasesafefound and eckbryceannabasesafeclosed:
                label eck_bryce_annabasementsafecode:
                menu:
                    "Enter the code.":
                        $ eckancd = renpy.input(_("Code:"), allow="0123456789", length=10)
                        play sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        queue sound2 "fx/beep.wav"
                        $ renpy.pause (3.0)
                        
                        if eckancd == _("156123587") and eckancdtries > 0:
                            m "Access granted."
                            $ eckbryceannabasesafeclosed = False
                            c "We're in."
                            Sb smile b flip "Good job!"
                            play sound "fx/door/lock.ogg"
                            $ renpy.pause (3.0)
                            Nm stern b "Hm."
                            Sb drop b flip "Um..."
                            c "Alright."
                            Nm blank b "Well, we managed to open it. Good for us."
                            c "Come to think of it, storing any evidence here would've probably been pretty stupid, so I don't know what we were hoping for."
                            Sb normal b flip "Yeah. Too obvious."
                            Nm shy b "Storing your valuables and money, on the other hand, makes a lot more sense."
                            play sound "fx/pages.ogg"
                            c "Apartment ownership papers, work contracts, bank agreements, graduation certificates, diplomas... Her entire legal side of life is stored in this safe."
                            c "There's also some cash and several golden adornments here. Strange. I don't remember many dragons wearing jewelry, besides Emera."
                            Nm normal b "We only put those on for special occasions. They are also a sound money investment in a practical sense."
                            Nm stern b "Alright, we aren't here to rob her, right? So let's put all this stuff back where it belongs and pretend nothing ever happened."
                            Sb drop b flip "Agreed."
                            c "Sorry, I got a little carried away."
                            Nm normal b "Don't worry, it happens to everyone."
                            show sebastian normal b flip with dissolve
                            jump eck_bryce_annabasementsearch
    
                        else:
                            m "Error. Invalid code."
                            jump eck_bryce_annabasementsafecode
                            
                    "Leave the safe.":
                        jump eck_bryce_annabasementsearch
                
            "Leave.":
                scene black with dissolve
                $ renpy.pause (2.0)
                jump eck_bryce_annahomesearch
    
#   for now