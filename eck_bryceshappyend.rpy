#   Well, here it is. An attempt to create Bryce's better ending.
#
#   As usual, hi, dear reader. Spoilers below, so watch out. I guess. It's not like you'd worry about that considering that you've opened the source file.
#   Anyway, let's see how this mod would turn out. Personally, I don't feel it is as good as Anna's tbh, but it's all up to people.
#
#   Quite happy with how Naomi turned out tho. She's cute.
#   
#   SPOILER ALERT. Everything below this point can be one.
#   
#   Ending list for the future reference (and the curious people stalking this file post-release):
#   Totally not stealing ideas from Nier: Automata, but hey, it helps players keep track of the endings they've seen, so...
#   
#   (main) An [A]brupt End - default, no Anna mod.
#   (main) [B]reaking Point - side with Bryce, do badly on the investigation <-- changed
#   (main) No Matter the [C]ost - side with Bryce, do good on the investigation
#   (main) Weak [D]efenses - help Anna, do badly on the investigation <-- changed
#   (main) Good and [E]vil - help Anna, do good on the investigation
#
#   (mini) [F]orever on Duty - choose to leave
#   (mini) Pointless [G]rudges - shoot Maverick
#
#
#   Might as well add them to Anna's mod.
#   (main) An Odd [A]ttraction - default good path
#   (main) A Narrow [B]ridge - heartbreak arc recovery
#   (main) [C]aring for the Future - adopt Amely
#   (main) [D]amage Control - tell Remy the truth
#   
#   (mini) [E]nd of Hope - dismiss Adine
#   (mini) [F]allible Ideals - mess up Emera's meeting
#   (mini) Fallen from [G]race - give up on Anna
#   (mini) No [H]ugs Allowed - get friendzoned
#   (mini) [I]mperfect Hearts - mess up the recovery
#
#
#
#
#
#   Oh, and Selvy. I feel bad for you right now, looking at the number of lines. XD
#









label eck_bryce_maverickmap:
    if brycegoodending == True:
        menu:
            "Give the facility map to Maverick. {image=image/ui/status/havemap.png}":
                play music "mx/mysteryambience.ogg"
                $ renpy.pause(1.0)
                c "There's one more idea I had, but I can't try it by myself."
                Mv normal flip "What is it, [player_name]? I don't have a whole day to waste on you."
                c "I got these plans for the underground facility in the archives. I know I should've asked for them, but it's believed to be related to humans, so I thought..."
                Mv angry flip "If you want to confess some minor theft, go annoy Bryce. I'm off-duty right now and I'd rather spend this time on something useful."
                c "It's a copy, not the original, so no theft happened. Will you listen to my idea now?"
                Mv "Go ahead."
                c "What if Reza is using one of the secluded rooms as a hideout? This whole complex is pretty massive, but it's mostly empty and devoid of life. Hiding there would've been easy."
                Mv "..."
                Mv normal flip "Impossible. The facility's entrance is heavily guarded day and night. No way he could sneak in or out unnoticed."
                Mv angry flip "Are you trying to send me on the wrong track to help out your crime buddy? If so, you'd need to try harder. Such an obviously false lead isn't going to work on me."
                c "Are you sure that's the only entrance, though? Sure, the main one would be looked after, but if this complex is really related to humans, it might have several extra entry and exit points."
                c "We rarely build structures with only one door, especially if it's something important."
                Mv normal flip "..."
                Mv "So do we. I see your point now."
                c "Maybe, if the current lead won't net us anything, you should go and check? I'll give you the schematics. You know the local area much better than I do, so maybe you could figure something out."
                Mv "I don't trust you."
                Mv nice flip "But you may be onto something here. The underground complex could be worth a try."
                play sound "fx/paper.wav"
                $ persistent.havemap = False
                $ eckbrycemappassed = True
                m "I handed over the rolled-up facility map to Maverick. He hastily grabbed it and hid it under his folded wing."
                Mv "Why didn't you tell Bryce about it?"
                c "He's too impatient, and we can't risk any rash actions. Besides, if Reza isn't there, it would be a huge waste of time for the whole police department. But if he is, any large police group would spook him."
                c "On the other hand, with this map, you can easily check the facility yourself while also being discreet enough not to attract any undesired attention."
                Mv "You know what? If this gets us somewhere, I might start to like you. Maybe you aren't just a clueless pawn after all."
                show maverick normal flip with dissolve
                c "Thanks?"
                Mv "You can take it as a compliment if you wish."
                c "Just don't try to be a hero. If you find Reza..."
                Mv "Don't teach me how to do my job, [player_name]. I know what to do."
                c "Still, take care."
                Mv nice flip "..."
                Mv normal flip "Don't worry about me."
                show maverick normal with dissolve
                stop music fadeout 2.0
                $ renpy.pause(1.0)
                return
                
            "Say nothing.":
                return
    else:
        return

#   Also includes Sebastian fix. Yay. I'll copy-paste that later.
#   It is done. In a separate file just in case.
    
label eck_bryce_gtfo:
    # Reserved space. I mean, you don't expect to get away with killing Maverick, do ya?
    # scene outside the portal
    scene black with dissolveslow
    $ brycestatus = "abandoned"
    $ renpy.pause (2.0)
    play music "mx/threat.ogg"
    scene np1r at Pan((500, 150), (500, 150), 0.0) with dissolveslow
    # something dark for BG music
    $ renpy.pause (1.5)
    show bryce sad with dissolve
    Br "What have you done, [player_name]?"
    Br "He thought he could trust you... I thought I could trust you, no matter how bleak things were."
    Br angry "And this is how you repay us?!" with hpunch
    c "I don't know what came over me, Bryce. All the anger I've accumulated... it just clouded my mind."
    Br sad "I see."
    Br stern "For the sake of everything you and I have shared together, I'll give you one last chance. Return to your world, and don't you dare show your face here ever again or I will jail you for the rest of your life."
    Br "Your friend Reza will stay with us a little longer, but he'll join you soon."
    c "Bryce..."
    Br "This is your choice. Take it or face the repercussions. I don't care."
    Br sad "I can't care anymore."
    Sb "Hey, Chief. What's going on?"
    
    show bryce sad flip at left with dissolve
    show sebastian normal b at right with easeinright
    
    Br stern flip "[player_name] is leaving. You are to provide escort to the portal."
    Sb shy b "But why?"
    Br "You will see."
    show sebastian disapproval b with dissolve
    c "Before I go, there's something you must know. There's a comet on the way to your world. Warn the council, and use the underground facility's generators to divert it."
    Br brow flip "..."
    Br stern flip "Very well."
    Br "Goodbye."
    Sb "Follow me, [player_name]."
    
    $ renpy.pause (1.5)
    scene black with dissolveslow
    $ renpy.pause (1.5)
    
    window show
    
    n "Standing in front of the control console for the portal, I had two options."
    n "Either I was to go back to the human world and face the full consequences of my failure. To slowly perish together with the rest of my city seemed like the only fair outcome for this."
    n "Or I could use the emergency coordinates to travel back to the day of my arrival and try again with the new timeline to set things right."
    n "Of course, I knew what had to be done. Not for my sake, but for the people back home and for the dragons here, the cycle had to continue regardless of how I felt."
    n "Was it really a choice? Did I ever have any?"
    
    window hide
    nvl clear
    window show
    
    n "Soon after my departure, the dragons executed their plan and diverted the comet away from their planet."
    n "Following the fierce diplomatic exchange, the council declared humanity an unreliable partner and called off the exchange deal."
    n "Together with the PDAs, Reza was returned to Earth."
    n "Human officials questioned the council about my disappearance, demanding my return. To his credit, Reza diffused the situation, stating that he saw me enter the portal on the dragon's side."
    n "It was presumed I'd gone into self-imposed exile, unable to cope with the failure of my mission and the burden of living with it."
    n "Without the power, our city soon succumbed to the harsh world of the broken Earth."
    
    window hide
    stop music fadeout 2.0
    $ renpy.pause (2.5)
    $ persistent.eckbryceendingseeng = "G"
    show eckbryceendingseenimgg with dissolveslow
    $ renpy.pause (1.5)
    hide eckbryceendingseenimgg with dissolveslow
    play sound "fx/system.wav"
    s "Looks like you've messed up this one. Maybe letting your anger flow isn't always the best answer to your current situation?"
    s "It might make you feel good for a moment, but never forget the consequences. Try again, and with a different approach if you wish. Or don't. Your choice."
    s "As always, I promise to keep quiet if you reload the save file. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng]"
    $ renpy.pause (1.5)
    jump eck_bryce_badendcredits
    
    
label eck_bryce_leave:
    # Reserved space for a noble self-sacrifice. Actually, maybe, it wouldn't even be an ending per see. Just an extra scene.
    scene np1r at Pan((500, 150), (500, 150), 0.0) with dissolveslow
    $ renpy.pause (0.5)
    play music "mx/gravity.ogg"
    $ renpy.pause (1.5)
    
    m "In the dark of night, I stood in front of the control panel, one button-push away from activating the emergency coordinates."
    m "For a moment, I looked back, giving the sleeping town a short glance. They were safe in this timeline, but the price of it was too high for my city and humanity as a whole."
    m "There was only one way to set things right."
    m "I put on the mask, pulled the crude brown hood over my head, and stepped into the glowing portal."
    
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    
    window show
    
    n "Soon after my departure, the dragons executed their plan and diverted the comet away from their planet."
    n "Humanity never re-established contact and chose to look for other solutions to the growing problem of lack of power, but it was all in vain and only delayed the inevitable fall."
    n "Just like the rest, our city soon succumbed to the harsh world of the broken Earth."
    
    window hide
    nvl clear
    
    stop music fadeout 2.0
    $ renpy.pause (3.0)
    $ persistent.eckbryceendingseenf = "F"
    show eckbryceendingseenimgf with dissolveslow
    $ renpy.pause (1.5)
    hide eckbryceendingseenimgf with dissolveslow
    play sound "fx/system.wav"
    s "A noble act. But can you handle the heavy burden? Only time will tell."
    s "Of course, there's more to this story, but to see it I'm afraid you'd have to reload the save from before making the choice. Or don't. It's all up to you, [player_name]. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng] "
    jump eck_bryce_goodendcredits
    
