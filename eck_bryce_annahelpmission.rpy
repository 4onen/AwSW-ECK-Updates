




























label eck_bryce_annahelpblood:
    
    $ renpy.pause (2.0)
    scene facin3 with dissolveslow
    play music "mx/movingon.ogg"
    $ renpy.pause (2.0)
    
    m "The large building and its spanning corridors were eerily quiet at such a late hour."
    m "The lone security guard at the entrance lazily looked over the paper Bryce had made up for us before letting us pass without further questions."
    m "Memories of my very first day flooded my mind. Despite the huge burden of responsibility upon me, everything had felt so much simpler back then."
    m "Reza was my friend, and humanity had great hopes for the generators deal. Maybe, if things had turned out differently, both worlds could have been safe by now. Yet, Izumi's meddling and lies had ruined everything."
    m "Lost in thought, I didn't notice how we approached Anna's lab door."
    
    show sebastian normal b flip at left with dissolve
    show naomi normal b at right with dissolve
    
    Nm "This should be the place. Are you alright, [player_name]?"
    c "I'm fine. Just remembering my first day here."
    Sb smile b flip "How long ago that was. I felt so nervous when we met, remember? You don't know it, but I spent a good ten minutes working up the courage to ring the doorbell."
    Nm smile b "And I thought I was shy around people."
    c "Considering all the myths you have about humans, I'm not surprised. It took time before you saw that I'm just a person, not some sort of deity."
    Sb "We aren't much different in the end."
    Nm "But, despite that, you were the one who saved our world."
    c "I'd never have done it without Bryce and Mav. They were the ones who put their lives on the line."
    Nm normal b "I guess you're right."
    
    play sound "fx/door/handle.wav"
    nvl clear
    $ renpy.pause (2.0)
    scene eckpdaslab at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    
    show sebastian normal b flip at left with dissolve
    show naomi normal b at right with dissolve
    
    $ renpy.pause (1.0)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (1.0)
    
    c "Naomi, you're the paper expert here. What do we need, exactly?"
    Nm "Let me see."
    play sound "fx/paper.wav"
    Nm stern b "This is bad."
    Sb drop b flip "What's wrong?"
    Nm "The paper stack is new and freshly opened. This won't do. We need to find an older batch if we want to make the story believable."
    Sb normal b flip "We should look for leftovers somewhere."
    c "We also need to find a suitable pen or something."
    Nm smile b "That will be easy. Anna always has one behind her frills when at work, and there's no better option for us with this. We just need to get it from the locker and..."
    play sound "fx/knobrattle.ogg"
    $ renpy.pause (1.0)
    Nm stern b "Would've been too easy, wouldn't it?"
    Sb "Code lock. There's nothing I can do."
    show naomi normal b with dissolve
    c "Let's search the room."
    
    $ eckbryceannahelplab1 = True
    $ eckbryceannahelplab2 = True
    $ eckbryceannahelplab3 = True
    $ eckbryceannahelplab4 = True
    $ eckbryceannahelplab5 = True
    $ eckbryceannahelplabpaper = False
    $ eckbryceannahelplabpen = False
    
    label eck_bryce_annahelpbloodsearch:
    if eckbryceannahelplabpaper and eckbryceannahelplabpen:
        jump eck_bryce_annahelpbloodleave
    else:
        pass
    
    menu:
        "Check the shelves." if eckbryceannahelplab1:
            m "For a time, we studied the cupboards and shelves for any clues."
            c "I don't think there's anything here, but I like how neatly everything is organized."
            Sb drop b flip "A lot of items are brand new. Isn't it odd?"
            Nm stern b "The other investigation group trashed this place pretty badly. I wouldn't be surprised if they broke more things than they confiscated."
            c "Must've been a mess. Makes one wonder how much evidence they destroy because of poor handling."
            Sb disapproval b flip "Sloppy work. In our field, this is unacceptable."
            Nm normal b "Let's not follow their steps."
            Sb normal b flip "Yeah, we're better than this."
            c "Nothing on the shelves, though."
            $ eckbryceannahelplab1 = False
            jump eck_bryce_annahelpbloodsearch
            
        "Study the computer." if eckbryceannahelplab2:
            m "The lab computer had no password protection; thus, we easily accessed both local files and Anna's mail."
            Nm "Don't waste time on the reports and such. If there was anything incriminating, we'd have had a copy by now."
            Sb "Look, a letter from the maintenance department. Anna didn't even get to open it."
            c "It's probably nothing useful, but let's see."
            c "\"Good day. As you requested, we've changed the code lock broken during the investigation group work. The default numbers are 987. Please change them at your earliest convenience.\""
            Nm smile b "I'd say it was extremely useful for our case."
            play sound "fx/door/lock.ogg"
            Sb smile b flip "And here's the pen we're after."
            $ eckbryceannahelplabpen = True
            $ eckbryceannahelplab2 = False
            show sebastian normal b flip
            show naomi normal b
            with dissolve
            jump eck_bryce_annahelpbloodsearch
        
        "Look through documents." if eckbryceannahelplab3:
            Nm "Most of the papers have been taken by the investigation group and later passed on to us. I doubt much is left of it at all."
            Sb "Actually, I found a heap of old lab reports and experiment logs."
            play sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            m "As I skimmed through numerous documents, it quickly became apparent that most of them dated as far back as last year and beyond."
            Nm "These papers won't do, regardless, [player_name]. Not only do they far predate your arrival to our world, but they're also fully filled up, signed, and sometimes have a stamp on them."
            c "Yeah. You can't write one official document on another."
            stop sound fadeout 1.0
            stop sound2 fadeout 2.0
            Sb "At least we didn't find any extra incriminating evidence against Anna to deal with."
            Nm "That could be unpleasant indeed."
            $ eckbryceannahelplab3 = False
            jump eck_bryce_annahelpbloodsearch
            
        "Open the cupboards." if eckbryceannahelplab4:
            m "A careful search through numerous cabinets, shelves and cupboards mostly revealed various scientific equipment and glassware."
            m "It took us a long time to look through everything, until one drawer got our attention."
            Sb smile b flip "We might be in luck. Look."
            Nm smile b "Drafts! That's exactly the sort of papers I've been looking for. Let me see."
            play sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            queue sound2 "fx/paper.wav"
            Nm normal b "Too dirty... too old... too full... this one's torn... I got it!"
            stop sound2 fadeout 1.0
            m "She happily presented me with a near-clean paper sheet with only a single stray line at the top. Must've been a printing error."
            Sb smile b flip "Good work."
            show naomi normal b
            show sebastian normal b flip
            with dissolve
            $ eckbryceannahelplabpaper = True
            $ eckbryceannahelplab4 = False
            jump eck_bryce_annahelpbloodsearch
            
        "Look under the furniture." if eckbryceannahelplab5:
            Sb "Do we really have to? The space is pretty limited here, and there's a lot of fragile equipment around us."
            Nm smile b "It's going to be fine. If I can do it, you can as well. Look."
            $ renpy.pause (1.0)
            play sound "fx/bottlesmash2.ogg"
            show naomi blank b with dissolve
            c "Be careful with your tail!"
            Nm "They aren't going to be happy. Do you think beakers are expensive?"
            Sb drop b flip "Shouldn't be, but let's leave the search to [player_name]."
            Nm "All things considered, I agree."
            m "Unsurprisingly, the floor was pristine clear save for the glass shards. Not a single piece of rubbish or dust could be found, let alone any larger items of interest."
            c "(Can't let the research be contaminated, I guess.)"
            c "You were right, Seb. Nothing down there at all."
            Sb normal b flip "I suspected that to be the case. They were doing serious research here, and the clean working environment is crucial for science."
            Nm shy b "And we've probably brought in a lot of germs and other contaminants on us the moment we entered."
            Nm normal b "Oh well."
            c "I don't think this lab was sterile to begin with, so it's alright."
            $ eckbryceannahelplab5 = False
            
            jump eck_bryce_annahelpbloodsearch
            
            
label eck_bryce_annahelpbloodleave:
    c "Should I write my request here?"
    Nm "That would be ideal for our story. It must be clearly written in this lab and somewhat in a hurry."
    
    hide naomi with dissolve
    hide sebastian with dissolve
    
    m "I sat down by one of the tables and cleared out some space for myself. Sebastian took another stool nearby and Naomi chose to settle on the floor."
    play sound "fx/chair.wav"
    $ renpy.pause (1.0)
    show sebastian normal b flip at left with dissolve
    show naomi normal b at right with dissolve
    
    c "Alright, I got it. But how should I word the request?"
    Sb "Something about the scientific interest of humanity? Say, you wanted to know about the similarities and differences between our species."
    play sound2 "fx/writing.ogg"
    queue sound2 "fx/writing.ogg"
    Nm "I like it. Also, add that you are submitting your blood sample freely for all and any analysis dragonkind deems necessary."
    queue sound2 "fx/writing.ogg"
    queue sound2 "fx/writing.ogg"
    m "The wording was far from the most coherent and beautiful writing I'd ever done, but it certainly contributed to the whole rushed impression."
    stop sound fadeout 1.0
    stop sound2 fadeout 1.0
    m "After signing up the request, I passed it on to Naomi, who swiftly glanced over it before hiding it under her folded wing."
    Nm smile b "Wonderful. You've even made a couple of grammatical errors. This should do nicely."
    c "Those are... fully intentional to convey, uh, the feeling of this request being done hastily."
    Sb smile b flip "Of course. A totally believable explanation."
    Nm "It's alright, either way. You should be proud you can write by hand at all, and beautifully so. It's not a gift I, or other quadruped dragons, have."
    c "Thanks, Naomi. You must face some challenges in everyday life."
    Nm normal b "It's not too bad. You get used to it over the years, and we have our own benefits like being bigger and stronger for one."
    c "I see. So, are we done here?"
    Sb "I believe so. Great job, everyone."
    Nm "Let's head back to the department."
    
    $ eckbryceannaclues -= 3
    $ eckbryceannahelpblood = False
    jump eck_bryce_annahelpmenu
    
    
    
    
    