label eck_bryce_rezaencounter:
    
    # mod endings reset query
    python:
        if not persistent.eckannacured:
            persistent.eckannacured = False
    
    # for returning players only
    if persistent.eckannacured == False:
        s "Have you completed \"Not-so-Tragic Hero\" before?"
        menu:
            "Yes":
                $ persistent.eckannacured = True
            "No":
                pass
    else:
        pass
    
    if persistent.eckbryceendingseena == "A" or persistent.eckbryceendingseenb == "B" or persistent.eckbryceendingseenc == "C" or persistent.eckbryceendingseend == "D" or persistent.eckbryceendingseene == "E" or persistent.eckbryceendingseenf == "F" or persistent.eckbryceendingseeng == "G":
        play sound "fx/system.wav"
        s "Looks like you have already experienced some or all endings for Savior mod. Would you like to reset the list of endings seen?"
        menu:
            "Yes, reset the list.":
                $ persistent.eckbryceendingseena = "..."
                $ persistent.eckbryceendingseenb = "..."
                $ persistent.eckbryceendingseenc = "..."
                $ persistent.eckbryceendingseend = "..."
                $ persistent.eckbryceendingseene = "..."
                
                $ persistent.eckbryceendingseenf = "..."
                $ persistent.eckbryceendingseeng = "..."

            "No, keep the list.":
                pass
    else:
        pass
    
    # start of the copy-pasted vanilla
    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed
    m "Inside, I was met with a long, illuminated hallway that was lined with doors on both sides."
    m "Since the lights were already on, Reza had to be very close. I wasn't surprised at the building still having electricity. Its generators were also powering the portal after all."
    play sound "fx/door/hallwaydoor.ogg"
    m "Suddenly, one of the doors opened, and out came Reza, carrying a large cardboard box."
    m "When he spotted me, he set it on the ground."
    play sound "fx/box1.wav"
    $ renpy.pause (1.0)
    show reza normal with dissolve
    play music "mx/path.ogg" fadein 0.5
    Rz "There you are, [player_name]. You don't know how glad I am to see you. I've wanted to talk with you for so long. I even tried to contact you, but that didn't work with one of them on your tail the whole time."
    Rz "But talking can wait. Now that you're here, we've got everything. Come on, help me with this and let's get out of here."
    c "No."
    Rz annoyed "No? What are you talking about?"
    c "I'm not doing anything until you answer a few questions."
    Rz amused "You want to talk now? Sure, why not? We've probably got a few hours if we wanted to. None of them will disturb us here. We could even get the backup generator as well after we send this one over."
    c "When did you realize we were in the past? How did you know about the comet?"
    Rz normal "I've known for a while. It's what I wanted to talk with you about when we met at the portal. How about you?"
    c "I only recently found out."
    Rz annoyed "Looking back, it just seems so obvious to me now. I'm not sure how exactly you figured it out, but there are so many damn clues when you think about it."
    Rz normal "I mean, how could a supposedly completely different, independent civilization speak the same language as us? What was this supposed to be? An alternate reality? No, it was just a different time."
    Rz annoyed "When was there ever anything resembling these... creatures on Earth? It's not hard to make the jump from dragons to dinosaurs when some of them here look pretty damn near identical to dinosaurs we knew about."
    Rz "And then, there are also the prehistoric fruits, the plants and the fact that their technological level is nearly exactly the same as our own past society."
    Rz normal "But we don't even have to think that abstract. You just needed to look at the sky."
    Rz annoyed "The sun, the moon, even the stars are the same. Constellations change over time, of course, but you know we could account for that stuff."
    Rz "You could've just pointed your PDA at the sky and it would've told you the time period - including the imminent threat of being eradicated."
    Rz "You could even see the meteorite in the sky, and how it would change its position day after day."
    c "Are you done being condescending?"
    Rz normal "I guess so."
    c "You killed those dragons, Reza."
    Rz annoyed "What are you talking about? I didn't kill anyone."
    c "Don't lie to me. You did it! I remember it now."
    Rz "What do you mean? That doesn't make any sense."
    c "Are you telling me you weren't the one who stole the generators and those other things these past two weeks?"
    Rz normal "No, I was in hiding. After what happened at the portal, I didn't dare to do anything that could jeopardize our mission."
    c "Why didn't you just come back?"
    Rz annoyed "How could I? They wanted to arrest me. I was a fugitive."
    Rz normal "I was surprised they didn't apprehend you, but then you weren't the one who shot at one of their police officers."
    c "Come on, Reza. The murders only started happening after you were gone, and the police have gathered plenty of evidence. You're the only one with a motive."
    Rz annoyed "All I did this whole time was trying to find ways to contact you so you could talk to our people and figure something out for me. Why would I escalate the situation like that?"
    Rz "Besides, how did you know so much about what the police were doing?"
    c "I've been helping them because you were going about this the wrong way."
    Rz angry "I didn't kill anyone, I'm telling you!"
    c "They have proof, Reza. I've seen it myself. Just turn yourself in and we'll go from there. Nobody can help you if you don't do that."
    Rz annoyed "No, I'm not going to turn myself in for something I didn't do. Not for these... beasts. Who knows what they'll do to someone like me in captivity?"
    c "How else do you expect this to end?"
    Rz normal "I'm not doing anything until I've got free passage back home. Actually, I could just leave this place right now. The portal's fixed, after all."
    c "That's not going to happen."
    Rz amused "Let me ask you one thing: How exactly are you planning to stop me? I'm the one with the gun here."
    c "You would shoot me to save your own hide?"
    Rz annoyed "Only if you insist on standing in my way."
    c "You're not going to get away that easily."
    stop music fadeout 2.0
    Rz "What are you going to do, huh? I'll be long gone by the time you call the cops."
    c "I don't need to, Reza. They're already here."
    play music "mx/termination.ogg"
    # end of the copy-pasted vanilla
    
    m "Suddenly, Bryce was standing next to me."
    show reza at Position (xpos = 0.9) with ease
    show bryce stern flip at Position(xpos=0.1, xanchor='center') with easeinleft
    Rz angry "You planned this, didn't you, [player_name]?"
    Rz "Traitor!" with hpunch
    Rz "And to think I let you distract me with such a cheap trick! Just because I thought there was still a shred of humanity within you..."
    play sound "fx/rev.ogg"
    show reza gunself with dissolve
    show reza gunpoint with dissolve
    m "He pulled out his gun, not sure which one of us he should be aiming at."
    Rz "Just let me go and I'll forget this thing ever happened."
    c "Do you think you can really do that, Reza? Do you think this is worth risking your life for?"
    Rz angry "I've been risking my life for this every day for the last two weeks. What did you do during that time? Sip champagne in your nice apartment?"
    Rz "Besides, this generator and the whole building came from our time."
    Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist=10)
    
    show reza at Position(xpos=0.45, xanchor='center')
    show bryce at Position(xpos=-0.3, xanchor='center')
    with ease
    
    show izumi normal behind reza at Position(xpos=1.25, xanchor='center')
    m "Suddenly, the Administrator came out of the shadows in the hallway behind Reza."
    show izumi at right with ease
    
    As "No, they belong to me."
    play sound "fx/rev.ogg"
    show reza angry flip
    m "Confused, Reza spun around, aiming his gun at the newcomer who was slowly walking towards him."
    Rz "Who the fuck are you? Freeze! I said freeze!"
    show izumi at Position(xpos=0.8, xanchor='center') with ease
    
    As "Want to waste your bullets on me? Feel free. You can't stop all of us."
    play sound "fx/rev.ogg"
    Rz gunpoint flip "If you say so."
    play sound "fx/gunshot2.wav"
    $ renpy.pause (0.5)
    play sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/impact3.ogg"
    hide izumi with easeoutbottom
    
    m "He pulled the trigger, and the Administrator fell to the ground with a dull thud that knocked her mask off."
    $ persistent.izumiseen = True
    show izumiinjured3 at Pan((300, 0), (600, 608), 7.0) with fade
    $ renpy.pause (5.0)
    hide izumiinjured3
    show bryce at Position(xpos=0.1, xanchor='center')
    show reza at Position (xpos = 0.9)
    with fade
    
    m "My first instinct was to run away, but as Bryce started charging, so did I."
    show reza gunpoint
    play sound "fx/gunshots4.ogg"
    
    show bryce at Position (xpos = 0.30)
    with ease
    $ renpy.pause (0.5)
    hide bryce with easeoutbottom
    
    m "Reza was quick with his aim, shooting Bryce twice before pointing his gun in my direction."
    
    play sound "fx/rev.ogg"
    hide reza with dissolve
    show reza gunself with dissolve
    play sound2 "fx/boxdive.ogg"
    
    m "I dove behind the box with the generator for cover, just as Reza was about to pull the trigger."
    m "But no shots came."
    $ renpy.pause (0.5)
    show reza gunpoint flip with dissolve
    play sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/gunshot2.wav"
    queue sound2 "fx/silence.ogg"
    queue sound2 "fx/impact.wav"
    show maverick angry with easeinright
    hide reza with easeoutleft
    m "Suddenly, a grey blur charged him from the side corridor. Reza managed to turn around in time to fire a single bullet, but it was in vain."
    m "Maverick slammed into him at full speed, sending Reza flying into the nearby concrete wall, knocking the air out of his lungs."
    play sound "fx/growl.ogg"
    $ renpy.pause (0.75)
    m "The grey dragon opened his maw and leaned closer to deliver the fatal bite." 
    Br "Stop! We got him. It's over."
    Mv "Is it? He has diplomatic immunity. He will walk."
    c "No, not after everything he's done. I'll make sure of that."
    m "Carefully, I walked up to Reza and picked up his gun lying nearby. Giving it a short glance, I stuffed it into one of my larger pockets."
    stop music fadeout 2.0
    show eckrezako at Pan ((100, 56), (0,0), 7.0) with fade
    $ renpy.pause (2.5)
    play music "mx/prayer.ogg"
    $ renpy.pause (3.5)
    hide eckrezako with fade
    m "A quick search through Reza's inventory revealed a staggering amount of spare ammo, all put into speedloaders for convenience."
    c "(This is way too much for simple self-defense.)"
    Br "Yeah. Better not leave this thing unattended. Too bad... We don't have handcuffs to secure him."
    Mv "Damn, Chief, he got you good."
    hide maverick with dissolve
    m "I rushed over to Bryce to check on him."
    show bryce brow with dissolve
    c "Are you alright?"
    Br "I'm... fine. Those bullets didn't go far past my scales. Damn it hurts, though."
    m "Slowly, he got back on his feet."
    show bryce normal flip at Position (xpos = 0.2) with dissolve
    show maverick normal at Position (xpos = 0.8) with easeinright
    Br "Good save, Maverick."
    Mv nice "I'm merely doing my job."
    c "So you decided to give my theory a try?"
    Mv normal "There was a second entrance at Tatsu Park. I watched over it for a couple of days, but Reza never showed up anywhere near it."
    Mv "I wanted to call your hunch bogus, [player_name], but then I decided to check on the inside of the facility myself before drawing the final conclusion. However, I was stopped by a sealed metal door."
    Mv "The access code was scribbled on the map, but my claws didn't allow me to properly handle the locking mechanism. For a time, I had to wait and observe."
    Mv "When everyone went to see the big fireworks, I realized that it was the only chance I was going to get. Since I needed someone with hands to open the door, I went to the portal area to get Sebastian. He was at some secluded spot not far from it, and I talked him into helping me."
    Mv "Together we managed to access the second entrance, and this time nothing was blocking my way. Seb returned to his post, and I went into the complex to explore."
    Mv "Soon I heard voices and gunshots, so I rushed over here as fast as I could."
    c "Nice detective work."
    Mv nice "I know my job. Good call on the map."
    c "So, do you trust me now?"
    Mv "I might. Don't get your hopes up."
    c "Thanks for not letting Reza shoot me, by the way."
    Mv "I couldn't let our oh-so-important Ambassador [player_name] get killed, could I?"
    c "I officially support this notion. My death would've left a terrible stain on your police department's reputation."
    Br smirk flip "And don't get me started on the amount of paperwork I'd have had to do."
    hide bryce with dissolve
    hide maverick with dissolve
    
    # start of the copy-pasted vanilla
    m "Bryce spent some time to check out everyone's injuries. Luckily, it seemed both Bryce's and Maverick's were comparatively minor and didn't need any immediate attention."
    m "The Administrator was not so lucky, however. She squirmed as Bryce moved her clothes out of the way to get a good look at her bullet wound."
    As "No, don't."
    m "As I returned to them, I heard Bryce audibly gasping."
    show bryce stern with dissolve
    Br "Damn it."
    c "Is it bad?"
    Br brow "[player_name], do you remember the first victim? The blood on his muzzle from fighting back was neither yours nor Reza's, but still distinctly human. I thought it was an error, or that our DNA tests weren't compatible."
    Br stern "But Reza doesn't have a matching bite wound from him. She does."
    m "I considered the implications of Bryce's words. Whereas Reza usually didn't hesitate to admit the killings to reach a goal he thought noble, he had denied any such actions this time."
    m "Of course, there was no use ignoring the evidence before us. This could only mean one thing."
    c "Why did you do it, Izumi? Why did you kill them?"
    hide bryce with dissolve
    if persistent.annabadending == True:
        show izumi normal 3 d with dissolve
    else:
        show izumi normal 3 c with dissolve
    Iz "He did kill them, you know. Just not in this timeline."
    Iz "If you can even remember my name now, then you should also remember what else he would have done. How he would enslave them to use as weapons back in the future and how he doesn't care what happens to this world."
    Iz "I had to do it in order to put you on the same trail he would have."
    Iz "If I had come to you during the first night and tried to explain to you that I am a time traveller who had to kill in order to prevent a suffering that is magnitudes greater - genocide, slavery - would you have believed me?"
    Iz "Who could've known that, sometimes, even Reza can change?"
    Iz "If he didn't kill anyone, there would have been no investigation, and you wouldn't have known how dangerous he is when he shows his true colors."
    Iz "You just saw that even in this scenario he wouldn't shy away from shooting others to get what he wants."
    Iz "Besides, I didn't want to risk jeopardizing our experience by changing things. It could erase all the progress we have made and the things we learned over the many times we've done this now. "
    Iz "If I didn't shove you out of the way in the cellar when the light fixture came down, you would've died then and there. That's what happened the first few times."
    Iz "There was a lot of trial and error involved to get where we are now. You wouldn't believe the lengths I have to go to every single time and the consequences if I don't."
    Iz "You could not have followed the same path and arrived here if I didn't kill them. The fact that you remembered that it was originally Reza who did it only proves just how important this is."
    Iz "Only if the events stay the same long enough will you be able to learn from them and remember, despite the effects the repeated teleportations have on your memory."
    Iz "This only tells me that I made the right call."
    c "If Reza had nothing to do with it, then what was he doing when he was trying to take the generator?"
    Iz "I slipped him a note he thought came from you. It said to meet here and take the generator before you'd leave together. He played his part well enough so you couldn't tell the difference."
    c "So, he really did think that I planned all of this, that I lured him here to have him arrested by Bryce."
    Iz "For all he's done, I think he deserves to know what betrayal feels like."
    
    show izumi at Position (xpos = 0.8)
    with ease
    
    show maverick angry flip at Position (xpos = 0.0) with easeinleft
    play sound "fx/growl.ogg"
    Mv "I've listened to this long enough now. It was you, and that's all that matters to me."
    show bryce stern at Position (xpos = 0.5) with easeinbottom
    Br "No, Maverick! Stop!"
    show maverick rage flip with dissolve
    play sound "fx/roar2.ogg"
    Mv "I'll tear you apart!" with Shake((0, 0, 0, 0), 2, dist=10)
    play sound "fx/wooshimpact3.ogg"
    show maverick at Position (xpos = 0.30) with move6
    
    hide bryce with easeoutbottom
    show maverick at Position (xpos = 0.6) with move6
    show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top")
    show izumi at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top")
    with move9
    # end of the copy-pasted vanilla
    
    play sound2 "fx/bite.ogg"
    m "Bryce tried to go between them, but Maverick aimed his shoulder squarely into Bryce's bullet wound. Bryce collapsed, convulsing in pain, as Maverick pounced on Izumi and tore into her."
    m "My hand reached for Reza's gun. It got entangled in my pocket, making me waste precious seconds to pull it out."
    play sound "fx/reload.ogg"
    m "To make matters worse, my poor handling made the revolver's drum fling open. Both empty casings and unspent ammo scattered on the floor. My hands were shaking while I hastily reloaded the weapon."
    $ renpy.pause (0.5)
    play sound "fx/rev.ogg"
    $ renpy.pause (0.5)
    play sound "fx/gunshot.wav"
    $ renpy.pause (1.5)
    hide maverick with dissolve
    m "Without hesitation, I fired a warning shot at the wall right next to Maverick's head."
    show maverick scared c at Position (xpos = 0.8) with dissolve
    c "Step. Away. From her."
    Mv normal c "I told you I'd show no mercy if I found the killer."
    show bryce angry flip at Position (xpos = 0.2) with dissolve
    Br "That's enough, Maverick! Stand down or I'll arrest you!"
    m "But it was too late. The Administrator, Izumi, was dead."
    show bryce stern flip with dissolve
    c "We needed her! The coordinates to the human world are deleted, and she was the only one who had the knowledge to restore them!"
    c "You've just doomed my entire species to extinction. Millions of lives will be lost because you couldn't contain your murderous urges for one single moment!"
    Mv "Can't you restore the coordinates by yourself?"
    c "She was an engineer. Do I look like one to you?"
    c "By the time I fully learn how to operate the portal, if I ever manage that, my people will certainly pull the plug on the generator trade plan."
    Br stern flip "You messed this up really hard, Mav. I may be unable to overlook an offense of this scale."
    Mv scared c "How was I supposed to know?!"
    Mv normal c "You can blame me for her death all you want, but you can't accuse me of dooming your species on purpose, [player_name]."
    c "Maybe if you stopped your crusade against humanity long enough to think, this wouldn't have happened."
    
    m "I noticed how Maverick's eyes darted towards the gun I was holding."
    menu:
        "Make Maverick pay.":
            m "Shaking with anger, I pointed it at him and pulled the trigger as many times as I could."
            $ save_name = _("Bryce 6 Failure")
            stop music fadeout 2.0
            $ renpy.pause (2.0)
            play sound2 "fx/rev.ogg"
            queue sound2 "fx/silence.ogg"
            queue sound2 "fx/silence.ogg"
            queue sound2 "fx/gunshots3.ogg"
            show maverick scared c with dissolve
            Br angry flip "[player_name], no!"
            $ renpy.pause (2.5)
            play music "mx/rezatheme.ogg"
            Mv "How funny... You called me out for killing her out of vengeance. Now look at yourself."
            show bryce stern flip with dissolve
            Mv "Do you think this will help anyone?"
            m "He was trembling and took a few slow steps towards me, only stopping when I aimed the gun at him."
            Mv angry c "Just when I thought I could trust you. I should have known you'd shoot me, just like Reza did."
            c "No, it's not like that."
            Mv "You're a poor liar."
            show bryce sad flip with dissolve
            c "No! I don't think I can explain."
            m "He shook his head weakly."
            Mv nice c "Thanks for proving me right, [player_name]."
            Mv "Do you remember when I confronted you a while back and asked you to explain your reasons?"
            if c2mav == "ambassador":
                Mv "You told me you both just came as ambassadors and nothing more."
                m "He gave a weak chuckle as a trail of blood slowly ran down from the corner of his muzzle."
                Mv "What an interesting kind of ambassador you turned out to be."
            else:
                Mv "You told me I wouldn't understand."
                Mv "You're right... I don't..."
            hide maverick with dissolve
            m "His head slumped as he closed his eyes. He was dead."
            show eckmaverickshot at Pan ((580,0), (0, 326), 12.0) with fade
            $ renpy.pause (9.5)
            stop music fadeout 2.0
            jump eck_bryce_gtfo
        "Toss the gun away.":
            pass
            
    stop music fadeout 2.0
    $ renpy.pause (2.5)
    play music "mx/confrontation.ogg"
    m "Shaking with anger, I threw the gun down the side corridor with as much strength as I could muster. Maverick visibly flinched at my sharp move."
    show maverick relief c with dissolve
    show bryce normal flip with dissolve
    m "The only remaining solution for the situation at hand was the emergency coordinates. I had no other choice besides going back. Again."
    c "(But not right now. Not in a state like this.)"
    Mv scared c "For a moment, I thought you'd shoot me."
    c "Remember that one time you confronted me a while ago? I said I'd never do such a thing to you. And I'm sticking with the promise."
    Mv normal c "I see."
    c "No matter how much I despise you for taking away the hope of my people, hurting you will not fix anything."
    Br "Do you think she could even restore the coordinates? Last time I deleted something in the police computer, it was gone for good."
    c "I don't know... I just don't know."

    if persistent.annabadending == True:
        m "Suddenly, a vision-like memory took over my mind, making me freeze in place."
        scene black with flash
        $ renpy.pause (0.5)
        c "We could just send them a letter."
        Iz "I'm afraid that won't be possible."
        c "And why is that?"
        Iz "After what happened during some of our other attempts, I decided to delete the coordinates to humanity's portal when I repaired this one a few days ago."
        c "But the portal has ways to locate other functional portals, right? We could re-establish the connection."
        Iz "Unfortunately, looking for other portals through time and space would be a significant energy expenditure that we can't afford right now. Not if we want to stop the comet."
        scene hallway at Pan((0, 0), (0, 150), 3.75) with flash
        $ renpy.pause (2.5)
        show maverick normal c at Position (xpos = 0.8) with dissolve
        show bryce normal flip at Position (xpos = 0.2) with dissolve
        m "It didn't matter if Maverick had killed Izumi or not in the end. My mission was a failure long before I confronted Reza."
        m "No longer overtaken by anger, I subtly glanced at the grey dragon. Part of me felt guilty for lashing out and nearly shooting him."
    else:
        pass
    
    Br "Are you alright, [player_name]?"
    c "I... I'm not sure."
    Br sad flip "I understand. Let me escort you back to your apartment. There's nothing left for you to do here."
    c "Thanks, but I can make it on my own."
    Br stern flip "Not this time. Don't worry, I've got your back."
    m "I sighed heavily. I wanted to be alone to think about my further course of action, but at the same time, somehow, I couldn't say no to Bryce."
    c "Okay."
    Br stern flip "Maverick, grab Seb, call in the investigation group, and help him with the police work over here."
    Mv normal c "Alright, I'll deal with everything."
    Br "Don't forget to clean yourself, you're covered in blood."
    Mv "On it."
    Mv "And... [player_name]."
    c "Yes?"
    Mv "I did what I had to do. You can't expect me to be sorry about it." 
    Mv nice c "But in your case... I was wrong. My apologies."
    menu:
        "You better be sorry.":
            Mv angry c "I offered my apology to you, [player_name]. Take it or leave it."
            Br angry flip "That will be enough!"
            c "Let's just go."
        "Whatever.":
            Mv normal c "..."
            c "Let's go, Bryce."
        "I guess you couldn't know.":
            Mv "In our line of work, we can only trust our friends and colleagues. But in yours, not even colleagues are trustworthy."
            c "At least I still have friends to cover my back."
            Mv nice c "You do."
            Br smirk flip "Good to see you get along."
            c "I wouldn't use such big words just yet, Bryce. But maybe we'll get there someday."
            Mv "Maybe."
        "No. I'm sorry." if persistent.annabadending:
            Mv scared c "..."
            Br brow flip "For what?"
            c "I nearly lost control over myself and shot you."
            Br stern flip "Maverick ruined the chances of your species for survival, though. So I can understand your anger, and I will not let his offense slide easily."
            c "He didn't ruin anything. Izumi did by deleting the coordinates."
            Br "But she could restore them, couldn't she?"
            c "Yes and no. She had the knowledge, but currently it's impossible due to huge time and energy requirements. And we have neither of these to spare if we want to stop the comet."
            Mv normal c "What about the comet? Is there something else going on?"
            c "I'll explain it in detail tomorrow. One day won't make a difference, and I'm too exhausted right now."
            Br normal flip "Let's go, [player_name]. You need to get some rest."
    
    stop music fadeout 2.0
    $ renpy.pause (2.5)
    play music "mx/termination.ogg"
    c "Wait. Where's Reza?"
    m "I looked around frantically, scanning the corridor, but found no traces of him. At least he didn't get the chance to steal back the generator."
    Br angry flip "Quickly. Outside!"
    play sound "fx/run.ogg"
    nvl clear
    $ renpy.pause (2.0)
    scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow
    $ renpy.pause (2.0)
    m "We were too late. When we stepped out of the facility, we only caught a glimpse of a weak glow as the portal slowly powered down after the recent use."
    m "I ran towards the control console. Vague hope filled my heart. The human world coordinates were still here. I only needed to let them know to wait a little more until we diverted the comet and..."
    c "No, no, no! Not this time, too!"
    m "When I tried to contact my world again, nothing happened. Whatever Reza had told them, it must have convinced them to pull the plug immediately. My knees buckled and I collapsed on the ground in disbelief. We were so close."
    show stars at Pan((0, 0), (0, 200), 20.0) with dissolve
    $ renpy.pause (5.0)
    m "And yet so far."
    nvl clear
    stop music fadeout 2.0
    $ renpy.pause (1.0)
    scene black with dissolveslow
    $ renpy.pause (1.0)
    m "I didn't notice how the world around me went dark, or how my back hit the soft grass."
    # Look up the Adine ending ver though. Done.
    $ renpy.pause (3.5)
    scene stars at Pan((0, 0), (0, 0), 20.0)
    # also why not add a blinking effect? Need to look up how to though..
    show bryce stern
    with dissolveslow
    show dark2 with dissolve
    hide dark2 with dissolvemed
    $ renpy.pause (1.5)
    show dark2 with dissolve
    hide dark2 with dissolvemed
    $ renpy.pause (1.5)
    show dark2 with dissolve
    hide dark2 with dissolvemed
    $ renpy.pause (1.5)
    Br "[player_name], are you alright?"
    play music "mx/chronos.ogg"
    c "I'm sorry, I didn't mean to cause you any trouble. All this stress is finally catching up with me."
    Br smirk "It's all good. Let me help you."
    play sound "fx/sheet.wav"
    $ renpy.pause (1.5)
    
    scene np1r at Pan((500, 150), (500, 150), 6.0)
    show bryce normal
    with dissolve
    $ save_name = _("Bryce 6 Main")
    $ renpy.pause (1.5)
    c "Thanks. Did anything happen while I was out?"
    Br "Not really. Sebastian is here, and I've assigned him to look after things underground. He also told me you were the one to convince him to abandon his post and watch the fireworks."
    c "I did. Please, don't punish him. It's just... I didn't think it'd be much of a problem, and..."
    Br smirk "Thank you. I don't want to think what could've happened if he'd run into either of those two murderous bastards all by himself. You might've saved his life."
    Br normal "Also, I've sent Maverick to deliver the eggs back to the hatchery and get some help. Medics should be here soon if you want them to take a look at you. Fainting like that can't be good."
    c "No need. It's not like you guys have any experience with human anatomy."
    if brycestatus == "good":
        Br flirty "Well, I know a few things about some parts of you."
        c "Um. No. That won't help, Bryce."
    else:
        Br flirty "I almost got a glimpse, but alas."
        c "Even if you did, it wouldn't have helped, Bryce."
    
    Br laugh "I know."
    Br wink "But it could make you feel better."
    c "..."
    Br "..."
    Br sad "I'm sorry. I was just trying to make some jokes to cheer you up. You've gone through so much today."
    c "Thank you. I'll be fine, but I need time to think about everything."
    Br normal "Whatever you need."
    Br "So, are you stuck in our world now? I saw you try to use the console, but it didn't work at all."
    c "Yes. The coordinates aren't gone, but my people on the other side have shut down their portal. In the end, it wasn't Maverick or Izumi who doomed humanity, it was Reza."
    Br stern "Damn. So what now?"
    c "I don't know. I'm too tired right now."
    Br normal "Alright. Let me make sure everything's in order, and then we can go."
    c "Won't the police team need your assistance?"
    Br "No. They know what needs to be done, and if they find anything important, I'll read the reports tomorrow."
    c "Aren't you too wounded to go to work, though? Reza shot you twice."
    Br brow "You're right, I almost forgot about it. The wounds don't hurt much anymore, but I'd better wait for the medics to get those bullets out and patch me up."
    c "Your natural armor is tough. I don't think I'd be able to walk around after being hit twice in the chest."
    Br smirk "Impressive, huh?"
    c "Yeah."
    c "If Reza shot me first, or Maverick hadn't shown up..."
    Br normal "I'd say it's best not to think about such things. They're all in the past, and we're safe. Good enough for me."
    $ renpy.pause (1.5)
    Sb "Hey, Chief."
    m "I turned around to face the familiar voice."
    show bryce normal flip at left with dissolve
    show sebastian normal b at right with easeinright
    c "Good evening, Seb."
    Sb smile b "Good to see you awake, [player_name]."
    Br "What is it, Sebastian? Did you find something?"
    Sb normal b "I don't know who that other human is, but... look what they had in one of their pockets."
    m "Sebastian reached out his hand to demonstrate a metallic object. In the bright moonlight, I easily recognized it. It was a copy of Reza's gun, likely from another timeline."
    Br brow flip "So, there's another one."
    Sb "I think we should carefully search this whole place."
    Br normal flip "I agree. This warrants a full detailed investigation. Maverick should be back soon with some backup and the medical team."
    c "I guess Reza's case can be closed."
    Sb drop b "He escaped, though, and who knows what he'll tell your people about us. Do you think they'll try to attack?"
    c "No. Sending just me and Reza alone took a huge toll on our power supply. They can't afford to send any more people. I doubt Reza would want them to find out the truth, either."
    Sb normal b "I see."
    c "By the way, did you enjoy the fireworks?"
    Sb smile b "They were great. This year I think it was the biggest performance I've ever seen."
    Br smirk flip "You also avoided a huge danger along the way."
    Sb drop b "I'm sorry. I know I shouldn't have left my post. In our line of work, such careless behavior isn't good, but..."
    Br normal flip "I'm glad you're safe, Seb. That's all."
    c "So am I. Also, if I may suggest, don't mention going anywhere in your report for today."
    Sb shy b "Will that be alright, Chief?"
    Br smirk flip "Sure. Let's say that the culprit managed to sneak past you."
    c "Sounds good to me."
    Sb "Thanks. I don't want to get into trouble."
    c "I think you could've gotten into much larger trouble if you'd stayed at your post. Neither Izumi nor Reza had any reservations about killing, and the fireworks provided them with the perfect cover."
    Sb drop b "I see your point. Maybe all those nightmares I've been having lately were more than simple dreams."
    Br brow flip "Nightmares?"
    Sb "I saw myself die on this exact spot. It felt so real, and the fireworks were there, too."
    c "I hope that dream will never come true now."
    Sb normal b "So do I."
    Br smirk flip "What do you think if we had an extra BBQ get-together to celebrate the end of this damned case?"
    Sb smile b "I'm in."
    c "Back into the dragons' den it is!"
    Br wink flip "You enjoyed it last time, [player_name]."
    Sb normal b "I doubt that Naomi or Zhong will be able to make it, though."
    Br stern flip "Then, in the worst case scenario, it'd be just us three and Maverick."
    Br laugh flip "But you know what? This is actually fitting. We were the ones to do most of the field work, and now we'll get to celebrate."
    c "When I think about it, it's pretty weird. I've been to the police department numerous times, but I've never seen Naomi."
    Br smirk flip "You two managed to completely avoid seeing each other this whole time. She helped with a lot of background tasks on the case, but always in a different place from where you were."
    c "I see."
    Sb smile b "Quite funny how it all turned out. And here's our backup."
    m "I turned my head to face whatever Sebastian was looking at. A large group of airborne dragons quickly approached us from the town's general direction."
    m "They were led by Maverick, who by now had a diagonal white bandage wrapped around his shoulder and chest."
    Br normal flip "Yep. Here they are. [player_name], it might be better if you wait for me at the road to town."
    c "Alright. I'll let the police do their work."
    Br smirk flip "You've helped us enough, so get some rest. Stuff here shouldn't take long."
    stop music fadeout 2.0
    $ renpy.pause (1.0)
    scene black with dissolveslow
    $ renpy.pause (1.0)
    scene np2y at Pan ((0, 100), (0, 100), 0.0) with dissolve
    $ renpy.pause (2.0)
    
    play music "mx/flux.ogg"
    m "While Bryce and Sebastian were busy organizing the investigation, I walked away from the main group and sat down on the grass below a lush green tree."
    m "Medics checked on Bryce's wounds, extracted both bullets and applied some bandages before releasing him."
    m "In meantime, Maverick led the bigger police team inside the complex, while Sebastian was tasked with looking for evidence outdoors."
    m "Watching everything from a distance provided me with some minor entertainment, but I soon started to nod off."
    m "Being half-asleep, I didn't notice a lone figure approach me."
    if persistent.naomimet:
        $ renpy.pause (2.5)
        Nm "Hello, [player_name]. Haven't seen you for a while."
        $ naomistatus = "none"
        c "Hey, Naomi."
        Nm shy b "Mind if I settle next to you? That flight was long and exhausting."
        Nm blank b "And in the end, my assistance wasn't even required."
        c "Sure. Make yourself comfortable."
        hide naomi with dissolve
        $ renpy.pause (1.5)
        play sound "fx/sheet.wav"
        m "Naomi walked up to my side and lay down on her belly about half a meter away."
        $ renpy.pause (2.5)
        show naomi normal b with dissolve
        Nm shy b "Unfortunately, I couldn't anticipate that Reza would use today's fireworks to cover his escape. Human logic and motives are too alien to me, so your actions are hard to predict... for now."
        c "Actually, I too didn't realize that he'd make his move today until the very last moment."
        Nm normal b "I see. But you've made the right call and acted when you had to."
        Nm smile b "Good job, [player_name]."
        c "Reza managed to slip away, though, and he wasn't the murderer to begin with."
        Nm blank b "I see. Then who was it?"
        c "The other human, Izumi, did it."
        Nm stern b "Who is Izumi, and why do we have a third human in our world? This throws a wrench into everything I've worked on."
        c "It's a long story, and it doesn't matter now."
        Nm "It matters to me. I have to write the report on this whole mess and add notes for future references, you know."
        c "I think it would be better to leave that to Sebastian or Maverick. What's important is Reza has escaped, Izumi is dead, and the murders are stopped."
        Nm normal b "Alright. So less work for me, and I'm fine with that."
        
    else:
        $ renpy.pause (2.5)
        "???" "Hello. You must be [player_name]."
        show naomi normal b with dissolve
        c "Hey. Yes, that's me."
        "???" "I'm sorry for disturbing your rest, but I couldn't miss this chance."
        Nm "I'm Naomi. Nice to meet you." 
        c "Likewise."
        Nm shy b "Mind if I settle next to you? That flight was long and exhausting."
        Nm blank b "And in the end, my assistance wasn't even required."
        c "Sure. Make yourself comfortable."
        hide naomi with dissolve
        $ renpy.pause (1.5)
        play sound "fx/sheet.wav"
        m "Naomi walked up to my side and lay down on her belly about half a meter away."
        $ renpy.pause (2.5)
        show naomi normal b with dissolve
        Nm "I work with Bryce, so he should've probably mentioned me a few times during the Reza case investigation."
        c "To be honest, he didn't talk about you all that much. I think I first heard about you during the BBQ get-together that you couldn't attend."
        Nm stern b "How typical, but I'm not surprised. He always loses track of everything: evidence, testimonies, the amount of beer he drinks..."
        Nm normal b "Oh well. At least we finally got to meet in person."
        c "So what type of work do you do?"
        Nm "I'm the analyst. Every bit of information you found landed on my desk, and from there I tried to connect the facts and events into a single coherent picture."
        Nm shy b "Unfortunately, I couldn't anticipate that Reza would use today's fireworks to cover his escape. Human logic and motives are too alien to me, so your actions are hard to predict... for now."
        c "Actually, I too didn't realize that he'd make his move today until the very last moment."
        Nm normal b "I see. But you've made the right call and acted when you had to."
        Nm smile b "Good job, [player_name]."
        c "Reza managed to slip away, though, and he wasn't the murderer to begin with."
        Nm blank b "I see. Then who was it?"
        c "The other human, Izumi, did it."
        Nm stern b "Who is Izumi, and why do we have a third human in our world? This throws a wrench into everything I've worked on."
        c "It's a long story, and it doesn't matter now."
        Nm "It matters to me. I have to write the report on this whole mess and add notes for future references, you know."
        c "I think it would be better to leave that to Sebastian or Maverick. What's important is Reza has escaped, Izumi is dead, and the murders are stopped."
        Nm normal b "Alright. So less work for me, and I'm fine with that."
        Nm blank b "As much as I like analyzing the evidence and building the case, I hate the paperwork that comes with it."
        c "You don't get to do a lot of the outside work, do you?"
        Nm shy b "I'm not the fighter type. The rest of the team are much better at this. Seb is quick and agile, Bryce is strong and Mav is... pretty scary sometimes."
        Nm "As for me? Like everyone else, I was trained to neutralize the suspects, of course, but I'd rather stay away from violence and instead do the mental work."
        c "You look pretty large, though."
        show naomi annoyed b with dissolve
        c "Um. Don't take it wrong, please. I mean general body size, compared to other dragons I've met so far."
        Nm smile b "Oh. I understand what you mean. You know, I'm stronger than Mav, believe it or not."
        Nm blank b "But unlike him, I don't have it in me to physically hurt others. Sparring is one thing, but actual fighting and putting my life on the line scare me too much."
        Nm "Unless I'm left with no other choice."
        c "You and me both. I prefer to avoid hurting others."
        Nm stern b "Too bad those two humans didn't share your views. All these murders, Bryce and Mav getting wounded, unborn children stolen from the hatchery..."
        Nm sad b "This is just too much. If something else will come up after this... I don't know if I'll be able to take it."
        c "Don't worry, this seems like a quiet town. I'm sure nothing is going to happen for a long while."
        c "And now that we've met, you can always give me a call if you feel like you need to talk to someone."
        Nm shy b "Thank you."
        Nm "Sorry about the breakdown. I didn't mean to dump it all on you. Normally I hang out with others, which helps a little, but this time they were all too busy chasing Reza, and I was left alone with my thoughts."
        c "It's alright. Bryce told me what sort of things police officers have to go through."
        Nm blank b "I'm spared from witnessing most of the stuff first-hand, but sometimes even reading about certain events is pretty disheartening."
        c "I understand. Especially when you have to do it day after day."
        Nm smile b "At least someone understands me."
        
    
    if naomiromance > 2:
        Nm blank b "Too bad our little thing didn't work out in the end."
        Nm smile b "But we are still friends, right?"
        c "Sure thing."
        Nm normal b "Alright then."
        $ naomistatus = "none"
        
    else:
        pass
        
    
    Br "Hey, [player_name]. I'm done here for today so... Naomi?"
    $ renpy.pause (2.0)
    show naomi smile b at Position (xpos = 0.8) with ease
    show bryce normal flip at Position (xpos = 0.2) with easeinleft
    Nm "Hey, Bryce."
    Br smirk flip "Hi. I didn't expect to see you here."
    Nm blank b "I'm the flyer on duty today, remember? Maverick dragged me all the way here from town, and apparently for no good reason."
    c "He probably just gathered everyone he could."
    Nm "Also thanks for not introducing me to [player_name] this whole time."
    Br laugh flip "That completely slipped past me."
    Nm smile b "Way too many things do, Bryce. You need to improve your attention span."
    Br smirk flip "I'm working on it."
    Nm "One botched ship model at a time."
    Br laugh flip "My latest one isn't that bad. [player_name] can attest to that."
    show bryce smirk flip with dissolve
    Nm normal b "Can you?"
    c "I'd say Bryce has... um... good potential."
    Nm smile b "That sounds more accurate."
    Br laugh flip "Hey, whose side are you on?"
    Nm "On the side of truth."
    c "Yeah. So, what's our plan now?"
    show bryce normal flip with dissolve
    Nm blank b "I'd like to hang out some more, but I must return to my duties. You're wounded, Bryce, and you, [player_name], look pale and exhausted, so you two should probably go home."
    Nm normal b "Will you be alright? I can escort you back to town."
    Br smirk flip "We'll be fine, Naomi. Don't worry."
    c "I'm still a little shaken, but nothing serious."
    Nm smile b "That's good to hear."
    Nm shy b "[player_name], if you don't mind, we could meet up again in a few days at a nicer place."
    c "Sure."
    Nm smile b "Give me a call when I'm off the clock, then." 
    Br normal flip "Naomi, will you be able to join our group for the BBQ? I've decided to organize another one to celebrate the end of Reza's case."
    Nm normal b "Sounds like an idea to me. I won't miss our get-together this time, promise. And don't forget my algae."
    Br smirk flip "You don't have to ask."
    c "Are you a vegetarian?"
    Nm "No. I just prefer balanced meals, unlike those steak munchers."
    Br "Seb would beg to differ."
    c "I see."
    Nm shy b "Oh, I really should head back to my duties."
    Nm smile b "Bye, guys."
    c "See you!"
    Br "Take care."
    hide naomi with dissolve
    play sound "fx/takeoff.ogg"
    $ renpy.pause (1.5)
    stop music fadeout 2.0
    $ renpy.pause (2.5)
    
    
    # on the way back home? Road > Pick up the fun basket > Town square > Outside the apartment.
    # play some comforting music?
    hide bryce with dissolve
    play music "mx/sleepingcity.ogg"
    show bryce smirk with dissolve
    $ renpy.pause (1.5)
    
    Br "She's quite charming, isn't she?"
    c "Shame I didn't get to meet her earlier."
    Br laugh "Sorry about that."
    c "I'm surprised you didn't try to hit on her."
    Br smirk "I would, but she's my subordinate, and things could get a little complicated because of it."
    c "I see."
    Br normal "Let's go home. I'm about to fall asleep on the go."
    c "Yeah. This was a long night. At least we stopped Reza and Izumi, and your world should now be safe."
    Br brow "My world? What are you talking about?"
    c "That comet you've probably heard about. It's going to hit us, and the damage caused is going to be unimaginable. We're talking about a global extinction event level of disaster."
    Br "Then things aren't looking good for us right now. How are we safe?"
    c "Because you still have the generators from the facility that Reza tried to steal. Their power will be just enough to divert the comet safely."
    Br normal "I see. You better pass on that information to the council, and fast."
    c "I will relay all the necessary data to them as soon as I can. We have a few weeks before the impact, so my report can wait until tomorrow."
    Br "How did you learn about that comet being a threat to begin with?"
    c "That's... a long story for another time. In short, Izumi warned me about it when we first met. I couldn't imagine back then that she'd turn out to be the killer."
    Br brow "I see. What was with all that time travel nonsense she was going on about?" 
    Br sad "I zoned out and missed most of what she said. I tried asking Mav while you were out cold, but he said he got enraged and didn't bother to listen."
    c "I think she was just trying to confuse everyone or pretended to be crazy to get off the hook for all the murders."
    Br stern "You appeared to understand her, however. [player_name], what are you hiding?"
    m "I let out a drawn-out heavy sigh. It was silly to think I could trick the chief of police."
    c "You want to know the truth? Alright, but I want this to remain between us two."
    show bryce brow with dissolve
    c "The portal doesn't just allow you to jump between worlds, it can also be used for time travel. Izumi and I've been doing this for many cycles by now, trying to save both this world and humanity."
    if persistent.trueending:
        c "And we managed to succeed, but I was not happy with the outcome. I thought I could do better than this."
    else: 
        c "And we have failed every time so far. Either your world, humanity, or both of them have been lost in the previous attempts."
    Br "As crazy as it is, I somehow believe you, [player_name]. Recently I've been having dreams of events that never happened yet felt too real to be fake. Were they caused by your travels?"
    c "What you saw were alternative timelines that are as real as this one."
    Br sad "Damn. This must be hard for you, to relive the same days over and over. And some of the stuff in my dreams was straight up terrible. Did you have to go through all that?"
    c "Yes. I've seen so many people die, Bryce. Sometimes I had to abandon ones who grew to care about me, and there was nothing I could do to save them."
    Br stern "You aren't having it easy."
    Br "So I assume this try is a failure as well, and now you must go back in time again."
    c "I have to, even though I'm so tired."
    Br sad "Maybe you could rest here at least for a few weeks? I'll do my best to help you."
    stop music fadeout 2.0
    As "That might not be necessary."
    $ renpy.pause (1.5)
    play music "mx/mystery2.ogg"
    
    c "Wait. Izumi? But you're dead."
    show bryce at right with ease
    show izumi normal flip at left with dissolve
    m "Suddenly, a hooded figure stepped out of the bushes. I recognized the cloak and the mask, but that voice... There was something different yet familiar about it."
    Br angry "Freeze! You're under arrest for multiple murders."
    As "But I'm innocent, officer."
    if brycestatus == "good":
        As "You wouldn't attack and jail your lover, would you? I thought we had something special between us."
    else:
        As "You wouldn't attack and jail your best human friend, would you? That would be so rude and unjust of you."
    show bryce brow with dissolve
    hide izumi with dissolve
    m "The figure reached out to its mask and slowly removed it, making me let out a surprised gasp. My own weary yet confidently smiling face was looking at us from under the hood's crude fabric."
    Br "How?"
    m "Swiftly, the figure put the mask on again and took a step back."
    show izumi normal flip at left with dissolve
    As "I'll explain it in due time. Hah, time... Let's take a short walk. Nobody should disturb us for a while."
    
    scene farm night with dissolvemed
    $ renpy.pause (1.0)
    show bryce brow at right with dissolve
    show izumi normal flip at left with dissolve
    
    As "I'm your backup, [player_name]. Izumi knew that should both she and you die, the cycle would be interrupted, and both worlds would be doomed. That was a risk we couldn't take."
    c "But how are you... am I here? I remember going into the past many times and..."
    As "You never went to the past. I did a few times before, but even that is a mere fraction of our travels. Why do you think you didn't remember anything on your first day here?"
    if persistent.lorembadending == False:
        pass
    else:
        As "Why do you think you now remember getting shot and dying? Had it never crossed your mind this shouldn't be possible?"
    As "With how higher consciousness works, it gradually transfers the memories into your brain, making it feel like you are recovering them. However, it's not the case. You've received them from many other iterations of us but believed them to be your own."
    Br stern "This hurts {i}my{/i} brain."
    c "So why are you here?"
    As "Because I want myself to be happy, you know. On this try, we've managed something that I failed to achieve in the past, so I believe you deserve to enjoy your rewards."
    As "I'm going to make you an offer. Take it or leave it, it's all up to you."
    c "I'm listening."
    As "I will go back instead of you, and you'll get to stay here and live your life the way you see fit."
    c "But won't this timeline disappear if one of us alters the past?"
    As "No. This is merely one of the countless possible outcomes, and it will continue its development no matter what alterations anyone would do to the past."
    c "But that means..."
    As "Those failed timelines... yes, they continue their existence in their respective universes, and nothing can be done about it."
    c "That's a scary thought."
    As "It is."
    c "Alright. So, what if I decline your offer?"
    As "Then I will take your place here. Either way, one of us has to go back, and one will stay here."
    As "I know how tired you are. But until both worlds are rescued, until they are all safe, we have to keep going."
    menu:
        "I will go.":
            $ save_name = _("Bryce 6 Departure")
            c "Maybe then it's my turn to take this responsibility. You've done your part."
            As "Then so be it."
            Br "But what about me?"
            As "In my timeline, it went almost the same way between us. But I failed to save the generator and thus doomed your world."
            As "I had to leave you behind in the vague hope that I would rescue you next time."
            As "I missed you, Bryce."
            c "Hopefully you two will be happy here."
            Br sad "But how do you expect that when I'll have to live with a copy?"
            As "I'm as much [player_name] as [player_name] of this timeline is. A few weeks older and wearier, but I'm still myself."
            Br brow "I see."
            c "Do I have to leave now?"
            As "That would be wise. However, I know how you feel. Take as long as you want. I will wait."
            c "Thank you."
            stop music fadeout 2.0
            $ renpy.pause (2.5)
            scene black with dissolveslow
            $ renpy.pause (1.5)
            jump eck_bryce_leave
            
        "I'm going to stay.":
            c "I didn't think I'd get this chance, so I'm going to take it."
            Br normal "Good to hear."
            As "So be it. You worked hard for this future, so it's only fair for you to be the one to experience it."
            As "I'll take my leave as soon as the investigation team goes away. A fourth human might be too much for them."
            c "Take care."
            As "You too."
            m "As quietly as it appeared, the figure vanished into the thick green vegetation, leaving us both confused yet somewhat relieved."
            hide izumi with dissolveslow
            
    stop music fadeout 2.0
    $ renpy.pause (2.5)
    play music "mx/slow.ogg"
    
    hide bryce with dissolve
    show bryce brow with dissolve
    Br "That was... something else. One thing is to hear about time travel, but to see it with my own eyes..."
    c "That was as big of a shock to me as it was for you. I don't know what to trust anymore, and what memories are truly mine."
    Br normal "I'd say it doesn't matter. You and I know what happened in the last few days, and anything before that isn't relevant for us anymore."
    c "Besides the comet."
    Br laugh "I said before."
    c "True."
    Br normal "What are you going to do now that you no longer have to go back? I assume your ambassador mission is over?"
    c "I suppose so. And the council is likely going to take away my status and funding."
    Br stern "Yeah, I have that suspicion too."
    Br smirk "But hey, I'm sure they'll give us all medals for this. Especially when they learn about the incoming disaster, and how we secured the equipment to prevent it."
    c "I don't think I can buy food and supplies with a medal, though."
    Br laugh "..."
    Br "That's a good point."
    Br wink "Maybe you'd want to join the police department, then? You'll need to pass some training, of course, but you have a great talent for investigation work."
    Br normal "It's a quiet town, so things rarely happen around here, and the pay is decent."
    c "I'll think about it. It's not like I have anything else to do now."
    Br normal "I know you might feel lost and scared being stuck in an alien world, but I want you to know that, if you need something, I'm always here."
    c "Thank you, Bryce."
    Br "Anytime, [player_name]."
    c "I just remembered. We've left the fun basket at the viewing spot."
    Br normal "Damn. I'd completely forgotten about it."
    c "Let's go pick it up before someone else does."
    Br flirty "We wouldn't want them to have fun instead of us, right?"
    c "Definitely not."
    
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene viewingspot with dissolvemed
    $ renpy.pause (2.0)
    
    show bryce normal with dissolve
    Br smirk "Looks like nobody's been here while we were gone."
    c "That's good to hear."
    if brycestatus == "good":
        Br flirty "You know, it's just us two here right now. We could have some fun and get some stress relief like that one night."
    else:
        Br flirty "You know, it's just us two here right now. I know that one night didn't work out, but we could have some fun and get some stress relief now if you want."
    
    c "Maybe some other time, when you aren't wounded and I'm not exhausted."
    show bryce normal with dissolve
    Br "You're right."
    c "You can still escort me home, though."
    Br smirk "Sounds good."
    
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene np5 with dissolve
    $ renpy.pause (2.0)
    
    show bryce normal with dissolve
    Br wink "Can I come in?"
    c "It's pretty late, so you can stay for the night. But let's agree to limit ourselves to just sleep."
    Br smirk "Aww. You're no fun."
    c "Are you late somewhere, Bryce? We have all the time in the world now."
    Br "You wouldn't make me wait that long, would you? I might run off to Emera by then."
    c "But {i}can{/i} you?"
    Br laugh "When I think about it, probably not."
    c "Remember, patience is a virtue."
    Br smirk "The one I'm lacking."
    c "So, are we going to stand here all night long, or are we going to go in?"
    play sound "fx/door/handle.wav"
    Br normal "Oh, right."
    
    $ renpy.pause (2.0)
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.5)
    
    # And so, it's now morning.
    
    scene o4 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    
    $ renpy.pause (2.0)
    window show
    play music "mx/dash.ogg"
    n "Somehow, my dreams were more turbulent than ever that night. My mind went through a whole colorful storm of visions, too chaotic to make out anything specific, which gave me a fever-like headache."
    n "I saw things that I knew happened in different timelines; I saw things that never did. I even saw myself do something I never imagined I'd do."
    n "Yet, among all of this, there was still hope. Maybe not for me or this timeline, but for our little corner in the infinite multiverse as a whole. As long as there was an iteration of me working hard on our goal, we could still win, I knew it."
    n "I... we weren't alone in this, after all."
    n "Somehow, my mind had no problems making peace with my fate in this world. Ever since Earth had been hit by the flare, I guess I'd always dreamed of going back to a quiet simple life."
    
    window hide
    nvl clear
        
    m "I woke up late in the morning, barely rested enough to function properly. Leftovers of thoughts and images from the night before still spun within my head."
    m "Being pressed into the wall by Bryce, who was sprawled comfortably across my whole bed, didn't help matters at all. I pried myself free, walked over him, and got off the bed into the fresh morning air."
    play sound "fx/undress.ogg"
    m "Throughout the whole thing, the dragon just continued to sleep like a log, completely undisturbed by all and any of my actions. Leaving him be, I quickly dressed up and headed for the kitchen."
    
    $ renpy.pause (2.0)
    scene eckkitchenx3 with dissolveslow
    $ renpy.pause (2.0)
    
    m "After making myself some improvised breakfast, I was sitting in the kitchen enjoying my food when Bryce finally showed up."
    # The line above doesn't sit well with me but idk how to fix it.
    show bryce smirk with dissolve
    Br "Good morning, [player_name]. This looks nice. Got some for me?"
    c "Good morning. I thought you wouldn't get up until noon, so I cooked just for myself."
    Br laugh "I'm a heavy sleeper, but it can't be that bad."
    c "I pried myself free from you, stepped on you twice while getting out of bed, and made a lot of noise while putting on my clothes."
    c "You didn't even nudge."
    Br smirk "Oh. You got me there."
    Br wink "So, can I get my food?"
    c "You can help yourself to some snacks. They're in the fridge."
    Br "Do you have any beer?"
    c "The day has just started, Bryce. There should be soda or juice somewhere, though."
    Br laugh "I'm just joking."
    Br normal "Actually, I was thinking about trying to cut down on alcohol, you know."
    c "Good idea. Some drinking is okay, but I think you're having too much too often. What made you reconsider your habits, though?"
    Br smirk "You did."
    c "How so?"
    hide bryce with dissolve
    m "Bryce grabbed some food from the fridge and sat on the opposite side of the table."
    $ renpy.pause (2.0)
    show bryce normal with dissolve
    play sound "fx/dishes.wav"
    $ renpy.pause(1.5)
    stop sound fadeout 1.0
    Br stern "You know why I started drinking. It was the only thing that helped me deal with police work."
    Br "But ever since you and I started hanging out, I feel... better. It started subtly, but the more time we've spent together, the more I've realized how important you've become to me."
    Br sad "That evening I had a moment of clarity and saw how much damage my drinking can do to what we share. It's no longer about fun or quelling my stress levels. It's becoming a problem. Something has to change, [player_name]."
    c "You know what they say. The first step to solving the issue is to admit it exists. I'll gladly help you."
    Br normal "Thanks."
    c "You're on sick leave, right?"
    Br smirk "Yep. Doc said I'll be out of commission for about a week at least."
    c "Poor Naomi and Seb. They'll have to do all the work now."
    Br laugh "It's a quiet town; they'll be fine."
    c "If you say so. To be honest, humanity had a lot more problems with crime even in our most prosperous times back in the day."
    Br normal "You guys never had it easy, did you?"
    c "I guess not."
    Br "Anyway, do you have any plans for today?"
    c "I don't really know what to do with all this free time. Before I always had a task at hand to complete, but right now I'm almost lost."
    Br wink "I know something that can take a while."
    c "Bryce. You can't be serious."
    Br laugh "That's not what I meant!"
    Br flirty "Not that I'd oppose the idea."
    Br smirk "How about we buy a model set for a ship? Then we could build it together. I'd like to see what your agile hands can do."
    c "Alright. We don't have anything better to do."
    Br brow "We might want to get an extra set or two, though."
    c "What for?"
    Br "Spare parts. You've seen my claws and how clumsy they are."
    c "Good point. Actually, I can't be certain I won't break anything, either."
    Br smirk "Then let's go."
    c "Who's going to pay, though? I doubt I can use my card for such purchases without raising some eyebrows at the council."
    Br "That's not a problem. I can afford a few model sets, especially if we're planning to cut down on the alcohol spending."
    c "Sounds good to me."
    Br normal "Want to do it at my place or yours?"
    c "Nothing personal against your apartment, but I'd rather choose mine. Yours is..."
    Br smirk "A drab? I know. It's a temporary arrangement, remember. So I agree, yours is a much better option all around."
    $ renpy.pause(1.5)
    play sound "fx/door/handle.wav"
    stop music fadeout 2.0
    $ renpy.pause(1.0)
    scene black with dissolveslow
    $ renpy.pause(1.0)
    # some calm music
    play music "mx/clouds.ogg"
    
    window show
    n "Before going shopping, I insisted that we paid a visit to Emera. The council had to know about the incoming comet."
    n "Reluctant at first, Bryce agreed to tag along. I realized why he didn't want to meet her again and, given the circumstances, I couldn't blame him. However, the information I had was too important to let simple personal disagreements get in the way."
    n "Even with the immediate threat to the generators gone, the world's fate remained uncertain until the comet had been dealt with."
    window hide
    nvl clear
    
    scene park3 at Pan ((100, 0), (100, 0), 0.0) with dissolve
    
    window show
    n "Upon arriving at the Ministry, at first we only received a near-mechanical response from the secretary that Emera was busy for the moment."
    n "However, with enough persuasion, which involved mentioning the possible disaster and waving around my ambassador status, we were allowed to see the Minister personally."
    n "The secretary led us to the tall door at the end of a corridor, knocked on it, and quietly returned to the lobby. Without further delay, Bryce and I entered the office."
    window hide
    nvl clear
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene emeraroom with dissolvemed
    play music "mx/politics.ogg"
    $ renpy.pause (2.0)
    m "At first, Emera's face demonstrated a moderate amount of annoyance when she lifted her gaze away from the papers, but it quickly changed to her usual unreadable expression."
    
    show bryce normal flip at left with dissolve
    show emera normal b at right with dissolve
    
    Em "Greetings, Ambassador [player_name]."
    c "Good day, Minister."
    Em "I'm glad to see you, Chief. How is your health?"
    Br stern flip "Good day. I'm doing fine, thank you."
    Em frown b "I've received the news about Reza, but I sincerely hope that we'll be able to sort out the diplomatic issues."
    Em ques b "This deal is too important for both of our nations, and the incident, while unfortunate, should not stand in its way. I trust that humanity feels the same way and would not withdraw their offer."
    c "So far I see no reason to cancel the exchange, Minister."
    Em normal b "Then it's settled. Was that the goal of your visit here?"
    c "Sadly, no, I've come here for a different reason. There is some crucial information I have to report to the council."
    Em frown b "Yes? Please continue, Ambassador."
    c "Your world is in great danger due to the incoming comet. According to the calculations my PDA has performed, your planet is going to be hit by it very soon. The approximate suggested damage is great enough to cause a global extinction event."
    Em frown b "Our scientists believe that the comet should pass us safely, but we can't be certain."
    c "Then they're wrong. You know how much more advanced our electronics are. The mistake probability is very low."
    Em normal b "I see..."
    Em "Very well. I will relay this information to the Ministry of Science. They should be able to develop a plan."
    Em ques b "How did you find out about the threat?"
    c "I heard about the approaching comet in the local news. While most experts have indeed stated that it should fly past us, I had my doubts."
    c "After doing my own research and putting the data through my PDA, I saw that the threat is real. On paper, the scientists were right, but what everyone missed is that your moon has its own gravity field that will steer the comet right into your planet."
    Em normal b "Thank you for sharing your concerns."
    c "Do you have any actions planned for such an event?"
    Em "Yes. We have the means to divert it, however it would require large amounts of power we might not be able to gather in time. That's all I know."
    c "You can use the generators from the underground facility. They're much stronger than your standard models."
    Em frown b "The ones that were nearly stolen?"
    Br "Yes. With the aid of Ambassador [player_name], my team managed to prevent the theft. Unfortunately, one of the suspects is dead, and the other has escaped."
    Em ques b "I've read the reports, and I'm aware of the recent events. Your input isn't currently required, Chief."
    Br stern flip "I apologize, Minister."
    Em normal b "However, the exceptional bravery and great detective work of your unit, in addition to securing the assets crucial to our survival as a nation, most certainly deserve recognition."
    Em "I'll see to it that the council will review the possibility of awarding you all with the highest honor. It also includes [player_name], who went above and beyond the ambassador duty during the incident."
    menu:
        "I was merely doing my job.":
            c "It was my obligation as an ambassador to make sure that relations between our worlds remain friendly."
            Em "I wouldn't say so. You had every opportunity to simply wait it all out, yet you didn't. Your help and service to our community are immeasurable."
            c "I believe your judgment, Minister."
            
        "It's a great honor.":
            c "I deeply respect your judgment, Minister, and I'm honored to be the very first human to be awarded by the council."
            Em "You've fully earned your medal, along with Chief Bryce's unit. If not for the generator itself, then for the warning about the comet."
            c "Thank you, Emera."
            
        "I'm glad our hard work is recognized.":
            c "It's good to hear that all the effort and time we've put into this case is acknowledged by the council."
            Em "You've done a great job, and it should be regarded as such."
            c "Thanks, Minister. We're doing our best."
    
    Em "Is there anything else you want to discuss?"
    c "That should be everything for now on my side."
    Em "Very well. I have an official query to you, given the chance provided by this personal meeting."
    c "Yes, Minister?"
    Em ques b "What can you tell me about the third human whose body has been discovered in the underground complex? Her visit was not in our agreement."
    c "Uh."
    m "For a few seconds, I shut my eyes and took a deep breath."
    c "(I should've thought of an explanation earlier.)"
    c "By the looks of her clothing, she's one of the outsiders who has nothing to do with our city. She probably managed to sneak in and used the portal without anyone noticing."
    Em frown b "Isn't your portal guarded?"
    c "It is. But it's outside the city walls, and our security isn't perfect, unfortunately. They could also have been distracted by something else to allow for the infiltration to happen."
    Em "That oversight, however, cost the lives of several of our citizens and cast a shadow of suspicion on your colleague, which forced him into desperate actions."
    c "On behalf of humanity, I offer you our most sincere apologies. Maybe some compensation is in order?"
    Em "That won't be required. The council understands that your world is facing dark times, so we're willing to move past this incident for the sake of everyone."
    c "Thank you."
    Em normal b "However, until the main investigation is complete, I have to freeze all activity regarding our agreement until further notice."
    Em "The only exception would be generator manufacturing, of course, due to the long production cycle. But we will not send any of them to your people, and we will not start the research on the PDAs."
    Em "Your ambassador status is fully retained, and so is your financial aid."
    c "I understand."
    Em "That will be all on our side. I assume this concludes our meeting."
    c "It does. Goodbye, Emera."
    Em "Goodbye, Ambassador [player_name], Chief Bryce."
    Br "It's been a pleasure, Minister."
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    scene park3 at Pan ((100, 0), (100, 0), 0.0) with dissolve
    $ renpy.pause(2.0)
    play music "mx/clouds.ogg"
    show bryce normal with dissolve
    
    Br smirk "Your stern official side always amazes me. If I didn't know the truth already, I'd have never been able to tell that Izumi's story you presented was all made up."
    Br laugh "And I'm the chief of police!"
    show bryce smirk with dissolve
    c "I support the truth and justice, Bryce. But not everything has to be said or revealed. Some things are better off never brought into the light."
    Br wink "Like that second you?"
    c "Shush."
    Br stern "Oh damn, right."
    c "I guess we are free to go ship shopping now, though."
    Br smirk "Yep. I know a good store nearby. Follow me."
    
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    scene black with dissolveslow
    $ renpy.pause(1.0)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    # scene evening apartment
    play music "mx/cruising.ogg"
    show bryce smirk with dissolve
    
    c "I didn't expect it would take us the whole day to find a decent model kit."
    Br "Most of the shops are still on holidays after the festival. On the bright side, we got a sweet deal for the ships. They're normally much more expensive."
    Br wink "It saved us enough money for a fine bottle of wine for tomorrow."
    m "I sighed heavily."
    c "Bryce. Aren't we supposed to be helping you get rid of alcohol addiction?"
    Br normal "True. But I don't think I want to stop drinking completely. You help me a lot, [player_name], by just being there for me."
    Br stern "But as much as I hate to admit it, I need a way to cope with my work, and I can't put all of my stress on your shoulders."
    Br normal "So I was wondering if, instead of gobbling down beer after beer every day, I... we could enjoy a fine drink together on some occasions?"
    c "Just not too much. I won't be able to carry you back home."
    Br laugh "That's the idea."
    Br smirk "We'd only drink a little and enjoy each other's company."
    c "Which would also quell your craving for alcohol. That's pretty smart. I like the idea."
    Br normal "Good to hear."
    c "Alright, let's get to the shipbuilding."
    Br brow "Be wary, it can get very frustrating."
    c "Isn't it part of the fun, though?"
    Br smirk "You could say that."
    $ save_name = _("Bryce 6 Ship")
    jump eck_bryce_buildashipsetup
    
    
label eck_bryce_buildashipaftermath:
    $ save_name = _("Bryce 6 Post-ship")
    hide screen eckextrainfo
    $ eckextradisplay = 0
    $ eckdisplayvar1name = ""
    $ eckdisplayvar1 = 0
    $ eckdisplayvar1unit = ""
    $ eckdisplayvar2name = ""
    $ eckdisplayvar2 = 0
    $ eckdisplayvar2unit = ""
    if eckbryceshipprogress < 100:
        if eckbryceshipgriefstage > 4:
            Br laugh "I told you, it can get very frustrating!"
            c "I suppose so."
            Br "Damn, you managed to scare me for a moment. I've never seen you so angry before. Let's finish the model some other day."
        elif eckbryceshipgriefstage > 1:
            Br smirk "Yeah. This is where I usually stop as well when making things gets too irritating."
            c "So it's similar to alcohol. You better know when to stop."
            Br laugh "Sounds about right. Let's continue later."
        else:
            Br sad "Awww. But we've just started."
            c "I'm sorry. I'm just not feeling it right now. Maybe it's the stress of yesterday's events."
            Br brow "We should continue some other day."
    else:
        Br brow "Wow. I didn't expect that."
        c "(Neither did I.)"
        Br laugh "We did it! [player_name], we've finished the model!"
        # find some ship model PNG
        c "Looks pretty good to me."
        Br "Yeah. Nothing like the mess I normally end up with. Looks like your hands made all the difference."
        # hide the ship PNG
        show bryce smirk with dissolve
        Br "Thank you. You have no idea how much it means to me that you stuck around until the end."
        $ brycestatus = "good"
        c "You're welcome, Bryce."
        Br "We should try it again someday and build a new ship."
    
    Br normal "Woah, it's pretty late. I didn't notice how time flies."
    c "Unless you want to go across town in the dark, looks like you're staying here for one more night, then."
    Br flirty "No complaints here."
    c "My food supply isn't going to last this way, you know. I wasn't prepared to be a host for a huge hungry dragon."
    Br smirk "What's the problem, then? I can just go grab some supplies for us."
    c "I haven't seen any stores that work around the clock, and I think Zhong has gone to bed by now."
    Br normal "Damn."
    c "Don't worry, we should have enough for tonight, but we better stock up tomorrow."
    Br "Sounds good to me."
    
    stop music fadeout 2.0
    $ renpy.pause(1.0)
    scene black with dissolveslow
    $ renpy.pause(1.0)
    play music "mx/forge.ogg"
    
    window show
    
    n "Following my suggestion to use the underground facility generators, the dragons had no issues with diverting the comet away from their planet."
    n "The council's investigation of Reza and Izumi's case, however, revealed the truth about the state of the portal. Ultimately, it resulted in the termination of my ambassador mission due to the loss of contact with humanity."
    n "Nonetheless, to honor my service to their community, I was rewarded with the ownership of my apartment and a solid sum of money to help me adjust to the new world and find my place in it."
    n "Taking up Bryce on his offer, I joined the local police force as an investigator. Ironically, I now had to work with Naomi more than anyone else, but we quickly got along."
    n "Since no training could prepare me to take on a dragon with my bare hands, I was given Reza's gun as a tool of intimidation. Not willing to actually use it, I chose to keep it at home in a secure place."
    
    window hide
    nvl clear
    
    if persistent.eckannacured == False:
        jump eck_bryce_defaultpath
        
    else:
        
        jump eck_bryce_annamodpath
    
    