label eck_bryce_annahelpreports:
    
    $ renpy.pause (2.0)
    scene eckpolicedeptstorage1 with dissolveslow
    play music "mx/fountain.ogg"
    $ renpy.pause (2.0)
    
    show naomi normal b with dissolve
    
    c "Where are those lab reports stored?"
    Nm "They should be in locker 235."
    $ renpy.pause (1.5)
    play sound2 "fx/door/lock.ogg"
    queue sound2 "fx/metalbox.ogg"
    $ renpy.pause (1.5)
    c "There're some other items here."
    Nm "Look to your left in the far corner. You'll see a plastic folder."
    c "Got it. But we can't really do anything here, right?"
    Nm smile b "Of course not. My office should be safe enough to work on the documents, and I have a printer. I'll explain what I have in mind once we get there."
    
    $ renpy.pause (2.0)
    scene black with dissolvemed
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (2.0)
    scene ecknaomioffice1 at Pan ((0, 150), (0, 150), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    
    m "When we entered the room, Naomi hopped onto the couch and stretched lazily."
    play sound "fx/sheet.wav"
    show naomi normal b flip at left with dissolve
    c "Hey! I thought we were going to work on the documents."
    Nm smile b flip "We still are. But with you occupying my computer, I can only assist by giving advice and such. And I'd rather do so with full available comfort."
    c "Why do you even have a couch?"
    Nm normal b flip "Sometimes I have to stay at work until very late hours, you know. Taking a nap helps me a long way if I have a busy stressful evening ahead."
    Nm smile b flip "Also, it just feels good to lie down sometimes and study the case in calm and relaxing conditions, rather than hunching awkwardly over a table for hours."
    Nm shy b flip "Or maybe I'm just lazy."
    Nm normal b flip "But Bryce is happy with my performance, and so is the rest of the department. I guess it's all good."
    c "Yeah, you're doing great. I was just surprised to find the couch, nothing more."
    m "I took a look at the laptop standing on the desk, noticing how much larger than normal it was, and quickly realized that getting used to typing on it would take some time."
    c "That's a pretty big computer."
    Nm "It's designed for dragons like me and our not-so-nimble fingers – especially mine, which have webbing between them."
    Nm "I hope the keyboard isn't too uncomfortable for your smaller hands."
    Nm shy b flip "Seb complains about it all the time when he has to search for something in my work files."
    c "Don't worry, I'll manage."
    Nm smile b flip "Alright. This is going to take a while, so when you feel tired just let me know and we'll swap."
    c "But what's your plan?"
    Nm normal b flip "Those reports contain pretty incriminating evidence against Anna. They have been registered and cataloged in our database, so we can't make them disappear."
    Nm "We also can't directly alter the documents for it will be extremely obvious even to the untrained eye, let alone any serious expert."
    c "Okay. I understand that. But what can we do?"
    Nm "One moment."
    show naomi normal flip with fade
    $ renpy.pause (1.0)
    Nm smile flip "Much better."
    Nm normal flip "We can add or remove pages as long as we keep the total amount of them at 27. That would require writing up things of our own, but with network access, it should be doable."
    Nm "Generally there are four stats that we should keep track of when editing this: the universal coherence of the text, its authenticity, the amount of incriminating data, and its overall scientific value."
    Nm "The positive ones should at least be half of what they used to be, and the incrimination would have to drop below a quarter. How to approach this task is up to you. We can reset and start over at any moment."
    c "Can I use humankind's knowledge when adding things of my own?"
    Nm "Sure."
    Nm "But please limit its use – else you'll get caught easily."
    c "Got it."

    
    $ eckbryceannahelpdoccohe = 100
    $ eckbryceannahelpdocauth = 100
    $ eckbryceannahelpdocincr = 100
    $ eckbryceannahelpdocvalu = 100
    $ eckbryceannahelpdocpage = 27
    $ eckbryceannahelpdochumdata = 3
    $ eckbryceannahelpdoctime = 0
    $ eckbryceannahelpdocday = True
    
    show screen eckextrainfo
    $ eckextradisplay = 6
    
label eck_bryce_annahelpdocgame:
    
    $ eckdisplayvar1name = "Authenticity:"
    $ eckdisplayvar1 = eckbryceannahelpdocauth
    $ eckdisplayvar1unit = "%"
    $ eckdisplayvar2name = "Coherence:"
    $ eckdisplayvar2 = eckbryceannahelpdoccohe
    $ eckdisplayvar2unit = "%"
    $ eckdisplayvar3name = "Incrimination:"
    $ eckdisplayvar3 = eckbryceannahelpdocincr
    $ eckdisplayvar3unit = "%"
    $ eckdisplayvar4name = "Value:"
    $ eckdisplayvar4 = eckbryceannahelpdocvalu
    $ eckdisplayvar4unit = "%"
    $ eckdisplayvar5name = "Pages:"
    $ eckdisplayvar5 = eckbryceannahelpdocpage
    $ eckdisplayvar5unit = ""
    $ eckdisplayvar6name = "Moves taken:"
    $ eckdisplayvar6 = eckbryceannahelpdoctime
    $ eckdisplayvar6unit = ""
    
    if eckbryceannahelpdoctime > 20 and eckbryceannahelpdocday:
        scene ecknaomioffice2 at Pan ((0, 150), (0, 150), 0.0)
        show naomi normal flip at left
        with dissolvemed
        $ eckbryceannahelpdocday = False
        
    else:
        pass
    
    if eckbryceannahelpdoccohe < 1 or eckbryceannahelpdocauth < 1 or eckbryceannahelpdocvalu < 1 or eckbryceannahelpdocpage < 10:
        Nm stern flip "This is going nowhere, [player_name]. Let's start over."
        Nm normal flip "Don't rush, we have time."
        jump eck_bryce_annahelpdocgamereset
    else:
        pass
    
#   m "Current status: \n Authenticity: [eckbryceannahelpdocauth]%% \n Coherence: [eckbryceannahelpdoccohe]%% \n Incrimination: [eckbryceannahelpdocincr]%% \n Value: [eckbryceannahelpdocvalu]%% \n Pages: [eckbryceannahelpdocpage]"
    
    if eckbryceannahelpdoccohe > 45 and eckbryceannahelpdocauth > 45 and eckbryceannahelpdocvalu > 45 and eckbryceannahelpdocpage == 27 and eckbryceannahelpdocincr < 30:
        jump eck_bryce_annahelpdocgamewin
    else:
        pass
    
    menu:
        "Remove an incriminating page. (-5 A, -15 C, -10 I, -15 V, -1 P)":
        
            $ eckbryceannahelpdocauth -= 5
            $ eckbryceannahelpdoccohe -= 15
            $ eckbryceannahelpdocincr -= 10
            $ eckbryceannahelpdocvalu -= 15
            $ eckbryceannahelpdocpage -= 1
            $ eckbryceannahelpdoctime += 1
        
            jump eck_bryce_annahelpdocgame
            
        "Write up something using the knowledge of humankind. (-5 A, +10 C, +0 I, +15 V, +1 P) Remaining uses: [eckbryceannahelpdochumdata]." if eckbryceannahelpdochumdata > 0:
        
            $ eckbryceannahelpdocauth -= 5
            $ eckbryceannahelpdoccohe += 10
            $ eckbryceannahelpdocincr += 0
            $ eckbryceannahelpdocvalu += 15
            $ eckbryceannahelpdocpage += 1
            $ eckbryceannahelpdochumdata -= 1
            $ eckbryceannahelpdoctime += 1
            
            jump eck_bryce_annahelpdocgame
            
        "Use network to create some harmless reports. (-10 A, +10 C, 0 I, 0 V, +1 P)":
        
            $ eckbryceannahelpdocauth -= 10
            $ eckbryceannahelpdoccohe += 10
            $ eckbryceannahelpdocincr += 0
            $ eckbryceannahelpdocvalu += 0
            $ eckbryceannahelpdocpage += 1
            $ eckbryceannahelpdoctime += 1
        
            jump eck_bryce_annahelpdocgame
        
        "[[Show more options.]":
            jump eck_bryce_annahelpdocgame2
            
label eck_bryce_annahelpdocgame2:
    menu:
        "Remove a page which no longer fits into the picture. (+5 A, +10 C, 0 I, -5 V, -1 P)":
        
            $ eckbryceannahelpdocauth += 5
            $ eckbryceannahelpdoccohe += 10
            $ eckbryceannahelpdocincr += 0
            $ eckbryceannahelpdocvalu -= 5
            $ eckbryceannahelpdocpage -= 1
            $ eckbryceannahelpdoctime += 1
        
            jump eck_bryce_annahelpdocgame
            
        "Use network to create some filler text. (-5 A, +10 C, 0 I, -5 V, +1 P)":
        
            $ eckbryceannahelpdocauth -= 5
            $ eckbryceannahelpdoccohe += 10
            $ eckbryceannahelpdocincr += 0
            $ eckbryceannahelpdocvalu -= 5
            $ eckbryceannahelpdocpage += 1
            $ eckbryceannahelpdoctime += 1
        
            jump eck_bryce_annahelpdocgame
            
        "Reword and reuse some of Anna's earlier works. (+10 A, -5 C, +5 I, +10 V, +1 P)":
        
            $ eckbryceannahelpdocauth += 10
            $ eckbryceannahelpdoccohe -= 5
            $ eckbryceannahelpdocincr += 5
            $ eckbryceannahelpdocvalu += 10
            $ eckbryceannahelpdocpage += 1
            $ eckbryceannahelpdoctime += 1
        
            jump eck_bryce_annahelpdocgame
            
        
        "[[Show more options.]":
            jump eck_bryce_annahelpdocgame3
            
label eck_bryce_annahelpdocgame3:
    menu:
        "Remove useless filler. (+5 A, -5 C, 0 I, +5 V, -1 P)":
        
            $ eckbryceannahelpdocauth += 5
            $ eckbryceannahelpdoccohe -= 5
            $ eckbryceannahelpdocincr += 0
            $ eckbryceannahelpdocvalu += 5
            $ eckbryceannahelpdocpage -= 1
            $ eckbryceannahelpdoctime += 1
        
            jump eck_bryce_annahelpdocgame
            
        "[[Back to page 1.]":
            jump eck_bryce_annahelpdocgame
            
        "[[Reset and start over.]":
            m "Are you sure you want to reset?"
            menu:
                "Yes.":
                    jump eck_bryce_annahelpdocgamereset
                "No.":
                    jump eck_bryce_annahelpdocgame3
            
label eck_bryce_annahelpdocgamereset:
    
    $ eckbryceannahelpdoccohe = 100
    $ eckbryceannahelpdocauth = 100
    $ eckbryceannahelpdocincr = 100
    $ eckbryceannahelpdocvalu = 100
    $ eckbryceannahelpdocpage = 27
    $ eckbryceannahelpdochumdata = 3
    
    jump eck_bryce_annahelpdocgame
    
label eck_bryce_annahelpdocgamewin:
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/sleepingcity.ogg"
    Nm smile flip "Looks good to me. Great job, [player_name]."
    
    hide screen eckextrainfo
    $ eckextradisplay = 0
    $ eckdisplayvar1name = ""
    $ eckdisplayvar1 = 0
    $ eckdisplayvar1unit = ""
    $ eckdisplayvar2name = ""
    $ eckdisplayvar2 = 0
    $ eckdisplayvar2unit = ""
    $ eckdisplayvar3name = ""
    $ eckdisplayvar3 = 0
    $ eckdisplayvar3unit = ""
    $ eckdisplayvar4name = ""
    $ eckdisplayvar4 = 0
    $ eckdisplayvar4unit = ""
    $ eckdisplayvar5name = ""
    $ eckdisplayvar5 = 0
    $ eckdisplayvar5unit = ""
    $ eckdisplayvar6name = ""
    $ eckdisplayvar6 = 0
    $ eckdisplayvar6unit = ""
    
    Nm normal flip "It's a little mediocre for a scientist of Anna's talent, but overall it should be perfectly believable."
    c "That was exhausting beyond belief. My eyes hurt, I can't feel my fingers anymore, and my thoughts are all tangled up."
    Nm shy flip "I'm sorry. You should've told me earlier so we could swap to let you rest."
    Nm "It's very late, too."
    c "I guess I got too lost in my work and didn't even notice how the time flew by."
    Nm "I'm sorry I didn't bring your attention to it."
    c "It's alright. Do you think anyone else is still at work?"
    Nm normal flip "Out of our group, we're the only ones left on duty right now. There's a rapid response team always on standby, but they're in the other wing."
    Nm "I guess it's about time we depart as well."
    play soundloop "fx/eckrainloop.ogg" fadein 2.0
    m "I walked up to the window and looked outside. My sight immediately caught multiple puddles glistening with ripples under the street lamps. Countless falling drops sparkled in the beams of their lights."
    c "I'd rather just sleep here. The weather is pretty ugly, and I didn't prepare any clothing for it."
    stop soundloop fadeout 2.0
    play sound "fx/sheet.wav"
    show naomi normal flip at center with ease
    Nm smile flip "I'm going to keep you company, then."
    Nm "But first, I'll be right back. Hopefully Zhong hasn't closed his shop yet."
    c "It's fine, just go home. I'll see you tomorrow."
    Nm smile flip "Don't fall asleep while I'm away."
    hide naomi with dissolve
    $ renpy.pause (0.5)
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.5)
    play sound "fx/door/door_close.ogg"
    $ renpy.pause (1.0)
    m "All alone in the office, I did my best to resist the urge to lie down and take a nap."
    play soundloop "fx/eckrainloop.ogg" fadein 2.0
    m "Instead I stood by the window and stared at the night town below. Several yawns escaped my lips as tiredness from the long day at work quickly caught up with me."
    m "To keep myself awake and kill some time, I tried out one of the card games Naomi had on her computer but lost every single time."
    c "(This is certainly not Solitaire.)"
    stop soundloop fadeout 2.0
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    play sound "fx/door/door_close.ogg"
    $ renpy.pause (1.5)
    
    show naomi smile with dissolve
    
    Nm "I got us some supplies. We haven't eaten for the whole day, and that simply won't do."
    c "Thanks for reminding me. Honestly, I forgot about food completely."
    Nm normal "We both did. And aren't you tired of sitting at the computer, [player_name]?"
    c "I was just struggling to stay up while you were away."
    Nm normal "I see. Sorry, it took longer than I thought, but dinner's ready."
    c "Let me clean up the desk."
    
    hide naomi with dissolve
    m "After a short improvised meal of cold fried bird pieces with some bits of surprisingly delicious cooked algae chips, we got ready to settle for the night."
    
    show naomi normal with dissolve
    
    play sound2 "fx/door/lock.ogg"
    c "Why did you lock the door?"
    Nm blank "I'd rather not have anyone walk in while we're sleeping and give Bryce any wrong ideas."
    c "Yeah. Good thinking."
    
    play sound2 "fx/switch.wav"
    $ renpy.pause (0.7)
    show dark2
    
    Nm normal "Alright, this couch is too small for two of us, so it's all yours. I'll take the floor."
    
    menu:
        "You don't have to.":
            Nm "What do you mean?"
            
            menu:
                "I'll sleep on the floor.":
                    Nm shy "But..."
                    c "It's fine. I was the one who made you stay here, and you had to go outside in the rain."
                    Nm normal "I'm used to water, you know."
                    c "Still, you only stayed here because of me, and I don't want you to sleep on the hard floor. At least let me repay you this way."
                    Nm shy "If you're sure."
                    c "I am. Don't worry about anything."
                    c "Good night, Naomi."
                    Nm "Good night."
                    
                    hide naomi with dissolve
                    
                    m "For a few minutes I just lay on the carpet floor. Lab reports and scientific data still bounced around my brain restlessly, giving me a dull headache."
                    play sound "fx/sheet.wav"
                    m "Suddenly, I heard some rustling followed by something large leaning against my side. A leathery blanket draped itself over my body."
                    
                "We could share the couch.":
                    Nm shy "But how are we going to fit?"
                    c "We can manage if you promise not to squish me against the wall. I get enough of that from Bryce."
                    Nm smile "I'll be careful."
                    
                    hide naomi with dissolve
                    
                    m "Through some trial and error, we managed to settle together on the couch with minimal discomfort for either of us."
                    m "As I was slowly falling asleep, I felt a leathery blanket drape itself over my body."
                    m "It wrapped around me, gently pulling me into Naomi's warm side."
                    
                    Nm "It's going to be cold in the morning."
                    c "Thank you. Good night, Naomi."
                    Nm "Good night, [player_name]."
            
        "Thanks.":
            c "Something soft to sleep on sounds amazing right now. Thank you, Naomi."
            Nm smile "You are welcome. Good night, [player_name]."
            c "Good night."
            
    $ eckbryceannaclues -= 4
    $ eckbryceannahelpreps = False
    jump eck_bryce_annahelpmenu
    
    
    