label eck_bryce_defaultpath:
    $ save_name = _("Bryce 6A Main")
    window show
    n "During my first month in the police, I was working on Anna's case about possibly illegal experiments she had been conducting in the labs."
    if annascenesfinished > 2:
        if annastatus == "good" or annastatus == "neutral":
            n "Of course, I knew what she was up to, having taken part in this research myself. However, revealing any of that information would've been a betrayal of her trust."
        else:
            n "Of course, I knew what she was up to, having taken part in this research myself. She was pretty rude during our last meeting, so I suspected there had to be something she was hiding."
    else:
        n "Only having a vague idea with no concrete evidence, Naomi and I did our best to dig out the truth about Anna, given the limitations."
    n "However, the case had to be closed soon, for reasons I wish didn't have to be. One night, she was taken to the intensive therapy ward. Several days later, she passed away in her sleep. As it was disclosed later, she had cancer."
    $ annadead = True
    n "Our police team were among the very few people who decided to attend Anna's funeral. It marked a bleak closure to my first investigation as a police officer."
    n "Later in the evening, we gathered at Zhong's bar."
    window hide
    nvl clear
    stop music fadeout 2.0
    $ renpy.pause(1.5)
    scene eckzhongbar1 with dissolveslow
    $ renpy.pause(1.5)
    play music "mx/library.ogg"
    
    show sebastian normal at Position (xpos = 0.9) with dissolve
    show naomi blank behind sebastian at Position (xpos = 0.8) with dissolve
    show bryce stern flip at Position (xpos = 0.1) with dissolve
    show maverick normal flip behind bryce at Position (xpos = 0.2) with dissolve
    
    Br stern flip "Here we are."
    
    play sound "fx/chair.wav"
    $ renpy.pause(1.5)
    play sound "fx/chair.wav"
    
    c "Why did you decide to gather us here? I doubt you hold such events for every suspect who..."
    Br "You're right, [player_name]. But most of us had a lot of history shared with Anna. And some had more than others."
    show maverick sideeye flip with dissolve
    Br "She might've been a suspect for this case, but despite all our past disagreements and conflicts, she was also someone who helped us numerous times in the past."
    Nm sad "Let's not forget that it's also [player_name]'s very first investigation as a full member of our team, and it ended so tragically."
    c "I'll be alright, Naomi. But thank you for the concern."
    show naomi normal with dissolve
    show maverick normal flip with dissolve
    Mv "You know, Anna and I used to be something. I was chasing culprits in the streets, and she spent her time in the labs doing the research and analysis on evidence. Those were the days. Sometimes, I miss them."
    c "Sounds like you had a perfect team."
    Mv nice flip "We did."
    Mv normal flip "Until one day we realized that we'd lost everything that held us together. There was no drama or arguments; we simply agreed to part ways."
    c "I didn't expect that."
    Mv "It only made sense with our lines of work."
    c "No, I mean, I didn't think you'd be the one to open up about anything, Mav."
    Mv sideeye flip "Don't count on seeing it often."
    Nm "We aren't all made of stone, [player_name]."
    show maverick normal flip with dissolve
    play sound "fx/steps/clean2.wav"
    m "Zhong walked up to our table with a small notebook and a pen in his hands."
    $ renpy.pause(1.5)
    
    scene eckzhongbar2
    show zhong serv b
    with dissolve
    
    Zh "Hello. What would be your orders?"
    Nm "I'd like a bottle of cherry wine."
    Br "The usual for me. Two."
    Mv "I'll take whisky."
    Sb "Same as Chief but just one please."
    Zh "How about you, [player_name]?"
    menu:
        "Beer.":
            Zh "So a bottle of cherry wine, four generic beers and whisky. Noted. I'll be right back."
        "Cherry wine.":
            Zh "So two bottles of cherry wine, three generic beers and whisky. Noted. I'll be right back."
        "Whisky.":
            Zh "So a bottle of cherry wine, three generic beers and two shots of whisky. Noted. I'll be right back."
        "Do you have any cocktails?":
            Zh "So a bottle of cherry wine, three generic beers, whisky and today's special. Noted. I'll be right back."
        "Soda.":
            Zh "So a bottle of cherry wine, three generic beers, whisky and soda. Noted. I'll be right back."
            
    $ renpy.pause(1.5)
    scene eckzhongbar1
    show sebastian normal at Position (xpos = 0.9)
    show naomi blank behind sebastian at Position (xpos = 0.8)
    show bryce stern flip at Position (xpos = 0.1)
    show maverick normal flip behind bryce at Position (xpos = 0.2)
    with dissolve
    play sound "fx/steps/clean2.wav"
    
    Br "How are you holding up?"
    c "You told me that police work comes with a lot of stress, but I couldn't expect... this sort."
    m "Suddenly, I felt Bryce's muscular forearm on my shoulders."
    Br smirk flip "It always hits you where you least expect it. But, remember, you aren't alone, and if you need to talk to someone, I would be glad to help."
    Br "And I'm sure the rest of the team would do the same for you."
    c "Thank you, Bryce."
    play sound "fx/steps/clean2.wav"
    $ renpy.pause(1.5)
    scene eckzhongbar2
    show zhong serv b
    with dissolve
    
    Zh "Here's your order."
    play sound "fx/dishes.wav"
    $ renpy.pause(1.5)
    stop sound fadeout 1.0
    Br "Thanks, Zhong."
    
    $ renpy.pause(1.5)
    
    scene eckzhongbar1
    show sebastian normal at Position (xpos = 0.9)
    show naomi blank behind sebastian at Position (xpos = 0.8)
    show bryce stern flip at Position (xpos = 0.1)
    show maverick normal flip behind bryce at Position (xpos = 0.2)
    with dissolve
    play sound "fx/steps/clean2.wav"
    
    Sb "Maybe avoid Maverick, though, if you want to chat."
    Nm "Yeah. Don't take it wrong, Mav, but you just don't strike anyone here as the type who'd care about small talk."
    Mv "I'm not taking it wrong. In fact, I agree with you, as I have no interest in dealing with someone else's personal problems."
    c "Well, that's fair. You probably have enough on your mind."
    Mv sideeye flip "It's of no importance to you."
    c "Isn't it? You know I'm on your side; I always was. Bryce and I even convinced the council that you can't be blamed for Izumi's death so they won't put a warrant on you."
    c "We didn't start on the best terms and, honestly, for a while we had no improvements, but maybe it's about time we put our past conflicts aside? Is something bothering you?"
    Mv angry flip "Maybe you should learn to mind your own business instead. I hold nothing against you, and I'm content with the current state of things. Don't make me reconsider it."
    Mv normal flip "Is that clear enough for you?"
    Nm stern "Mav, you really aren't yourself today."
    Mv angry flip "I'm not spilling my guts in front of the live audience. Are you bored and want a show, Naomi? Ask the lovey-dovey couple of Bryce and [player_name]."
    Nm angry "That is {i}not{/i} what I meant!"
    Nm annoyed "Unlike you, I actually care about others, and your state concerns me. Is that clear enough for {i}you{/i}?"
    Mv "I've had enough of this. Bye."
    
    hide maverick with dissolve
    Nm sad "Wait!"
    hide naomi with dissolve
    play sound "fx/chair.wav"
    
    stop music fadeout 2.0
    $ renpy.pause(2.5)
    play music "mx/ashes.ogg"
    $ renpy.pause(1.5)
    
    Sb "That escalated quickly."
    c "Maybe I shouldn't have pushed him."
    Br sad flip "Don't blame yourself. Maverick has probably reached his breaking point with what happened to Anna. I only hope he'll be able to move past it."
    Sb drop "Chief, are you sure it's safe to let Naomi chase him all by herself?"
    Br stern flip "There's nothing we can do. They have wings and we don't."
    Sb "True."
    m "I took a short nervous sip of my drink."
    c "Do you think it's possible to track them? I'd rather be safe than sorry."
    Br "Agreed."
    Sb normal "It's hard but doable. Meet me outside in a few minutes."
    hide sebastian with dissolve
    hide bryce with dissolve
    show bryce sad with dissolve
    Br "I'm sorry about everything. You just can't catch a break recently, [player_name], can you?"
    c "It's fine, Bryce. None of this is anyone's fault. Let's make sure our friends are alright."
    Br smirk "That's the spirit."
    Br normal "Go catch up with Seb. I'll pay the tab and join you."
    play sound "fx/chair.wav"
    
    $ renpy.pause(1.5)
    scene eckoutsidebar1 with dissolve
    $ renpy.pause(1.5)
    
    show sebastian disapproval with dissolve
    
    c "Hey. Did you find anything?"
    Sb "It's late, and not many people are outside."
    Sb smile "However, I was able to catch a couple of witnesses who gave me an approximate direction that Maverick and Naomi took. It also matches with the scratch marks both of them left on the ground during takeoff."
    c "You're pretty good."
    Sb "Years of practice tend to pay off. But that's not all."
    Sb "As far as I know, there's only a couple of spots in that direction that are secluded yet reasonably accessible, and I doubt Maverick would fly into the wilderness."
    c "Impressive. So we know where they are."
    Sb "We can't know for sure, but I'm fairly certain."
    
    show sebastian normal at right with ease
    show bryce normal flip at left with easeinleft
    
    Br "Hey, Seb, did you manage to dig up anything?"
    Sb "Affirmative. I think I know the area we need to go to. Follow me."
    c "Don't run too fast. I can't keep up!"
    Br flirty flip "Ever wanted to ride a dragon?"
    c "Oh my."
    Sb shy "Um, Chief..."
    Br laugh flip "What? Just get on my back, [player_name], and hold on."
    
    hide bryce
    hide sebastian
    with dissolve
    
    m "I did as suggested and wrapped my arms around the sides of his thick neck. Bryce's wide body and hard armor plates made it somewhat uncomfortable to sit on, but it was bearable."
    m "Sebastian quickly charged in a specific direction, and Bryce followed suit. Now I could see why dragons like Seb were called \"runners\", as even the fastest humans couldn't dream of reaching such speed on foot."
    
    $ renpy.pause(1.5)
    scene eckdusktownsquare at Pan((0, 220), (0, 220), 0.0) with dissolveslow
    $ renpy.pause(1.5)
    
    m "The sky was getting darker as we moved through the town. The initial feeling of awkwardness of using Bryce as transport soon vanished, replaced by some odd excitement."
    m "Despite the circumstances, riding on a dragon's back turned out to be much more fun than anticipated."
    
    $ renpy.pause(1.5)
    scene eckwildlands2 with dissolveslow
    $ renpy.pause(1.5)
    
    m "Eventually, we arrived at the forest area just outside of town. What we found, however, defied every expectation any of us could've had."
    m "Under a large tree, on a patch of short grass, lay Maverick with his eyes shut tight. Side-by-side next to him rested Naomi, her wing draped over his back. Unlike him, however, she remained awake and stared intently at us as we approached."
    
    stop music fadeout 2.0
    $ renpy.pause(2.5)
    play music "mx/shoal.ogg"
    $ renpy.pause(1.5)
    
    show sebastian shy flip at Position (xpos = 0.1) with dissolve
    show bryce normal flip behind sebastian at Position (xpos = 0.2) with dissolve
    show naomi normal at right with dissolve
    # Seb in front of Bryce on the left, Naomi on the right.
    
    Sb "I have so many questions."
    Nm smile "Were you concerned for me, guys? You didn't have to rush here. Everything's under control."
    Br stern flip "We were concerned about both of you."
    Nm blank "Don't. He... we're going to be alright. I hope."
    Nm sad "If only you knew what I learned today. I've managed to talk him into opening up a little just for me, and... it wasn't pretty."
    show sebastian normal flip with dissolve
    Br "How's he doing?"
    Nm blank "He was on edge for so long. I'm impressed he made it this far without the aid of heavy drinking, medicine or anything of the sort. But today, back at the bar, I think he finally snapped."
    Nm sad "We all know how police work is, and what it does to us. Losing one of the very few people he ever cared about must've been the last drop for Mav."
    c "If you want, we could try and help somehow."
    Nm blank "All he needs is time and some rest, and I doubt you'd be able to offer either. Soon he should be back to normal, anyway."
    Nm normal "Just go home, everyone. I'll watch over him and make sure things are alright. It looks like we'll be staying here for the night."
    c "Are you sure it's safe?"
    Nm smile "We're close to town, there's no real danger."
    Nm shy "Thanks for checking on us. I hope we didn't make you worry too much. Mav acted on impulse, and he wasn't thinking straight."
    Sb smile flip "Don't let your guard down. He's sleeping now, but by morning he's going to be the same old Maverick again."
    Nm "I hope so. His softer side is pretty depressing, and I've had enough of it for a while."
    Br smirk flip "Enjoy your night together, and see you tomorrow."
    Nm stern "It doesn't mean anything, Bryce. I was merely offering him some friendly comfort."
    c "That's still a very personal way to provide it."
    Nm "And I thought you were on the side of truth."
    c "I always am."
    Nm smile "Are you? I'm still waiting for that call from you about the meeting you've promised me. Have you forgotten about it? We wanted to visit some nice places, hang out and all that stuff."
    c "Oh, right."
    c "Wouldn't that be a date, though, not just a meeting?"
    Nm normal "Don't get ahead of yourself."
    Br wink flip "You wouldn't steal [player_name] from me, right, Naomi?"
    Nm smile "I'm not a fan of second-hand goods."
    c "Hey!"
    c "I should've known better than walking right into a dragon's den."
    show bryce laugh flip with dissolve
    Sb drop flip "And Maverick is still asleep somehow. You'd think he'd be awake by now with us talking in full voice."
    Br brow flip "Yep. Sleeping like a brick. Is he breathing?"
    Nm shy "He's been through a lot. Let him be."
    show sebastian smile flip with dissolve
    Br "Maybe you two should take a day off tomorrow? Try and get him back on his feet. After everything we've been through, I don't want to lose a friend to damn stress and depression."
    Nm normal "I'm not sure how much more I can do, but I'll try. Thanks, Bryce."
    Br smirk flip "You're one of very few people who's managed to get along with Mav, so if anyone can help him, it's you."
    Nm shy "Don't look too much into it, though, or make any assumptions."
    c "Of course. We aren't trying to hook you two up or something."
    Nm stern "That's exactly what you guys are trying to imply."
    Br "Maybe you're the one looking too much into it?"
    show naomi shy with dissolve
    Sb normal flip "Let's call it a day. It's late, and I still have to travel across the whole town to get home and prepare for tomorrow's shift."
    show naomi normal with dissolve
    c "I agree."
    Br normal flip "Yeah."
    Br wink flip "Looks like I'll be crashing at your place again tonight, [player_name]."
    c "You know that I don't mind."
    Nm "See you later, guys."
    Sb "Take care."
    Br "Bye."
    
    stop music fadeout 2.0
    $ renpy.pause(2.5)
    scene black with dissolveslow
    $ renpy.pause(1.5)
    
    scene eckkitchenx with dissolveslow
    play music "mx/feelings.ogg"
    # some more calm music
    # make it mod's end? Sounds about right.
    
    show bryce smirk with dissolve
    Br "It feels good to be finally done with this day. You have to give me credit, [player_name] – I almost didn't drink despite the circumstances."
    c "You didn't get to. We had to run after Naomi and Maverick."
    Br laugh "Shhh. That's not the point."
    c "If you say so."
    c "Do you think they'll be alright, though?"
    Br normal "Yes. Naomi is pretty good with people, but don't be deceived by her friendly face. She can stand up for herself."
    Br "Maverick, on the other hand..."
    show bryce sad with dissolve
    Br "I'm not sure. You know, I've suspected he was at breaking point for a long time, but I could never have expected it would be Anna's death that would push him over the edge."
    Br stern "Think what you want about Mav, but he never had it easy. Do you know that one day he had to kill his own brother to save me?"
    stop music fadeout 2.0
    if annascenesfinished > 1:
        menu:
            "I've heard about it.":
                c "Yes. Anna told me about that incident and the reason behind it. It must've been a horrible experience for him."
                play music "mx/chronos.ogg"
                jump eck_bryce_defaultpathend
                
            "I had no idea.":
                jump eck_bryce_mavflashback
            
    else:
        jump eck_bryce_mavflashback
        

label eck_bryce_mavflashback:

    c "No. But why? What happened?"
    Br "Sadly, there was no other way out of that situation. Let me start from the beginning."
    
    scene black with flash
    show maverick nice b gray with dissolveslow
    play music "mx/dramatic.ogg" fadein 3.0
    
    m "He was still new to the force. Just like Seb, he was young and eager to help make the world a better place. However, those illusions weren't meant to last."
    m "A serial killer showed up in town soon after Mav joined. To make matters worse, the victims were apparently eaten."
    m "Panic and terror spread rapidly among the population. We tried our best to stop the murders and threw everything at the case: investigation teams, patrols, public warnings, but we were largely unsuccessful."
    m "Until that one cursed night."
    m "Mav and I were on patrol duty when we found our suspect munching on his fifth victim."
    m "At that point, he was merely a dragon-shaped wild animal, devoid of emotions or higher levels of thinking. I wasn't new back then, and I'd seen a lot during my years in the police, but that scene is still engraved in my memory."
    m "I don't think I can imagine how Mav felt at that moment. Yet, that wasn't even the worst part about the case."
    
    scene black with dissolvemed
    $ renpy.pause (2.0)
    scene fb gray
    show bryce stern old b gray at Position(xpos = 0.76)
    show maverick nice b gray at Position(xpos = 0.96)
    with dissolvemed
    
    Br "Stand back, Maverick. I'll handle this."
    Mv scared b gray "Miles?"
    m "The suspect was Maverick's brother."
    show bryce stern old b gray at Position(xpos = 0.70) with ease
    
    Br "Step away from the body, Miles."
    m "Miles couldn't comprehend our speech. I doubt there was much left of him at that point. However, he recognized us as a threat to his territory and food."
    m "And he was ready to protect what was his by all means necessary."
    show miles angry flip gray at Position(xpos = -0.0) with easeinleft
 
    play sound "fx/growl.ogg"
    m "Miles raised his head from his kill, blood dripping from his maw. Normally, I'm not afraid of a fight, but that one time I felt some deep cold fear. Fangs bared, the feral dragon snarled and stood strong in front of his meal. There was no going back."
    Br brow b old gray "Whatever this is, Miles, it's over. Don't make it worse now."
 
    play sound "fx/snarl.ogg"
    show miles growl flip gray with dissolve
    $ renpy.pause (1.0)
    
    show miles growl flip gray at Position(xpos = 0.16)
    with move6
    
    play sound "fx/bite.ogg"
    show miles bite flip gray with dissolvequick
    
    show bite 2 flip gray at Position (xpos = 0.45)
    hide bryce
    hide miles
    with dissolvequick
    
    $ renpy.pause (0.0)
    scene black with dissolvemed
    
    m "Before I knew it, Miles was upon me. Despite my superior training and strength, I found myself clearly outclassed from the beginning, which greatly confused me. Only much later, I found out that some mental diseases do that to people, giving them near-impossible reflexes, coordination and strength at the cost of sanity."
    m "Miles had the advantage with his relatively small frame and great speed, and all the advantages I had meant nothing since I couldn't land a single proper hit."
    m "Everything happened so fast that Maverick didn't know what to do."
    m "We rolled on the ground and I ended up on my back. Miles pinned me and clamped his jaws on my neck. My front plates provide decent protection, but they couldn't hold off his assault on their own."
    play sound "fx/bitescr.ogg"
    
    m "My claws were the only thing preventing Miles from biting down, but they were slipping. With them slick with blood and quivering with fatigue, I was quickly losing grip as I tried to push him off."
    m "For a brief moment, I thought it was the end."
    m "Suddenly, the jaws relaxed and I was able to free myself. When I looked up, I saw that Maverick had managed to get to Miles from behind. He bit through his brother's neck from above."
    
    play sound "fx/squish.ogg"
    $ renpy.pause (1.0)
    m "Blood flowed down Maverick's jaws and over Miles' lifeless body. He had saved my life, but the young dragon wore a wide-eyed, empty stare."
    stop music fadeout 2.0
    window hide
    
    $ renpy.pause (2.0)
    
    Br "Maverick blamed himself for not taking better care of his brother. He knew Miles had problems and was taking medication for it, but he wished he could have done more."
    Br "Maverick takes solace in the fact that he was able to save me, but he's never been the same since that incident."
    $ renpy.pause (2.0)
    
    scene eckkitchenx
    show bryce stern
    with dissolveslow
    play music "mx/chronos.ogg"
    c "It must've been a horrible experience for him."
    jump eck_bryce_defaultpathend
    