label eck_bryce_annahelpdamion:
    play music "mx/sprite.ogg"
    $ renpy.pause (2.0)
    scene eckoutsideuniv2 with dissolveslow
    
    show sebastian normal with dissolve
    
    c "I don't think I've been here before."
    Sb "We're next to the local university. Though, at this hour, there's nobody here."
    c "Did Damion live on a campus? He looked a little too old for a student."
    Sb smile "Of course not. It's not even completed yet. The university is scheduled to open next year so that we won't depend on the outside people to cover certain jobs, mostly at the production facility."
    c "I see."
    Sb "Damion's apartment is across the street from here."
    c "So, do you have any idea how we can negate the collection he gathered?"
    Sb normal "Don't ask me. I'm still not convinced that we're doing the right thing by helping Anna. But your vote was the decisive one, and the chief is with you, so I'm playing along."
    c "Look, Seb. I know that our actions are sketchy at best, there's no denying that. But if we look at the bigger picture, she was trying to save herself and many others at no harm to anyone."
    c "As for the legal side, do you think she'd get a fair trial considering the pressure from the council?"
    Sb drop "I see your point."
    c "To me, it feels like another character assassination attempt, to be honest. Not to say she's completely innocent, but her case feels blown out of proportion."
    c "What sort of harm could come from studying my blood, for example?"
    Sb normal "Considering how Anna is, I'm not surprised she made plenty of enemies in high places."
    Sb "Naturally, any mishap on her side is an open opportunity for them to bring her down. She probably thinks herself too valuable to get jailed, but I wouldn't be so sure."
    c "I had the same thoughts."
    c "Honestly, I'd have had no problems if she was just to be demoted or faced some disciplinary action. Rules are there for a reason, after all."
    c "But I won't stand there and watch her get sent to prison for something so minor."
    Sb smile "And we are back to the discussion of whether or not we can be judges."
    c "I guess that's what it boils down to."
    Sb "You know that it's not our job to make such decisions, and our opinions are biased."
    Sb smile "But when no side is unbiased, our point of view is as good as any other."
    c "So, you don't mind helping?"
    Sb "I never did. Else, why would I be here?"
    Sb normal "I was merely voicing my concerns."
    c "Thanks, Seb."
    Sb smile "I think it's Anna and Mav who should be thanking you, [player_name]."
    c "But why him?"
    Sb "She's his ex. When he took Naomi's side, I knew exactly why."
    c "Do you think they'll reconcile and get back together?"
    Sb normal "Who knows. But first, let's make sure they get the chance."
    c "Right."
    
    scene eckoutsidedamion at Pan ((0, 150), (0, 150), 0.0) with dissolvemed
    show sebastian normal with dissolve
    
    Sb "Damion's apartment should be in this building. Stay put. I'll scout the area."
    c "Alright. I still can't get used to being the only human."
    Sb "Yeah. You stand out quite a lot, [player_name], so be careful."
    
    hide sebastian with dissolve
    
    m "I tried my best to blend in with the surroundings, despite seeing no one anywhere in proximity."
    m "For several long minutes, I sat on a bench hidden in the bushes at the side of the road, out of sight of any locals who could be passing by."
    
    show sebastian normal with dissolve
    
    Sb "Seems clear. Let's move in."
    c "Are you sure?"
    Sb smile "You can never be completely certain in our line of work."
    Sb normal "But I'd say we are good. None of the windows have lights in them, and I haven't seen anyone on the street nearby."
    c "Okay. What about the lock?"
    Sb "It looks simple enough. I saw no other security measures, either."
    c "Good. Let's go."
    
    stop music fadeout (2.0)
    scene eckdamionroom
    show dark2
    with dissolvemed
    
    play sound "fx/micro.ogg"
    $ renpy.pause (1.5)
    play sound "fx/micro.ogg"
    $ renpy.pause (1.5)
    play sound "fx/micro.ogg"
    $ renpy.pause (1.5)
    play sound "fx/door/lock.ogg"
    $ renpy.pause (0.5)
    play sound "fx/door/handle.wav"
    $ renpy.pause (1.5)
    
    show sebastian normal behind dark2 with dissolve
    play sound2 "fx/switch.wav"
    $ renpy.pause (0.7)
    hide dark2
    
    play music "mx/mysteryambience.ogg"
    
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (0.5)
    play sound "fx/door/lock.ogg"
    
    Sb smile "And we are in. Do you have a plan, [player_name]?"
    c "Unfortunately, no. Damion's collection likely has been carefully gathered and assembled to include the most straightforward and incriminating pieces of information against Anna."
    Sb normal "Yeah. It wouldn't be possible to make it harmless through subtle tampering. We need to find something that would discredit the whole package."
    Sb drop "Which won't be easy, since this place has already been searched carefully."
    c "Any legal loopholes we could use?"
    Sb normal "I'm not sure."
    Sb "If we could prove that said items have been used as a tool of illicit activity, it should be possible to push the story of them being specifically fabricated by the culprit."
    c "He had the motive, means and opportunity for that."
    Sb smile "Indeed."
    Sb normal "Normally, I'm against slandering the name of a deceased person who can no longer stand up for themselves. But this is an exception."
    c "Do you think we have a chance to find anything?"
    Sb "There were no allegations of possible blackmail during the initial search. Thus, only materials directly related to Damion's work have been taken."
    Sb "Everything else should be untouched."
    c "Alright. Maybe there's something we could use."
    
    $ eckbryceannahelpdamdra = True
    $ eckbryceannahelpdamtv = True
    $ eckbryceannahelpdamcomp = True
    $ eckbryceannahelpdamund = True
    $ eckbryceannahelpdamout = True
    
label eck_bryce_annahelpdammenu:
    show sebastian normal with dissolve
    
    if eckbryceannahelpdamdra or eckbryceannahelpdamtv or eckbryceannahelpdamcomp or eckbryceannahelpdamund or eckbryceannahelpdamout:
        pass
    else:
        jump eck_bryce_annahelpdamexit
    
    menu:
        "Search the drawers and cupboards." if eckbryceannahelpdamdra:
            Sb "He didn't have a lot of possessions, it seems."
            c "Yeah, nothing of use for us here. The only thing I can say is that he really liked to keep everything in strict order."
            Sb disapproval "I expected more books, however."
            c "How odd, indeed."
            Sb "Strange. He kept several photos of, I assume, his family members, but they were all piled in a drawer."
            c "As if he didn't want to see them but couldn't bring himself to throw them away."
            Sb normal "I don't think it's relevant to our case, however."
            c "You're right."
            
            $ eckbryceannahelpdamdra = False
            jump eck_bryce_annahelpdammenu
            
        "Look around the TV." if eckbryceannahelpdamtv:
            m "All I found was a remote and a collection of assorted movies."
            c "Oh my."
            Sb shy "Some of these are certainly not for the younger viewers."
            c "He looked adult enough to me."
            Sb normal "I know he was."
            c "Maybe we still shouldn't watch those."
            Sb "I never suggested that. One of the cases, however, has a calling card with Anna's home number scribbled by hand."
            c "An interesting place to store it."
            Sb "We should document this for future use."
            
            $ eckbryceannahelpdamtv = False
            jump eck_bryce_annahelpdammenu
            
        "Check Damion's computer." if eckbryceannahelpdamcomp:
            m "It didn't take long to find a laptop standing on the desk in one of the rooms."
            c "I'm surprised. It's not passworded."
            Sb "He was probably confident that no other person would try to use it."
            c "The network is still running. I wonder if we can access his mail."
            play sound "fx/keyboard.ogg"
            $ renpy.pause (2.5)
            c "And here it is. The password was saved, apparently."
            Sb smile "Good for us."
            c "Indeed. Nothing too incriminating so far, however. Mostly work talk, some orders, some spam."
            Sb normal "Spam?"
            c "Advertising letters you never asked for. It's a term we used back home for it."
            Sb "I see."
            c "Hm, a happy birthday from his family members in another town. Curious, they also seem to want to apologize for something. I wonder if they know what happened to him?"
            Sb "We have informed them, of course."
            Sb drop "It wasn't pretty. I was the one to do the phone call, and I don't want to refresh that day in my memory."
            c "Must be pretty hard to tell someone that their relative or a loved one is dead."
            Sb disapproval "It's one of the things you never get used to in the force, [player_name]."
            Sb "No matter what crimes they commit or dirty background games they play, people are still people. With friends, families and ones who care about them."
            c "Even someone like Reza or Izumi."
            Sb normal "Even someone like them."
            c "Nothing else in the mail. Damion kept copies of his document collection on the hard drive, however."
            Sb "Erase them."
            c "Wait. He had a program called Image Studio."
            Sb "So what?"
            c "We can use this to let Anna's lawyer argue that the documents we've recovered from him have been digitally tampered with."
            Sb smile "Smart."
            c "And his computer is conveniently small enough to carry."
            
            $ eckbryceannahelpdamcomp = False
            jump eck_bryce_annahelpdammenu
            
        "Search under the furniture." if eckbryceannahelpdamund:
            m "For a time, Seb and I carefully scanned the dusty floor for anything of interest."
            hide sebastian with dissolve
            c "I feel like it's a waste of time."
            Sb "Maybe."
            $ renpy.pause (2.5)
            Sb "Or maybe not."
            show sebastian smile with dissolve
            m "He picked up a small square object with glistening gold-colored parts on one end."
            c "What is it?"
            Sb "A data storage card. Normally used in cameras and similar devices."
            Sb normal "Now we only need to find what to read it with. Can we use your PDA?"
            c "It doesn't have any suitable slots."
            Sb "I see."
            c "There's a camera on a shelf here."
            Sb smile "Good one."
            play sound "fx/button_unpress.ogg"
            m "Sebastian easily inserted the data card into the camera and pushed the switch-on button."
            m "He turned the screen towards me so that we both could see what was on it."
            show sebastian disapproval with dissolve
            c "If I didn't know any better, I'd say Anna had a creepy stalker."
            Sb "A lot of those are actually related to their work, but not all of them."
            c "Keep scrolling."
            Sb drop "Maybe we should stop. These pictures are rather unsettling for me."
            c "Why?"
            Sb "I've seen similar behavior before in my line of work. Most of the time it's relatively harmless, but I know some cases that went... badly."
            c "Alright. But does this give us anything?"
            Sb normal "Yes. It proves that Damion had been collecting information about Anna on purpose and had a strong motivation to do so."
            
            $ eckbryceannahelpdamund = False
            jump eck_bryce_annahelpdammenu
            
        "Check out the kitchen and the bathroom." if eckbryceannahelpdamout:
            m "Searching through the bathroom and kitchen brought us nothing. Food in the fridge was long spoiled and unleashed a suffocating rotten smell the moment we opened the door."
            m "Out of curiosity, I checked the medicine Damion had been keeping and found several packages of anti-stress and anti-depressant pills that were easily recognized by Sebastian."
            Sb "He seems to have stopped taking them a while ago..."
            c "Those are the type of meds that often hurt you more than they help, to be honest. Maybe it was for the best that he quit."
            Sb "He won't be needing them anymore, either way."
            play sound2 "fx/sheet.wav"
            m "Sebastian turned around to leave the bathroom and accidentally knocked over a stack of towels with his tail."
            c "Be careful!"
            Sb drop "Sorry. Didn't notice it."
            Sb normal "Wait. What is that?"
            m "He pointed at the small notebook sticking out from underneath the pile of fabric."
            m "Quickly, I picked it up and opened it at a bookmarked page."
            c "A diary. Interesting."
            Sb drop "From my work experience, this combined with meds is not a good sign."
            c "Looks like you're right. Listen to this. Dated a day before his murder."
            show sebastian normal with dissolve
            c "\"As always, Anna has been smug and insufferable today. I didn't sign up to do her personal projects in my free time.\""
            Sb "Sounds pretty accurate to me so far."
            c "\"I'm tired of being on the sidelines already, but this adds insult to injury. Just because she's more talented doesn't mean that she's better than me and can do whatever she wants while I'm stuck in the lab for days.\""
            c "\"I swear, one day I'll just send everything to hell and make the cops lock her up. I've got enough material for that. Then I'll be the facility manager, and things will be alright."
            c "\"How I wish I didn't have to deal with her temper daily, but my consolation prize is good enough for now.\""
            Sb "How petty."
            c "Yeah. Anna might be a pain to work with, but it's pretty sick to call your blackmail extortion a prize."
            c "There're several other records with similar stories about how Anna isn't actually a better scientist and he was never given a fair chance. He also gloated about having a way to put Anna in her place."
            c "At least he spared us the details on it."
            Sb "This might be one of the key pieces of evidence."
            m "I continued to skim through Damion's diary back to the very beginning."
            c "Oh."
            Sb "What's wrong, [player_name]?"
            c "One of the first records says he moved into this town to get away from the memories of his now-deceased abusive mother."
            c "Looks like, in the early days, Anna reminded him of her so much he wondered if she was haunting him from beyond the grave. Eventually, he got over it and developed a plan for how to get some benefits out of his current position."
            c "But only recently, during Reza's visit, he got, as written, \"An opportunity for revenge.\""
            Sb drop "The story isn't getting any better. Let's leave this to the analysis department."
            c "But {i}I am{/i} the analysis department."
            Sb normal "Then please, don't talk about it when I'm nearby. This notebook is giving me the creeps."
            c "Alright. I'm sorry."
            
            $ eckbryceannahelpdamout = False
            jump eck_bryce_annahelpdammenu
            
    
label eck_bryce_annahelpdamexit:
    
    Sb "Nothing else left to do here."
    c "We've gathered enough evidence to prove the act of blackmailing and extortion, so we're done here."
    Sb "It will be hard to open a case against a deceased person, however."
    c "That won't be necessary. We merely need to brand Damion's collection of evidence as unreliable and likely fabricated."
    Sb "I see."
    Sb "But wouldn't it look suspicious for us to add extra items so long after the initial search? Especially since those items undermine the rest heavily."
    c "Nobody yet knows the full list of things stored in that cell. So we can easily add anything and pretend it had always been there."
    Sb "Sometimes, us being understaffed is a blessing in disguise."
    m "Sebastian slowly sneaked up to the main door, leaned the side of his head against it, and lifted his hand as a sign for me to keep quiet."
    m "For several seconds, everything seemingly froze."
    Sb smile "Clear. We should be good to go."
    c "After you."
    play sound2 "fx/switch.wav"
    $ renpy.pause (0.7)
    show dark2
    play sound "fx/door/lock.ogg"
    $ renpy.pause (0.5)
    play sound "fx/door/handle.wav"
    $ renpy.pause (1.5)
    hide sebastian with dissolve
    $ renpy.pause (2.5)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (0.5)
    play sound "fx/door/lock.ogg"
    
    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    play music "mx/sprite.ogg"
    scene eckoutsideuniv3 with dissolveslow
    
    show sebastian smile with dissolve
    Sb "Looks like we made it."
    c "At last. It took us a while, but I'm happy to leave that experience behind."
    Sb normal "So am I. You can stay at my place for tonight, if you want. It's very late, and your apartment is on the other side of town."
    Sb "I, on the other hand, live just a couple of blocks away."
    c "Thanks, Sebastian."
    Sb smile "Don't mention it."
    Sb normal "I have a TV, a spare couch and plenty of snacks. What do you say we have a small party? After everything we've discovered today, I could use some fun to wind down a little."
    c "Sounds lovely. I'm in."
    Sb smile "I'm glad we're on the same page."
    c "The evidence is safer that way, too."
    Sb "Yeah."
    
    $ eckbryceannaclues -= 5
    $ eckbryceannahelpdamion = False
    jump eck_bryce_annahelpmenu
    
    
label eck_bryce_annahelplab:
    $ renpy.pause (2.0)
    scene eckcomproom1 at Pan ((0, 150), (0, 150), 0.0) with dissolvemed
    play music "mx/confrontation.ogg"
    $ renpy.pause (2.0)
    
    show bryce normal b with dissolve
    
    m "The main office was full of computers, all lined up on desks in near-perfect order."
    m "Most of the employees sat or stood in front of their respective monitors, while a smaller group of dragons zipped around endlessly, switching between workstations."
    c "Looks pretty impressive for an independent investigation group."
    Br "They work with a lot of different cases, often things outside of our main scope. We've cooperated on several occasions in the past, but to be honest their professional ethics leave a lot to be desired."
    c "Anna's lab is a prime example."
    Br "Yeah."
    Br "It's not the first time, either. But legally they are flawless, for lack of a better word. They know exactly what the borders are and always stop right at the very edge."
    Br stern b "I've received several complaints about their activity, but, as you can guess, there was nothing to incriminate."
    c "They must have a good judicial department."
    Br "They can afford it."
    c "Just like all this hardware."
    Br normal b "Yeah."
    Br "It appears we walked in during the lunch break."
    c "Look, not all of the computers are occupied. This could be our chance."
    Br brow b "Plenty of people are still walking around. They'll catch you easily."
    c "Maybe you could try and distract them?"
    Br "Not a good idea. We don't want them to get suspicious about our whole department."
    c "Alright. Then just play along. I'll figure out a plan."
    Br normal b "Try and think of something. I'll go have a talk with the manager about the cases they're currently investigating. You have time until I return."
    Br "Be careful."
    c "I'll do my best."
    
    hide bryce with easeoutleft
    
    $ eckbryceannahelpinv1 = True
    $ eckbryceannahelpinv3 = True
    $ eckbryceannahelpinv4 = True
    $ eckbryceannahelpinv5 = True
    $ eckbryceannahelpinv6 = True
    $ eckbryceannahelpwifi = False
    $ eckbryceannahelpnet = False
    
label eck_bryce_annahelplabmenu:
    menu:
        "Try to use one of the free computers." if eckbryceannahelpinv1:
            m "The moment I sat down in front of the monitor, I heard a polite yet firm request to stay away from their hardware."
            c "(I guess they won't let anyone close to their files.)"
            m "Hastily, I apologized and took another chair in the corner of the room, away from all the computers."
            
            $ eckbryceannahelpinv1 = False
            jump eck_bryce_annahelplabmenu
            
        "Have a chat with employees.":
            if eckbryceannahelpwifi:
                m "I pointed at my PDA and politely asked if I could use their wireless network to access some websites. Surprisingly, one of the employees gladly provided me with the password."
                c "(That was easier than I expected.)"
                m "I thanked him for the help and returned to my place."
                $ eckbryceannahelpinv2 = False
                jump eck_bryce_annahelplabmenu2
                
            else:
                m "I tried to stir up conversation with one of the dragons, but he excused himself, citing how busy he was."
                jump eck_bryce_annahelplabmenu
            
        "Use your PDA to scan for available networks." if eckbryceannahelpinv3:
            m "A quick search revealed a single protected network covering the office. It was compatible with my device but required a password."
            $ eckbryceannahelpinv3 = False
            $ eckbryceannahelpwifi = True
            jump eck_bryce_annahelplabmenu

label eck_bryce_annahelplabmenu2:
    menu:
        "Remotely access file-sharing folders." if eckbryceannahelpinv4:
            if eckbryceannahelpnet:
                $ eckbryceannahelpinv4 = False
                jump eck_bryce_annahelplabcollapse
                
            else:
                m "I tried to blindly find a suitable place to plant the viruses but failed to locate any."
                jump eck_bryce_annahelplabmenu2
            
        "Search through the main data server." if eckbryceannahelpinv5:
            if eckbryceannahelpnet:
                m "My attempt to communicate with the investigators' archives ended in a quick failure due to additional layers of digital protection."
                c "(Looks like I can't get to it directly.)"
                $ eckbryceannahelpinv5 = False
                jump eck_bryce_annahelplabmenu2
            else:
                m "As much as I wanted to see their records, I couldn't do so without at least knowing the server's address."
                jump eck_bryce_annahelplabmenu2
            
        "Take a look at the network structure." if eckbryceannahelpinv6:
            m "It wasn't hard to connect to the main hub and find the addresses of every other device currently connected. It required no additional permissions and allowed me to freely navigate the menus."
            c "(It's quite fascinating how they still haven't moved far from our digital solutions after all those years.)"
            m "To prevent a possible global virus spread, I terminated the connection to the outside world and thus isolated all local computers."
            "Investigator 1" "I think our network is acting up again."
            "Investigator 2" "Damn. That's like the fifth time this week."
            $ eckbryceannahelpnet = True
            $ eckbryceannahelpinv6 = False
            jump eck_bryce_annahelplabmenu2
            
label eck_bryce_annahelplabcollapse:
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/fervor.ogg"
    m "Transferring the file only took a few seconds."
    m "A tingle of guilt nipped at my mind for a few seconds while my fingers hovered over the option to unpack the virus archive. This whole situation was entirely my fault, and I was about to make it worse for others just to fix my own mistakes."
    m "With a heavy heart, I confirmed my command. Despite the minor differences in general environment, numerous malicious programs got to work almost immediately. My PDA was secure, but the same couldn't be said about the dragons' computers."
    m "Minutes later, panic spread through the office."
    "Investigator 1" "Why is there a huge picture of a naked human female blocking my screen?! I can't close it! Could someone help?"
    "Investigator 2" "I see a countdown! Is this a bomb? Please don't be a bomb."
    "Investigator 3" "What is Bitcoin and how do I send 300 of whatever \"dollars\" are to decrypt my files? This isn't even a real address, just a bunch of random letters and numbers."
    c "(I should've chosen more carefully what to upload, but too late now.)"
    m "Eventually, someone got the idea to shut down the power completely to prevent any further damage, but I knew that it was too late for both the individual computers and the data sever."
    scene eckcomproom2 at Pan ((0, 150), (0, 150), 0.0)
    show dark2
    m "Bryce swiftly approached me with a concerned look on his face."
    show bryce stern b behind dark2 with dissolve
    Br "Whatever just happened, I don't think we'll be able to cooperate with them today."
    c "Yeah."
    Br flirty b "Although, I caught a glimpse of some interesting images. Those human females were certainly something."
    c "Seriously, Bryce?"
    Br laugh b "I'm just joking! You are my one and only human."
    c "That's because I am."
    Br flirty b "You know what I mean."
    c "You sure choose the best time and place for such talks."
    Br smirk b "You're right. Let's take this outside."
    c "Panic, darkness and apparent system collapse, yet all you're thinking about right now is this?"
    Br laugh b "I can't change anything about those things, so why worry?"
    c "Good point. We better move, though."
    
    scene buildingoutside with dissolvemed
    show bryce normal b with dissolve
    
    c "You put up a decent act in the end. Though, couldn't you pick a less awkward topic to get us to leave?"
    Br laugh b "Nope. C'mon, let me have some fun."
    c "Alright, alright. It worked, and nothing else matters."
    Br normal b "But let's get serious, [player_name]."
    Br stern b "It's pretty obvious who's the culprit here. Everything points to you and your PDA, and they'll easily figure out the rest."
    c "It was the only way, sadly. But I don't think they'll be able to prove any sort of ill intent on my side. Computer viruses can lay dormant for years."
    Br "It would still make you suspicious."
    c "A risk I'll have to take. Hopefully those programs wiped everything clean, including each other."
    Br normal b "Please be careful, [player_name]."
    c "I will. Don't worry, Bryce."
    Br flirty b "So, are we dropping at your place or mine this evening?"
    c "I'd say yours for the sake of diversity."
    Br normal b "Aw, but I like your spacious bed."
    c "So do I. But think about all the warm snuggles in the limited space."
    Br flirty b "There's some fine beer in the fridge, too."
    c "Normally I'd be against you drinking, but maybe just today we can make an exception."
    
    $ eckbryceannaclues -= 5
    $ eckbryceannalabavail = False
    jump eck_bryce_annahelpmenu
    
    