label eck_bryce_defaultpathend:
    
    Br "It was."
    Br "And to make matters worse, they soon found out that Miles wasn't given the correct medication from the beginning."
    c "Your medicine leaves a lot to be desired."
    Br stern "I wish I could disagree with you."
    Br sad "And now, the only other person Mav had ever cared about is gone."
    Br "After all these years, he still harbored some feelings for her, likely hoping that one day they would reconcile, and things would return to the way they used to be."
    c "Sadly, it's impossible to make things as they used to be, no matter how hard we try. Not even time travel will help you there."
    Br stern "I know. But maybe he was willing to try."
    c "Yet it's too late now. Hopefully he'll be able to move on."
    Br sad "Yeah."
    Br normal "Personally, I prefer not to dwell on the past. My life is here and now with plans and goals set for the future."
    Br smirk "And you help me make it so much brighter."
    Br normal "Of course, I realize that you miss home and your people, and this world must feel pretty alien to you, but I'm happy to have you here."
    Br "Always remember, you are not alone."
    hide bryce with dissolve
    m "Bryce got up slightly and leaned over the narrow table in a clumsy attempt to nuzzle my face. Pushed back by the heavy impact, I had to grab onto the sides of his head to prevent my chair from tilting backwards."
    m "For a few moments, we just laughed while I regained my balance. Seizing the opportunity, I rubbed my cheek against his; the bumpy scales brushed against my softer skin."
    m "Soon, we parted and returned to our normal sitting positions. I gave Bryce a short smile before switching my attention back to the dinner."
    show bryce smirk with dissolve
    Br "We should do such things more often."
    c "No objections here."
    Br "Thought so."
    Br flirty "Alright, I'm done with dinner, so see you in bed."
    c "You are quite bold, aren't you?"
    Br "We can sleep, or, if you wish, we could make it more interesting."
    c "We'll see how things go."
    hide bryce with dissolve
    m "My plate was soon empty as well. I dumped the dirty tableware into the kitchen sink and headed out of the room."
    stop music fadeout 2.0
    
    $ renpy.pause (2.0)
    scene o3 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    play music "mx/gymno.ogg"
    # some smooth music
    
    m "I wasn't surprised to find Bryce sprawled over my bed, looking at me with a playful smile."
    
    show bryce flirty with dissolve
    
    Br "So, are you joining, [player_name]?"
    c "In a moment."
    Br smirk "You know, with how many times I've been here, this place is starting to feel almost like home."
    c "You're always welcome here."
    Br "And you are welcome in my apartment."
    Br laugh "If I had one."
    show bryce smirk with dissolve
    c "Still no news as to when you'll get the proper place to live in?"
    Br normal "None. I'm suspecting that it's going to take a while. Stuff is pretty complicated, and I don't want to explain it all to you in detail."
    c "But you are getting it, right?"
    Br "Yep. But I still have to stay in that temporary arrangement for now."
    c "Back on Earth, we have a saying. \"There's nothing more permanent than things that are considered temporary.\" "
    Br smirk "Let's hope it won't come to that."
    c "Yeah."
    Br flirty "But enough with the boring talks. How about taking this sleepover a little further? It's been a while since we last had any good fun."
    menu:
        "Decline.":
            c "Not today, Bryce. So many things happened, and it's hard to get in the mood after a funeral, you know."
            Br sad "I'm sorry, I always pick the worst time for everything."
            c "It's alright. Let's just go to sleep and be done with this day."
            hide bryce with dissolve
            play sound "fx/undress.ogg"
            m "Without haste, I removed my daily clothing and climbed over Bryce on my side of the bed. Right after sliding under the blanket, suddenly I found myself held in a tight hug as Bryce smirked at me from above."
            show bryce smirk with dissolve
            Br "There, feeling better?"
            m "I fully relaxed in his arms."
            c "Thanks. I needed that."
            m "The big dragon nuzzled the top of my head before fully settling down for the night."
            Br "Sleep well, [player_name]."
            c "Good night, Bryce."
            hide bryce with dissolve
            m "For several long minutes, I couldn't help but relish our embrace before eventually drifting off to sleep. I was still held tightly against Bryce's segmented chest, smiling to myself."
            m "His scales were hard and rough to the touch, but at that moment I felt soft, warm and secure."
            
        "Accept.":
            c "So many things have happened today. I could use something to get my mind off them."
            Br "That's what I was thinking."
            c "Then it looks like we're thinking the same way."
            hide bryce with dissolve
            play sound "fx/undress.ogg"
            m "Without haste, I removed my daily clothing and climbed over Bryce on my side of the bed. Right after sliding under the blanket, suddenly I found myself held in a tight hug as Bryce smirked at me from above."
            m "His muzzle approached my lips, and I shut my eyes."
            # No lemon 4 U, dear reader. :P
            
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    $ persistent.eckbryceendingseena = "A"
    show eckbryceendingseenimga with dissolveslow
    $ renpy.pause (1.5)
    hide eckbryceendingseenimga with dissolveslow
    
    play sound "fx/system.wav"
    s "Congratulations! You've reached the end of Bryce's Happier Ending, saved dragonkind and refrained from senseless murder. Good job, [player_name]."
    if persistent.trueending == True:
        s "Humankind has been rescued in another timeline, and you've settled for a nice happy life in this one. Not that bad of an outcome, right?"
    else:
        s "Don't relax just yet, though. You still have humanity to save in another timeline, even if this specific iteration of you no longer has to."
    
    s "There's another path available for you to explore, but to reach it you'd need to play \"Not-so-Tragic Hero\" first."
    s "Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng] "
    jump eck_bryce_goodendcredits
    
label eck_bryce_annamodpath:
    play sound "fx/system.wav"
    s "Looks like you've played the \"Not-so-Tragic Hero\" mod. Would you like to explore the default arc, or would you rather choose the alternate path?"
    menu:
        "Normal turn of events.":
            s "So be it."
            jump eck_bryce_defaultpath
        
        "The alternate path.":
            s "So be it."
            pass
    
    $ save_name = _("Bryce 6 Anna")
    window show
    n "During my first month in the police, I was working on Anna's case about possibly illegal experiments she had been conducting in the labs."
    if annascenesfinished > 2:
        if annastatus == "good" or annastatus == "neutral":
            n "Of course, I knew what she was up to, having taken part in this research myself. However, revealing any of that information would've been a betrayal of her trust."
        else:
            n "Of course, I knew what she was up to, having taken part in this research myself. She was pretty rude during our last meeting, so I suspected there had to be something she was hiding."
    else:
        n "Only having a vague idea with no concrete evidence, Naomi and I did our best to dig out the truth about Anna given the limitations."
    
    n "While we hadn't yet properly analyzed the evidence we'd gotten during the search of Damion's apartment, it did provide us with some additional insight into the research she was doing. It wasn't enough to draw any conclusions, though."
    n "At first glance they were just scraps, copies of printed reports, and other assorted data. Naomi quickly concluded that, so far, the case had little to stand on but warranted closer inspection."
    n "With no other options left due to lack of staff, Sebastian was assigned to track Anna's movement and report anything of interest. She knew she was under close investigation, so we weren't surprised to end up with nothing at first."
    window hide
    nvl clear
    window show
    n "Soon, however, we found out she was making periodic visits to the local hospital for purposes unknown."
    n "Through enough persuasion, our department managed to convince one of the personnel to speak up – unofficially, of course – about Anna's visits. Patient confidentiality was sacred here, just like back on Earth."
    n "As it turned out, she was going through cancer treatments. That explained her official project but did little in the way of proving her guilty or innocent in the case of illegal experiments. At worst, it only gave her a stronger motive."
    n "Anna's next action, however, raised every red flag imaginable. She was seen talking with the chief physician at the cafe and slipping him a rather sizeable envelope."
    n "Two days later, Anna went into hospital but didn't come out. A simple query confirmed her presence at one of the wards, and it was decided to send me to pay her an unofficial visit."
    window hide
    nvl clear
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene testingroom with dissolveslow
    play music "mx/path.ogg"
    $ renpy.pause (2.0)
    show anna normal with dissolve
    $ annastatus = "none"
    An "Ah, if it isn't [player_name] in the flesh. Working for the police full time now, I see. Have you come to arrest me?"
    An smirk "Because I've got some news for you. I don't care."
    c "Hello, Anna."
    An normal "Why so formal? Did you finally dig up enough dirt to smear my name and jail me for good? I've heard it's pretty alright in there, and I won't have to go to work anymore."
    c "You really aren't helping your case right now."
    An smirk "Do I look like I give a damn?"
    c "Alright. I'm not here officially, so whatever you say is going to stay between us. And you aren't getting arrested just yet."
    An normal "Says the person most likely carrying a recording device in their pocket."
    An smirk "But I love the last addition of yours. Perhaps, I'll play along and humor you. So what does the precious human police officer want from a humble recovering dragoness?"
    c "We know that you've passed an envelope to the chief physician. What was it all about?"
    An normal "Straight to business, I see. Let's say it was our private agreement, and the details are none of your concern."
    An smirk "I'm fairly content with the total resolution, though."
    c "Would you give me any details?"
    An face "Why would I?"
    An normal "You're looking for a way to jail me, since I've stepped on some tails in the council and they want me out of the picture."
    c "I'm trying to find the truth."
    An face "If that's what you believe, then you're just a pawn, just like the rest of the force."
    c "We're not anyone's pawns. The case is completely under our jurisdiction."
    An "Keep telling yourself that."
    An normal "But if you're right, maybe we could work together. How about I let you know the full story, and then you can decide what side you want to be on."
    
    if annascenesfinished > 2:
        An "After all, you are my accomplice. And while I know I won't be able to drag you along with me to jail, I can at least soil your reputation before getting locked up."
    else:
        pass
    
    c "Well, I'm listening. It's not like I'm losing anything by hearing you out."
    An smirk "Smart choice."
    An normal "As you probably know, my current main project is finding the cure for cancer. Many scientists believe it to be beyond our reach to defeat this disease. However, I have reasons to think otherwise."
    c "Humanity also had to face cancer, but we managed to discover the cure."
    An smirk "I know. But more about it later."
    An normal "Shortly after starting my work, in an ironic twist of fate, I ended up contracting that very same disease myself. As you can imagine, it quickly turned from an ambitious project into a desperate fight for my own survival."
    An "According to the prognosis doctors gave me, even with the right treatments, I had several years left at most."
    c "So you were working against the clock."
    An sad "Time wasn't my only enemy."
    An disgust "All those backwards traditions, laws that haven't been changed for centuries, and hard-headed politicians with their {i}sacred ways of life{/i} did their absolute best to hamper my project in every way imaginable."
    An "Yes, I used some controversial methods in my research without the council's approval. I had no time to wait for some old people to decide if I was worthy of living or not."
    c "I assume it didn't go well, though."
    An face "A major understatement."
    An disgust "What I received was a massive smearing campaign, followed by police persecution for what they called illegal experiments."
    An normal "They knew I'd started my work already, but they couldn't tell how far I'd gotten. I was forced to scrap all of my progress on the research before your colleagues got their dirty hands on it."
    An "Despite the lack of direct evidence, I was sentenced harshly. However, for that same reason, they had to suspend my punishment. Instead, I was given a list of conditions and assigned to the local production facility."
    c "So you managed to slip away from the law."
    An disgust "So what? I lost everything I'd been working on." 
    An normal "Despite the risks, I continued my research. However, with limited resources and constant council supervision, I made little progress."
    An sad "And the troubles didn't stop there, either."
    An disgust "Damion, my assistant. That piece of shit has been blackmailing me since he found out I was working on Reza's samples."
    c "Did studying human samples go against the conditions of the suspended sentence?"
    An face "What do you think, genius?"
    
    if annascenesfinished > 2:
        c "So I helped you to break the law."
        An disgust "If this is what you are concerned about then yes, you did."
    else:
        pass
    
    c "Blackmailing explains the odd evidence we've discovered in his apartment. So he was trying to get some leverage on you, but for what purpose?"
    An sad "It's none of your concern."
    An cry "I didn't mind giving him what he wanted, though. I just wanted to live."
    An "..."
    An disgust "Either way, he got what he deserved by the hand of that lunatic killer, and I'm not going to cry about it."
    c "I see."
    c "So you confess that you've actually performed illegal experiments both recently and in the past."
    An smirk "Good luck in the court, because I'm not repeating those words again for anyone."
    An normal "Are you interested in the rest of the story, or did you get what you want already?"
    c "Go on. As I said, I'm only looking to piece together a picture of the situation."
    An "After Damion's death, I was forced to halt everything again. Your department was onto me, so I had to play it safe while the clock to my death was ticking. My condition was worsening rapidly, and the prognosis didn't look good."
    An smirk "A couple of weeks ago, however, I had a burst of sudden inspiration."
    An normal "Something told me to check on several of the PDAs you'd brought back in the day. Inside the databanks, I found humanity's medical archives, and one of them had the very cure I've spent so many years and so much effort looking for."
    An "At first I was skeptical about the possibility of recreating it, but further research proved that our medicine is fully capable of doing it."
    c "So this is why you were meeting with the head physician."
    An smirk "You're smarter than you look."
    An normal "I convinced him to synthesize the serum for me in the hospital's lab and provide all the necessary surgery without the need of approval from the Ministry of Healthcare."
    An "As you can see, he has completed his part of the deal."
    c "So, are you cured now?"
    An "The docs said so. Despite the genetic differences between our species, the method worked fine for me without any alterations."
    c "Good to hear."
    An face "Oh, cut the polite crap. You don't care and I know it. If you did, you wouldn't be here questioning me."
    c "No, I mean it. We might be in opposition now, but I don't want anyone to die and I'm glad you're well."
    An sad "If you say so. I'm still a little torn about this ordeal myself."
    An normal "It feels good to no longer be dying, you know."
    An sad "Yet, it rendered all of my efforts, all of my sacrifices, all those years spent... meaningless. I thought it was up to me to do the impossible and accomplish something no dragon before me could, but I failed miserably."
    c "It made you the person you are now, though."
    An face "A spiteful sarcastic witch whom nobody likes? Amazing development, isn't it?"
    c "Don't be so harsh."
    An normal "It's different. I'm simply being honest with you, [player_name]."
    An "By the way, I will submit the full report about my findings in the PDAs as soon as I'm out of here in a couple of weeks."
    An normal "Hopefully, you guys will at least let me do that before sending my life down the drain again." 
    c "Are you going to take the credit?"
    An face "Don't be stupid. I have no research to present with those discoveries, even if I wanted to claim them as my own."
    c "But you don't?"
    An sad "No. Honestly, I don't care what others think about me. I know I didn't make this serum or develop the surgery. I know that I've failed my cancer research despite giving my everything to it."
    An disgust "The rest doesn't matter. Whoever gets the recognition for it gets it. I don't give a damn."
    c "I guess you want to move on and leave everything related to it behind."
    An "Oh, it's only been a constant reminder of my imminent death for the last few years, cost me most of my savings, and is also the sole source of every single freaking problem in my shitty life."
    An face "What gave you this amazing idea that I want to leave it all behind?"
    c "Alright, alright. I get it. No need to be so sarcastic."
    An sad "..."
    An normal "This is my story, [player_name]. Do with it what you wish."
    c "I see. Thank you for your time."
    An face "It's not like I have better things to do in a hospital bed all alone."
    An normal "So, what do you say?"
    c "There might still be a way out of this for you, I think. The council initiated the case, but it's up to our group to handle and resolve it."
    c "I need to talk with the rest of the team about our next move. You have broken the law, but the reasoning behind it is beyond rock solid. And once your findings go public, they'll save countless innocent lives."
    c "On the other hand, rules are rules, and we can't just neglect them. Even with the best intentions in mind, you're still a criminal on several accounts."
    An sad "Looks like I'm at the mercy of your department."
    c "Yeah. I can't make such decisions on my own. We'll agree on a course of action first, and then follow through with it."
    An normal "But remember. If you decide to oppose me, I won't go down easily."
    c "That I never doubted."
    An "I didn't get this cure just to spend my life behind bars."
    An smirk "If you help me, however, expect the council to give you all hell unless you figure out a smart way to ruin their case."
    c "True. They are likely very interested to see you in jail."
    An normal "Obviously."
    An "I guess this concludes your visit here, [player_name]."
    An smirk "Either way, good luck. You'll need it."
    c "Thanks. Good luck as well."
    
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene office at Pan ((0, 250), (0, 250), 3.0) with dissolveslow
    play music "mx/hydrangea.ogg"
    $ renpy.pause (2.0)
    
    m "The next morning, we gathered in Bryce's office to discuss the future plan of action in regards to Anna's case."
    
    show sebastian normal b at Position (xpos = 0.9) with dissolve
    show bryce normal b behind sebastian at Position (xpos = 0.8) with dissolve
    show naomi normal b flip at Position (xpos = 0.1) with dissolve
    show maverick nice b flip behind naomi at Position (xpos = 0.2) with dissolve
    
    Br "Good morning, everyone. So, what did you find, [player_name]?"
    c "She actually told me the whole story, but strictly unofficially, so it can't be used as a testimony."
    Nm smile b flip "Impressive."
    Br "We need more details. Go on."
    c "Alright. Anna started her cancer research..."
    
    $ renpy.pause (2.0)
    scene black with dissolvemed
    $ renpy.pause (2.0)
    
    scene office at Pan ((0, 250), (0, 250), 3.0) 
    show sebastian disapproval b at Position (xpos = 0.9)
    show bryce stern b behind sebastian at Position (xpos = 0.8)
    show naomi blank b flip at Position (xpos = 0.1)
    show maverick normal b flip behind naomi at Position (xpos = 0.2)
    with dissolveslow
    
    c "...the operation was apparently a success, so she's currently on her way to a full recovery."
    Br "Damn. That's a whole pack of offenses from illegal experiments to lying under oath to bribery. We have to get to the bottom of this."
    Nm stern b flip "She had all the reasons to do what she did, though. And as far as we know, it caused no harm to anyone. I suggest we let her be."
    Nm normal b flip "Any repeat offenses are highly unlikely. Anna was given her cure, she's no longer desperate, and thus has no motive for further felony."
    Nm "The long talk [player_name] gave her should be a good enough deterrent."
    Br "We can't let the culprits go just because they didn't cause harm to anyone by breaking the law. Anna has committed a crime, and it's up to us to make sure she'll be held responsible."
    show maverick sideeye b flip with dissolve
    Sb "I agree with the Chief. The court will decide what she deserves. Our job is to provide them with evidence to reveal the truth."
    Nm annoyed b flip "You do understand that we're talking about someone trying to save herself and many others, right? The good from her actions far exceeds any damage to our traditions her actions may have done."
    Sb "That's not for us to decide, Naomi."
    show naomi stern b flip with dissolve
    Br "And what do you expect us to do? Do you want us to mishandle the case on purpose? That's a crime by itself."
    Mv normal b flip "You've already done so once for me, Chief. I see no reason why we shouldn't try to help her."
    Br brow b "Quite odd to hear that from you, Mav."
    Mv "Reza's case helped me realize a lot of things. Our laws are flawed, and they do no justice. Do you think Izumi deserved to live in the comfort of our prison for the rest of her life after killing so many?"
    Mv "Do you think Anna should face punishment for saving herself and many others?"
    Sb drop b "We aren't judges to make such calls."
    Br stern b "Agreed. It's a dangerous path of thinking, Mav."
    Mv "We can make our own calls."
    show sebastian disapproval b with dissolve
    Nm normal b flip "For once, I agree with Maverick. We are competent enough to assess the damage done by the culprit and decide if the case is worth pursuing. I see no reasons for persecution."
    c "Also, I have my doubts about the fairness of the trial should it happen."
    Br "But she lied under oath during the previous case. I can't overlook such an offense."
    Nm stern b flip "And whom did it harm?"
    Br "She broke the law, and responding to it is our duty. Other details are not important."
    Nm "In our line of work, details are everything, Bryce."
    Mv nice b flip "A minor detail makes the difference between ripping apart a defenseless human and self-defense."
    Br "Do you want me to review Reza's case again, Mav?"
    Mv "Then we'll all be fired."
    Br stern b "Damn."
    Nm annoyed b flip "We aren't just cogs in the machine or tools of the council. First and foremost, we are here to help and protect people."
    Sb "We're here to help people by upholding the law."
    Nm normal b flip "The laws were created as means to do so, not as the end goal in themselves."
    Br "But we can't overlook or change the laws to fit every case. Rules and regulations are here for a good reason."
    Nm "And prisons were also made to rehabilitate and reeducate criminals and to make an example for others."
    Nm stern b flip "What sort of lesson would punishing Anna teach her and others? Don't cure cancer? Don't try to save yourself from a disease? Don't break traditions and just let people die?"
    Sb drop b "You're pushing it."
    Nm "Tell me I'm wrong, Seb."
    Sb "..."
    Br "In an ideal world, I'd agree with you, Naomi. However, we are bound by our own obligations."
    show sebastian normal b with dissolve
    Br normal b "Anna helped us multiple times in the past, and I'm not doing this with an easy heart, but it's our job and duty to uncover the truth and present it to the court."
    Mv "No. Our duty is to make sure our society is safe by all means necessary."
    Br "Then what makes us better than vigilantes?"
    Mv "Nothing."
    Br brow b "..."
    Nm "We shouldn't be the ones to decide the sentence, let alone carry it out, Mav. But you are right in one thing. We can decide if the person should be further persecuted. That is part of our job."
    Sb shy b "Still. We can't falsify evidence and make the wrong conclusions on purpose. Even if you believe it to be the right thing to do, it'd be a crime."
    Nm smile b flip "I can write a conclusion so logically perfect, simple minds will never find fault in it, let alone be able to prove any ill intent on my side."
    show sebastian normal b with dissolve
    Nm normal b flip "But it's too late for it at this point."
    Nm "Anna is no friend to me. She helped me a lot at work, but I best prefer our communication when I'm in my office, she's at the production facility, and we are one phone button push away from ending the conversation at any moment."
    Nm "But to do what is right, I'm ready to go as far as I have to, for her sake or for anyone else."
    Br stern b "We'll end up on a slippery slope if we choose to help Anna at the cost of our work integrity."
    Br "She's a culprit, so we have to proceed with the investigation like it or not. I'm not fond of it myself, but we must do what we must do. That's the nature of police duty."
    Br "Regardless of personal preferences, the law should always come first."
    Sb drop b "And don't forget the council. They will not be happy about their case being ruined."
    Mv angry b flip "The council owes me, Bryce and [player_name] the very existence of this world and everything in it. They wouldn't dare try to smear our names so soon after giving us the honors for stopping the comet."
    Br normal b "Speaking of whom. You've been awfully quiet, [player_name]. What do you think? We have an even split so far, so whatever you say will be the decisive vote."
    show sebastian normal b with dissolve
    c "You are the chief, though."
    Br sad b "I won't sacrifice the trust of my team. We might argue, but we are a tight-knit group and we'll act as one."
    show bryce normal b
    show maverick normal b flip
    with dissolve
    
    # with the new idea Selvy has, player would only get this choice after ending C.
    # the changing factor would be Naomi's behavior.
    menu:
        "We must help Anna.":
            # for now
            jump eck_bryce_annahelp
            
        "Duty comes first.":
            jump eck_bryce_annaarrest
    

#   Notes to self for the good path:
#   Selvy - Today at 00:45
#   Well, the ways of helping her evade persecution that I can think of include:
#   - Evidence: Getting rid of / tampering with / making such up that absolves her
#   - Legal trickery
#   - Persuasion
#   - Finding her somewhere away from law's reach to live
#   - Someone takes the fall for her (pretends they pressured her into breaking the law)
#   Depends on how far you want to go with 'not-really-following the law'

#   If you want to work with the law, it'd be persuasion or maybe legal trickery
#   and if against, the others
#   to varying degrees

    
    
label eck_bryce_annahelp:
    $ save_name = _("Bryce 6 Help")
    $ annastatus = "neutral"
    $ eckbryceannaclues = 12
    c "I'll have to side with Naomi and Maverick here. Anna broke the law to save herself and many others from a certain painful death. Even if her intentions were selfish, the good from the cure here far outweighs any legal issues."
    Br "She's a criminal, however. We can't just look away and pretend she didn't do anything."
    c "Our society's core idea is that every life and every person is precious. Nothing can be more important than that."
    Br smirk b "I see what you mean."
    Sb drop b "The council isn't going to be pleased."
    Mv "The council will never find out we did anything to ruin the investigation."
    Nm smile b flip "I like the way you think, Mav. If we build a case that directly points out Anna as innocent, it should work."
    show sebastian normal b with dissolve
    c "Another option would be to try and simply get her out of the scope, so to say."
    Br brow b "What do you mean?"
    c "Fake her death and make her disappear. Some humans back on Earth did this rather successfully."
    show naomi blank b flip with dissolve
    Mv "Not going to work here. It would send her on the run from the law for the rest of her life, and that's hardly acceptable."
    Nm normal b flip "We could also present someone else as the real criminal of her story."
    Sb "That's pretty dishonest, though."
    Mv "Not if said person is already dead."
    c "Damion."
    Nm smile b flip "Precisely. And considering he blackmailed her, I wouldn't feel too bad about smearing his name post-mortem."
    Br normal b "I'd prefer us not to go too far into the grey law area, guys."
    show naomi normal b flip with dissolve
    c "Then our best bet is to deconstruct, or prove unconvincing, every bit of evidence we have against her."
    Mv "That won't be easy."
    c "How bad is our situation, then?"
    Br "While most of the items and documents recovered so far can only be considered indirect clues, together they might be seen as a foundation for the real conviction."
    Mv "A risk I'd rather not take."
    Br "The main investigation isn't finished yet, so the evidence list might be expanded later on."
    c "Aren't we the only team on Anna's case?"
    Br stern b "From the police side, yes. But the council has their own people working on it as well. They share their data with us, but they might withhold some of the items."
    Nm "What if we try and keep one step ahead? Any finds they make could worsen our situation, so the logical solution would be to prevent them from getting their hands on anything in the first place."
    Mv "Intercept the evidence before they get it and starve them out. I like the idea."
    Br brow b "Yes, this could be a solution."
    Br normal b "Maverick, go to the hospital and stay by Anna's side. Explain to her that we are willing to help, but she'll need to work with us. Maybe she can give us some hints as to what and where to search."
    Mv nice b flip "Got it, Chief."
    show maverick nice b with dissolve
    hide maverick with easeoutleft
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (2.0)
    Sb "She probably won't cooperate, though."
    c "I suspect she won't trust us. Not immediately, at least."
    Nm "So we should concentrate on the deconstruction of the evidence we've already discovered."
    Br "And what do we have?"
    Nm "So far, the most important pieces are Reza's samples, lab reports regarding [player_name]'s blood analysis, and data on several experiments going against the conditions of the suspended sentence."
    Nm "None of them are crucial enough, however."
    Nm "We have the collection Damion was holding, which might be more interesting, but it hasn't been categorized fully yet. The legal side of using it is tricky, too."
    c "Is there something wrong with it?"
    Nm "From the standpoint of the law, one could argue that we had no justification for searching his apartment with him being a victim rather than a suspect. It was also related to a completely different case – Reza's case, in particular."
    c "I see."
    if annascenesfinished > 2:
        $ eckbryceannaclues += 5
        $ eckbryceannalabavail = True
        Nm "The council's group also reported finding a large amount of human research materials in Anna's lab during their own sanctioned search. They are yet to provide the exact data, however."
        c "I helped her out with some minor experiments, but I didn't know it was illegal."
        Sb drop b "This, however, puts Anna in a tough spot."
        Nm "Depending on the scale of that research, the consequences might range from sentence extension to immediate conviction."
        Br stern b "Damn. It doesn't look good. This piece should be our top priority."
        show sebastian normal b with dissolve
    else:
        $ eckbryceannalabavail = False
        pass
    
#   Br normal b "What should be our first move?"
#   c "From the looks of it, our colleagues are the biggest threat right now. Let's see what they know and have in their possession."
#   Sb "They won't give us anything, and if they did, any tampering on our side would be obvious."
#   c "What is their official status?"
#   Nm "From what I understand, they are state-funded investigation agency. Unlike us, they have no authority to arrest people or open official cases, however."
#   Sb "Crossing them would be unwise."
#   Br "Yeah. They might have less power, but their regulations are also much more relaxed compared to the set of rules we have to follow."
#   c "And what if we'd pay them a visit at night when nobody's here?"
#   Br sad b "That would be a crime, [player_name]."
#   Nm smile b flip "I'm in."
#   Br brow b "Really?"
#   Nm normal b flip "I don't mind crossing a few lines to do the right thing."
#   Br "I see."
#   Sb drop b "I guess, you'll need me."
#   c "Seb?"
#   Sb "I can pick most mechanical locks."
#   c "A useful skill. Where did you learn it?"
#   Sb smile b "Sometimes you have to get through a locked door to reach your goal without making noise."
#   Br normal b "Very well. If you want to go, guys, I'm with you. I'll be on the lookout."
#   Sb normal b "But how are we going to coordinate our actions over distance?"
#   c "I have an idea."
#   m "I lifted my arm and tapped on the PDA strapped to it."
#   c "It can create a local wireless network and exchange voice or text messages with other similar devices."
#   Sb drop b "Sounds complicated."
#   c "Don't worry about it. I'll take care of the setup and teach you all how to use it."
#   Br "Now, we only need to get one for each of us from the production facility."
#   Nm "Should be easy. We are the ones responsible for the storage and have all the keys needed. We should be very careful not to damage them though. The databases those PDAs hold are invaluable."
#   c "They are rather resilient so don't worry about minor hits or scratches."
#   Br "That's good."
#   c "First, I suggest we should scope out the place. Being the analysts, Naomi and I can pay them a visit and ask about the state of things without raising any suspicion."
#   Nm "Normally I just call them when I have questions they might help me with, but I've been to their offices a few times."
#   c "From here, we'll be able to plan our approach."
#   Br "I trust you to handle this operation, [player_name]."
#   c "If there's one thing we, humans, are good at, it's planning and plotting."
#   Br smirk b "Somehow, I believe you."
#   
#   Nope, too beyond the law. Gonna leave it there for people curious enough.
    

    Br normal b "Either way, [player_name], you've cast the decisive vote, so our next step is up to you."
    $ eckbryceannalaberased = False
    $ eckbryceannahelpblood = True
    $ eckbryceannahelpreps = True
    $ eckbryceannahelpdamion = True
    $ eckbryceannahelpwarning = True
    
    jump eck_bryce_annahelpmenufirst
    
    
    
label eck_bryce_annahelpmenu:
    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    scene black with dissolveslow
    play music "mx/hydrangea.ogg"
    $ renpy.pause (2.0)
    scene office at Pan ((0, 250), (0, 250), 3.0) with dissolveslow
    show sebastian normal b at Position (xpos = 0.9) with dissolve
    show bryce normal b behind sebastian at Position (xpos = 0.8) with dissolve
    show naomi normal b flip at Position (xpos = 0.1) with dissolve
    
label eck_bryce_annahelpmenufirst:
    
    if eckbryceannaclues < 3 and eckbryceannahelpwarning:
        Nm smile b flip "In its current state, Anna's case looks pretty good for her. Good job, everyone."
        c "Will it be enough to prove her innocent in the court?"
        Nm "I'm fairly certain. We can look for any remaining pieces we've missed if you choose to make sure, but most likely it won't be necessary."
        Sb drop b "Uh, guys. I've been thinking, and there's something that concerns me."
        show naomi normal b flip with dissolve
        Br brow b "Go on."
        Sb normal b "Wouldn't it be suspicious that all evidence on Anna's case has mysteriously become irrelevant after [player_name] paid visits to the related locations and discovered new details?"
        Br stern b "Damn it. You are right."
        c "Thanks for bringing it up, Seb. This idea completely slipped past me, to be honest. We'll need to cover our tracks."
        Nm blank b flip "But how will we do that? I can clean up the paper trail, but it won't be sufficient on its own."
        Br smirk b "I have an idea. I'll write an official assignment to you, [player_name], to check on the PDAs in the production facility. This would give you a legal reason to visit Anna's lab."
        Nm smile b flip "Sounds good. The lab reports will only need some minor dry chemical cleaning to remove all traces of you ever touching them."
        Sb "For Damion's apartment, it will be easy to cover up our visit. No witnesses saw us, so we only have to make sure none of our own cameras recorded you placing anything in that storage cell."
        if eckbryceannalaberased:
            c "Nothing can be done about the viruses I've used to destroy that data, but with no other evidence I should be alright."
        else:
            pass
        Br normal b "You may still be at risk, [player_name], but I doubt they'd decide to accuse you of anything without direct proof."
        c "I hope so."
        $ eckbryceannahelpwarning = False
        
    else:
        pass
    
    menu:
        "Blood analysis and Reza's samples." if eckbryceannahelpblood:
            c "So, what is the crime in doing research on me or Reza?"
            Br "She was supposed to get permission from the council before attempting any work on human samples, which she didn't."
            Br "By itself, it's worth no more than a stern warning or possibly a minor fine, but in the context of her case it can be seen as indirect evidence pointing towards her rule-breaking habits."
            Sb drop b "It can also be linked to the main cancer research if the prosecution side pushes hard enough."
            Nm "But it can be deflected as irrelevant just as easily."
            c "What if I asked her to do this research for me? Say, out of scientific interest both personal and for humanity as a whole."
            Sb smile b "Smart thinking."
            Br brow b "They can argue she had to deny you such requests and redirect you to the council."
            c "My visit here was supposed to be reasonably short, so I had no time for the extra paperwork. I can testify in the court to prove it if necessary."
            Nm shy b flip "Paperwork... If we made an official request signed by you dating back to the day Anna took some of your blood, her research on it could be seen as a completely different act."
            c "I can write it up, but won't they check when it was created? It's easy to see the age difference between documents."
            Nm normal b flip "Leave that to me. I know a few tricks that can fool the modern analysis methods. We will need the exact paper from Anna's lab for authenticity, however."
            Nm "A pen from that place wouldn't hurt, too."
            c "So, our next stop is the production facility."
            
            stop music fadeout (2.0)
            $ renpy.pause (2.0)
            scene black with dissolveslow
            jump eck_bryce_annahelpblood
            
            
        "Experimental data." if eckbryceannahelpreps:
            c "What do we have on the experiments Anna has been conducting?"
            Nm "We've recovered several reports regarding them, some mentioning potentially law-breaking activities. Everything there has been carefully analyzed and cataloged and can be found in our database."
            Nm smile b flip "You're quite welcome."
            Br smirk b "So this is why you were staying in your office until sunset a few weeks ago."
            Nm shy b flip "I kept getting carried away."
            Nm normal b flip "Legal troubles aside, her research is pretty interesting, but I'm not sure that genetics is the answer to the cancer problem, considering the nature of the disease is still unknown."
            Sb "Let's save this discussion for another time."
            Br laugh b "Agreed. Preferably when I'm not around."
            c "Alright, alright. What approach do you think we should take for those papers?"
            show bryce normal b with dissolve
            Nm "We can't destroy them, but we can alter them to be much less accusatory."
            Br "The experts will easily see any edits made to the reports."
            c "Yeah. But what if we make our own pages instead and replace or remove the undesired ones?"
            Nm smile b flip "Exactly what I was thinking."
            Sb drop b "Sounds risky."
            show naomi normal b flip with dissolve
            Br smirk b "I believe in [player_name]."
            c "Thanks, Bryce."
            Nm stern b flip "I'll be working on this too, you know."
            Br "There was never any doubt about your skills, Naomi."
            Nm smile b flip "Alright, I'm going to let it slide."
            Sb normal b "I just hope they won't track this back to us."
            Nm normal b flip "We'll have to be careful."
            Nm "I know how to make this idea work, I think. Follow me, [player_name]."
            
            stop music fadeout (2.0)
            $ renpy.pause (2.0)
            scene black with dissolveslow
            jump eck_bryce_annahelpreports
            
        "Damion's collection." if eckbryceannahelpdamion:
            c "What did Damion gather on Anna?"
            Nm "I didn't get the chance to study his evidence in detail yet."
            c "How so? It's been in the police's possession for a very long time."
            Nm stern b flip "You weren't in the force until recently, and with Bryce and Maverick on sick leave, Seb and I didn't have time to spare."
            Br smirk b "I don't blame you."
            c "We don't know what sort of compromising documents Damion might've collected during the time he was working with Anna."
            Nm "Analyzing them and developing counter-arguments for each point will take too long."
            Nm shy b flip "Assuming it's even possible to debunk everything he'd been using to blackmail her."
            Sb "We could try to present his information as fake."
            Br brow b "Any expert will confirm those papers to be genuine. Their age, ink used and all other details line up perfectly."
            c "You might be onto something here, Bryce. If we could argue that his whole collection has been fabricated to get leverage on Anna, we wouldn't need to analyze it."
            Sb "It would be hard to prove."
            c "Maybe we'll find something in Damion's apartment."
            Br "We can't do that. The warrant has long expired, and we have no formal legal reason to issue a new one."
            c "Then we'll have to act of our own accord. Did he live alone?"
            Br normal b "As far as we know, he did. He also had no direct relatives nearby, so it's unlikely for anyone to visit his place anytime soon."
            c "Except for us."
            Sb smile b "I can handle most mechanical locks, so we won't need the key."
            Nm smile b flip "It would be wise to wait until late at night."
            Nm shy b flip "However, I don't think I'll be of much help on this mission. I'll stay back if nobody objects."
            c "It's alright. Seb and I should be able to handle the task."
            show naomi normal b flip with dissolve
            Br brow b "What about me?"
            c "Bryce, it would be best if you stay out of this as well. People can recognize you easily, and I don't want to get you in trouble if our attempt fails."
            Br normal b "Very well. Be careful, you two."
            
            stop music fadeout (2.0)
            $ renpy.pause (2.0)
            scene black with dissolveslow
            jump eck_bryce_annahelpdamion
            
        "Human biometric data." if eckbryceannalabavail:
            c "What sort of trouble did I get Anna into by agreeing to her tests?"
            Nm blank b flip "Truth be told, that event alone is enough to convict her harshly, regardless of every other piece."
            c "But she only did some scans and studied my fingernail under a microscope!"
            Br stern b "She wasn't supposed to do anything with you at all. You were an ambassador of a different world, not her test subject."
            Br "She thought nobody would find out. However, the council investigation group analyzed the materials recovered from the lab before submitting them to us for detailed investigation."
            Br "They've discovered the additional notes, scans and records made by Anna during her tests on you, [player_name], albeit without material samples."
            c "Where are they stored?"
            Nm "From my experience, that investigation group has a decent network of computers, including a data server."
            c "And what about physical evidence?"
            Nm "They are legally obligated to transfer it to us. However, in this case, Anna didn't leave any to begin with."
            Sb drop b "Unless they're hiding it on council's request."
            Br stern b "They have no reason to doubt or suspect us."
            show sebastian normal b with dissolve
            Nm normal b flip "I agree with Bryce. They were always following the rules and regulations to the letter."
            c "Then we just need to wipe out their data."
            Br brow b "Wouldn't that be hard to do?"
            Nm blank b flip "I hope we won't be causing them too much grief. There are some nice people working there."
            Sb "They aren't that nice from what I've heard."
            Nm "I know that some of them have questionable work eithics to put it mildly, but many of them are genuinely trying to help people or to set things right."
            c "I'm afraid the only way to do it is to release a malicious program into their system to destroy all files."
            Nm shy b flip "Can't we try something else? I don't want to harm their work too much."
            c "If we had a choice, I'd have tried other options."
            Nm sad b flip "Oh well..."
            Br stern b "How are we going to do that program thing?"
            c "I have an archive of viruses. Got it back in the day, before the flare, to test my information security. They're badly outdated but might still work."
            c "It's only a matter of somehow accessing their computers."
            Nm blank b flip "You'll need to do it from the inside, I'm afraid."
            Br "That's very risky."
            c "In all senses, I'm the one who caused this mess and I'm ready to do what it takes to fix it."
            Br normal b "I'm with you. We'll look more like an official visiting group this way, and I can watch your back while you work."
            c "Thanks. It's surprising you don't mind such a legally questionable course of action."
            Br brow b "I'm only doing this for you, [player_name], and for our group."
            
            stop music fadeout (2.0)
            $ renpy.pause (2.0)
            scene black with dissolveslow
            jump eck_bryce_annahelplab
            
            
        "I think our job here is done." if eckbryceannaclues < 10:
            if eckbryceannaclues < 3:
                Nm smile b flip "Sounds about right to me, too."
                Sb drop b "It has been quite an adventure for all of us. I don't think I'd want to go through it again."
                Br "I hope it wasn't in vain."
                c "It's all up to Anna's laywer now, but our odds look good."
                Br "We'll see at the trial."
                
                stop music fadeout (2.0)
                $ renpy.pause (2.0)
                scene black with dissolveslow
                jump eck_bryce_annahelpsuccess
                
            else:
                Nm stern b flip "But we haven't done much."
                c "It'd be risky for our whole department to continue. Let's hope that our efforts were enough."
                Br "I agree with [player_name]. We better stop now before we cross a certain line."
                Sb "Yeah. Anna's case isn't looking good already for the prosecution side. There's no point in putting everything at risk because of worrying about chances."
                Nm "We'll see on the day of trial."
                
                stop music fadeout (2.0)
                $ renpy.pause (2.0)
                scene black with dissolveslow
                jump eck_bryce_annahelpfailure
            
            
#   Failure consequences ideas
#
#   Selvy - Today at 23:25
#   I guess
#   I was just looking for some punishment, and then that gave the idea of sending MC back to the time machine
#   On the lighter side of things, MC could just get disqualified from the investigation, and have to watch Anna get sentenced to prison for the foreseeable future
#   less harsh on MC, but a lot harsher on the player xD
#   if you really want to make them suffer

#   Chaos_Knight - Today at 23:27
#   I like the way you think

#   Selvy - Today at 23:27
#   I was afraid of that

#   Chaos_Knight - Today at 23:27
#   I had the same idea myself XD
#   Maybe get MC fired as well?

#   Selvy - Today at 23:39
#   Then you get removed from the force by the council, forced to find another job
#   I'm just gonna say 'you' instead of 'MC' because screw that
#   and you can choose whether to attend Anna's trial or not
#   either you witness her getting sentenced harshly, or you hear from it via m "..."
#   If you're there, Anna passes you by on the way to prison, and you exchange sad looks
#   You try to give your condolences, but she's not in the mood to talk and gives you the cold shoulder on the way out
#   Either way, you go home with Bryce and he admonishes you for what you were doing, but understands and consoles you
#   then it ends with "at least I still have you / wish my first case didn't end this way... and become my last"
#   bittersweet, mostly bitter ending
#   Ta-dah
#   And obviously no hanky-panky alternative in that ending, because what kind of mood would that be for that stuff
    
    
    
    
label eck_bryce_annaarrest:
    
    $ save_name = _("Bryce 6 Duty")
    $ annastatus = "bad"
    $ brycestatus = "good"
    c "I have to agree with you and Seb. Anna had good intentions, but they don't excuse the crimes she committed. We should try our best to gather as much evidence as possible."
    show bryce normal b with dissolve
    Nm shy b flip "We know she's guilty, but are her crimes severe enough to warrant punishment?"
    c "Let the trial decide that. I have my doubts about its fairness, but we can't be the ones to make such calls."
    Nm sad b flip "So be it. Then let's make sure that everything is handled properly."
    Mv "I stand by my initial position."
    show naomi blank b flip with dissolve
    Br brow b "Mav. I understand that you probably have some personal motives in protecting Anna, but please, have some faith in us. Our goal isn't to harm anyone but to uphold the law. Nothing more."
    Mv "If you know that I'm compromised, why not remove me from the case?"
    Br "Because I trust that you'll support the rest of the group."
    c "Maybe you should go to Anna instead of me and explain to her our current course of action so she won't get the wrong idea about us being enemies."
    Mv normal b flip "You are a fool to believe she'd cooperate with any of us."
    c "She wouldn't, that's a given. But you can help her."
    Br "[player_name] has a point. The four of us will handle the investigation, and you can work with her on how to present the case to the court. You have my permission to keep her up to date about our findings."
    Mv "On it. Am I required for anything else?"
    Br "No, you're free to go."
    show maverick normal b with dissolve
    hide maverick with easeoutleft
    $ renpy.pause (2.0)
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (2.0)
    c "Any idea where to look for evidence?"
    Sb "Checking Anna's apartment would be a good start."
    Br "Agreed. I'll sign the warrant for it. Be careful and don't mess up anything there. The other group who handled her case before us has been very sloppy, so let's not repeat their mistakes."
    Nm "Can I come along?"
    Br "Of course."
    Nm smile b flip "Thanks."
    Nm normal b flip "I haven't gotten to do any outside work in a very long time."
    c "Ah, the thrill of rummaging through someone's personal belongings, am I right? It's like a box of chocolates, you never know what you might get."
    show sebastian smile b with dissolve
    Nm stern b flip "Digging through people's items brings me no joy, but if you were in my place, you'd be happy about any activity outside of the office."
    c "I was just trying to make a joke."
    Nm normal b flip "Oh."
    Sb "That was a good one."
    Br "I'll stay here. I'm pretty big, and I don't want to break things in her apartment."
    c "Yeah. Let's keep the mess and damage to a minimum."
    Nm smile b flip "It's not all about body size, Bryce. I'm doing just fine thanks to my grace and agility."
    Br smirk b "You don't have my strength and muscles, either."
    Nm "You have them, so I don't need to."
    Sb normal b "We can chat later. First, let's get our job done."
    show bryce normal b with dissolve
    c "We need the keys to Anna's apartment, though, unless you want to break in. She takes her security seriously, so don't expect to find them in a flowerpot or under the rug."
    Sb smile b "I can open most locks."
    Nm blank b flip "I thought we were upholding the law?"
    c "Yeah. Let's save lockpicking for the last resort."
    Sb normal b "Anna uses janitor services. They might be in possession of a copy of the keys."
    Br "Good idea. I'll give them a call to come to her apartment and open the door for us."
    c "Finally, I'm not the one to do the errands."
    Sb "It's less about the errands and more about the fact that they aren't allowed to pass the keys to anyone, not even the police."
    Nm smile b flip "Which means less work for us. Plus, we get a witness who can confirm that we haven't planted any incriminating evidence. Not complaining."
    Br normal b "Alright, you all know what to do. I'll be waiting for your reports."

    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    scene black with dissolveslow
    play music "mx/martyr.ogg"
    $ renpy.pause (2.0)
    scene eckannahouse2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    
    m "When we made our way to Anna's house, the janitor company representative was already waiting for us at the front door."
    m "Following a short introduction, he opened the door for us and we walked into the apartment."
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    scene eckannalivingroom1 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    $ renpy.pause (2.0)
    play sound "fx/door/door_close.ogg"
    
    show sebastian normal b flip at left with dissolve
    show naomi normal b at right with dissolve
    
    Nm "It's pretty nice here."
    Sb "Yeah. It's way better than the place I have to live in."
    Nm smile b "C'mon, don't be like that. Your place is good too. It just needs to be put in order and could use a bit of extra care."
    Sb disapproval b flip "I don't have enough time for it."
    Nm "If you want, I'll help you out this weekend. I was planning to spend it on the beach by the ocean or exploring the seabed, but we could fix up your apartment instead."
    Sb shy b flip "Um. Thank you."
    c "Can you smell it in the air?"
    Nm normal b "The air refresher? Yeah, the aroma Anna chose is rather unusual and sweet, but I'd say it's alright."
    c "No. The scent of the upcoming date."
    Nm stern b "Really now, [player_name]."
    Sb smile b flip "It does sound like a date, Naomi."
    Nm shy b "So what if it does? I just wanted to help you, because you're my very good friend."
    c "Hey, I'm not judging."
    Nm "Let's get to work before it gets even more awkward."
    Sb shy b flip "Agreed."
    c "Shall we split up to cover the apartment faster?"
    show sebastian normal b flip with dissolve
    Nm normal b "We can't. Our witness should be able to keep track of all our movements."
    Sb "But we can still spread out within the same room, so let's make the most of this investigation."
    
    $ eckbrycelivingbooks = False
    $ eckbrycelivingtrophy = False
    $ eckbrycebathsearched = False
    $ eckbrycebathpills = False
    $ eckbrycekitchensearched = False
    $ eckbrycekitchenfridge = False
    $ eckbrycepcopen = False
    $ eckbrycebedvisited = False
    $ eckbrycebedbooks = False
    $ eckbrycebasementvisited = False
    $ eckbrycebasementopen = False
    $ eckbrycecureprojectfirst = True
    $ eckbryceannapcscanunchecked = True
    $ eckbryceannapcnoteunchecked = True
    $ eckbryceannapcarchunchecked = True
    $ eckbryceannagotpcevidence = False
    $ eckbryceannaarchiveopen = False
    $ eckbryceannaclues =0
    $ eckancdtries =6
    $ eckanpwtries =6
    $ eckancd = "1111"
    $ eckanpw = "qwerty123"
    $ eckanpw1 = "qwerty123"
    $ eckanpw2 = "1234567890"
    
    show screen eckextrainfo
    $ eckextradisplay = 1
    
    $ eckdisplayvar1name = "Clues found:"
    $ eckdisplayvar1 = eckbryceannaclues
    $ eckdisplayvar1unit = ""
    