label eck_bryce_annahelpfailure:
    play music "mx/bells.ogg"
    $ save_name = _("Bryce 6D Main")
    window show
    n "Somehow, the other investigation group managed to discover the evidence tampering and link it back to me, specifically."
    n "It caused a massive backlash from the council, which resulted in me getting fired from the force. However, due to my previous service to both the local community and the world as a whole, they didn't go any further than that."
    n "Thankfully, nobody else in our group suffered any consequences. Bryce was concerned about the future of our police team, but a complete lack of official statements or responses from the council indicated that they didn't want to push the issue further."
    n "Anna's case, on the other hand, was greatly reinforced once my actions had been revealed. It had given them every reason to believe that the evidence I'd tried to tamper with was incriminating enough."
    n "On the final day of the trial, we gathered in one of the court's many waiting rooms."
    window hide
    nvl clear
    
    scene eckwaitingroom1 at Pan ((0, 150), (0, 150), 0.0) with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/aquavitae.ogg"
    
    show sebastian disapproval at Position (xpos = 0.9) with dissolve
    show bryce stern behind sebastian at Position (xpos = 0.8) with dissolve
    show naomi blank flip at Position (xpos = 0.1) with dissolve
    show maverick normal flip behind naomi at Position (xpos = 0.2) with dissolve
    
    m "With limited space and no other option, I had to share an armchair with Sebastian."
    Br "This place is pretty cramped."
    Nm "I know! And this cursed table leaves me no forearm room at all."
    Mv "Same. The staff said it was used for a meeting consisting of runners and small flyers. They didn't expect us to come in next."
    c "How long do you think the trial will take?"
    Br brow "A while."
    Br stern "Tell me, do you think it was worth it to try something so risky, [player_name]?"
    c "I just wanted to do the right thing, you know."
    Mv "Yet, you failed. Perhaps not trying would've been a better option for you."
    Mv "You thought you could fix everything, but in the end you only made it worse for everyone involved, especially for yourself and Anna."
    Sb "At least nobody else got hit."
    Br "Yeah. That would've been a disaster."
    Nm stern flip "And now Anna is going to face the full consequences of our failure."
    c "We can't be sure yet what the court will decide."
    Nm "Don't lie to yourself. We both know that her case is as good as closed. We should've been more careful and thought of clean-up in advance."
    Br "Or not broken the law at all."
    c "Everything is a lot more obvious in hindsight, isn't it?"
    Sb normal "True. We couldn't predict how it would turn out back then."
    Mv "We didn't need to foretell the future, we only needed to do our job better than that. I did my part, but you botched yours, [player_name]."
    Nm annoyed flip "Don't put the blame on [player_name]. Each of us can think for themselves and we let this mess happen, whether you want to admit it or not."
    Mv sideeye flip "I'm sharing my observations, that's all."
    show naomi blank flip with dissolve
    c "It was my fault from the very begining, no denying it."
    Br sad "Maybe I should've interfered as the chief of police before this went too far. You all are my responsibility. But, just like the rest of us, I couldn't predict the outcome and consequences of our plan."
    c "Don't blame yourself, Bryce."
    Sb "At least they didn't jail anyone from our team."
    show bryce normal with dissolve
    c "They couldn't afford it. Locking up a savior of the world wouldn't look good in the news."
    Mv "Same reason they never investigated what happened in the corridor of that underground complex near the portal. Public images and people's approval are more important than the truth."
    Nm "That's politics for you. I bet [player_name]'s recent story will never make it to a single media outlet."
    c "Not complaining."
    Br "For once, their interests match ours."
    c "Else I imagine finding a new job would've been a nightmare."
    Sb "You can always participate in scientific work and earn tons of money. I heard mere samples of human blood could set you for life, let alone offering a human's direct cooperation."
    c "I see."
    Nm "You could also apply for the position of a data analyst and help sort out the electronic devices you've brought to our world. It would be a shame not to use the knowledge they contain."
    Br "Either way, I'll help you out with money while you're making your choice."
    c "Thank you. I'd prefer to do some actual work for a living, so that data analyst idea sounds good."
    Mv normal flip "Nothing stops you from selling blood samples on the side. As far as I'm aware, it's perfectly legal, and their value eclipses the most expensive items I know."
    c "At least I'd be able to pay back Bryce."
    Mv "Several thousands times over."
    Br smirk "You don't have to."
    show bryce normal with dissolve
    c "How long do you guys think the trial is going to take? The suspense is killing me."
    Nm "As long as they deem it necessary. You are well aware how formal every detail has to be, so naturally it takes time."
    Br "At least we're formally at work while sitting here chatting."
    Sb "They don't have a radio or TV here, do they?"
    Mv "I'll ask staff."
    show maverick normal with dissolve
    hide maverick with easeoutleft
    m "Naomi stretched over the entire available soft surface with a contented groan and put her head down on the armrest."
    play sound "fx/sheet.wav"
    show naomi at Position (xpos = 0.15) with ease
    Nm smile flip "Ah, a whole couch to myself."
    Nm normal flip "For now."
    c "Mav is going to want his seat back, though."
    Nm "I know."
    Sb "Anyone need some snacks or drinks? We're here for a while, so might as well make the wait more comfortable."
    Br "Just bring the usual for everyone. You can take my card."
    Sb smile "Thanks, Chief."
    hide sebastian with easeoutleft
    c "I'm still wondering if things could've been different."
    Br stern "You don't plan to use the portal again, do you?"
    c "No, not anymore. It feels so weird to have the ability to go back and fix any mistakes you make along the way."
    c "You can't help but wonder about the opportunities, and it almost makes you too careless."
    c "Until you realize that your mistakes aren't going to disappear just because you can't see them anymore. They will always continue to exist in the life you've left behind, and nothing can be done about it."
    Nm shy flip "I don't follow."
    Nm blank flip "It sounds like you're saying can just go back in time and change whatever you'd want."
    Br "It's a long story, Naomi."
    c "I promise, I'll tell you everything one day."
    Nm smile flip "Don't let the blunder with our planned meeting repeat itself, though."
    c "Hey, we can still make it happen."
    Nm normal flip "I guess I'll be waiting for that mythical phone call, then."
    $ renpy.pause (1.0)
    show maverick normal flip behind naomi at Position (xpos = 0.2) with easeinleft
    $ renpy.pause (1.0)
    Mv "I've managed to obtain a TV. Naomi, can I get my sitting space back?"
    Nm shy flip "Oh, yes, sure."
    play sound "fx/sheet.wav"
    show naomi at Position (xpos = 0.1) with ease
    show naomi normal flip with dissolve
    m "Maverick placed his trophy on the desk and, after some fiddling with the power cable, turned it on."
    m "It was the usual boring news program, but it was better than letting the unnerving silence take over the room. Conversation died down as everyone switched their attention to the screen."
    show sebastian normal flip at Position (xpos = 0.9) with easeinleft
    show sebastian normal with dissolve
    Br smirk "Welcome back, Seb. Got the supplies?"
    Sb "Yeah. This should be enough for everybody here while we wait."
    
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene eckwaitingroom2 at Pan ((0, 150), (0, 150), 0.0)
    show sebastian normal at Position (xpos = 0.9)
    show bryce normal behind sebastian at Position (xpos = 0.8)
    show naomi normal flip at Position (xpos = 0.1)
    show maverick normal flip behind naomi at Position (xpos = 0.2)
    with dissolvemed
    
    m "By the time we were given a warning that the trial had finally concluded, it was far into the evening. Stress and anxiety had mostly subsided in my mind, but their echoes still roamed free at the back of my head."
    m "In a matter of minutes, all parties were going to leave the courtroom. I felt a cold shiver run down my spine."
    c "I guess it's time we find out the verdict."
    Br brow "I have a bad feeling about this."
    Mv "So do I."
    Nm shy flip "I'll stay back and clean up."
    Sb shy "I'll help."
    c "Is something wrong?"
    Nm sad flip "If things didn't turn out so well... I don't want to be there to see and experience all that. Just tell me later how her case ended, alright?"
    Sb disapproval "As for me, I know you guys had a history with Anna, and I don't want to get in the way."
    c "Alright, I see. Still, thanks for being with us, you two."
    Sb normal "You're welcome."
    Nm normal flip "I'm always glad to help."
    
    scene eckcourtcorridor2 at Pan ((0, 150), (0, 150), 2.0) with dissolvemed
    show bryce brow flip at Position (xpos = 0.1) with easeinleft
    show maverick normal flip behind bryce at Position (xpos = 0.2) with easeinleft
    
    Br "Here they are."
    stop music fadeout 2.0
    $ renpy.pause (3.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (3.0)
    show anna sad at right with easeinright
    play music "mx/fragments.ogg"
    
    m "Anna walked out of the room followed by two security guards and, I assumed, her lawyer. Her expression alone told me everything there was to say."
    m "As they walked past us, she stopped for a moment."
    $ annastatus = "bad"
    An disgust "Thanks for your aid, [player_name]. You did an amazing job making everything so much worse for me."
    An sad "I have two weeks of house arrest before they take me away to jail. Don't bother coming over or trying to apologize. I don't give a damn."
    c "But I didn't mean to..."
    An disgust "Didn't you hear what I just said? I don't need your excuses."
    Mv "Anna, I'm sorry we failed."
    An sad "I guess our little thing was never meant to be, Mav."
    Mv "I'll be waiting."
    An "Don't. It will be a while until we see each other again. Build your own life and don't look back. Farewell."
    m "She gave us one last disappointed glance before heading off towards the exit."
    hide anna with easeoutleft
    Mv "So this is what happens when you try to be more than an unwitting pawn, [player_name]."
    show maverick normal with dissolve
    hide maverick with easeoutleft
    m "Maverick rushed off to follow Anna. He stopped her right at the door and suddenly pulled her into a tight embrace with his forearm and both wings."
    m "They parted soon after. He looked back at me and Bryce, then left the building and took off."
    hide bryce with dissolve
    show bryce stern with dissolve
    c "I guess there's nothing else left to do here."
    Br "Yeah, we're done."
    c "Mind going for a walk?"
    Br normal "Not at all."
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene black with dissolveslow
    play music "mx/markday10.ogg"
    $ renpy.pause (2.0)
    scene eckduskforest at Pan ((0, 0), (0, 0), 8.0) with dissolveslow
    show bryce normal with dissolve
    
    Br "Do you still think it was really worth it, [player_name]?"
    c "I don't know, Bryce. I just don't know."
    Br stern "You could've ended up in jail! You don't realize that, do you?"
    c "I was aware of the consequences. But you know how it goes. Everyone is certain that they're smart enough and they won't get caught. As it seems, I'm no better than these fools."
    Br sad "Don't get me wrong. I'm not angry or mad at you. I was just worried you could've ended up in some big trouble trying to help someone I'm not certain you should have."
    c "I had to try, Bryce."
    c "She hasn't done anything that warrants a prison sentence. Yet here we are."
    Br stern "It's a miracle we weren't all fired – or worse – after the investigation was concluded."
    Br "But I can't say that you're the one who dragged our entire department into this. It was our group decision to help Anna. For better or worse."
    c "Sadly, for worse. Much, much worse. My first and last case didn't turn out so well, did it?"
    Br normal "At least I still have you, [player_name]."
    show eckclouds2 at Pan((150, 50), (0, 0), 12.0) with fade
    $ renpy.pause (5.0)
    c "And I'm happy to have you and your support, Bryce."
    Br smirk "Poor decisions or not, no matter the circumstances, I'll be there for you. I promise."
    c "Thank you."
    hide eckclouds2 with dissolve
    Br normal "It's getting late. Do you want me to escort you home?"
    c "Sounds lovely."
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene black with dissolveslow
    window show
    n "On the next day, we learned about an attack on Anna's apartment during the night. An unknown culprit managed to knock out both guards stationed nearby and aided her escape under the cover of darkness."
    n "At the same time, Maverick didn't show up for his shift. Our police department managed to easily connect the dots and figure out how exactly events went. However, any attempts to figure out the culprits' whereabouts were fruitless."
    n "No traces of either Maverick or Anna were ever discovered. Their eventual fate was unknown."
    window hide
    nvl clear
    $ renpy.pause (2.0)
    $ persistent.eckbryceendingseend = "D"
    show eckbryceendingseenimgd with dissolveslow
    $ renpy.pause (1.5)
    hide eckbryceendingseenimgd with dissolveslow
    play sound "fx/system.wav"
    s "Congratulations, you've gone with your heart and tried to do the right thing by helping Anna. Sadly, your performance left a lot to be desired and only worsened the situation."
    s "Perhaps calling your job completed before it's done might not be the wisest idea. You're dealing with a sensitive matter after all, [player_name]."
    if persistent.trueending == True:
        s "In the end, though, humanity is safe in another timeline, you and Bryce are still together, and your bond has survived a great test. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng]"
    else:
        s "In the end, the cycle continues in another timeline, you and Bryce are still together, and your bond has survived a great test. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng]"
    
    jump eck_bryce_goodendcredits
    
    
label eck_bryce_annahelpsuccess:
    play music "mx/forge.ogg"
    $ save_name = _("Bryce 6E Main")
    window show
    n "With the combined efforts of our group, we managed to avoid raising any suspicion from the council when transferring Anna's case to the court."
    n "Naomi also formally started a case against Damion for blackmailing and extortion, but had to close it almost immediately because of death of the suspected individual."
    n "Maverick did his part and, using Anna's directions, was able to quickly clear out or dispose of all the incriminating items and documents not yet discovered by the police."
    n "Due to the lack of direct evidence, the prosecution side of Anna's trial quickly ran out of arguments to support their position, which soon started to crumble."
    n "On the final day of the trial, we gathered in the court waiting room."
    window hide
    nvl clear
    
    scene eckwaitingroom1 at Pan ((0, 150), (0, 150), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    
    show sebastian normal at Position (xpos = 0.9) with dissolve
    show bryce normal behind sebastian at Position (xpos = 0.8) with dissolve
    show naomi normal flip at Position (xpos = 0.1) with dissolve
    show maverick nice flip behind naomi at Position (xpos = 0.2) with dissolve
    
    m "With no other option, I had to share an armchair with Sebastian."
    Br "This place is pretty cramped."
    Nm blank flip "I know! And this cursed table leaves me no forearm room at all."
    Mv "Same. The staff said it was used for a meeting consisting of runners and small flyers. They didn't expect us to come in next."
    c "How long do you think the trial will take?"
    Br "It should be over soon. The verdict is as good as decided already."
    Br smirk "Looks like your little gamble has paid off, [player_name]. But was it the right thing for us to do? So many laws and regulations were broken."
    c "I know. Sadly, our only choice was either this or to let a talented scientist face prison for trying to save lives."
    Nm smile flip "Don't feel bad, Bryce. All's well that ends well."
    Mv "We give no slack to actual criminals, and we never will. In Anna's case, however, I believe we've followed our oath to the letter. To serve and protect our people."
    Sb "Yeah, when you put it that way."
    Br normal "The council didn't share your point of view, guys. I had a rather tense phone call with one of their representatives yesterday."
    show naomi normal flip with dissolve
    c "Any reasons for concern?"
    Br laugh "Not at all."
    Br normal "They gave me a stern warning not to mishandle the cases, and that they'll keep an eye on our performance from now on."
    c "So they don't have anything on us."
    Br smirk "Yep. They are unhappy, but that's it."
    Mv "Looks like we've avoided danger on that front. We shouldn't relax just yet, though."
    Sb drop "Yeah. They might try and get back at us later."
    Br "We are a tight-knit group of professionals. I'm sure we'll manage."
    Nm smile flip "Yeah. Don't forget, we have a legendary human on our side, too."
    c "Oh c'mon, guys. You of all people know I'm nobody special."
    Nm "Nobody special with a medal for saving our planet."
    Sb smile "An important detail, if you ask me."
    Mv "Bryce and I have those medals, too. However, you are right. The council members were likely trying to win some popularity points by jailing a scientist going against tradition and all that. But we got in the way."
    Mv "They wouldn't risk a public backlash by attacking us in any way, unless they had a fool-proof plan."
    c "A good point."
    m "One of the staff members entered the room and notified us that the trial had concluded. All too happy to leave the cramped room behind, we moved to the corridor."
    
    scene eckcourtcorridor1 at Pan ((0, 150), (0, 150), 2.0) with dissolvemed
    show sebastian normal at Position (xpos = 0.8) with dissolve
    show bryce normal behind sebastian at Position (xpos = 0.7) with dissolve
    show naomi normal flip at Position (xpos = 0.1) with dissolve
    show maverick nice flip behind naomi at Position (xpos = 0.2) with dissolve
    
    Nm blank flip "I'm still a little worried about the outcome."
    Sb smile "We can't be certain about anything in our line of work, but our odds look good."
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play sound "fx/door/door_open.wav"
    $ renpy.pause (3.0)
    show anna smirk at Position (xpos = 0.9) with easeinright
    m "Anna separated from the group of dragons exiting the courtroom and walked up to us. A wide self-confident smirk was plastered on her face."
    play music "mx/jazzy2.ogg"
    
    An "Hey, guys. I see you've gathered a welcoming party for me."
    Br "Hello, Anna."
    c "I assume I don't have to ask how your trial went."
    An "Naturally not."
    An "Now, why don't we find a more pleasant place to talk?"
    An normal "I've had enough of this building lately."
    
    $ renpy.pause (2.0)
    scene forest1 at Pan ((0,0), (0,0), 0.0) with dissolveslow
    $ renpy.pause (2.0)
    
    show sebastian normal at Position (xpos = 0.8) with dissolve
    show bryce normal behind sebastian at Position (xpos = 0.7) with dissolve
    show naomi normal flip at Position (xpos = 0.1) with dissolve
    show maverick nice flip behind naomi at Position (xpos = 0.2) with dissolve
    show anna normal at Position (xpos = 0.9) with dissolve
    
    c "Why in the forest of all places?"
    An face "You don't want all those extra ears around us, do you? Else you might as well turn in your badge."
    Br "It's pretty quiet here, though."
    An normal "That was the idea."
    An sad "..."
    An blush "Either way, I owe you all big time. Especially [player_name], Maverick and Naomi for standing up for me when the decision was made."
    An normal "The suspended sentence isn't over yet, and it's irritating, but at least I'm free."
    Mv "I'm glad the issues have been resolved."
    An smirk "Of course you are, Mav."
    show maverick sideeye flip with dissolve
    Nm smile flip "You're welcome. We didn't always get along, but I couldn't let such injustice happen to you."
    An sad "I know I'm a pain in the backside to deal with. You don't have to sugarcoat it."
    Nm normal flip "Any plans to change that?"
    An normal "No."
    Nm blank flip "Thought so."
    Nm smile flip "I'd have been worried if the answer was different, though."
    c "So, back to business as usual now, Anna?"
    An "Yep. I have a lot of work to do and no assistant to help me. But if any of you need something, I'll do my best to fit you into my schedule."
    show naomi normal flip with dissolve
    Br "Maybe you'd want to come over to our next get-together?"
    c "The one we planned to mark the end of Reza's case but didn't get to organize yet?"
    show maverick nice flip with dissolve
    Br smirk "Now we can celebrate the resolution of two cases at the same time."
    Sb "We normally start at late evening or early night, so it shouldn't interfere with anyone's work."
    An "I have to get up early, but one day off wouldn't hurt, I guess. Do I need to bring anything?"
    Mv "No. Normally Bryce covers for everyone."
    Br laugh "Guys, there might be too many of you for my budget now!"
    Nm smile flip "We should pool in some money."
    show bryce smirk with dissolve
    Mv "Agreed."
    Sb smile "Not a problem for me."
    c "I guess we can discuss the organizing part later, though."
    An "Alright, I'll be there. Give me a call about the time and date."
    Br "Of course."
    An "For now I'd say we should split. I need time to rest and think everything over, and you wouldn't want to be seen too much with me for the next week or so."
    show naomi normal flip with dissolve
    Mv "Not even me?"
    An smirk "You are an exception."
    Mv "Good."
    Br normal "You have a point. We wouldn't want to stir up extra suspicion."
    An "Bye, everyone."
    hide anna with easeoutleft
    $ renpy.pause (2.5)
    Br "Either way, guys, let's head back to the department. We still have several hours until our daily shift ends."
    Sb normal "I was hoping for a day off."
    c "Let's not give the council any reason to doubt our qualifications."
    Br "Yeah. Until their inspection is over, we better do everything by the book. Especially you, [player_name]."
    c "It wouldn't be the first time my work got compromised because I tried to do the right thing. I'm used to it."
    Mv "You shouldn't be. Sooner or later, your luck might run out, and you'd better be prepared."
    Sb "Yeah, don't get reckless. We've been walking on the edge already."
    c "I know. But sometimes you just have to take the risk."
    Mv "Sometimes you do. Just remember to pick your battles wisely so you don't end up staring at a gun pointed in your face while your only means of self-defense is a cardboard box."
    c "You still haven't forgotten."
    Mv laugh flip "Hahaha!"
    Mv nice flip "Why should I? I was the damn hero of that day."
    c "Until the Izumi incident."
    Mv sideeye flip "She had it coming."
    Nm stern flip "I suggest we don't bring that up. It's a happy day, and we should keep it that way."
    Br "Agreed. We've had enough negativity on our hands lately."
    Sb drop "And don't get me started on the unsettling stuff."
    Br "Yeah."
    c "Alright, you've made your point."
    Nm smile flip "Much better. Anyone up for some lunch on our way to the department?"
    Br smirk "It is our break time, actually."
    Sb smile "Convenient."
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene black with dissolveslow
    play music "mx/movingon.ogg"
    $ renpy.pause (2.0)
    scene eckbeachb at Pan ((0, 0), (300, 0), 4.0) with dissolveslow
    $ renpy.pause (3.0)
    show bryce smirk with dissolve
    c "You've decided to start setting up earlier this time."
    Br laugh "With so many people attending, the organization won't be easy."
    c "Do you need my help?"
    Br smirk "I'm fine. It's mostly about having you around to talk with while I work on preparations."
    c "Yeah, I've never told you this, but... I'm sorry for going against you during the vote on Anna's case."
    Br brow "..."
    Br smirk "Actually, I'm thankful you did. You've reminded me why I joined the force. To help people and protect them, not to just enforce a list of rules written in some book."
    Br normal "After dealing with crime for so long, you get used to painting the world black and white. The perspective shift you, Mav and Naomi had was like a wake-up call of sorts."
    c "We're often deciding people's fates, Bryce, and we can't be mechanical about it."
    Br "I know."
    c "And you have to admit that setting one foot on the other side of the line was quite an experience."
    Br smirk "Yeah. But let's not do that ever again. One time is more than enough for me."
    c "Unless we'd have no choice."
    Br normal "Of course."
    Br flirty "I'd cross any lines for you, [player_name]."
    c "So would I for you, Bryce."
    Br laugh "I think you've corrupted me, though!"
    Br smirk "Just a year ago I wouldn't even dream of going against the law. But here we are now."
    c "Back home many people used to believe that, as you grow wiser, you learn that the world is a lot more complex than the simple conflict of good agaist evil."
    Br brow "Are you saying that I'm getting old? But I'm too young for that!"
    c "Wisdom doesn't equal old age, Bryce."
    Br laugh "I was worried for a second."
    $ renpy.pause (3.0)
    Br smirk "And preparations are complete."
    c "That was fast."
    Br normal "You've been to our get-together before. All we need is a good spot, several large rocks and food."
    Br wink "This time I also got some drinks."
    c "Don't you dare."
    Br laugh "Don't be so stern, [player_name]."
    Br smirk "I've learned my lesson about alcohol. It's just a little of everything to suit all tastes and lighten the mood."
    c "I see."
    Br "Want to go for a swim while we wait?"
    c "I don't want to spend the rest of the day soaked."
    Br normal "Right. I forgot that you don't have scales so water drops won't simply roll off you."
    c "Yeah. Besides, I think others will be here very soon, so we don't have much time."
    
    hide bryce with dissolve
    
    window show
    n "Maverick was the first to show up. He gracefully landed right next to our gathering spot and, after exchanging brief greetings, wandered off to the water's edge."
    n "Naomi joined soon after, carrying a paper bag with supplies of her own. In response to our questioning looks, she said that she got them just in case."
    n "A group consisting of Sebastian, Anna and Zhong were the last ones to arrive. It was surprising to see her get along with two other dragons she likely barely knew. Of course, her overall friendly tone didn't spare them completely from her sarcastic venom."
    n "By the time they showed up, the sun had completely set."
    n "With everyone present, we all gathered around the rocks Bryce had been arranging earlier."
    window hide
    nvl clear
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    # change music a bit?
    play music "mx/serene.ogg"
    scene beachx at Pan ((0, 0), (300, 0), 5.0) with dissolveslow
    $ renpy.pause (3.5)
    # Total chars to manage for the scene: Bryce, Mav, Naomi, Seb, Anna and Zhong. 6 dragons + MC
    # Life is pain.
    
    show bryce normal at Position (xpos = 0.77) with dissolve
    show naomi normal at Position (xpos = 0.88) with dissolve
    show sebastian normal at Position (xpos = 0.95) with dissolve
    show maverick nice flip at Position (xpos = 0.23) with dissolve
    show anna normal flip at Position (xpos = 0.16) with dissolve
    show zhong normal flip at Position (xpos = 0.1) with dissolve
    
    c "You weren't joking when you said that our get-together was going to be huge."
    An "So, what do you normally do here?"
    Zh "Have fun, fry some steaks or algae, talk with each other and enjoy the company. It's all very simple."
    Br "Yep. Zhong summed it up perfectly."
    Sb "Though, I think this time we might not stay as one huge group for the whole event."
    Nm blank "Yeah. I'm honestly not very comfortable with so many people around me. I feel so clamped and awkward."
    Nm smile "Don't take it wrong, guys, you're all my good friends."
    Mv "I'm fine with whatever."
    An "Doesn't sound too bad. I've actually never attended such gatherings before, so it's a fresh experience for me."
    Br "It's nice, calm and relaxing. Exactly what we all need with how our line of work is."
    An sad flip "Mine is no better than yours."
    Nm blank "I can imagine."
    show anna normal flip with dissolve
    Zh "Mine's alright. But I have to cover two positions at once to make ends meet."
    An "Have you lot ever considered spicing things up and going on a hunting trip together?"
    c "But then I'd end up hungry for the whole event."
    Br wink "I'd share my catch with you."
    show bryce normal with dissolve
    Mv "You have that gun toy. If anything, you're the one who'd have it easy."
    c "I don't like using it. It reminds me too much of the ugly things back home. The ammo is scarce, too."
    Nm smile "I prefer fishing."
    Sb smile "I don't mind hunting, but I get enough running at work."
    An "It was just a suggestion."
    Br smirk "Who wants to start the fire?"
    Sb "I did it last time."
    c "And it was decent."
    Sb "Yeah, but we should switch things up a little. Zhong?"
    Zh "I could."
    Br "Let's agree in advance, though. No cheese."
    Zh "Aw."
    Nm stern "Or I'm going to make you eat algae with cheese like you did to me."
    Sb drop "I haven't ever seen those two things mixed in my life, and it already sounds disgusting."
    show sebastian normal with dissolve
    Nm "It's as bad as it sounds, Seb."
    Zh "Okay, you proved your point. Maybe someone else wants to start the fire?"
    show naomi normal with dissolve
    Sb "Bryce?"
    Mv "If you want to experience his cooking, you might just pick up that stone slab and start chewing on it."
    Br stern "Why, you..."
    An face flip "We aren't getting anywhere."
    An smirk flip "Want me to light up the fire?"
    Br normal "Be our guest."
    Zh "I'm fine with that. Let it be your introduction to the BBQ get-togethers with us."
    Mv "Time to show off those outdoors skills you've been bragging about, Anna."
    An normal flip "Mm-hmm, I will."
    Sb "Hopefully not at the expense of our steaks."
    Mv "What's the worst that can happen?"
    Br laugh "In your case? Nothing really."
    Sb "Yeah, Mav. But some of us have taste buds."
    show bryce smirk with dissolve
    An face flip "Oh, don't be so wussy."
    Br smirk "So, Mistress of Ceremony, it is time to begin."
    An "I can't believe you guys are doing this nonsense."
    An normal flip "Alright, fine."
    
    show anna normal with dissolve
    hide anna with easeoutleft
    $ renpy.pause (2.0)
    m "Anna carelessly walked up to the pile of stones Bryce and I had prepared. She eyed it from a few different angles before looking back at us."
    An "Shouldn't there be wood or something?"
    Mv "No. That's how our tradition works. Want me to help?"
    Nm blank "Let's not start a wildfire, Mav."
    Zh "It would save us a lot of time with cooking, though."
    c "Could we not?"
    Mv "Just hide in the ocean until it's over. Big deal."
    Sb "Get on with the fire already."
    play sound "fx/firex.ogg"
    m "Taking a deep breath, Anna opened her maw wide and let two streams of liquid rain from the corners of her mouth onto the rock pile. Seconds later, a large fire sparked up amongst the stones."
    $ renpy.pause (2.0)
    stop sound fadeout 2.0
    show anna normal flip behind zhong at Position (xpos = 0.16) with easeinleft
    hide zhong
    show zhong normal flip at Position (xpos = 0.1)
    
    An smirk flip "See? Nothing to worry about."
    Nm "You have an intense flame."
    c "I'm sorry I never asked, but what's your fire like, Naomi?"
    Nm normal "Water dragons don't have it. But we can spit acidic venom, which is pretty useful."
    Nm "It works underwater, you can blind larger animals from a long distance, or shoot down low-flying birds for a quick snack."
    Zh "It won't make a good cooking tool, though."
    Mv "Obviously."
    show anna normal flip with dissolve
    c "And I'd rather not take my chances eating something that has been poisoned."
    Nm smile "It's totally safe to eat, actually."
    Nm shy "For me, at least."
    Zh "I'm with [player_name] on this one. Venom earns a big 'no' from me."
    Br "Alright. Make your picks and knock yourselves out, everybody."
    show naomi normal with dissolve
    Mv "I've been waiting for this."
    
    show zhong normal with dissolve
    hide zhong with easeoutleft
    hide maverick with easeoutright
    hide anna with easeoutright
    hide naomi with easeoutleft
    show bryce normal flip with dissolve
    hide bryce with easeoutright
    hide sebastian with easeoutleft
    
    m "Everyone added their food to the fire and gathered in a circle around the burning pile of rocks. With a flame so intense, it only took a few minutes to properly sear everything."
    m "Once done with cooking, the dragons spread across the beach, forming smaller sub-groups. Bryce and I settled near the forest's edge."
    
    show bryce normal with dissolve
    
    Br "A little dry and overcooked, but I'd say she did alright."
    m "I took a bite from my own piece of food. Its temperature was just below being too hot to hold or chew on."
    c "Yeah. It was fast, too."
    Br smirk "No wonder. The flame wasn't much weaker than Maverick's. She has much better aim, though."
    Br normal "Mav's fire seems to set everything ablaze in an arc in front of him, rather than burning the target he's aiming at."
    c "That explains the jokes about a wildfire."
    Br "It's not really a joke."
    c "Huh."
    Br flirty "Some day, want to go out with nobody but us two and a fun basket?"
    c "Oh my. I like the way you think."
    Br "That's the spirit."
    Br normal "Of course, not today or tomorrow, but are you up for it in general?"
    c "Maybe. Sounds like an adventure."
    Br flirty "One you won't forget."
    c "No doubt here."
    m "Bryce glanced back at the main gathering spot."
    Br normal "Want to rejoin Seb and Zhong? Seems like everyone else has split up and moved away from the fire."
    c "Maybe it's because we separated from them?"
    Br laugh "Oh, c'mon, they can't be that fast to follow our example."
    c "I'm going to check on the others and then come back to the fire."
    Br smirk "Sure thing."
    
    hide bryce with dissolve
    
    
    # Anna and Mav encounter
    m "I walked up to Maverick and Anna sitting side-by-side on the sand. He was busy munching on a sizeable steak while she sat staring at the horizon, her food almost untouched."
    show maverick nice flip at Position (xpos = 0.23) with dissolve
    show anna normal at Position (xpos = 0.87) with dissolve
    
    c "I hope I'm not interrupting anything."
    An "It's fine, [player_name]. Mav and I have wanted to talk to you in private for some time."
    c "Alright. What about?"
    Mv "You've done a great job helping Anna, and you know I don't throw such words around easily."
    c "Uh, thanks?"
    Mv normal flip "I've caused you enough trouble from your first day here, [player_name]. Yet, you've proved your intentions true and my doubts to be unfounded."
    Mv "Thus I offer you my apologies. Anna and I both would also like to thank you for taking a huge risk to give her this chance."
    An face "I can speak for myself, you know, Mav."
    An normal "But I agree with you. Your whole team helped me, but [player_name]'s actions are the main reason I can walk freely today."
    Mv "I won't forget that."
    c "I was happy to help. So, peace?"
    Mv "Peace, [player_name]."
    c "Maybe we'll become good friends eventually."
    Mv "If you choose. For what you've done, I'd consider you a friend already."
    c "Sounds good to me."
    Mv "Then it's settled."
    An normal "And if you ever need anything from me or Maverick, just ask."
    c "Sure. You two get along well, I see."
    An smirk "It didn't take much to start our flame again."
    Mv nice "I missed the good old days you and I shared, Anna."
    An "Perhaps you weren't alone in that sentiment. The past is gone, of course, but we can create something new together."
    c "Good luck with your new attempt and watch out for the life-work balance, you two."
    Mv "In the past, we got so absorbed in our work we didn't notice how we drifted apart. I won't let it slip this time."
    An normal "Neither will I."
    
    hide anna
    hide maverick
    with dissolve
    
    # Naomi (Sebastian joining later)
    
    m "Leaving Anna and Maverick to themselves, I spotted a lone figure in the moonlight resting a few meters away from the shore in the water. I easily recognized Naomi thanks to the crest shape and headed towards her."
    m "I decided against wading into the sea, however."
    show naomi normal with dissolve
    c "Hey."
    Nm "Hey."
    c "Why are you all alone?"
    Nm shy "Oh, I just get nervous when too many people are around."
    Nm normal "Don't get me wrong, [player_name], but since you and Anna joined, it became too crowded for me."
    c "I see."
    Nm "I like hanging out with you guys. It helps me a lot to get through day after day of police duties. But with so many of us here, I felt exhausted and needed a timeout."
    c "It's alright."
    c "Looks like everyone has split up into smaller groups."
    Nm blank "I hope it's not because of me."
    c "Of course not. Anna probably wanted some time with Mav, Bryce and I had a little something to discuss, and the rest of the crew are still next to the fire."
    Nm normal "Oh."
    Nm "I'll go back in a moment, too. It doesn't feel right to make myself into a weird outcast, either way."
    c "We've gathered here to have fun. It doesn't have to follow any specific rules or anything."
    Nm "But what would the others think of me?"
    c "I doubt anyone would mind."
    Nm "Maybe you're right."
    m "My eyes fell on Naomi's arm drawing slow circles in the water. It didn't look like simple idle movement."
    c "What are you doing?"
    Nm smile "Oh, I'm just playing with a small school of fish. They think my fingers are food, chase them around and nibble at the scales. It tickles a lot but they're fun to watch."
    c "Aren't they afraid of you?"
    Nm "Not really. In their little minds, the unmoving part of me is probably a rock or something."
    c "I doubt they question anything at all, really."
    Nm "A fair point."
    Sb "Hey, guys."
    
    show naomi normal at right with ease
    show sebastian normal flip at left with easeinleft
    
    c "Do you need something?"
    Sb smile flip "Naomi forgot her food in the fire. Here, I rescued it for you."
    Nm smile "Oh, my bad. Thank you, Seb."
    Sb "Could you take it off me? I don't want to wade into the water."
    Nm "Sure. Give me a moment."
    
    hide naomi
    hide sebastian
    with dissolve
    
    play sound "fx/wading.ogg"
    $ renpy.pause (0.5)
    play sound2 "fx/wading.ogg"
    
    m "Naomi stood up on all fours, stretched her limbs, and then quickly made her way to the shore. She grabbed a stack of food off Sebastian's hands and sat down on the smooth sand."
    
    show naomi normal at right
    show sebastian smile flip at left
    with dissolve
    $ renpy.pause (1.0)
    play sound "fx/pizzabite.ogg"
    $ renpy.pause (1.5)
    Nm smile "A little overcooked, but good. Nice save."
    Sb "You're welcome."
    Nm normal "Want some? It's a lot like your vegetables."
    Sb "Uh, I'll pass. I never liked seafood."
    Nm smile "It's not just algae, silly."
    m "Naomi propped herself almost vertically to free up both hands and snapped the piece she'd taken a bite from in half, revealing the steaming hot inside of a juicy steak."
    Nm "There, take it."
    Sb shy flip "Thanks."
    Sb smile flip "I've just finished my meal, though. Want half of this, [player_name]?"
    c "Why not. Thanks."
    show naomi blank with dissolve
    
    m "Under the crispy almost tasteless outer layer of algae, the juicy meat itself had a pleasant smooth texture preserved surprisingly well considering the time it spent on a heated rock."
    m "For a time, we were in relative silence. Not wanting to get sand in my clothes, I chose to stand. Sebastian and Naomi, on the other hand, sat next to each other while we were eating."
    
    Sb "Are you feeling alright?"
    c "Me?"
    Sb normal flip "Considering the constant smirks and glances you and Bryce exchange, I wouldn't worry. I was asking Naomi."
    Nm "I'm fine, Seb. Don't worry."
    Sb "Why did you run off, then?"
    Nm "You know how I don't like big gatherings. I'm aware how weird it sounds, but I feel lonely and very uncomfortable when surrounded by chatting people."
    Nm "And when I try to contribute, unless someone talks to me directly, it seems like I'm making unrequested remarks nobody asked for or listens to."
    Sb "But we're all friends here, not strangers, and you're an important part of our team."
    Nm sad "You're right. But I can't help it."
    Sb "Are you feeling bad because of Anna's case?"
    Nm "I guess I can't hide it from you."
    Nm blank "[player_name] knows how exhausted I was after Reza's case. Remember what you told me?"
    c "That it's a small town and not many things happen."
    Nm stern "Some small town it turned out to be. As if Reza and a planet-destroying comet weren't enough, we were dealing with an extremely delicate case with Anna. I know I stood up for her during our argument, but..."
    m "Naomi took a long pause."
    c "But what?"
    Nm blank "This whole time my mind has been questioning our decision. We were breaking the law, after all, and I was afraid of the council's retaliation if they found out about our actions."
    Nm "I didn't have much to lose myself. At worst I'd have settled for a simpler life or looked for an accountant job or something. But to think that my vote contributed to any of you guys losing your jobs and getting your lives ruined..."
    Nm sad "It horrified me."
    c "Working against Anna's case was a risk we all understood well. You didn't make us do it; each of us made the decision for ourselves."
    Sb smile flip "Yeah. And I had my doubts about our course of action as much as you did, Naomi. But, hey, it all ended well. We aren't fired, Mav got his girlfriend back, and Anna might be easier to deal with from now on. Sounds like a success to me."
    Nm shy "I guess you have a point. Now you know why I was so tense and stressed, and I hoped to get some respite during our get-together. However, with too many people around, I couldn't."
    Sb "Want to go out sometime? It might help you feel better."
    Nm smile "That sounds lovely. Thank you, Sebastian. We could go swimming together and explore the ocean floor, then drop into a cafe so we won't have to deal with cooking."
    Sb drop flip "Uh, I'm not good in the water. Even after training, we runners tend to have problems with something as simple as not drowning."
    Nm "That's why you'll have me to help and teach you. It's going to be fun, promise."
    c "I think you two might have different definitions of fun."
    show sebastian normal flip with dissolve
    Nm "Actually, I have a lot of other ideas, too. We can discuss the details later, Seb. I hope you won't pull a [player_name] on me, though."
    Sb drop flip "Naomi, didn't we agree..."
    c "Hey, what's that supposed to mean?"
    show naomi shy with dissolve
    Sb "Uh, nothing."
    Nm "Yep. Nothing at all. You certainly didn't become an inside term for leaving people hanging."
    c "Really now."
    Nm smile "You only have yourself and your memory to blame."
    Sb smile flip "Don't feel bad. It's all harmless fun."
    c "Alright, I'll see you at the campfire. Don't have too much fun here without me."
    Sb "We'll be alright. We aren't on the same stage of knowing each other as you and Bryce are, anyway."
    c "Why, you..."
    Nm "See you, [player_name]."
    
    hide naomi
    hide sebastian
    with dissolve
    
    # Bryce and Zhong
    m "Feeling my face burn red, I quickly walked back to the pile of rocks that used to be the campfire. Only Bryce and Zhong were sitting next to it."
    
    show bryce smirk at Position (xpos = 0.85) with dissolve
    show zhong normal flip at Position (xpos = 0.2) with dissolve
    
    Br "...and then I made the decision to cut my amount of alcohol."
    Zh "You should've done so a long time ago. You were starting to worry me."
    Br "Yeah, it was becoming a problem, Zhong. Something had to be done."
    c "Hey."
    Br "Good to see you back. I was explaining to Zhong why I don't visit his bar as often."
    Zh "It's not my bar, technically."
    c "Is the store yours?"
    Zh "Why would I need a second job if I had something like that? Though, bartending is somewhat fun, if not very well-paid."
    Zh "At least, with the extra money to spend, I can keep my son happy. It's all that matters to me. We're going on a trip soon, too."
    Br normal "Across the whole country. I remember."
    c "Safe travels, then."
    Br "Once we get a vacation, we could go on a trip as well. You haven't seen much outside of this town, have you?"
    c "To be honest, I didn't think about it yet."
    Zh "There's a lot of things to see. I'm sure you'll find at least some of them quite interesting."
    c "Maybe sometime later. I've barely come to terms with the fact that I'm to spend the rest of my days in this world."
    Br wink "I'll make sure you enjoy your stay."
    Zh "You don't like it here?"
    show bryce brow with dissolve
    c "It's a wonderful land with great people, and I enjoy your company a lot, guys. But nothing can replace home, and I won't see another human ever again."
    Br sad "Didn't you lose your home when the flare hit and turned everything upside down?"
    c "I guess you're right. Life past that day was a dark grey blur of trying to survive the new reality."
    Zh "How bad is it in your world?"
    c "I don't want to bring down everyone's mood."
    Br "In short, Zhong, it's absolutely terrible."
    Zh "I'm sorry to hear that."
    Zh "Hopefully we won't meet the same fate one day."
    Br normal "I'd say enough with the dark stuff."
    c "Let's try and move on. There's nothing we can fix or change here."
    c "(Not me; not anymore, at least.)"
    Zh "Agreed."
    Br "We didn't get to my supply of drinks yet, actually."
    c "Are you sure it's a good idea?"
    Br "You know that I'm done with heavy drinking, so I promise it won't be anything you'd have to worry about."
    c "I'll keep an eye on you."
    Br flirty "Same here."
    Zh "What do we have?"
    Br normal "A little of everything, but since even Seb has run off somewhere, I suggest we wait."
    c "Speaking of whom."
    
    show bryce normal at Position (xpos = 0.77) with ease
    show naomi normal flip at Position (xpos = 0.88) with easeinleft
    show sebastian smile flip at Position (xpos = 0.95) with easeinleft
    show zhong normal flip at Position (xpos = 0.1) with ease
    show naomi normal with dissolve
    show sebastian smile with dissolve
    
    Sb "We're back."
    Nm "I'm sorry for taking so long. We were discussing some things."
    c "Got your plan for the meeting figured out?"
    Nm "Mostly. Just a few details left."
    Br wink "Are you two having a date?"
    Nm stern "Those are very big words to describe our friendly meeting. I'm not feeling well lately, and Seb decided to help me. That's all."
    show bryce normal with dissolve
    Sb "Yeah. It's nothing serious."
    c "C'mon, Bryce, not everyone here is out to score themselves a date all the time."
    Nm shy "Not that I would mind going on one..."
    Sb shy "..."
    Zh "Awkward."
    Nm sad "I shouldn't have said it out loud. I'm sorry, Seb. I hope you won't back out from your idea because of it."
    Sb "Uh. You've caught me off-guard here."
    Sb "But, honestly, I wouldn't mind either, Naomi."
    show naomi shy with dissolve
    Zh "How cute."
    Br smirk "I know, right."
    Nm smile "We'll see how things unfold, and I doubt I can predict the outcome of the case."
    Sb smile "That's what makes it interesting."
    c "Oh yeah. You can never guess what will happen next."
    Br laugh "Except for you and the whole portal thing."
    Nm normal "Portal? But it's only used for transporting people and items between worlds, isn't it?"
    Sb "Yeah, how is it related to knowing things in advance?"
    show bryce smirk with dissolve
    c "(For a moment I was struck by a cold sweat.)"
    c "That's a different story for another time. Besides, it's not applicable anymore as far as you know, Bryce."
    Br normal "Oh, right."
    Zh "I have so many questions."
    Br "It's complicated."
    Nm "Alright. Is it something I should be worried about? Like that comet?"
    c "No, of course not. It's pretty silly, to be fair. For a few days after going through the portal, I was seeing dreams of the events yet to happen, and they often matched reality almost perfectly later on."
    Nm "You aren't alone. I experienced it myself during Reza's case."
    Nm "Oh, and several times in my dreams I saw a wall of fire approaching our town. I don't mean a wildfire or anything, but an actual rolling wave of flame, smoke and debris as wide as the horizon itself moving at some huge speed."
    Nm sad "I knew there was no escape. Not even diving into the sea could've saved me. So I sat there and watched it approach rapidly, sweeping away everying in its path until it reached me, and I woke up."
    Nm "It was so terrifying."
    Zh "And I thought it was merely a weird vision I got from overworking myself."
    Sb drop "I had the exact same one. I also saw myself being killed by one of the culprits right before the final confrontation with Reza and that other human."
    Nm blank "I think that wall of fire is related to the comet. If it hit us, the effect would've been exactly like that."
    Br "A scary thought."
    c "Yeah, I wouldn't want to experience anything like that first-hand."
    m "I saw Bryce reach out for his drinks stash and bring it into the circle we'd formed around the campfire. He pulled out the bottles and settled them on the sand together with some plastic cups of assorted sizes and shapes."
    Br smirk "Let's have a toast."
    show sebastian normal with dissolve
    c "I guess one or two wouldn't hurt."
    Sb "Sounds good to me."
    
    play sound2 "fx/pour.ogg"
    queue sound2 "fx/pouringwine.ogg"
    $ renpy.pause (1.0)
    play sound "fx/pouringwine.ogg"
    queue sound "fx/pour.ogg"
    
    m "We all picked our drinks together with the suitable tableware."
    Br "To our bright future."
    Sb smile "Bright as in happy and not because of a burning wall of fiery doom."
    Br laugh "Yeah."
    Nm smile "Naturally."
    show bryce smirk with dissolve
    
    play sound "fx/gulping.wav"
    $ renpy.pause (2.0)
    Zh "You've made good picks, Bryce."
    Sb "All these years of drinking had to teach him which stuff is good."
    Zh "But he normally went with nothing but generic beer. How could that teach him anything?"
    Br "None of you considered that I'd done my research before choosing the drink?"
    Nm "Bryce doing careful patient research about anything? As our staff analyst, I have some serious doubts about this claim!"
    Br laugh "C'mon, guys, I'm learning patience together with [player_name]!"
    
    if eckbryceshipprogress < 100:
        Br "It's a bit bumpy, but we're getting there. Building the ship models and everything."
        Sb "I can imagine why it's bumpy, though."
        show bryce normal with dissolve
        Nm stern "Get your mind out of the gutter, Seb."
        c "Can't say he's entirely wrong, though."
        Zh "Please, spare us the details."
        Nm blank "Yes. I never asked for this."
        show bryce smirk with dissolve
    else:
        Br smirk "We even built a whole complex ship model together in one evening!"
        c "It was long and frustrating, and we broke several parts that we had to replace, but it felt totally worth the effort."
        Sb "Alright. I'm impressed."
        Zh "So am I."
        Nm "That's certainly something."
        
    Sb "It was a matter of time before training progress showed, then."
    Br "Told ya."
    
    show maverick nice flip behind zhong at Position (xpos = 0.23)
    show anna normal flip behind zhong at Position (xpos = 0.16) 
    with easeinleft
    
    An smirk flip "Having fun without us, guys?"
    show bryce normal with dissolve
    c "We've just started, and there's plenty for everyone."
    An "Honestly, I was never a big drinker. It doesn't do much good to your brain, and mine is important for the work I do."
    Mv "A single round or two should be alright, though."
    Zh "That's true for everyone, isn't it? We all need to think to perform our duties."
    An normal flip "A fair point, but as a researcher I require much greater clarity at any given moment."
    Nm normal "I can relate to that."
    An "Our work isn't all that different when you exclude the outside circumstances. I take my facts from scientific experiments and data, you gather yours from evidence."
    An "But at the core of it, we perform similar analyses, draw conclusions and offer new directions for our projects."
    Nm "Mine are a lot more subjective all around, though. You can't be certain about anything when working with people."
    An "That is why I prefer science."
    Mv "Besides, science isn't trying to run away from you, lie on purpose or fight back."
    An "Exactly my point."
    Zh "I personally enjoy working with people, but in my case it makes sense for us to get along."
    c "The thing is, you work for and with people, while police duties are often about going against someone. Our stakes are much higher, too. It makes all the difference."
    Zh "I've had some conflicts with my customers before, but you might be right. Spoiled milk complaints or bar visitors unwilling to pay are nothing but minor incidents."
    An "I have to give you credit for your patience, Zhong. To be honest, I can't imagine myself in a position that would require constant interactions with people."
    Br laugh "Me neither!"
    Sb "I can! But not for long and with terrible consequences."
    An face flip "Rolling out the jokes, aren't you?"
    show bryce normal with dissolve
    An normal flip "Oh well, it's the truth, though. I can barely tolerate most of the population already. If they kept on pestering me, I'd have told them to go do unspeakable things to themselves."
    Zh "And that is how you go out of business not even a month after opening. Customers are important, no matter what flaws they might have."
    Zh "Not that I've never had an urge like that myself..."
    Sb "That's inevitable when you're working in services or retail."
    Zh "Yeah."
    Nm smile "I always try to act friendly and polite when shopping and do my research first before asking staff for help."
    Zh "If only more customers followed your example."
    Mv "You're just awkward around people, Naomi. It's a little different."
    Nm shy "Well, I {i}do make an effort{/i} not to bother others unless I have to."
    Br "And I just have a list of stuff I always get. Nice and simple."
    Mv "Same. Mostly I already know what I need in advance."
    show naomi normal with dissolve
    Br smirk "I'd say it's time for another round. How about drinking to our friendship and unity?"
    c "Can't say no to that idea."
    An "I agree. Besides, I have a day off tomorrow."
    
    play sound "fx/gulping.wav"
    $ renpy.pause (2.0)
    Br "A day you won't spend in the lab? Are you the real Anna we know?"
    An smirk flip "I've got some other things in life now, and I'm no longer working against the clock."
    c "It's about time you've decided to take better care of yourself. It might do you some good."
    Nm smile "Work-life balance is important. Trust me, I know. No matter how exciting the case might be, never forget to get proper downtime and rest."
    Zh "Speaking of rest, I should probably get going. Babysitter can't stay forever."
    Br normal "Take care, then."
    An normal flip "Mav and I will take our leave as well. It has been a fun experience."
    Br "Oh well. Thanks for joining, y'all."
    Mv "Yeah. I look forward to our next get-together."
    Br "Bye. Be careful in the dark."
    
    show zhong normal with dissolve
    hide zhong with easeoutleft
    
    show anna normal with dissolve
    show maverick nice with dissolve
    hide anna with easeoutleft
    hide maverick with easeoutleft
    
    show naomi normal at Position (xpos = 0.16) with ease
    show naomi normal flip with dissolve
    # Juggling 7 character personalities at once in your head isn't easy. At all. URGHHHH...
    $ renpy.pause (1.5)
    c "Looks like it's just us four now."
    Nm smile flip "Yeah. On the bright side, it's pretty quiet."
    Sb drop "They didn't clean up after themselves, though."
    Br smirk "The party is still going, so it's alright. We'll deal with trash later."
    c "I wonder what time it is?"
    Sb normal "Should be a long while before morning."
    Nm "I'd love to meet the sunrise, but I'm not sure we'll stay up that long."
    Sb smile "There's nothing stopping us."
    Nm "Unless we all pass out or fall asleep on the sand. I wouldn't be concerned about it if not for [player_name]. The mornings are cold at this time of the year, and humans are much more sensitive to it than we are."
    Br flirty "I'll keep [player_name] warm, don't worry."
    c "Not in public, Bryce!"
    Br smirk "I meant simple snuggles, nothing more."
    Sb "I have my doubts about this claim, Chief."
    Br "Oh, shut up."
    Nm "I support your stance, Sebastian. There's more to it than he's letting on."
    c "We aren't playing a detective game on this, are we?"
    Sb "Maybe. Maybe not."
    Nm "I suggest we don't push it, Seb."
    Br "So, one more round?"
    c "I thought you said enough drinking?"
    Br laugh "It's the last one for the night, I swear!"
    c "Alright. Just for today."
    Nm "I'm in."
    show bryce smirk with dissolve
    Sb "Same. I don't mind."
    Br "[player_name], it's your turn to declare the toast, though."
    menu:
        "To us.":
            c "I'd say, let's drink to us and everything that binds our amazing team together."
            Br "I couldn't have said better myself."
            Nm "A great toast, indeed."
            Sb "I agree."
            
        "To our success.":
            c "Let's drink to our present and future victories, both at our work and outside."
            Nm normal flip "It's not the most important thing in life, but cheers."
            Br "Sounds pretty good, [player_name]."
            Sb "To our success!"
            
        "To love.":
            c "Let's drink to the most wonderful emotion in the world, love."
            Sb "It's so cheesy, Zhong might come back and eat it."
            Nm normal flip "Don't be like that. [player_name] is just trying to be romantic."
            Br flirty "You could be a little more subtle, but I agree. To love."
    
    
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene eckmorningbeach with dissolvemed
    
    show bryce smirk at Position (xpos = 0.86) with dissolve
    show naomi smile flip at Position (xpos = 0.20) with dissolve
    show sebastian smile flip at Position (xpos = 0.15) with dissolve
    m "Several hours later, when we looked at the sun slowly rising above the horizon, I couldn't help but wonder what was waiting for us in the future."
    m "Yet, despite all concerns and disagreements, our team stood strong together. And no matter what challenges we were going to meet along the way, I knew that I could always count on Bryce and his support."
    m "Subconsciously, I snuggled up closer to his scaly armored side. He looked at my face, gave me a short smirk, and returned his gaze to the lightening sky. The part of my mind that wanted a peaceful life was finally happy."
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ persistent.eckbryceendingseene = "E"
    show eckbryceendingseenimge with dissolveslow
    $ renpy.pause (1.5)
    hide eckbryceendingseenimge with dissolveslow
    play sound "fx/system.wav"
    s "Congratulations, you've gone with your heart and helped Anna avoid jail. Thanks to your impressive performance, everything went as smoothly as physically possible."
    s "With another stressful chapter of your life now left behind, you can only wonder what the future will bring. But no matter what, you won't be facing it alone."
    if persistent.trueending == True:
        s "In the end, humanity is safe in another timeline, you and Bryce are still together, and your bond has carried you two through a great adventure. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng]"
    else:
        s "In the end, the cycle continues in another timeline, you and Bryce are still together, and your bond has carried you two through a great adventure. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng]"
    
    jump eck_bryce_goodendcredits