label eck_bryce_annahomesearch:
    scene eckannalivingroom1 at Pan((0, 250), (0, 250), 0.0)
    show sebastian normal b flip at left
    show naomi normal b at right
    with dissolve
    # Ain't it convenient I already have a search of Anna's house in the other mod?
    $ eckdisplayvar1 = eckbryceannaclues
    menu:
        "Look around the living room.":
            $ renpy.pause (2.0)
            m "Tidy and spacious, if somewhat dusty, the living room had a cozy charm to it. I spotted a couple of books on the sofa. Their titles were a little too specific even for my level of knowledge, but there was something about stem cells."
            m "In the far corner stood a large shelf filled to the brim with assorted trophies, framed diplomas, and other prizes of all shapes and colors."
            
            label eck_bryce_annalivingsearch:
                $ eckdisplayvar1 = eckbryceannaclues
                show sebastian normal b flip at left
                show naomi normal b at right
                with dissolve
                menu:
                    "Check the books." if eckbrycelivingbooks == False:
                        m "I sat on the sofa and skimmed through both of the books I found on it. With my limited knowledge of biology, their contents meant little to me."
                        Nm stern b "It's not the time to relax, [player_name]. You wanted us to deal with this case, so let's deal with it."
                        c "There might be something here."
                        Sb smile b flip "Owning books about science isn't a crime."
                        m "Despite the remarks of my colleagues, I gave the tome in my hands one last glance and spotted a bookmark sticking out from between the pages."
                        m "On its front, a group of ornate flowers was drawn forming into intricate patterns of dark saturated colors. On its back, however, the bookmark was mostly white – except for a single faded line written by hand evidently a while ago."
                        m "All it said was \"g3n3t1cs\"."
                        c "(An odd way to write a word.)"
                        $ eckbrycelivingbooks = True
                        jump eck_bryce_annalivingsearch
                    
                    "Check the books." if eckbrycelivingbooks:
                        m "Trying to refresh my memory, I looked at the bookmark again. Faded \"g3n3t1cs\" was scribbled on its back with a pen."
                        jump eck_bryce_annalivingsearch
                        
                    "Look behind the TV.":
                        m "Nothing but layers of dust waited for me behind the large boxy TV and underneath the cupboard it was standing on."
                        jump eck_bryce_annalivingsearch
                    
                    "Look in the cupboard.":
                        m "Books, more books, and a few trinkets. Not one item of interest."
                        jump eck_bryce_annalivingsearch
                    
                    "Check the trophies." if eckbrycelivingtrophy == False:
                        m "One after another, I picked up each trophy, prize and diploma Anna had stored on the shelf and studied them carefully from every angle."
                        m "One of the bronze-colored cups had a small sheet of paper attached to the bottom of it. The ink had almost completely faded, but I managed to read part of the message written there."
                        m "Upon closer inspection, however, it was revealed to be information about the manufacturer. Next to it was \"...igh school Science F..ir of 1753\"."
                        Nm smile b "For a moment you looked like you'd found a treasure."
                        c "I thought I did, but alas. Did you guys find anything new?"
                        Nm normal b "Nope."
                        Sb "Negative."
                        $ eckbrycelivingtrophy = True
                        jump eck_bryce_annalivingsearch
                    
                    "Check the trophies." if eckbrycelivingtrophy:
                        m "Despite additional efforts, I found no information to speak of. The only thing worth any interest was an almost faded line reading \"...igh school Science F..ir of 1753\"."
                        jump eck_bryce_annalivingsearch
                    
                    "Change the search location.":
                        jump eck_bryce_annahomesearch
            
        "Search the bathroom.":
            $ renpy.pause (2.0)
            play sound "fx/door/handle.wav"
            scene black with dissolve
            $ renpy.pause (2.0)
            scene eckannabath with dissolvemed
            
            if eckbrycebathsearched == True:
                jump eck_bryce_annabathsearch
            else:
                pass
            
            show sebastian normal b flip at left with dissolve
            show naomi normal b at right with dissolve
            
            m "Anna's bathroom was unsurprisingly average-sized, with sleek, simplistic furniture and fixtures. It actually reminded me a lot of my own, but in red."
            m "Stored in a wall cabinet were medical supplies, but out of all the pills, I only recognized painkillers."
            
            Nm stern b "It's quite cramped here with all of us present at once."
            c "What about your grace and agility?"
            Nm "Not if I have no wiggle room at all!"
            Sb drop b flip "Don't wiggle anything. One move of yours, and I'm in the bathtub. You take up all the space and I can barely balance on one leg here without falling."
            show naomi annoyed b with dissolve
            Nm "Not my fault this bathroom is so tiny."
            c "I don't see much to investigate here, anyway. Maybe you two should wait in the corridor?"
            Nm normal b "Good idea. Let's go, Seb."
            Sb "Uh-oh."
            m "Naomi made a step back, trying to make her way to the exit, but she didn't account for her shoulder width and bumped into Sebastian. With mild amusement, I watched him lose his balance and nearly tip over the bath's edge, but he was quickly caught by Naomi's half-folded wing and held against her side."
            
            play sound "fx/bed.ogg"
            show sebastian at Position (xpos = 0.1) with ease
            show naomi at Position (xpos = 0.75) with ease
            Sb shy b flip "Um. Thanks."
            Nm shy b "You're welcome. I think we can leave now."
            Sb "Yeah."
            
            hide sebastian
            hide naomi
            with dissolve
            $ eckbrycebathsearched = True
            
            label eck_bryce_annabathsearch:
            $ eckdisplayvar1 = eckbryceannaclues
            menu:
                "Look under the bath.":
                    m "I removed the decorative cover and looked under the bathtub. A somewhat large, mean-looking spider looked back at me from its cobweb."
                    m "Besides the creature, some dust and the thick pipe, the space was completely empty."
                    jump eck_bryce_annabathsearch
                
                "Look inside the shower.":
                    m "No clues, no evidence, just a shower cabin."
                    c "(That's a lot of different types of body wash.)"
                    jump eck_bryce_annabathsearch
                
                "Search the cupboard." if eckbrycebathpills == False:
                    m "I dug through the pills and other medical supplies Anna had stored in the cupboard."
                    m "Several boxes of meds caught my attention, however. The names obviously told me nothing, and no visible hints were present on the packaging."
                    c "Hey, guys, can I ask you something?"
                    Sb "Sure, go ahead."
                    c "What is Pircackesic?"
                    Sb "It's normally used to reduce fever and headaches. I can imagine Anna had a lot of those with her work schedule."
                    c "Alright. And Grawsicon?"
                    Sb "Heartburn relief pills. Again, no wonder. I doubt she has enough time for proper meals."
                    c "Got it. Alright, what is Irrianor?"
                    Sb "No idea."
                    Nm "Those are for hormone regulation."
                    c "Why would she need that?"
                    Nm "I doubt she does anymore, if my hunch is correct."
                    m "The packaging of said meds appeared rather bent and misshapen. Curious, I extracted the contents, and besides the usual manual and the pills themselves, I found a note."
                    m "The top line simply read: \"stay strong.\""
                    c "(I don't feel well...)"
                    $ eckbrycebathpills = True
                    m "Pushing down the lump in my throat, I noticed the additional text beneath the main message, written in tiny letters: \"a:4 o:0 no space.\""
                    jump eck_bryce_annabathsearch
                
                "Search the cupboard." if eckbrycebathpills:
                    m "I looked at the note again. The top line simply read: \"stay strong\". Beneath it, however, I found an additional record saying \"a:4 o:0 no space\" written in tiny letters."
                    jump eck_bryce_annabathsearch
                    
                "Check the toilet's drain tank.":
                    m "Remembering the old cop movies back on Earth, I checked the drain tank for any hidden caches."
                    m "Sadly, Earth cop movies aren't applicable to the world of dragons, and all I got was a soaked hand and an unpleasant feeling of being dirty somewhere at the back of my mind."
                    jump eck_bryce_annabathsearch
                
                "Change the search location.":
                    scene black with dissolve
                    $ renpy.pause (2.0)
                    jump eck_bryce_annahomesearch
            
        "Search the kitchen.":
            $ renpy.pause (2.0)
            play sound "fx/door/handle.wav"
            scene black with dissolve
            $ renpy.pause (2.0)
            scene eckkitchenx4 with dissolvemed
            
            if eckbrycekitchensearched == True:
                jump eck_bryce_annakitchenearch
            else:
                pass
            
            m "The kitchen had all the necessary furniture and equipment. However, most of it was in pristine condition, showing that it was rarely used. The only exception was the coffee machine."
            c "(Looks like she's not a big fan of cooking at home.)"
            
            show sebastian normal b flip at left with dissolve
            show naomi normal b at right with dissolve
            
            Nm smile b "Can't say I'm surprised."
            Sb "What do you mean?"
            Nm "Look how clean and new everything is. She obviously never or almost never used any of this."
            Nm "Though, I don't find cooking very entertaining, either, let alone other chores that go along with it, like washing the dishes."
            Nm shy b "My work gives me enough boredom already, thanks to the bureaucratic nightmare of handling official papers and documents."
            Sb smile b flip "I like cooking. It's nice and relaxing, and you can always try something new."
            Sb normal b flip "If only I had more time for it."
            c "Though my skills leave a lot to be desired, it's still a fun and useful hobby."
            Nm smile b "I guess it would feel good to sit down and make something after a day of running errands and chasing down culprits."
            Sb "Yeah. It's just great."
            c "Wait, did you say sit?"
            Nm normal b "Yes?"
            c "Don't you normally stand while making food?"
            Nm smile b "Not if you're a large quadruped and need to free up both of your hands for some of the tasks."
            c "I didn't think of that."
            Nm normal b "It's alright. For better or worse, life is quite different for dragons like Bryce, Mav and me compared to the bipedal species."
            Nm "Not to ruin the mood, but we'd better start seeking that evidence, though. I want to be done before the end of the workday."
            
            $ eckbrycekitchensearched = True
            
            label eck_bryce_annakitchenearch:
            $ eckdisplayvar1 = eckbryceannaclues
            menu:
                "Search the fridge." if eckbrycekitchenfridge == False:
                    m "The supplies were pretty limited, mostly consisting of some meat snacks and assorted drinks. None of the packaging was damaged, so it was pointless to look inside."
                    m "However, an interesting find was waiting for me on the bottom shelf, behind a couple of juice bottles. I instantly recognized the vial before me. It was the very same one that Anna had used to collect my blood."
                    c "Now this is interesting."
                    Sb normal b flip "Got something?"
                    c "That's the vial of my blood. A very odd place to store such samples, isn't it?"
                    Nm "I believe it can be considered a piece of incriminating evidence. She wasn't allowed to perform any tests on humans, yet she did so anyway. Good find, [player_name]."
                    c "Let's store it here for now, though. We don't want it to spoil, right?"
                    Sb "Agreed."
                    $ eckbryceannaclues +=1
                    $ eckbrycekitchenfridge = True
                    jump eck_bryce_annakitchenearch
                    
                "Search the cupboards.":
                    m "For several minutes, we carefully inspected the tableware. Plates, forks, metal pots, glasses... Eventually, every item was checked and we put them all back in place."
                    c "(Nothing of interest for us, though.)"
                    jump eck_bryce_annakitchenearch
                    
                "Check out the pantry.":
                    m "A few vegetables and fruits were scattered amongst the mostly empty shelves. The place was clean, empty and somewhat sad."
                    jump eck_bryce_annakitchenearch
                    
                "Look in the oven.":
                    m "In a burst of inspiration, I decided to check the oven. Considering the lack of use, it could make a great hiding spot for smaller items."
                    m "Several extracted frying pans, grids and baking sheets later, I found myself sorely disappointed."
                    jump eck_bryce_annakitchenearch
                    
                "Investigate the breadbox.":
                    m "The bread was mostly stale, and with no pastries in sight. No evidence, either."
                    jump eck_bryce_annakitchenearch
                    
                "Change the search location.":
                    scene black with dissolve
                    $ renpy.pause (2.0)
                    jump eck_bryce_annahomesearch
            
        "Search the bedroom.":
            stop music fadeout (2.0)
            $ renpy.pause (2.0)
            scene black with dissolve
            play music "mx/elegant.ogg"
            $ renpy.pause (2.0)
            scene eckannabedroom4 with dissolvemed
            play sound "fx/door/handle.wav"
            jump eck_bryce_annabedroom
            
        "Check the basement":
            $ renpy.pause (2.0)
            scene black with dissolve
            $ renpy.pause (2.0)
            scene eckannacorridor at Pan((0, 250), (0, 250), 0.0) with dissolve
            
            if eckbrycebasementopen == True:
                $ renpy.pause (2.0)
                scene black with dissolve
                $ renpy.pause (2.0)
                scene eckannabasement with dissolve
                
                show sebastian normal b flip at left with dissolve
                show naomi normal b at right with dissolve
                jump eck_bryce_annabasementsearch
            elif eckbrycebasementvisited == True:
                show sebastian normal b flip at left with dissolve
                show naomi normal b at right with dissolve
                jump eck_bryce_annabasementcode
            else:
                pass
            
            show sebastian normal b flip at left with dissolve
            show naomi normal b at right with dissolve
            
            Nm stern b "Locked."
            Sb drop b flip "It's a code lock, too. There's no key and no mechanism to pick it."
            c "Do you think if we cut off the electricity, it would open?"
            Sb "No. Security systems always have either an emergency power supply that can last for hours if not days, or their own generators."
            Nm normal b "Then we'd better find the code somewhere. Property damage and breaking down doors isn't something I'd sign up for."
            Sb normal b flip "Same."
            $ eckbrycebasementvisited = True
            
            label eck_bryce_annabasementcode:
            
            menu:
                "Enter the code.":
                    $ eckancd = renpy.input(_("Code:"), allow="0123456789", length=4)
                    play sound2 "fx/beep.wav"
                    queue sound2 "fx/beep.wav"
                    queue sound2 "fx/beep.wav"
                    queue sound2 "fx/beep.wav"
                    $ renpy.pause (2.0)
                    
                    if eckancd == _("1753") and eckancdtries > 0:
                        m "Access granted."
                        $ eckbrycebasementopen = True
                        jump eck_bryce_annabasement
                        
                    elif eckancd == _("0909"):
                        m "Administrator code accepted."
                        Sb "How did you know that?"
                        c "It was just a lucky guess."
                        jump eck_bryce_annabasement
                        
                    elif eckancdtries > 0:
                        $ eckancdtries -=1
                        m "Error. Tries before lockdown: [eckancdtries]."
                        jump eck_bryce_annabasementcode
                        
                    else:
                        m "Lockdown in effect. Please contact your administrator to reset the system."
                        Sb disapproval b flip "Looks like we aren't getting anything here."
                        Nm stern b "Stupid code lock."
                        jump eck_bryce_annabasementcode
                        
                "Leave.":
                    scene black with dissolve
                    $ renpy.pause (2.0)
                    jump eck_bryce_annahomesearch
            
            
        "Leave." if eckbryceannaclues > 0:
            $ renpy.pause (2.0)
            
            if eckbryceannaarchiveopen == True:
                Nm stern b "You've left the computer running in the bedroom. Unless you want to start a fire or hit Anna with a huge electricity bill, I suggest we shut it down."
                c "My bad."
                show naomi normal b with dissolve
                jump eck_bryce_annahomesearch
                
            elif eckbryceannaclues > 10:
                c "We should have everything we need for now."
                Sb smile b flip "Impressive work, everyone."
                show naomi blank b with dissolve
            
            else:
                c "The evidence we have should be enough."
                Sb "I'm not sure, [player_name], but it will have to suffice."
                show naomi blank b with dissolve
            
    hide screen eckextrainfo
    $ eckextradisplay = 0
    
    $ eckdisplayvar1name = ""
    $ eckdisplayvar1 = 0
    $ eckdisplayvar1unit = ""
            
    stop music fadeout (2.0)
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.0)
    scene black with dissolve
    play music "mx/elegant.ogg"
    # something tense I guess?
    
    $ renpy.pause (2.0)
    scene eckannahouse2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    
    show sebastian normal b flip at left with dissolve
    show naomi normal b at right with dissolve
    play sound "fx/door/doorclose.ogg"
    $ renpy.pause (2.0)
    c "Let's head back to the station and report our progress to Bryce. Maybe Mav has managed to discover something as well."
    Nm "Somehow, I doubt it."
    Sb "They used to be pretty close. He might still try to save her from jail, and knowing him, he'll go as far as it would take."
    c "Sounds pretty scary, and there's nothing we can do about it."
    Nm "Mav is scary when he's fixated on something."
    Nm shy b "And seeing how this time he has strong personal reasons to act, I don't envy anyone in his path."
    Sb drop b flip "But that's us."
    Nm "Precisely."
    Sb "Mind us taking some days off, Naomi?"
    Nm stern b "If necessary, we have to stop Mav and prevent him from doing something stupid that could get him fired or, worse yet, jailed."
    c "Do you think we stand a chance, though?"
    Sb "Not really."
    Nm shy b "I agree with Seb. But we should coordinate with Bryce and do our best."
    c "For now, though, let's play along. We don't know yet if Mav has any ill intent."
    Sb "And our distrust could actually provoke him to act."
    Nm normal b "I see your point."

    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene office at Pan ((0, 250), (0, 250), 3.0) with dissolveslow
    play music "mx/hydrangea.ogg"
    $ renpy.pause (2.0)
    
    show sebastian normal b at Position (xpos = 0.9) with dissolve
    show bryce normal b behind sebastian at Position (xpos = 0.8) with dissolve
    show naomi normal b flip at Position (xpos = 0.1) with dissolve
    
    Br "Hello, everyone. Did you find anything at the apartment?"
    if eckbryceannaclues > 10:
        $ save_name = _("Bryce 6C Main")
        c "We have a lot of new information, but the largest piece of evidence will take time to process."
        Sb "Some of the smaller clues, however, already heavily point to the fact that Anna is guilty as charged."
        Nm blank b flip "The archives we've recovered might provide us with better insight on the situation, but with such a large volume of work, I'll need days if not weeks."
        Br "[player_name] will help you. I also believe that we shouldn't push the case until after Anna is released from the hospital."
        c "I'd also suggest we let her submit her findings about the cure for cancer."
        Nm "I agree."
        Br "You two are the ones to decide how fast our research is done, so act as you see fit."
        Nm smile b flip "Then it's settled. Any news from Mav?"
    
    else:
        $ save_name = _("Bryce 6B Main")
        c "We only managed to recover a few small bits of evidence and information."
        Sb "Some of those clues, however, already heavily point to the fact that Anna is guilty as charged."
        Nm "That, however, likely won't be enough for the court to make a decision one way or another."
        Br stern b "I see."
        c "So, what's going to happen to Anna in that situation?"
        Nm blank b flip "At worst, her suspended sentence will be extended. At best, nothing."
        Br "We must try and find a way to solve this case for good and either prove her innocent or guilty."
        Sb drop b "That won't be easy, Chief."
        Sb normal b "We've exhausted our means of investigation, and I don't see any others available."
        c "Should we try and put some pressure on the physician?"
        Nm "He'll just deny everything, and with how hospitals are run, I bet all the paperwork is in perfect order."
        Nm smile b flip "At least Mav will be happy to learn about this."
    
    Br brow b "I haven't heard anything from him since our morning meeting."
    c "Do you think we can trust him not to mess up this case on purpose?"
    Br "..."
    Br stern b "No. His sense of justice and personal bias worry me."
    Nm stern b flip "He'll throw himself at anything to do what he believes is right, punish the ones responsible and to protect the very few people he cares about."
    Sb drop b "And I'd rather not be between him and his objective."
    Br "We'll see. If Mav gives me a reason to doubt him, I'll remove him from the case by force."
    Sb disapproval b "Which could further aggravate him and push him towards desperate actions."
    c "Let's all agree to keep our suspicions a secret while possible. We don't know anything for sure, and accusing Maverick without proof wouldn't be right."
    Br normal b "Yeah. He's still our friend and a part of the team."
    Nm normal b flip "I'm surprised he hasn't returned yet. The shift is almost over."
    Sb normal b "Probably he went home. He lives close to the hospital, while our department is at the other end of town."
    c "Looks like somebody decided to end his workday early."
    Br smirk b "It's normal for a roaming investigator like Mav."
    Nm stern b flip "While [player_name] and I normally have to sit in the office by the clock."
    Sb "Following the schedule is part of our work obligations."
    Br normal b "You two don't have to chase the culprits and run errands, though."
    c "I beg to differ."
    Br laugh b "Alright, you got me."
    Br smirk b "You don't have to chase the culprits {i}anymore{/i}."
    Nm normal b flip "I like being the flyer on duty, though. Lots of fresh air, open sky, all while helping people below feel safer."
    Sb smile b "Unless there's a thunderstorm, like that one time."
    Nm shy b flip "Um, yes. Strong winds make a nasty combination with poor visibility."
    Br "Are you talking about that one time Naomi got stuck in the branches of an ancient tree, and we had to call in the rescue team?"
    Nm "It wasn't my proudest moment."
    Sb "We all make mistakes. At least you didn't get hurt."
    Nm "And with how ugly the weather was, nobody but Seb saw anything, thankfully."
    Nm blank b flip "Do we need to discuss anything else? Because I too have some embarrassing stories to tell about you guys."
    Sb shy b "..."
    Br normal b "No, that would be everything for today."
    show sebastian normal b with dissolve
    Nm smile b flip "See you all tomorrow, then."
    Br "Take care, everyone."
    $ renpy.pause (0.5)
    show naomi normal b with dissolve
    hide naomi with easeoutleft
    $ renpy.pause (0.5)
    hide sebastian with easeoutleft
    $ renpy.pause (1.5)
    play sound "fx/door/handle.wav"
    $ renpy.pause (2.5)
    play sound "fx/door/doorclose.ogg"
    
    hide bryce with dissolve
    show bryce smirk b with dissolve
    
    Br "Just like old times when we first met, isn't it, [player_name]?"
    c "I'm here full time, though, so no more slacking off for days."
    Br laugh b "What do you think we do when on standby?"
    Br smirk b "And ever since you've joined the force, I swear that even the amount of petty theft has gone down tremendously."
    Br normal b "Superstitions about the mythical humans are strong in our society, and having you in the police discourages a lot of would-be-criminals from even trying."
    c "I guess it's good they don't know I'm nobody special."
    Br flirty b "You are quite special to me."
    c "Aw. How sweet of you."
    Br "You know it's true."
    Br normal b "Thank you for siding with me earlier today, by the way. It means a lot to me."
    c "No matter if we like it or not, duty should come first."
    Br smirk b "That's what I was thinking."
    Br normal b "Personally, I hold nothing against Anna and her actions. But as the chief of police, I have to take action against violations of the law. That's our job, you know."
    Br "Without laws, our society will simply crumble."
    c "I'm all too familiar with situations like that, and I don't want your people to experience the same things I had to face."
    Br sad b "I know."
    c "Don't be so gloomy. All of this is nothing but distant past now."
    Br normal b "I see."
    Br smirk b "Mind if I crash at your place tonight?"
    c "You sure got used to my spacious bed, Bryce. Every time you get the chance, you sprawl over the whole surface and stretch out your limbs with the biggest grin on your face."
    Br laugh b "It's too comfortable! I can't help it."
    c "Considering the couch you have to sleep on back at your place, I can't blame you."
    Br normal b "Yeah. I'm still stuck with that arrangement."
    Br smirk b "Anyway, let's go home. Our shift for today is done."
    
    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    scene black with dissolveslow
    play music "mx/barren.ogg"
#   Idk what music to put here yet. Well, why not this one? Ok, maybe something else?
    $ renpy.pause (2.0)
    nvl clear
    
    if eckbryceannaclues > 10:
        jump eck_bryceannaattack
    else:
        jump eck_bryceannafailtrial

#   Short rundown planned:
#   Several days pass. Mav plays along. Naomi is busy with files.
#   Depending if you did good or not, a break-in will happen one evening which will damage the evidence.
#   Either way, Anna's case will fall apart.
        
label eck_bryceannaattack:
    
    window show
    n "In the following days, our group concentrated on the analysis of the current evidence."
    n "With the huge mass of data extracted from Anna's computer, everyone had something to do or check, and there seemed to be no end to the records and lab reports."
    n "As Maverick stated, she was extremely unhappy about us poking our noses into her personal computer, but otherwise refrained from making any additional comments."
    n "That alone was a big red flag to me."
    n "A few days before Anna's release from hospital, however, another incident got the attention of the entire police force."
    window hide
    nvl clear
    
    $ renpy.pause (2.0)
    scene eckpolicedeptoutside1 at Pan ((0, 150), (0, 150), 0.0) with dissolveslow
    $ renpy.pause (2.0)
    
    show sebastian normal b with dissolve
    
    c "Good morning, Seb. You're early today."
    Sb "Hello, [player_name]. I couldn't sleep well, so I decided to go for a walk until our shift starts."
    c "Quite an interesting time of day, isn't it? The sun is high in the sky, yet you barely meet anyone outside."
    Sb smile b "Yeah. People are just starting to wake up at this hour."
    Sb normal b "Do you think today will be another drag? I might consider picking up a new hobby if things continue like this."
    c "Probably. We have a lot of documents to cover and analyze, and who knows how long that's going to take. I'm surprised we didn't get sent on patrol duty yet."
    Sb "The other part of the local police unit has taken over that to let us concentrate on Anna's case."
    c "I see."
    Sb drop b "I'd rather chase the perps than read any more of those lab reports. All this science stuff is making my head hurt, and I'm not sure if I'm useful at all."
    c "Each to their own, I guess."
    Sb smile b "Yeah."
    Sb normal b "Our workday is about to start. Let's head inside."
    $ renpy.pause (2.0)
    scene black with dissolvemed
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (2.0)
    scene eckoutsidewall1 at Pan ((0, 150), (0, 150), 2.0) with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    show sebastian drop b with dissolve
    play music "mx/detective.ogg"
    Sb "Oh no."
    m "Not far from the building's entrance, we found Naomi lying on the grass next to a concrete wall. Her body was covered in bruises and claw marks."
    m "Sebastian and I carefully crouched near her."
    scene eckoutsidewall1 at Pan ((0, 150), (0, 350), 2.0)
    $ renpy.pause (2.0)
    show sebastian normal b flip at left with dissolve
    c "Damn! Is she alive?"
    m "Sebastian leaned down to touch her neck and check for a pulse. In response, she groaned and started to stir on the ground before grabbing her head with a quiet hiss."
    show naomi hurt b at right with dissolve
    # make closed eyes cr for her? Done.
    Nm "My everything hurts so much..."
    Nm sad b "Oh. [player_name]? Sebastian? What time is it?"
    Sb "Our shift is about to begin."
    Nm "So I've been out the whole night."
    c "Can you get up?"
    Nm shy b "Let me try."
    hide sebastian
    with dissolve
    
    # rustling sound
    play sound "fx/undress.ogg"
    scene eckoutsidewall1 at Pan ((0, 350), (0, 150), 2.0)
    show naomi blank b at right
    $ renpy.pause (2.0)
    Nm "I think I'm doing alright. Just need to..."
    Nm scared b "Ah!"
    hide naomi with dissolve
    scene eckoutsidewall1 at Pan ((0, 150), (0, 350), 1.0)
    play sound2 "fx/impact.wav"
    $ renpy.pause (0.5)
    with Shake((0, 0, 0, 0), 0.5, dist=20)
    $ renpy.pause (2.0)
    # drop sound with a screenshake
    # move camera down
    
    show sebastian shy b flip at left with dissolve
    show naomi cry b at right with dissolve
    
    c "Are you alright?"
    Nm "My arm..."
    Sb "Not good. It's broken."
    Nm sad b "I see."
    c "Alright, stay here, I'll call in the medic team."
    Nm stern b "No, we need to investigate the damage done first. I can walk on three limbs for now."
    c "What damage? What happened to you?"
    Nm annoyed b "Maverick."
    show sebastian drop b flip with dissolve
    c "What?!"
    Nm blank b "Yesterday, I stayed late to study several intriguing documents in detail. I lost track of time, and before I knew it, the sun had set completely."
    Nm stern b "When I exited the building, he blindsided me from the nearby bush. I tried to put up a fight, and he didn't get away unscathed, but I was too reluctant to harm him. I'm not that much of a fighter, you know."
    Nm "He held no such reservations and used his claws freely. In the end, he pinned me down and knocked me out cold."
    show sebastian disapproval b flip with dissolve
    c "That's just brutal and unnecessary. Has he lost his mind? What in the world could warrant attacking and hurting you, his friend, like that?!"
    Nm blank b "He couldn't just use a neck grab to put me to sleep because I'm a water dragon. I can hold my breath for over twenty minutes, and Mav knows that."
    Nm "In a way, my natural traits are partially to blame for this mess."
    c "Your traits have nothing to do with this incident, and they don't explain or excuse the violence against you at all."
    Nm stern b "I know. I'm just trying to find a logical reason for the brutality of his attack against me."
    Sb normal b flip "We have to find him."
    Nm sad b "Too late for that. I'm sure he's on the run far away by now."
    c "But why? You still haven't explained why he attacked you."
    Nm blank b "Let me get up first."
    hide naomi
    hide sebastian
    with dissolve
    $ renpy.pause (2.0)
    play sound "fx/undress.ogg"
    scene eckoutsidewall1 at Pan ((0, 350), (0, 150), 2.0)
    $ renpy.pause (2.0)
    
    show sebastian disapproval b flip at left with dissolve
    show naomi blank b at right with dissolve
    
    m "Slowly, Naomi got up once more, this time holding the damaged arm close to her chest. Sebastian tried to help and offered some support, but she politely declined. She stood on three limbs and slowly stretched her body."
    Nm "This will have to suffice for a time."
    c "So, why did he attack you?"
    Nm stern b "Because I'm the holder of keys to the evidence storage room. I used to keep them in my belt pouch, and as you can see, it's gone now."
    c "Do you think it's related to our advances in Anna's case?"
    Nm "Most likely."
    Sb shy b flip "Are you sure it's safe for you to walk?"
    Nm smile b "Thanks for the concern, Seb, but right now we have more important things to worry about."
    Sb "Shouldn't we at least call the medics now, so you'll get help as soon as possible?"
    Nm shy b "No. They'll take me away for who knows how long, and I'm the only one who can accurately assess the damage."
    Nm sad b "It hurts. I'm not trying to be a tough girl here, but you said it yourself, [player_name], \"Duty comes first\"."
    c "Alright. Let's hurry up, then."
    
    $ renpy.pause (2.0)
    scene black with dissolvemed
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (2.0)
    scene eckpolicedeptstairs1 at Pan ((0, 150), (0, 150), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    
    show sebastian normal b at Position (xpos = 0.9) with dissolve
    show naomi blank b behind sebastian at Position (xpos = 0.8) with dissolve
    show bryce normal b flip at Position (xpos = 0.1) with dissolve
    
    Br laugh b flip "Hey, guys! What's the rush?"
    c "Hello, Bryce. Sorry, no time to lose right now."
    Br brow b flip "Naomi? Are you alright? What's going on?"
    Nm stern b "Maverick attacked me last night and stole the keys to the evidence storage. Those cuts and bruises are nothing to worry about, but my arm is broken."
    Br stern b flip "Damn, I never imagined he would do such a thing to someone from our team."
    show naomi blank b with dissolve
    Br brow b flip "Did you call in medical help?"
    Sb "We didn't get the chance yet. Naomi insisted that we should check on the storage room first."
    show naomi sad b with dissolve
    Br stern b flip "Alright. Seb, notify the hospital and get them to send help over here. After that, grab all the first aid you can find and meet us at the evidence storage. Naomi, [player_name], and I will assess the damage."
    Sb "Got it, Chief."
    hide sebastian with easeoutleft
    Br "Naomi, how are you holding up? Lean on me if you need to."
    Nm shy b "Thanks, Bryce, but I'm fine for now."
    
    $ renpy.pause (2.0)
    scene black with dissolvemed
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (2.0)
    scene eckpolicedeptstorage1 with dissolvemed
    $ renpy.pause (2.0)
    
    show naomi normal b at Position (xpos = 0.8) with dissolve
    show bryce normal b flip at Position (xpos = 0.2) with dissolve
    
    c "Do you remember which storage cells we were using?"
    Nm "Of course. Just give me a hand here, [player_name]. The numbers are 233, 234 and 235. So second cabinet, third row from the floor, and you can figure out the rest."
    c "Here they are."
    play sound2 "fx/door/lock.ogg"
    queue sound2 "fx/metalbox.ogg"
    
    $ renpy.pause (1.5)
    play sound2 "fx/door/lock.ogg"
    queue sound2 "fx/metalbox.ogg"
    
    $ renpy.pause (1.5)
    play sound2 "fx/door/lock.ogg"
    queue sound2 "fx/metalbox.ogg"
    
    $ renpy.pause (1.0)
    Nm blank b "Empty?"
    c "Actually, no. But my data carrier is gone, and we seem to only have some of the evidence recovered from Damion's apartment and a few papers from the lab in the production facility."
    Br stern b flip "Damn it."
    Nm shy b "So, he took every piece of evidence I didn't get to register in the system and catalog yet. Smart. It will be hard to prove tampering with something that we didn't officially have."
    c "But there's only one way to check the database..."
    Nm scared b "My computer! Nearly all of my work and documents are there!"
    Br "You two stay here. I'll check on it and be right back."
    show naomi sad b with dissolve
    c "Do you know how to operate it?"
    Br "A bit."
    show bryce normal b with dissolve
    hide bryce with easeoutleft
    hide naomi with dissolve
    show naomi cry b with dissolve
    
    Nm "This is a mess."
    Nm "I knew Mav would try to interfere, but not like this."
    Nm "What did I do to deserve this? I was just trying to be helpful, and I never even supported the case against Anna."
    c "I'm sorry, Naomi. My actions were the reason he went rogue."
    Nm sad b "You did nothing wrong, [player_name]. You value our duty, and I respect that even if I disagree with your choice."
    Nm "But Mav?"
    Nm angry b "He only really cares for himself and a small circle of people he deemed worthy!"
    Nm sad b "And, as it turned out, we are not among them..."
    m "I glanced over the remaining pieces of evidence again."
    c "Look. This doesn't seem to belong here."
    Nm blank b "What is it?"
    c "I found an envelope in cell 235."
    play sound "fx/paper.wav"
    c "Let's see. A resignation paper signed by Maverick."
    Nm annoyed b "As if he's not getting kicked out of the police for this."
    play sound "fx/paper.wav"
    c "That isn't everything, though... He left a message to all of us and, actually, you specifically, Naomi. A farewell letter of sorts."
    Nm "What sort of lame excuses is he making up?"
    c "Actually, none, and he planned everything in advance. There's a lot of text here, we can read it in detail later, but listen to this."
    c "\"In the end, I've betrayed everyone's trust and hurt someone innocent to pursue my goals. What I did to you, Naomi, can't be justified, and I understand the anger you are likely feeling right now.\""
    show naomi stern b with dissolve
    c "\"One day, maybe you will forgive me, but I don't expect it to happen. You were always a good friend, and I'm sorry it has to end this way. I was left with no other choice to save someone I care about.\""
    show naomi sad b with dissolve
    c "\"I take full responsibility for this incident. I'm leaving both the force and this town. Don't try to find me. Farewell, everyone. Maverick.\""
    Nm blank b "Let me see."
    c "Here."
    play sound "fx/paper.wav"
    $ renpy.pause (1.0)
    Nm "You know, I really want to hate him for what he's done to me. But all I feel is... disappointment and some odd bitter sadness. There are so many questions in my head."
    Nm sad b "What would I have done in his place? If someone I loved was about to be jailed for a {i}crime{/i} in name only, which hurt nobody but some outdated traditions, and my friends turned their backs on me in the name of \"duty\"?"
    Nm blank b "I doubt I'd have just sat there on my rump and accepted such an outcome."
    Nm sad b "..."
    Nm shy b "Maybe police work is not for me, [player_name]. I signed up because I wanted to help people, but I don't want to be a cog in the heartless legal machine."
    c "I think you need some rest, Naomi. You're overstressed, so don't make any rash decisions. We aren't cogs, and our work is making everyone safer. It's just that sometimes we have to make uneasy choices."
    Nm "You're right. My thoughts are a mess at the moment."
    c "No matter the reason, Mav has no excuse for attacking and hurting you like this. If he just stole the keys, maybe I'd have understood him. But the harm and pain he had caused you are not acceptable."
    Nm sad b "I know. I wish it had never come to this."
    c "So do I."
    m "My line of thought was interrupted by Bryce."
    Br "I've checked your computer, Naomi."
    
    show naomi blank b at Position (xpos = 0.8) with ease
    show bryce stern b flip at Position (xpos = 0.2) with easeinleft
    
    Br "Thankfully it's intact, but all of the data on Anna's case has been wiped clean."
    Nm stern b "I thought so."
    Br "Nothing else was touched, though. At least he had enough decency left in him not to mess up other cases and records."
    c "But how are we going to handle the situation? Maverick is on the run, Naomi is hurt, and the investigation is crippled, most likely permanently."
    Br brow b flip "Accusing one of our own of such serious crime will be a disaster for the police department's reputation."
    c "But we can't just let it slide. Look what he did to her. And how are we going to explain what happened to the evidence we gathered?"
    Br "It's one of the situations where, one way or another, we lose. But we can try and minimize the damage."
    Nm blank b "Maverick was smart enough to only steal or destroy the evidence that hasn't been properly registered and thus formally didn't exist yet."
    Nm "Unless I make a claim about his attack, it will be impossible to prove even the mere existence of this incident."
    c "So, do you suggest we keep quiet about it? You were the one hurt the most, so it's your call."
    Nm "It will be for the best for everyone."
    c "Do you think it was Anna's plan?"
    Br "Wouldn't surprise me."
    c "He left behind these papers, though."
    play sound "fx/paper.wav"
    $ renpy.pause (1.5)
    Br stern b flip "I see."
    Br "I'll need time to think it all over."
    
    $ renpy.pause (2.0)
    scene black with dissolveslow
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/flashback.ogg"
    # something half-sad I guess?
    
    window show
    n "Soon, the medic team arrived and took Naomi to the hospital. Her arm bone was fractured, but thankfully it had no lasting effect on her health. Doctors said she needed at least a month to fully heal from the injury."
    n "She never filed any accusations against Maverick and chose to make up a story about an unfortunate flight accident when questioned by the hospital staff."
    n "Sebastian regularly took unpaid days off to help out Naomi at home during the recovery period. They started to spend a lot more time together after she returned to police duties."
    n "Bryce tried his best to stay strong, but I could see how close he was to breaking point. I did all I could to support him and even allowed him to stay in my apartment for a time."
    n "At least he didn't slip into drinking again. That alone made me a little happier."
    window hide
    nvl clear
    
    scene eckcourtcorridor1 at Pan ((0, 150), (0, 150), 0.0) with dissolveslow
    
    window show
    n "On the very first day of trial, Anna's case fell apart in a matter of hours due to the lack of direct evidence. It was a turn of events that was barely a surprise for anyone in our team."
    n "When she walked out of the courtroom, accompanied by her lawyer, I expected her to be all smug and happy about the recent victory."
    n "Instead, Anna stared at the floor, her shoulders slumped. For a moment, she lifted her eyes and gave us a short hateful glance before rushing off to the exit."
    $ annastatus = "abandoned"
    n "Maybe she wasn't behind Maverick's actions?"
    n "It seemed we had all lost something during that cursed case."
    window hide
    nvl clear
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene black with dissolveslow
    
    jump eck_bryce_dutyending
    
label eck_bryceannafailtrial:
    
    window show
    n "In the following days, our group concentrated on the analysis of the current evidence."
    n "With little to work with, we ended up either on patrol duty or simply idling in the office, trying to fight off boredom."
    n "Our investigation options were completely exhausted, and Anna understandably kept silent about any and all possibly incriminating events of her life."
    n "Regardless of the lack of evidence and weak overall case, Bryce decided to submit our findings to the court as per standard procedure."
    n "A few days after Anna's release from hospital, she sent out her findings about the cure to the Ministry of Healthcare and started preparations for the trial. Maverick remained close by, but refrained from telling us any details."
    window hide
    nvl clear
    
    $ renpy.pause (2.0)
    scene eckcourtcorridor1 at Pan ((0, 150), (0, 150), 2.0) with dissolveslow
    $ renpy.pause (2.0)
    show maverick normal at Position (xpos = 0.8) with dissolve
    show bryce normal flip at Position (xpos = 0.2) with dissolve
    
    Mv "I've got some details from Anna's lawyer on the current state of things. So far the prosecutor is having a hard time trying to present his position."
    Br "No wonder. The evidence we gathered can be considered indirect at best, and with the praise Anna received for uncovering the cure for cancer, the general public is on her side."
    c "She wasn't the one who developed it, though."
    Mv "Yes, she never claimed it as her own. That is common knowledge. But her initiative, hard work and inspiration swayed many people, including some of the council members."
    c "I guess they no longer want her head on a spike."
    Br laugh flip "Maybe they never did."
    show bryce smirk flip with dissolve
    Mv nice "But her methods were seen as a threat to our established ways of life."
    c "And I'm fairly sure she stepped on quite a few tails, considering the way she normally communicates with others."
    Br normal flip "Yeah, you don't make many friends with an attitude like that."
    Mv "I don't mind. If one's ego is fragile enough for simple words to hurt them, maybe the problem isn't with the words."
    Br wink flip "We already know you like her, Mav."
    show maverick scared with dissolve
    c "You and her are a match made in hell."
    show bryce laugh flip with dissolve
    show maverick normal with dissolve
    Mv "Very funny."
    c "Nobody said it was a bad thing."
    Mv "I doubt any of you would dare."
    Br smirk flip "Is that a challenge?"
    Mv nice "A warning, Chief."
    play sound "fx/door/hallwaydoor.ogg"
    c "Look. The trial seems to be over already."
    show anna smirk at Position (xpos = 0.9) with easeinright
    show bryce normal flip with dissolve
    An "How nice of you all. A welcoming party."
    Br "So you've won."
    An normal "Naturally. You can't imagine how great I feel right now. No more cancer, no more you guys on my tail, and even though my own cure research has failed, I'm ready to take on a new challenge."
    c "So, no hard feelings?"
    An "None. I got exactly what I wanted and a little bonus on top. If anything, I'm grateful you were the ones to handle my case."
    m "I noticed how Anna brushed her side against Maverick's while she moved her muzzle up to my ear for a whisper."
    show anna at Position (xpos = 0.65) with ease
    show maverick scared with dissolve
    An smirk "{i}And if that was intentional case sabotage, [player_name], you've executed it perfectly. I owe you.{/i}"
    show anna normal at Position (xpos = 0.9) with ease
    show maverick normal with dissolve
    $ annastatus = "good"
    Br laugh flip "Hey, don't get too personal with [player_name]!"
    An smirk "Or what? You aren't going to hit a girl, right?"
    An "So, why don't we hook up, [player_name]? Leave these two brutes to themselves. Imagine what you and I could do with our combined cunning intelligence."
    
    show bryce brow flip
    show maverick nice
    with dissolve
    
    c "Um, I never asked for this!"
    An "Didn't you? Think about all the possibilities you're refusing."
    c "..."
    Br smirk flip "..."
    An face "You are so easy to toy with, [player_name]."
    show maverick laugh with dissolve
    c "I was just playing along."
    An smirk "Of course you were."
    Mv nice "Good one."
    if eckbrycebathpills:
        c "So, are you holding up alright?"
        An normal "Right now, I'm better than ever, [player_name]. You can't possibly imagine how good it feels to leave my messed up past behind to rot."
    else:
        pass
    An normal "Anyway, my lawyer and I are going to a restaurant to celebrate the end of this case. Feel free to join us, guys."
    An smirk "Today I might be nice enough to cover the bill for everyone. Let it be a consolation prize for the police department."
    Br smirk flip "Can't say no to free food."
    
    $ renpy.pause (2.0)
    scene black with dissolvemed
    stop music fadeout 2.0
    
    jump eck_bryce_dutyending
    
label eck_bryce_dutyending:
    
    $ renpy.pause (2.0)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    play music "mx/creamclouds.ogg"
    # some nicer music
    $ renpy.pause (2.0)
    
    show bryce normal with dissolve
    
    c "That was a long day, Bryce."
    Br "I know, and I'm glad that, one way or another, this case is over now."
    if eckbryceannaclues > 10:
        Br stern "I still can't believe Mav did this. To attack his own friend like that and leave her hurt, unconscious and helpless. She could've died. I trusted him with my life, [player_name]."
        Br brow "I swear, if he had done something like that to you..."
        c "Don't overstress yourself. He attacked her because he was desperate and she had the keys he needed, nothing more."
        c "He also knew I have the gun we took from Reza, so I doubt he was willing to take such a huge risk."
        Br "You have a point."
        c "Did you notice how depressed Anna was after the trial?"
        Br "Yeah. But why? Her plan to sic Mav on us worked perfectly, and she got off scot-free easily."
        c "But was that her plan? She lost him, this time forever, and she didn't seem happy one bit about it. Maybe Mav did everything of his own accord?"
        c "It would explain the hateful glance she gave us. Anna blames us for pushing him to crime, and the worst part is, she isn't wrong."
        Br sad "Nothing we can do about it now. We were just doing our job."
        c "We were."
        c "Do you think she's going to be alright?"
        Br "She's a strong girl. With no cancer and no police on her tail, I doubt she'll have any problems setting her life straight."
        Br smirk "And I'm happy that you decided to follow your duties as a police officer. You did your job well, and I'm honestly proud of you, [player_name]."
        c "It's a shame Mav didn't, though."
        Br brow "Yeah."
    else:
        Br "We lost the trial, but maybe it's for the best."
        c "Our duty was to try and uncover the truth about Anna and present our findings to the court for them to make their decision. No more and no less."
        c "So, we didn't lose the trial because we were never a side there. The prosecution side lost, while Anna and her lawyer won. And you know what? I'm fine with that."
        Br "I guess you're right."
        Br "She didn't seem to hold a grudge against us, either, so we might continue our cooperation like before."
        c "Yeah. Especially since Maverick and she seem to have reconciled whatever their previous conflicts were."
        Br smirk "It's about time. Those two are made for each other."
        c "I can't imagine any other person being able to tolerate either of them in everyday life."
        Br laugh "You're right, [player_name]."
        Br wink "And I just realized something."
        c "Yes?"
        Br smirk "Our next get-together is going to be so much larger than usual."
        c "Let's wait and see. I don't want to jinx anything."
        Br laugh "A fair point."
    
    Br normal "But for you and me, this adventure didn't end too bad at least."
    Br smirk "You've shown understanding of the importance of our service, [player_name], and your support always means a lot to me."
    Br normal "For better or worse, it was our sense of duty that brought us together back during Reza's case."
    c "It feels like such distant past by now."
    Br "Many things have happened in the few months you've been here."
    c "It's about time I get some peace and quiet in my life. Else I might pick up drinking myself."
    Br laugh "Not a chance."
    c "Yeah, I was just joking."
    Br flirty "I can offer something else both relaxing and entertaining."
    c "You are as subtle as a volcanic eruption."
    Br "So, is that a yes or a no?"
    menu:
        "Yes.":
            c "Yeah, I don't mind some fun."
            Br normal "You know I don't, either."
            m "He moved his muzzle close to my face and smiled widely."
            Br smirk "You know, no matter what happens, as long as we have each other, I'm happy with my life."
            c "So am I."
            Br "I love the understanding you and I share."
            m "Suddenly I found his muscular arm wrapped around my waist. Moments later, I was pulled into a warm strong embrace."
            c "At least let me get my clothes off."
            Br flirty "But I enjoy personally unwrapping my presents. Especially something as precious as you."
            c "Oh my. You sure picked up your flirting game, Bryce."
            $ renpy.pause (2.0)
            scene black with dissolveslow
            play sound "fx/undress.ogg"
            Br "You haven't seen everything yet."
            
            #   Yep, you are not getting any lemon in my mods. :P
            
        "No.":
            c "I'm not really in the mood, Bryce. I'm sorry."
            Br normal "It's alright. You've done a lot for me already, and I need to learn patience."
            c "No, no. It's not about that. You're doing good. It's about me, really."
            Br "I understand."
            c "Thank you."
            Br wink "Would you like some cuddles, maybe?"
            menu:
                "Accept.":
                    c "That could be nice."
                    hide bryce with dissolve
                    m "Suddenly, he moved in closer and wrapped both of his arms around me in a strong yet somehow gentle hug."
                    Br "How does this feel?"
                    c "It's wonderful."
                    m "I gave his nose a quick peck with my lips."
                    Br "That's true for both of us."
                    c "Let's get some rest. Who knows what tomorrow will bring."
                    m "He let go of me and took a careful step back, a wide smirk plastered on his face."
                    show bryce smirk with dissolve
                    Br "Whatever it is, I'm ready."
                    c "So am I. Just, please, don't crush me against the wall again. It's pretty uncomfortable."
                    Br laugh "No promises!"
                    c "Oh you big, silly dragon."
                    $ renpy.pause (2.0)
                    
                "Reject.":
                    c "It's not the best time. Let's just get some sleep."
                    Br sad "Alright."
                    c "We can still share the same bed."
                    Br normal "For a moment I was worried you'd banish me to the couch."
                    c "Of course not. Just don't give me a reason to."
                    Br flirty "I can give you a few reasons to never consider casting me away in the future."
                    c "Oh my. We'll see."
                    Br smirk "We will."
                    
    scene black with dissolveslow
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    
    if eckbryceannaclues > 10:
        $ persistent.eckbryceendingseenc = "C"
        show eckbryceendingseenimgc with dissolveslow
        $ renpy.pause (1.5)
        hide eckbryceendingseenimgc with dissolveslow
        play sound "fx/system.wav"
        s "Congratulations – you've followed your sense of duty and managed to recover the most crucial pieces of evidence!"
        s "No doubt you did well on the investigation, yet the outcome isn't what anyone had hoped for. Do not fret, for time heals all wounds, both physical and emotional."
        if persistent.trueending == True:
            s "In the end, humanity is safe in another timeline, you and Bryce are still together, and your bond is much stronger than before."
        else:
            s "In the end, the cycle continues in another timeline, you and Bryce are still together, and your bond is much stronger than before."
        s "As for the rest of the police team, only time will tell how their lives will turn out. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng]"
        
    else:
        window show
        n "Our overall lighthearted mood at the department, however, was soon ruined by a sudden inspection group sent by the council."
        n "They mostly concentrated on the performance of our analytical unit, and – of course – they declared our quality of work unsatisfactory despite Naomi's and my methodical approach in handling the case."
        n "Bryce tried to reason with them and stated that our force was already understaffed, but his words fell on deaf ears."
        window show
        window hide
        nvl clear
        n "A few days later, Naomi and I were discharged from the police for being unfit to perform our tasks. Being the only human in this world, I had little concern about money, for I could easily make a living by taking part in research. However, I wanted to do something by myself."
        n "The very same week, Anna showed up and offered to take me in as an assistant. I gladly accepted."
        n "Naomi took a long vacation by the sea and afterwards decided to dedicate her time to the local rescue and emergency services. We still remained in touch."
        window hide
        nvl clear
        $ renpy.pause (1.5)
        $ persistent.eckbryceendingseenb = "B"
        show eckbryceendingseenimgb with dissolveslow
        $ renpy.pause (1.5)
        hide eckbryceendingseenimgb with dissolveslow
        play sound "fx/system.wav"
        s "So, you've followed your sense of duty. Yet, your investigative performance leaves a lot of space for improvement."
        s "Perhaps some important piece of data has managed to slip away from you? It might just change almost everything in the development of Anna's case."
        if persistent.trueending == True:
            s "In the end, humanity is safe in another timeline, you and Bryce are still together, and your bond is much stronger than before."
        else:
            s "In the end, the cycle continues in another timeline, you and Bryce are still together, and your bond is much stronger than before."
        s "As for the rest of the police team, only time will tell how their lives will turn out. Mod's endings seen: [persistent.eckbryceendingseena] [persistent.eckbryceendingseenb] [persistent.eckbryceendingseenc] [persistent.eckbryceendingseend] [persistent.eckbryceendingseene] [persistent.eckbryceendingseenf] [persistent.eckbryceendingseeng]"
    
    jump eck_bryce_goodendcredits
    
#   just to prevent crashes and other weird behavior
    
    



#   Honestly, Bryce's story didn't leave me with a lot of materials to work with, so I had to make some
#   of my own. For better or worse, his life is a lot less of a clusterfuck compared to, say, Anna.
#   Not to mention, I'm not that good at writing male romances... so yeah. Enjoy the interactivity for days.
#
#   If you feel like this mod isn't as good as Anna's, I understand. In fact, I'd say I feel the same way.
#   Yet, Bryce deserves to have his happy ending for his story, and hopefully, I've managed to at least get that right.
#
#   Anyway. The next project is probably going to be revolving around either Adine or Lorem. I don't feel confident
#   writing Remy just yet. For Adine it might be an extended romance ending (Yes, another one. I guess making one
#   is like every AwSW modder's obligation XD ).
#   
#   For Lorem, on the other hand, the mod is prob. just going to be called "Lorem's Good Ending". Not "Better Ending."
#   Just "Good Ending". Because vanilla game's one is so short, I might as well consider that it doesn't exist. XD
#   And I honestly like the little guy... (um, that's gonna be complicated, isn't it?).
#   I can make it romance or simple friendship. Or a bit more adventures. He's pretty fun to hang out with.
#
#   Either way, see you next time on "Chaos_Knight's Extended Endings: Season 3."