#   Why hello there.
#   
#   Looking for some spoilers I assume? Or want to see the other endings without saying/doing what you don't feel is right?
#   Or maybe just trying to find something funny or an easter egg?
#   Not that I mind really. Suit yourself.*
#   
#   "But where's the actual code?" you may ask. Well, it's right below, but I just thought it would impolite to greet a fellow curious person with just, well, code.
#   
#   Good luck!
#   EvilChaosKnight
#   
#    
#    
#    
#   *EvilChaosKnight and/or A4R91N cannot be held responsible for any damages caused by the (mis)use of this mod including but not limited to:
#   - Feels;
#   - Bruises, concussions, bone fractures and/or other traumas caused by facepalms due to poor writing;
#   - Bruises, concussions, bone fractures and/or other traumas caused by falling off the chair laughing due to poor writing;
#   - Flashbacks, PTSD and/or painful reminders about IRL events;
#   - Property damage in any form (broken furniture, PC catching fire etc.);
#   - Depression caused by the inability to physically hug the sassy red raptor-dragon lady;
#   - Depression caused by the inability to physically hug the nice and kind yellow wyvern lady with a banana-shaped tail;
#   - Any other psychological or bodily harm;
#   
#   Have a nice day.























   

label eck_annashappyend:

    stop music fadeout 2.0
    
    if persistent.eckannaendingseena == "A" or persistent.eckannaendingseenb == "B" or persistent.eckannaendingseenc == "C" or persistent.eckannaendingseend == "D" or persistent.eckannaendingseene == "E" or persistent.eckannaendingseenf == "F" or persistent.eckannaendingseeng == "G" or persistent.eckannaendingseenh == "H" or persistent.eckannaendingseeni == "I":
        play sound "fx/system.wav"
        s "Looks like you have already experienced some or all endings for Not-so-Tragic Hero mod. Would you like to reset the list of endings seen?"
        menu:
            "Yes, reset the list.":
                $ persistent.eckannaendingseena = "..."
                $ persistent.eckannaendingseenb = "..."
                $ persistent.eckannaendingseenc = "..."
                $ persistent.eckannaendingseend = "..."
                
                $ persistent.eckannaendingseene = "..."
                $ persistent.eckannaendingseenf = "..."
                $ persistent.eckannaendingseeng = "..."
                $ persistent.eckannaendingseenh = "..."
                $ persistent.eckannaendingseeni = "..."

            "No, keep the list.":
                pass
    else:
        pass
    
    $ renpy.pause(3.0)
    scene black with dissolveslow
    $ annastatus = "neutral"
    $ renpy.pause (1.0)
    $ save_name = _("Anna 6 Main")
    nvl clear
    window show
    play music "mx/dramatic.ogg"

    n "Seeing Anna like that crushed my heart. She might have been far from the nicest dragoness I had met, but I had grown to care about her."
    n "And now she was slowly dying, exactly the way she always feared the most. Yet she wasn't alone, and I was not going to stand by idly."
    n "But what could I do? I'd racked my brain over it for hours in the last few months but never got anywhere."
    n "And Anna... That accepting sad smirk of hers did not help at all. She had already given up all hope."
    n "At least, I was here for her."
    
    window hide
    $ renpy.pause (0.8)
    scene town3 with dissolvemed
    $ renpy.pause(3.0)
    
    m "I was wandering through the town aimlessly, too lost in thought and grief to notice or care where I was going."
    m "Looking how even normally curious and excited locals now tried to avoid my eyes, I think my face said everything there was to say."
    m "Suddenly, Adine landed right in front of me. A spacious but seemingly empty bag was strapped to her back. She must've been on the delivery job again."
    play sound "fx/landing.ogg"
    show adine normal b with dissolve
    m "I hadn't spoken to her much ever since our visit to the beach several months ago."
    m "With Reza, the comet and many other things occupying my mind, I had completely forgotten about her flyer competition."
    m "And, upon finally remembering, I'd been too ashamed to talk to her."
    $ adinestatus = "neutral"
    Ad "Hey, [player_name]!"
    menu:
        "Hey. Sorry, I'm not in the mood for a chat.":
            $ renpy.pause (0.5)
            Ad disappoint b "Are you alright?"
            c "I'm fine. Just need some time alone."
            Ad "I understand."
            Ad normal b "Give me a call when you feel better."
            c "Okay."
            Ad disappoint b "Bye. Sorry for bothering you."
            hide adine with dissolve
            m "I spent the rest of the day sitting on the bench on some unremarkable street, staring into nothingness."
            m "Anna had already accepted her fate. Why did I continue this pointless struggle? There was no cure in this world."
            m "Maybe I just needed to let go and try to carry on. But if I couldn't save one person I care about, how could I hope to save all of humanity?"
            stop music fadeout 2.0
            $ renpy.pause (2.0)
            scene black with dissolveslow
            $ eckannacurrentending = "E"
            jump eck_anna_stockdeathoutcome
            label eck_anna_midendinge:
            
                $ persistent.eckannaendingseene = "E"
                show eckannaendingseenimge with dissolveslow
                $ renpy.pause (1.5)
                hide eckannaendingseenimge with dissolveslow
                
                
                play sound "fx/system.wav"
                s "Looks like you've got a default (\"bad\") good ending for Anna."
                s "Kinda defeats the whole purpose of this mod, doesn't it? Don't be shy to load a save and try again, if you wish. I won't tell anyone, promise. \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
                
                jump eck_anna_stockcredits2
        "Hey, Adine. Good to see you.":
            pass
    
    if persistent.remygoodending == False:
        pass
        
    else:
        c "How are you doing?"
        Ad "I'm alright. With Remy's help, the orphanage is doing much better now. We started talking again after all these years, and have spent a lot of time together."
        c "I'm glad to hear that."
        Ad disappoint b "I never realized how hard his life was. He didn't have anyone who cared about him. But, he's not alone anymore."
        if varasaved == True:
            Ad giggle b "One of the kids seems to like him a lot, too."
            Ad normal b "Her name is Vara."
            c "I think I know her."
            Ad giggle b "They are so adorable together. She keeps sneaking out trying to follow Remy, and then he has to bring her back, often at night."
            c "I hope she won't run into trouble."
            Ad normal b "Me too. He looks so sad every time he returns her. Hopefully, he'll decide to take her in."
        else:
            pass
    
    c "I'm sorry I didn't show up for the flying competition. I got caught up with too many things at once."
    Ad giggle b "Don't worry about it."
    Ad normal b "Actually, I didn't participate."
    c "Was that because you hurt your wing joint during the training?"
    Ad "Yes. It didn't fully heal, and I didn't want to make a poor first impression on everyone. It could've ruined my chances to become a stunt flyer forever."
    Ad think b "I was also seeing those strange nightmares about crashing and dying during the competition."
    Ad normal b "So, I decided to cancel my application."
    
    if persistent.remygoodending == False:
        Ad disappoint b "If something were to have happened to me, I can't bear to think how Amely and the other children would've felt with nobody to look after them."
    else:
        Ad disappoint b "If something were to have happened to me, I can't bear to think how Amely and the other children would've felt."
        Ad "I couldn't leave Remy all alone right after giving him hope, either. Too many people depend on my help for me to be so reckless."
    
    c "I'm sorry to hear that you had to withdraw your application. It was your dream, and you worked so hard to prepare for it."
    Ad giggle b "There's always another year. Next time I'll come up with an even more awesome routine!"
    Ad normal b "And I hope that you will be there, too."
    c "I can't make any promises, but I'll try."
    Ad "You said the same thing back on the beach."
    c "I told you, I'm sorry. There's no need to remind me."
    Ad giggle b "I was just joking, silly. I knew you were very busy."
    c "..."
    Ad disappoint b "[player_name], are you alright?"
    Ad "You don't look well. Is something wrong? I'm sorry if my joke sounded mean."
    c "You don't need to apologize – it's not your fault. It's about Anna. She only has about a week left to live."
    Ad sad b "Oh no... That's horrible. What happened to her?"
    c "Cancer."
    Ad disappoint b "I see. Is there nothing that could be done?"
    c "That's what the doctors said. They can't cure her, only prolong her life, and that isn't working either anymore."
    Ad "If you feel like you need to talk to someone, I'm here."
    c "That would be nice. I'm sorry if I'm holding you up on your work."
    Ad normal b "It's fine, I'm finished for today. I was going to take the delivery bag back to the café, but I can do that tomorrow morning. Let's go somewhere quiet."
    c "Okay."
    
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    
    # insert EVERNING version of the beach here. Done.
    $ renpy.pause (2.0)
    scene eckbeachb at Pan ((0, 0), (300, 0), 5.0) with dissolveslow
    play music "mx/warming.ogg"
    $ renpy.pause (2.0)
    
    m "We walked through the town, staying away from the crowded areas. It reminded me of my very first day here, hiding from all the prying eyes."
    m "Adine led me to the secluded beach we visited last time we met. The warm orange light coming from the sunset made it even more comforting and beautiful than before."
    
    show adine normal b with dissolve
    Ad "This place should be quiet enough."
    Ad "Didn't you say humans go to the beach to relax and have fun?"
    c "I don't think it would help me right now."
    Ad disappoint b "I know. At least I tried to make you feel a little better."
    c "Thank you anyway, Adine."
    hide adine with dissolve
    
    show eckclouds2 at Pan((150, 50), (0, 0), 12.0) with fade
    $ renpy.pause (5.0)
    m "We sat down on the sand side by side and looked at the endless ocean and sky before us."
    m "The sun was slowly approaching the horizon, painting the clouds beautiful shades of yellow and orange."
    $ renpy.pause (1.0)
    scene eckbeachb at Pan ((0, 0), (300, 0), 5.0) with dissolveslow
    
    show adine normal b with dissolve
    Ad "I wish there was something we could do to help her."
    c "I wish so too."
    Ad disappoint b "Don't you hate it?"
    Ad "When there's something so wrong or terrible happening right in front of you, but you can only watch helplessly."
    c "And try to comfort the suffering person as much as possible, but ultimately unable to give them what they need."
    Ad annoyed b "You and I are facing different forms of the same struggle, it seems."
    c "We are."
    Ad disappoint b "I wish I got to know her better. Maybe she's not as terrible as her first impression."
    c "To be honest, she was very unkind to you that one time you met."
    Ad annoyed b "It doesn't mean I don't care. Unkind or not, she's dying from a horrible disease. Maybe it's the very reason she's so..."
    c "Hostile? Arrogant? Irritable?"
    Ad "Now you're being unkind yourself."
    c "Sorry. Though she's fully aware of her own behavior."
    Ad normal b "Maybe she was doing it on purpose? To keep everyone at a distance because she's afraid to let anyone come close?"
    c "She despises pity and attention, yet her biggest fear is to die bedridden and alone. I really don't understand her sometimes."
    Ad "Maybe she's lost and scared. I can't imagine how living with a terminal disease feels like."
    c "I hope you will never have to find out."
    Ad disappoint b "Yeah. I hope you won't, either."
    c "..."
    c "You know what's the worst? In the human world, we know how to cure cancer, even at this stage, but I can't travel back there anymore."
    Ad sad b "You... can't? Does this mean that you're stuck here?"
    c "Yes. And considering that nobody knows how the portal works, I doubt they'll ever reestablish the connection."
    Ad disappoint b "I'm sorry to hear that."
    Ad "You must be going through some very rough times, [player_name]."
    c "Nothing compares to the Reza incident. I'll manage."
    Ad normal b "I hope you feel at home here. You're always welcome to talk to me if you need anything."
    Ad giggle b "When I'm not busy at work for the whole day."
    c "I appreciate that."
    Ad think b "..."
    Ad "You said that humans can cure cancer."
    c "Yes. But it doesn't matter anymore. The connection is lost forever."
    Ad "I understand that. But didn't you bring those PDA things with you with every bit of knowledge humans have?"
    Ad "Shouldn't the cure be in there somewhere?"
    c "..."
    c "Adine."
    Ad "Yes?"
    c "You aren't just a great friend and a talented flyer. You're a genius."
    Ad giggle b "Oh, don't be silly."
    c "Nobody else even considered looking there, not even Anna or I. I'd say you have outsmarted us both."
    Ad "Maybe I should've been a scientist."
    c "Sure, there isn't absolutely everything in those PDAs, but biology and medicine data should be present. We didn't think you, dragons, would find it useful considering differences in anatomy, but to avoid being accused of omitting certain data it was included regardless."
    Ad normal b "Where are those PDAs?"
    c "They should still be at the production facility. I don't think they were moved yet. But to get access to them I'd need to talk to Emera."
    Ad think b "That won't be easy."
    c "My ambassador status might help with getting an audience with her, but talking her into helping is going to be a whole different story."
    Ad "Do you think you can convince her?"
    c "It's my only chance."
    Ad "Working hours are almost over, too."
    c "Looks like I have to run, then."
    Ad normal b "I'd fly you to the ministry, but I think you'd be too heavy."
    c "Don't worry, I'll manage."
    c "Goodbye, Adine. And thank you."
    Ad "Good luck, [player_name]."
    
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene emeraroom with dissolvemed
    play music "mx/politics.ogg"
    $ renpy.pause (2.0)
        
    m "Using my ambassador's status, I easily got the permission to speak with the minister directly. It was only a matter of time before they'd find out the truth about the current state of the portal, but for now, I still had my status and all of the benefits to go with it."
    #rewrite things a bit because I messed up time of narrative. Done.
    m "Despite being as occupied as always with paperwork, Emera agreed to meet with me in her office."
    
    show emera normal b with dissolve
    Em "Good day, Ambassador [player_name]. What a pleasant surprise to see you in person."
    c "Good day. It's nice to meet you too, minister."
    Em "I am quite busy right now, so please get straight to the point."
    Em "What brings you here today?"
    
    menu:
        "Just wanted to chat a little.":
            $ renpy.pause (0.5)
            Em ques b "So you've come to waste my precious time. Is this a human tradition?"
            menu:
                "Um, no...":
                    $ renpy.pause (0.5)
                    Em "How unprofessional."
                    Em "I expected better from you."
                    Em normal b "I am afraid I will have to end our meeting, then. I would gladly see you during my free hours next week."
                    nvl clear
                    m "I missed my chance. Because of it, I wasn't able to save Anna."
                    stop music fadeout 2.0
                    $ renpy.pause (2.0)
                    scene black with dissolveslow
                    
                    $ eckannacurrentending = "F"
                    jump eck_anna_stockdeathoutcome
                    label eck_anna_midendingf:
                        
                        $ persistent.eckannaendingseenf = "F"
                        show eckannaendingseenimgf with dissolveslow
                        $ renpy.pause (1.5)
                        hide eckannaendingseenimgf with dissolveslow
                        
                        
                        play sound "fx/system.wav"
                        s "Looks like you've got a default (\"bad\") good ending for Anna."
                        s "Kinda defeats the whole purpose of this mod, doesn't it? Don't be shy to load a save and try again, if you wish. I won't tell anyone, promise. \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
                        
                        jump eck_anna_stockcredits2
                "In a way it is.":
                    $ renpy.pause (0.5)
                    c "Our politicians often pay informal unofficial visits like this to discuss important matters in a more calming environment."
                    c "Especially when no making of public statement is required afterward."
                    Em normal b "Quite peculiar, yet obviously not without a merit."
                    Em "I wouldn't call those surroundings calming, but never the less, I'd gladly take care of your visit."
                    Em "What would your matters be?"
        "There's an important matter I must discuss with you.":
            $ renpy.pause (0.5)
            Em ques b "I understand. You wouldn't have come here otherwise. Please continue."
            
    c "As you know, I have delivered to you several PDAs that contain most of the knowledge humanity has to offer."
    Em normal b "That is correct. Your generators are almost complete and will be shipped soon as per agreement, if you are concerned."
    Em "Despite Reza's actions, you have proven humanity a reliable partner, and we will uphold our end of the deal."
    Em "Analysis of your data is also on hold until generators are complete, so neither side gets the benefits before another."
    c "I understand, Emera, thank you. But I'm here for a slightly different reason."
    Em "What is this reason, then?"
    c "Among many other things, those PDAs might contain information I require right now."
    Em "Then why don't you send a letter to the human world and ask them to provide it?"
    c "Well..."
    m "I panicked for a moment."
    c "I don't want to spend extra energy. We don't have much to spare."
    c "And it would take too long to get a reply via letter."
    Em "I see."
    Em "What sort of information are we talking about?"
    c "The cure for cancer."
    c "I can't be certain if it's there, but I have reasons to believe it is."
    Em "That could prove to be most useful indeed. It can and will save many lives."
    Em "Are you interested in this data because of Anna's predicament?"
    c "Yes."
    Em "You should understand that even if we extract the data, it has to go through the Ministry of Healthcare and the council."
    Em "Then we will have to run several tests and experiments to see it can be applied safely."
    Em "If the cure is proven to be safe and effective, the Ministry of Healthcare will have to sign an official approval note. And only then will they be able to begin production and application."
    Em "I hope you realize that it won't be fast. We are talking months."
    c "This is why I need your help. She doesn't have that time."
    Em ques b "I see..."
    Em "Everything has been organized this way for generations."
    c "Don't your traditions and beliefs also say that every life is important?"
    Em "That is true. However, order must also be maintained if our society is to last."
    Em normal b "We cannot be careless about our laws and ways of life, lest there be chaos."
    c "So a young girl has to die to maintain said order?"
    Em ques b "You sound a lot like her."
    Em frown b "I am not doing this with a light heart, but you should understand that it's those small things that slowly erode the system."
    Em "And if the system will collapse, can you imagine how many others might lose their lives?"
    if varasaved == True:
        c "Your system already has cracks through which entire families fall."
        Em "What do you mean?"
        c "There's a girl named Vara who had to look after her sick mother all by herself. And because of how your healthcare is organized, her mother is dead."
        c "If I hadn't tracked the poor kid to their hideout, who knows what would've happened to her, all alone in the forest."
        Em "That is most tragic. But mistakes can't be avoided, unfortunately."
    else:
        pass
    c "Won't your system change anyway with all the human technology and the advancements it would bring? You can't stay in one place forever."
    Em normal b "Changes are indeed inevitable. However, it's up to us how fast we will take them. Rushing without thinking might make us vulnerable."
    c "That is a fair concern for general technology leaps, but we're talking about a cure."
    c "Yes, I understand that allowing controversial research might've had negative effects if it was allowed to continue. I don't know to a full extent what it consisted of, so I'm not the one to judge."
    c "But in this particular case it's something that already exists, and only awaits approval for the application. It can't possibly cause any damage to the order of things."
    Em "Indeed. However, negligence towards laws and traditions can."
    c "That's exactly what the council would be doing if they let Anna and many others die while your bureaucratic purgatory is doing its work."
    c "Isn't your most important idea that every life is precious?"
    Em ques b "You must look at the bigger picture, something much bigger than you, me or Anna."
    c "I'm looking at it. And I see that the council is willing to see people die only to maintain the so-called {i}order{/i}."
    Em "This order is what kept us all alive for generations."
    Em normal b "It may sound impolite of me to say this, but I don't think you are the one who can decide what is good or bad for us."
    c "And yet it also means death for the few unlucky ones who don't fit within the limitations."
    c "It reminds me a lot of certain ideologies back in the human world, that were all too happy to sacrifice the few for the good of many. Most of them were later condemned as the greatest tragedies in the history of mankind."
    c "But your society is built on different ideals that value the lives of all people."
    c "Maybe it's about time you set your priorities straight?"
    Em ques b "Sometimes, as a leader you have to make sacrifices. This is sadly inevitable."
    Em normal b "But, perhaps, not this time. What do you want me to do?"
    c "I need your help to access the PDAs and extract the cure data."
    Em "I understand. That would not be a problem, for I am directly responsible for your visit here, as well as for the PDAs you've delivered."
    c "Thank you. But this is not all. Next, I'd need aid with actually producing the cure and making sure it gets to Anna as soon as possible."
    c "If it works, try and make sure it reaches all other critical patients you can get it to while proper paperwork is processed."
    Em "There's nothing I can do here, should I choose to break away from traditions. I am the Minister of Culture & Arts, and I have no power over healthcare or pharmacy."
    c "But, maybe, you could talk with the right people and convince them to help directly?"
    c "Unofficially, of course."
    Em "This is going far outside of normal rules and regulations."
    c "I hate to use this as an argument, but Anna and I are the only reason all of your species still exist. And you're willing to let her die just because of regulations?"
    c "The production of one single batch and its following application is all I ask for right now."
    Em "I understand your accomplishments and I may take risks in my work, but I follow the law, [player_name]. Are you asking me to break it?"
    menu:
        "I guess I am.":
            $ renpy.pause (0.5)
            Em normal b "I am sorry, [player_name], but if this will be revealed, people will turn on me in the blink of an eye. The backlash would be unimaginable."
            Em "We all deeply appreciate what you and Anna have done, but you are asking me to go too far. It's not potential political suicide. It's a crime."
            c "So she was right. She's going to die, and nobody will care."
            Em frown b "You have my condolences, but that is all I can offer."
            nvl clear
            m "I missed my chance, and because of it, I wasn't able to save Anna."
            stop music fadeout 2.0
            $ renpy.pause (2.0)
            scene black with dissolveslow
            
            $ eckannacurrentending = "F"
            jump eck_anna_stockdeathoutcome
            
            
        "It's justified this time.":
            $ renpy.pause (0.5)
            c "Laws are made to help people and society, but this kind of bureaucracy is getting in the way."
            c "If the cure is there, and it's working, it would save so many lives."
            Em normal b "I understand that. But you should also understand the consequences if the public will learn about my abuse of power."
            Em "Not just for me, but for you and humanity as a whole."
            Em "It took a lot from the council to portray Reza as a lone independent criminal. Some people are still asking very uncomfortable questions about him. Imagine what would happen should you also be branded a felon."
            c "We are different. Reza took innocent lives. I'm trying to save them."
            c "I'm sure people wouldn't be upset once they'd see how much good it would do."
            Em ques b "I guess that is also true."
            Em frown b "Yet it would set a dangerous precedent. I cannot put aside our law and traditions so easily, even for the greater good of everyone."
            Em "What you are asking for is basically corruption."
            c "I'm not bribing or blackmailing you. I'm only asking for help."
            Em "It's a matter of principle and the idea of abusing power."
            c "If the cure works, you can announce its discovery and take full credit for it. If anyone starts asking questions, say it was taken from humanity's data and was in the works for a while."
            c "The very data you and your ministry have officially acquired. Any investigation will confirm that said cure was indeed in the PDAs."
            c "In the light of such a breakthrough, everyone would be too excited to do a proper, deep behind-the-scenes check."
            Em normal b "But should any information about this be disclosed, the public backlash would be unimaginable."
            c "I understand that it's a risky idea, but..."
            Em "Let me finish, [player_name]."
            Em "Political suicide and losing this position mean little to me. It's merely a platform of opportunity, but I want to make it count."
            Em laugh b "Maybe the time has come to use its full potential."
            Em normal b "For the service you two have done, and for the sake of everyone else suffering from this disease, I will take that risk."
        "You can make a huge difference.":
            $ renpy.pause (0.5)
            c "Anna aside, if the cure were to be confirmed as working, you could save many lives and give their friends and families hope."
            c "Isn't that the very reason you went into politics in the first place?"
            c "To leave a mark and to help all these simple people."
            Em normal b "You know all the right buttons to push, don't you, [player_name]?"
            Em "When you put it that way, you leave me little choice but to agree."
            Em laugh b "Perhaps I underestimated you. You could make a fine politician."
            c "I'm already an ambassador."
            Em normal b "I can see why they chose you now. Beneath this friendly face, there's a whole lot more."
            Em "You are asking for potential political suicide, and I find myself eager to agree without a doubt."
            c "So, will you help?"
            Em ques b "Yes."
            Em normal b "Even if this doesn't work out very well for me and you, we would at least leave one last mark on this world."
            Em laugh b "And I will finally get my retirement."
    
    c "Thank you, Emera. I owe you."
    Em normal b "Don't thank me before the work is done."
    Em ques b "I assume neither one of us has time to waste right now."
    m "She quickly scribbled up something on a piece of paper, and then put a stamp on it."
    Em normal b "Take this warrant to the production facility. It will grant you access to the PDAs. When you have the data, bring it to me at once."
    Em "I will see to it that it enters the testing and application stage as soon as possible."
    
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene facin3 with dissolvemed
    play music "mx/nostalgia.ogg"
    $ renpy.pause (2.0)
    
    if sebastiansaved == True:
        show sebastian smile b with dissolve
        Sb "Good evening, [player_name]."
        c "Good evening, Sebastian."
        Sb normal b "Didn't expect to meet you here."
        c "Same. We haven't talked for a while."
        Sb "True. Why don't we meet up someday?"
        Sb "Give me a call when I'm off the clock. You should still have my number."
        c "Sure."
        c "But why did they assign you here?"
        Sb "I have to look after this room."
        Sb "As you know, Damion was killed by Reza, and Anna is in the hospital."
        Sb disapproval b "From what I overheard while guarding the place, she won't be returning either."
        Sb normal b "So, until the council finds the replacements, local police forces have been assigned to guard this place."
        Sb "We can't take any chances with the PDAs' security."
        c "Must be pretty boring."
        Sb smile b "You get used to this."
        Sb "Good call on that Reza case, by the way."
        Sb normal b "He would've gotten away if not for you, Maverick and Anna."
        c "It's a shame about Maverick, though."
        Sb "It wasn't your fault."
        Sb "I've read the report and the testimonies."
        Sb "Maverick tried to capture Reza alive and make him answer for his crimes. Else he would've gone for the neck."
        c "And he paid dearly for that."
        Sb disapproval b "He was a good officer, no matter what others may say."
        Sb "He was harsh, but he believed in justice above all else."
        Sb normal b "But I'm glad you two made it out alive."
        c "And saved the world."
        Sb smile b "That too."
        Sb normal b "So, why are you here?"
        c "I have this warrant to access the PDAs I've delivered."
        Sb smile b "Sure, come in."
        Sb normal b "Do you require any assistance?"
        c "I'll be fine, thanks."
        show sebastian normal b flip with dissolve
        hide sebastian with easeoutright
        
        play sound "fx/door/handle.wav"
        nvl clear
        $ renpy.pause (2.0)
        scene eckpdaslab at Pan((0, 250), (0, 250), 0.0) with dissolvemed
        stop music fadeout 2.0
        $ renpy.pause (2.0)
        play music "mx/archives.ogg"
        $ renpy.pause (1.0)
        
        m "Inside the facility room, I quickly located where the PDAs were stored."
        m "After managing to access the computer, I found out that the dragons apparently had already developed a way to read and transfer data between our devices and theirs."
        m "It was just a matter of finding the right files and information."
        
        show sebastian normal b with dissolve
        Sb "Mind some small talk?"
        c "Not at all, just don't ask too many questions. I'm a little busy."
        Sb smile b "I won't."
        Sb normal b "Since that festival night, I've been thinking. What if you hadn't convinced me to watch the fireworks?"
        Sb "Maybe I would've been able to stop Reza before he got his hands on the generator."
        Sb disapproval b "Maverick would've been alive now."
        c "Reza had a gun, and he was good at sneaking around."
        c "He probably would've shot you before you even saw him."
        Sb drop b "True. He didn't have to worry about being heard. The fireworks would've concealed the sounds of gunshots."
        Sb "And he didn't hesitate to kill anyone in his way."
        Sb "If I hadn't gone to watch the fireworks, I'd probably have died that night."
        c "We'll never know."
        Sb normal b "Actually, I had those nightmares about being killed on that exact spot."
        Sb drop b "They looked so real, too. Even the fireworks were there."
        Sb normal b "But those dreams stopped once Reza's case was resolved."
        Sb "You might've saved my life. Thanks."
        c "And even though it was supposed to be the other way around, originally."
        c "Quite ironic, isn't it?"
        Sb smile b "I just think it's funny."
        
        nvl clear
        hide sebastian with dissolve
        $ renpy.pause (1.0)
        window show
        
        n "After checking several devices, I found the one with the medical and biological archives."
        n "Our scientists back home did great work assembling and organizing all the data."
        n "I couldn't help but feel guilty using their labor for my own goals. They did all this work in hopes to get the generators they... {i}we{/i} needed so badly."
        n "But now there was no way to help them."
        n "I decided that, after Anna would be cured, I would head back into the past and try to set things right."
        n "I only hoped she would understand my decision."
        
        window hide
        nvl clear
        window show
        
        n "Finding the needed information proved quite trivial with my knowledge of both biology and computers. The data for the cure was right there, and the methods of its production didn't look too complex for dragons to use."
        n "I copied all the required files on the portable data carrier and put the PDAs back into the proper storage container."
        
        window hide
        
        show sebastian normal b with dissolve
        Sb "What were you looking for?"
        menu:
            "It's something for the ministry.":
                $ renpy.pause (0.5)
                Sb smile b "If you don't want to tell the truth, it's fine."
                Sb "You have the official warrant, and that's all I care about."
                c "How did you..."
                Sb "I work in the police force. I can see when people aren't telling me the whole story."
            "I was looking for the medical data.":
                $ renpy.pause (0.5)
                Sb "Trying to save Anna?"
                c "Yes."
                c "How did you know?"
                Sb smile b "The time of your arrival indicates this is more of a personal visit rather than official business."
                Sb "On my first day guarding this room, I found a letter about a cancer treatment plan. Our medicine can't cure that."
                Sb "Naturally you've decided to use human knowledge archives, which are far more advanced than ours."
                Sb "So, your motives for accessing medical data are pretty obvious considering her predicament."
                c "Remind me to never play Poker with you."
                Sb normal b "What's Poker?"
                c "It's a human card game."
                Sb smile b "Actually, you should show me one day."
                c "Okay, but no playing for actual money. I don't want to end up broke."
                c "How about our next meeting?"
                Sb "Sounds good."
            "I'm afraid it's classified.":
                $ renpy.pause (0.5)
                Sb smile b "Is it?"
                c "Alright, maybe it's not, but I'd rather not tell."
                Sb "It's fine. I'm not here to interrogate you."
        
        c "It was nice to see you again, but I have to go."
        Sb normal b "It's getting dark outside."
        Sb smile b "Take care."
    
    else:
    
        m "Inside the facility room, I quickly located where PDAs were stored."
        m "After managing to access the computer, I found out that the dragons apparently had already developed a way to read and transfer data between our devices and theirs."
        m "It was just a matter of finding the right data."
        
        nvl clear
        $ renpy.pause (1.0)
        window show
        
        n "After checking several devices, I found the one with the medical and biological archives."
        n "Our scientists back home did great work assembling and organizing all the data."
        n "I couldn't help but feel guilty using their labor for my own goals. They did all this work in hopes to get the generators they... {i}we{/i} needed so badly."
        n "But now there was no way to help them."
        n "I decided that after Anna would be cured, I'd head back into the past and try to set things right."
        n "I only hoped she would understand my decision."
        
        window hide
        nvl clear
        window show
        
        n "Finding the needed information proved quite trivial with my knowledge of both biology and computers. The data for the cure was right there, and methods of its production didn't look too complex for dragons to use."
        n "I copied all the required files on the portable data carrier and put the PDAs back into the proper storage container."
        
        window hide
        $ renpy.pause (2.0)
    
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    play music "mx/anna3x.ogg"
    $ renpy.pause (2.0)
    window show
    n "Emera stuck true to her word. I don't know what she did, whom she called and what connections she had to use, but she had succeeded."
    n "On the very same evening, I got a call from the local hospital which confirmed that they were going to prepare a test batch of the cure."
    n "I was thankful that it didn't require any of the advanced industry only humanity had during pre-flare days, like nanomachines or cybernetics."
    n "It was just the right mix of advanced surgery methods and some organic medicine used to specifically hunt down and eradicate cancerous cells and carcinogenic agents. The substance was easy to synthesize when the recipe was known, but extremely hard to discover and get right during research."
    n "The doctors said it would be ready by tomorrow noon, but they'd need Anna's permission to perform the operation."
    n "I had no illusions and knew how risky it was to apply human medicine to a dragoness. That 10%% of genetic difference could be the decisive factor. Still, this way she had a chance."
    nvl clear
    window hide
    
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene testingroom with dissolveslow
    $ renpy.pause (2.0)
    
    show anna cry with dissolveslow
    c "I've got some news for you."
    An "Go ahead. I doubt it'll change a single thing."
    c "It just might."
    An disgust "Really now. Excuse me if my imminent death gets in the way of my excitement."
    c "Remember when I told you humans know how to cure cancer?"
    An sad "What good is that going to do? You can't smuggle me there, you can't ask them for it, you can't do anything."
    An face "The cure might as well not exist."
    c "Yesterday I paid a visit to the production facility and extracted the medical data from one of our PDAs."
    c "Your people now have that very cure."
    An rage "This isn't the time for your stupid jokes, [player_name]!"
    c "I'm not joking. Doctors are preparing for it as we speak, both medication and the equipment."
    c "They only need your permission to go through with it."
    An face "Do they really have to {i}ask{/i} if I want to be saved?"
    c "The cure is extremely experimental and unsafe. Truth be told, it's a direct copy of the human one with almost no changes to it. You are the first dragon they are going to try it on."
    c "So yes, they have to ask if you're alright with this experiment."
    An normal "How ironic. After all these years of research and doing tests on others, I've become a test subject myself for someone else."
    c "You said you enjoy all sorts of new experiences."
    An smirk "Maybe not this one specifically."
    c "It might be pretty scary indeed when I think about it."
    An face "I'm not afraid."
    An "What's the worst that can happen to me if it fails? Death? I'm going to die anyway."
    An normal "But with this cure, maybe, I won't have to."
    c "So, I take it that's a yes."
    An face "Of course it is."
    An normal "This is my chance, and I'm going to take it."
    c "I will go let the doctors know, then. They should be ready to begin soon."
    An sad "Wait."
    An "I don't know if I will ever see you again. This might be our last meeting."
    An cry "So could you tell me something?"
    c "Of course."
    An sad "Why?"
    c "Why what?"
    An "You never told me why you did all of this for me."
    m "I carefully took her thin hand into mine and gave it a gentle squeeze."
    c "Because I care."
    c "And because I want to see you well again."
    An "Some person you chose to save."
    c "Every life is worth saving, if I can help it."
    An normal "I can't even imagine how you managed to get all of this approved in one evening."
    c "I didn't."
    c "It's a long story for another time. I will tell you after the operation."
    An smirk "Optimistic to the end, aren't you?"
    c "Of course."
    
    nvl clear
    show annasick at Pan((300, 169), (0, 0), 12.0) with fade
    $ renpy.pause (4.0)
    m "As I turned to leave, she called out to me again."
    An "[player_name]."
    c "Yes?"
    $ renpy.pause (2.0)
    An "Thank you for putting up with me all this time. Whatever happens to me today, I will not forget you."
    $ renpy.pause (1.0)
    m "Words catching in my throat, I only managed a fragile smile before having to turn my face away."
    nvl clear
    scene black with dissolveslow
    
    $ renpy.pause (2.0)
    scene eckhospitalcorridor with dissolvemed
    
    m "Soon, a group of medical personnel took Anna to the surgery ward."
    m "I, on the other hand, was now stuck waiting in the corridor. The bench wasn't all too comfy, but it sure beat standing for hours."
    c "(Always making me wait and worry, aren't you, Anna?)"
    
    scene black with dissolvemed
    $ renpy.pause (0.5)
    scene eckhospitalcorridor with dissolvemed
    
    m "It was well into the evening when one of the doctors left the ward and headed towards me."
    m "His unreadable expression made my heart freeze. I tried my best to brace for the worst as he approached."
    m "My only comfort was the thought that, at least, I had tried."
    
    play sound "fx/steps/clean2.wav"
    $ renpy.pause (2.5)
    
    m "The doctor then smiled and said that Anna's prognosis had improved dramatically after the treatment."
    m "It would take some time to be sure, but from the initial observations, the cure was working. He admitted it baffled the whole medical community, how something from a different world could be so effective when applied to their biology as well. I knew exactly how, but they didn't have to."
    m "Anna needed rest after the operation, so I decided to go back to my apartment. A tiny bit of doubt and concern still lingered in my mind when I thought about possible complications, but my heart felt much lighter."
    
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene o4 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    play music "mx/clouds.ogg"
    $ renpy.pause (2.0)
    $ persistent.eckannacured = True
    m "The next morning started with a phone call from the ministry secretary."
    m "They requested my presence at the portal immediately. The tone of their voice, as well as the urgency, made me nervous. I wondered if they had found out what Izumi had done. Maybe it was time for them to know the truth."
    m "As I was about to leave, I found a small note sticking out from underneath my main door. It was scribbled in a hurry, but the handwriting looked eerily familiar."
    nvl clear
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/intrigue.ogg"
    m "{i}The rest is not up to you, [player_name]. Don't try to return to the past, or else you will die. Stay where you are; this is for your own good. You should be thankful you are still alive.{/i}"
    m "A threat? They knew about the time travel, they knew about the return coordinates Izumi had installed, and they knew that I wanted to go back somehow. It made no sense."
    m "Only one person alive besides me ever had a chance to overhear anything related to it. It was Anna, but she couldn't possibly have left the hospital ward. Izumi was confirmed dead by the investigation team on the day we stopped Reza."
    m "None of this connected in any way in my mind, yet it was not the time to analyze the note. I left it on the table for later and headed out."
    stop music fadeout 2.0
    scene black with dissolveslow
    play music "mx/movingon.ogg"
    $ renpy.pause (2.0)
    scene np1x with dissolveslow
    $ renpy.pause (2.0)
    
    m "There was a whole delegation waiting for me at the portal, and they seemed way too anxious, which further fueled my own concerns."
    m "Apparently there was a huge background investigation of the Reza incident that was going on for the last few months. As a part of it, they had recently inspected the portal and its terminal. Of course, they found out that human world coordinates were gone."
    m "What it meant for me and my status, in the end, remained to be seen, however."
    
    show emera normal b with dissolve
    Em "Good day, Ambassador [player_name]."
    c "Good day, Emera."
    Em frown b "I am afraid I have some terrible news. We are unable to reach your world anymore because the coordinates are gone."
    Em normal b "That means we won't be able to uphold our end of the deal until this problem has been solved. Yet, as you know, we don't possess the knowledge or means to do so."
    c "Does this mean I'm stuck there for the rest of my life?"
    Em frown b "I am afraid so."
    c "Can I see the portal's terminal?"
    Em normal b "I believe that would be all right."
    hide emera with dissolve
    nvl clear
    #add a pic with non-broken terminal? That's effort though.
    window show
    n "I wasn't surprised to find coordinates to the human world deleted. I already knew it was the case long ago, but something else shook me to the core."
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/intrigue.ogg"
    n "Someone had already used my full biometric data to travel back to the day of my arrival. Not only that, but Izumi had set up everything in a way to prevent repeated use. The moment that person went through, the system automatically deleted the coordinates, thus locking me out from using that path to try and fix everything."
    n "Now I was truly stuck in this timeline."
    n "But the only person who could've used those coordinates had to be me, unless they had a perfect copy of my eyes and fingerprints and knew how to use the biometric scanner."
    
    window hide
    nvl clear
    window show
    
    n "Was it me from another timeline? I remembered the note. The handwriting didn't just look familiar. It was mine, albeit heavily distorted."
    n "That meant what I saw before me wasn't the first timeline, and my other self had been around this whole time, watching from the shadows."
    n "There had to be a good reason why the other me never interfered or tried to prevent everything before Reza went rogue. So many questions were left, and so many answers I would never get. I could only be sure about one thing. My other self knew something I didn't, and acted on it."
    n "Eventually, I managed to access the logs out of pure curiosity. According to them, the portal had been used last night. What was... I waiting for this whole time?"
    window hide
    
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/clouds.ogg"
    show emera normal b with dissolve
    Em "Did you find anything?"
    c "No. I don't think I can fix this, either."
    Em "I see."
    Em ques b "Then I am afraid we will have to revoke your ambassador's status, [player_name]. There is no longer a way to contact your people, and one will most likely never be reestablished."
    c "I understand."
    Em "However, to recognize your service to our world, you are allowed to keep your apartment with everything in it and become a full citizen if you wish so."
    m "It was a much better offer than I expected. I thought I would be given a small room in some dorm and a strong motivational speech to find my place in this world."
    m "So it was a pleasant surprise to receive some real aid."
    c "I will take your offer. Thank you."
    Em normal b "Very well. You will be notified when your papers are ready. Before that, however, you will need to come with us to settle some formalities."
    hide emera with dissolve
    nvl clear
    
    $ renpy.pause (2.0)    
    scene black with dissolveslow
    window show
    
    n "Nothing could've prepared me for the amount of paperwork I faced that day. I had to visit cabinet after cabinet, fill up many different forms, some of which obviously weren't designed for a traveler from another world."
    n "It reminded me a lot of the paperwork our governments used to put people through. The solar flare had put an end to most of these practices, though."
    n "By the time I was finally finished, the life of a rightless hobo had started to look like a decent alternative to the bureaucratic nightmare I'd had to endure."
    
    window hide
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene testingroom with dissolveslow
    play music "mx/creamclouds.ogg"
    $ renpy.pause (2.0)
    
    m "In the evening, I was finally allowed to visit Anna. The doctors said that she was making a fine recovery, but that she was still weak and needed a lot of rest."
    m "When I walked in, she was staring at the window. For the very first time, I saw her smile genuinely."
    m "Most of the tubes and wires from before were now gone. Only several monitors remained active, keeping track of her condition."
    show anna normal with dissolve
    $ renpy.pause (2.0)
    An smirk "I see you weren't joking yesterday."
    c "How are you feeling?"
    An normal "A lot better now that I'm not going to die in a few days."
    An face "I will have to rethink a lot of things, however."
    c "For example how to treat others around you."
    An smirk "Not a chance."
    c "At least stop stealing cattle from that farmer maybe?"
    c "The poor old dragon doesn't deserve all that grief."
    An "You are as guilty as I am."
    c "No, no, no, you will not put this on me!"
    An "Or will I? You could've stopped me or reported me to the police, but you didn't. By all accounts, you are my accomplice."
    c "Alright, you win here."
    An "As always."
    c "Still, you could try to be slightly nicer to others."
    An normal "If they'll be nice to me, maybe I'll consider it, [player_name]."
    c "Now that's a first small step on the road to not being a total pain in the back."
    An smirk "Oh, shut up."
    c "Aaaannnnd it's gone. We're back to square one."
    An "Some things are just not meant to change, are they?"
    c "Not that I mind."
    An normal "I know."
    An "You did so much for me. You put up with me at my very worst on the night I broke down in front of you. And now you've saved my life."
    c "Don't mention it."
    An face "It's hard not to."
    An normal "If you won't stop being so nice, I might actually start to care."
    c "This is how I am. You'll get used to it."
    An smirk "But then I'll get used to you."
    c "What's wrong with that?"
    An "You don't have the slightest idea what you might be walking into, [player_name]."
    c "I just might. But can I ask you something more... personal?"
    An normal "Even if I said no, I have a feeling you'd continue anyway."
    c "That one night we had. Does it mean anything to you?"
    c "Or did it just happen in the heat of the moment?"
    An embarrassed "...A bit of both."
    An "I thought I was going to die in prison soon, alone and forgotten. So I wanted to get the most out of the time I had left before they'd arrest me."
    An normal "And then there was you. A bleeding heart and do-gooder who deserves someone as nice to be happy with. Yet for some unimaginable reason I still can't comprehend, you chose to hang around with me."
    c "To be honest, our first date was me just trying to get back at you for being rude. But as time went, I saw something in you, something really hard to fit into words. I couldn't leave you in such condition, either."
    An "I guess I was a little swept up in the emotions about you being so nice to me. Nobody else ever was, unless they wanted something."
    An sad "Didn't it occur to you that I don't deserve you? Most people only needed one meeting with me to stay away forever after."
    An "But not in your case. You kept coming back for more like an addict and followed my every whim, when a more sensible person would've told me to sod off long ago."
    An smirk "You sure enjoy your torment, don't you?"
    c "It wasn't too bad, and I got to hang out with you."
    An normal "Don't lie to me. If the number of complaints you made during the tests told me anything, it was exactly as bad as I think it was."
    An face "You've made me feel bad for using you like that in my selfish interests. I hope you're proud of yourself, [player_name]."
    c "Those tests weren't just for your curiosity. Your life depended on that research."
    An rage "Stop it."
    An "You can't just brush off everything I've done to you like it was nothing."
    c "I can. What are you going to do about it?"
    An "..."
    An face "Your loss."
    c "Are you really that afraid to let anyone close to yourself?"
    c "Can't blame you though, considering how everyone you knew before either tried to use or sabotage you. Of course, you wouldn't trust people around you by this point, let alone an alien from another world."
    An sad "I'd rather not talk about that."
    c "Alright. I understand."
    An "Remember what I told you that night? That promise I made."
    c "Not really. We talked a lot."
    An face "I probably shouldn't remind you then."
    An smirk "But just because I'm feeling nice and alive today, I will."
    An normal "I said that if you'd cure me, I'd give you whatever you want."
    c "I thought it was a joke, or a local saying meaning that you really wanted to get it."
    c "You know that I'm helping you not because I want something from you, but because I care about you."
    An face "I wouldn't joke about something like that. It's my life we were talking about."
    An normal "So, what will it be? I won't say no to anything."
    c "I think it's a little too early to ask."
    c "You've just had an operation, and you need your rest, peace and quiet. I will think of something while you recover, I promise."
    An face "You're simply too nice for your own good."
    c "It's been working so far."
    An "That's the worst part."
    An normal "Fine, I will wait."
    An smirk "I can offer you a free bonus right now, though."
    $ renpy.pause (1.0)
    play sound "fx/kiss.wav"
    $ renpy.pause (1.0)
    m "Before I knew it, she caught me with a surprise kiss on the cheek."
    m "I could see it took her a lot of strength to lift her head and reach out to me, but in the end, she was smiling. And so was I."
    An "Don't get too used to handouts."
    c "I wouldn't dream of it. That bonus was pretty good, though."
    An "You shouldn't expect anything less from me."
    
    nvl clear
    scene black with dissolveslow
    $ renpy.pause (2.0)
    
    window show
    
    n "I spent the next few weeks by Anna's side, following closely her every step on the road to recovery."
    n "No longer having ambassador's status and funding, I had to make the starting money council gave me last as long as possible. That brought back all-too-familiar problems of managing my limited resources, albeit in a different shape compared to Earth."
    n "Buying all that fine healthy food for Anna to help her gain back her strength didn't help my budget, but I couldn't leave her to survive on hospital rations alone. They were sure nicer than ones back at home, but that was hardly a compliment."
    n "At least Adine shared a few recipes based on ramen. It never occurred to me how many different things you could cook out of it with the right ingredients."
    
    window hide
    nvl clear
    window show
    
    n "Soon, however, I was offered a position of lead PDA data analysis specialist at the production facility, and things started to look up. Thoughts of humanity's fate still haunted me every time I accessed the data archives, but now there was nothing I could do."
    n "I hoped that my other self would find a way to succeed where I had failed, and save the people back home."
    n "In the meantime, I was going to spend the rest of my life in this timeline, far away from the rest of my own kind. But, perhaps, it wasn't too bad."
    n "Especially compared to getting killed. Things must've been dire if I'd had to leave a message like that."
    
    window hide
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene eckwildlands2 with dissolveslow
    play music "mx/sleepingcity.ogg"
    $ renpy.pause (2.0)
    $ adinestatus = "good"
    $ annastatus = "good"
    m "On the day they released Anna from the hospital, I decided to take her for a walk in the green area near town."
    m "As we made our way through it, she didn't utter a single word. From the corner of my eye, I noticed how her gaze wandered over the surroundings as if she had just rediscovered them."
    m "Eventually, we settled on the soft grass under a tree. She leaned her side against mine with most of her weight, but remained unusually quiet."
    
    show anna normal with dissolve
    c "Are you alright?"
    An sad "I thought I would never see any of this again."
    An normal "Now I have a whole life ahead of me. The life I'm free to take on the way I see fit, free of disease or police persecution."
    An smirk "All thanks to you."
    c "It wasn't just me, actually. Adine got the idea where to find the cure, and Emera did all the bureaucratic heavy-lifting."
    An normal "I can't believe that minister was actually helpful for once."
    c "She's a lot different from what you might see at first glance."
    An sad "I didn't get that impression. All she cares about are popularity and approval ratings, like it's some stupid numbers game."
    c "Her main goal always was to help out the people."
    An "If you say so."
    An normal "And who's Adine?"
    c "She's the waitress in that café we went to on our first meeting."
    An disgust "She was helpful but irritating."
    c "Adine is actually a very nice person. She even looks after the hatchlings from the orphanage whenever she can, to help them feel better."
    An normal "How wonderful, another bleeding heart. Maybe you two should hook up."
    c "Like it or not, but she's the one who actually saved you."
    c "Adine thought of the cure being inside the PDA archives, something both you and I had missed."
    An "She's smarter than I expected."
    c "Maybe you could pay her a visit to say thanks?"
    An sad "Maybe I should. I'm not used to people helping me just for the heck of it."
    c "Both Adine and Emera provided their help freely. Neither of them asked for anything in return."
    An disgust "I'm sure Emera had her ulterior motives. She always does."
    c "Getting that cure done was almost certain political suicide, if not a borderline crime, yet she agreed. You have to give her at least some credit."
    An sad "I've had too much bad blood with the council."
    c "Write her a letter of gratitude or something. It doesn't have to be anything huge."
    An normal "You're asking me to stop hating too many people at once, [player_name]."
    c "You can't honestly hate everyone, can you?"
    An smirk "I don't hate you."
    c "But maybe it's time to expand that circle of trust?"
    An normal "Maybe it is. If only a little."
    An smirk "Now, what would you want from me for the cure?"
    c "I told you, I didn't do it because I wanted something from you."
    c "You don't owe me anything."
    An normal "Please. Carry on with your kindness like this, and my blood will turn into sugar."
    c "And what do you expect me to ask for?"
    An face "You're not making this easy."
    An disgust "Do you expect me to lay out all the possibilities for you?"
    c "No, of course not."
    An "Good, else I would've called the whole deal off."
    c "So, how about another date?"
    An face "Just a date? You went through hell to save my life, and all you ask for is a date?"
    An "You could've demanded anything, and I mean it, but you just want to hang out?"
    c "Did you honestly think I'd want to exploit you like that? It would never sit right with me."
    An smirk "Deal, let's arrange another date. A sick leave might have its benefits."
    c "As long as you're not late this time."
    An "Also, no children's trivia games."
    c "Hey, I'm the one setting conditions here."
    An normal "You aren't going to win a rematch anyway, don't even try."
    c "We'll see about that."
    An smirk "You know, I might agree to play it again just to see that smug smirk gone from your face when you lose."
    c "Then it's challenge accepted."
    An "Confident, aren't you?"
    c "I would have never made it this far otherwise."
    An normal "You still haven't told me how you managed to push the cure production through in one evening."
    c "It wasn't something I could tell with so many people around."
    An smirk "Now this is getting interesting."
    c "I didn't push it through alone, however."
    An face "I already heard that part."
    c "I convinced Emera to use her position and connections to directly reach out to people in power to make an experimental batch just for you."
    c "Now, since it worked, they can accelerate the process of the official cure implementation. It'll save many lives."
    An smirk "Cunning."
    An normal "Yet the world will never know whom to thank for it."
    An smirk "So we're both criminals now. I have been pardoned, and you haven't been caught... yet."
    An "Though they can't do anything about you due to diplomatic immunity, can they?"
    c "I don't have it anymore. I've lost my ambassador status and everything with it, save for the apartment."
    An normal "Whom did you piss off this time? Did your guys get upset about you siding with us and getting in the way of that murderous prick?"
    An sad "That would explain why you couldn't smuggle me out to your world to cure me."
    c "I didn't annoy anyone. Your council had a huge investigation going on Reza's case for the last few months. Eventually, they studied the portal and found out that the human world coordinates are gone."
    An ntdespair "Gone?!" with hpunch
    c "That other human, Izumi, deleted them."
    An disgust "Didn't that idiot realize the consequences?!"
    c "She realized them all too well. Possibly better than you or me. It was the only way to reliably prevent Reza from escaping with the generator we needed to divert the comet."
    c "What she didn't expect was to die."
    An sad "Which locked you out from your home, and me from my cure."
    c "Yes. There's no chance that the connection will ever be reestablished."
    An "So you're forever stuck in this world, and council took away your ambassador status."
    An disgust "They're as lovely as ever."
    c "They gave me citizenship and allowed me to keep the apartment. It's better than I expected."
    An normal "Now they can convict you if the whole story about the power abuse surfaces somehow."
    c "I just asked for help. I didn't resort to bribes or blackmail. Last time I checked, asking for harmless things isn't illegal."
    An smirk "You're pretty good at covering your tail and finding loopholes, too."
    An normal "Is that a human trait?"
    c "Only some humans have it."
    An smirk "I'm lucky this one does."
    c "Either way, whether they convict me or not, I'm glad to still have you around, Anna. That's all that matters."
    An sad "Said no dragon ever."
    c "And now you're being a sourpuss again."
    An "You'll have to excuse me for speaking the truth."
    c "It doesn't have to stay that way."
    An "Give me a break. People dislike me, I dislike people, and this is how it's going to stay until the end of time."
    An "I'm sure even you will get fed up sooner or later and leave."
    c "Or, maybe, you and I could become something one day."
    An normal "What if we have already become something?"
    m "I placed my arm around her shoulders and pulled her a little closer."
    c "I'd like for that to be the case."
    An smirk "Of course you would."
    c "Wouldn't you?"
    An sad "It's a big commitment, and I can't let anything hold me back. The work I do is far too important for our whole civilization to let personal affairs get in the way."
    c "I see."
    c "We could still be friends."
    An normal "However, it wasn't my work which saved me."
    An "You did."
    An smirk "So having someone who cares really has a lot of unexpected benefits. It might just be worth all the added trouble."
    c "It is, trust me."
    An normal "When I get back to work, I'll see about fitting you somewhere in the schedule if you want." 
    c "That would be nice, especially if not just during breaks."
    c "So, once you've fully recovered, I assume you're going to tackle new important research?"
    An "Naturally."
    An "My talents have gone unused for far too long already."
    c "Just... don't be so crazy and zealous about it."
    An smirk "But that's the most fun part."
    c "Remember what I told you about the work-life balance and burning out. You need to look after yourself."
    An "Work-what balance?"
    c "Anna!"
    An face "You're pretty dense sometimes. It was a joke."
    An normal "I've learned my lesson that staying at work for days might kill you."
    An "In Damion's case literally."
    An disgust "I won't miss that selfish piece of shit."
    c "I wish nobody had to die."
    c "But I'm glad it at least wasn't you."
    An normal "I'm glad, too."
    An sad "It makes me uncomfortable when I realize how many times I've dodged death in the last few months."
    An "First Reza raided my lab, then we had to fight the prick in that facility, then the comet nearly caused a global extinction event, and finally, cancer almost finished me off."
    An normal "Yet here I am, still given a chance, one I'm not sure I deserve."
    c "I guess the universe really likes you."
    An "Or, maybe, a certain someone was always there to save me."
    An smirk "Except for the fight against Reza. I totally saved your sorry ass from getting shot while you were fumbling about."
    c "You did. If not for you, we wouldn't have been here today."
    An normal "I could say the same to you. I still owe you so much, you big, kind wuss."
    c "But I'm happy with what I've already got."
    An sad "You didn't get anything out of helping me but endless trouble, and possible conviction if they'll find out about your {i}diplomacy{/i}."
    c "I did."
    An "Then what is it?"
    c "Not everything is about favors or benefits. Sometimes it just feels good to do the right thing, especially for the person you've grown to care about. You don't expect anything in return. Their happiness and well-being are their own rewards."
    An sad "I felt the same way when I tackled you out of harm's way when Reza nearly shot us. I didn't think about what was in it for me. I just couldn't let you get hurt or killed."
    An "Heck, I was ready to shield you from the bullets with my own body without a second thought."
    An "Is this how caring for someone feels like?"
    c "Yes. It is."
    c "I would've done the same for you."
    An smirk "I never doubted that."
    An normal "But, now that the ordeal we had to go through finally seems to be over, I was wondering something. I want you to be certain and completely honest with me."
    An "Promise you'll stay with me?"
    menu:
        " I... I can't be certain of how things will turn out. But I'll try.":
            show anna sad with dissolve
            stop music fadeout 2.0
            $ renpy.pause (2.0)
            play music "mx/fragments.ogg"
            $ annastatus = "abandoned"
            An "Even after enduring so much together, you can't be sure about us in the end. My doubts were right all along."
            An "You'll get fed up with my attitude eventually, and we both know it."
            c "It's not like that!"
            An cry "I know exactly how it is. I've been through it already. It will start sweet but turn bitter in a blink of an eye."
            An sad "Let's not wait until some stupid drama happens between us, and part while we're still on good terms."
            c "I understand, but..."
            An "Like always."
            c "I... Don't you at least want to hang around sometimes?"
            An cry "You wouldn't want to have anything to do with me soon enough anyway. Let this memory remain untainted and keep it as something light and warm we both can come back to and remember in our darker times."
            m "Anna slowly got up from the ground and started walking away. Her steps were slow and labored."
            show anna at Position (xpos = 0.4) with ease
            $ renpy.pause (0.1)
            show anna at Position (xpos = 0.3) with ease
            $ renpy.pause (0.1)
            show anna at Position (xpos = 0.2) with ease
            $ renpy.pause (0.1)
            show anna at Position (xpos = 0.1) with ease
            $ renpy.pause (0.1)
            m "For a moment, she stopped and looked back."
            An sad flip "Thanks again for saving my sad life. Now I need to find out what to do with it."
            show anna sad
            $ renpy.pause (1.5)
            nvl clear
            hide anna with easeoutleft
            
            m "Soon, she disappeared, leaving me all alone in the grass under the darkening cloudy sky."
            m "I couldn't help but feel like I'd just lost something... someone very important. And now there would be no going back."
            
            menu:
                "Follow Anna.":
                    jump eck_anna_heartbreak
                "Give up.":
                    pass
            
            stop music fadeout (2.0)
            $ renpy.pause (2.0)
            scene black with dissolveslow
            
            $ persistent.eckannaendingseeng = "G"
            show eckannaendingseenimgg with dissolveslow
            $ renpy.pause (1.5)
            hide eckannaendingseenimgg with dissolveslow
            play sound "fx/system.wav"
            s "Looks like you've got a neutral good ending. You've saved Anna's life but broken her heart."
            s "I'm sure she'll be fine. Or will she?"
            s "It's all up to your interpretation, really. \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
            $ renpy.pause (2.0)
            jump eck_anna_customcredits
            
        "Promise. No matter what.":
            pass
            
    c "I'd be glad to."
    An smirk "Thank you, [player_name]."
    An normal "I got used to having you after all."
    c "I got used to you too, Anna."
    $ save_name = _("Anna 6A Main")
    nvl clear
    
    $ renpy.pause (2.0)
    show eckclouds at Pan((150, 50), (0, 0), 12.0) with fade
    $ renpy.pause (5.0)
    m "Too occupied with our talk, we had completely lost track of time. The sun had almost completely set, and the lamp posts started to light up for the night. It was getting late."
    m "A chilly gust of the evening wind made me shiver. My clothes were never meant for anything but warm summer days. Thick, heavy clouds moving in closer from the darkening horizon marked the quick approach of a storm."
    m "We had to hurry if we were to avoid getting soaked by the rain."
    nvl clear
    scene eckwildlands3 with dissolveslow
    show anna normal with dissolve
    c "Looks like a storm's coming. Let's get you back home before the rain starts."
    An smirk "It's not a problem for my scales."
    c "It is a problem for me and my clothes, though. It can also be pretty chilly and windy, and you are still recovering. You don't want to catch a cold, do you?"
    An normal "Maybe they'll allow us to share the same ward?"
    c "That's not how I envisioned spending time with you, though."
    An "Same. I'm not returning to that hospital."
    An "Let's go."
    c "So, where do you live?"
    An face "..."
    An sad "Doesn't matter."
    c "Why so? Is everything alright?"
    An sad "I'm fine. But my apartment is a mess right now. You know, I haven't been there for weeks, and I'm in no mood or condition to clean it up."
    c "Don't you have someone else cleaning it up for you?"
    An face "Janitor services don't work at this hour."
    c "Oh, right."
    An normal "Mind if we go to your apartment instead?"
    c "Not at all. You're always welcome."
    
    window hide
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene eckkitchenx with dissolveslow
    play music "mx/campfire.ogg"
    $ renpy.pause (2.0)
    
    #Use rain for extra ambiance???
    #Eh, too loud and obnoxious. Also, it wasn't audible during Adine's 1st meeting.
    #Needs nicer kitchen for the background. Done. Kinda.
    
    m "By the time we made it to my apartment, it was an early night. We barely avoided the rain, as the first drops had started to fall moments before we reached the main door."
    m "With hunger nipping at my stomach for the last hour, I figured Anna wouldn't mind some late dinner either."
    m "I led her to the kitchen and gestured for her to sit at the table while I dug through the fridge."
    m "Thankfully, I still had a supply of bacon and meat snacks from the day of shopping before. Together with some bread and berry juice, it made for a dinner as fine as it could get given the circumstances."
    
    c "(I wonder where they get bacon from? I don't think pigs exist around here.)"
    c "(It's probably not the best time to ask such questions.)"
    
    show anna normal with dissolve
    c "I don't have much to offer, but..."
    An "I'll take it. It's my second favorite type of food, you know."
    c "And what type is it exactly?"
    An smirk "Free food."
    c "Just leave some for me."
    An "Of course. But this time I get to pick first."
    c "Want some coffee or anything else?"
    An normal "This will suffice. Coffee is good for when I need to keep on going while at work."
    An "Right now I'd just love to get some sleep in a place that doesn't reek of medicine and sanitizers."
    An sad "And doesn't remind me of death, disease and all those other wonderful things associated with hospitals."
    c "Then you're at the right place."
    An smirk "I know."
    
    m "I sat down on the other chair in front of my plate. Surprisingly, Anna had left me a sizable portion I wasn't sure I could take on. It was alright for a dragon, but a human stomach could never accommodate all of that."
    
    An normal "What? You asked me to leave you some. I did."
    An "And I remembered that you humans have to stuff your face every few hours, so you must be starving by now."
    An smirk "See? I can be nice and considerate too, if I want."
    c "Thanks. But this is a bit too much."
    An face "It's always either too little, too much, too hot, too cold and so on. You're impossible."
    c "Coming from you of all people."
    An smirk "Alright, you win this round. Now help yourself."
    
    nvl clear
    
    m "When Anna was done with her food, I had barely managed to overcome a third of my portion. Not willing to let it go to waste, I stuffed the rest back into the fridge."
    #Try to find an actual bedroom background? I haven't seen one anywhere though...
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    $ annascenesfinished = 5
    m "I helped Anna settle onto my bed and under the blanket. She wasn't at her full strength yet, as much as she didn't want to admit it. I was about to head out to make my own sleeping place on the couch, but she called out to me."
    
    show anna normal with dissolveslow
    An "Where do you think you're going?"
    c "To the living room. I will sleep on the couch for the night, since you've taken my bed."
    An "It's big enough for us both. Why don't you join me?"
    An sad "I don't want to sleep alone tonight."
    $ eckannahbrecoverpath = False
    #The choice if you want to be together or remain friends.
    menu:
        "Decline.":
            c "Wouldn't it be too awkward?"
            An face "Because we haven't gone much further already in the past, have we?"
            c "It was a heat-of-the-moment thing. You said so yourself."
            c "Now we don't have to rush things."
            An "Fine. What a prude."
            An sleep "Go enjoy your cold, lonely, uncomfortable couch then."
            c "Good night."
            An "Yeah, sweet dreams and whatever."
            nvl clear
            hide anna with dissolve
            
            m "She turned away to face the wall marking the end of our conversation for today."
            $ renpy.pause (1.0)
            scene o3 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
            $ renpy.pause (1.0)
            m "Without taking my clothes off, I settled on the soft couch and tossed a thin fabric blanket over myself."
            m "As I lay there, staring at the window, I couldn't help but wonder what awaited us in the future."
            m "I was confident that my other self would succeed in saving the humanity, but that was for another timeline. In a way, I was thankful that I had to stay here. The part of me that wanted a quiet life was happy."
            m "For the first time in many months, I felt at peace."
            stop music fadeout (2.0)
            $ renpy.pause (2.0)
            scene black with dissolveslow
            
            $ persistent.eckannaendingseenh = "H"
            show eckannaendingseenimgh with dissolveslow
            $ renpy.pause (1.5)
            hide eckannaendingseenimgh with dissolveslow
            
            play sound "fx/system.wav"
            s "You've got a friend(zone) ending! Congratulations? And I may or may not have coded that it's the only ending you can't reload after because there's no escape from the friendzone."
            s "Just kidding. Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
            $ renpy.pause (2.0)
            jump eck_anna_customcredits
            
        "Accept.":
            c "To be honest..."
            c "Neither do I."
            An smirk "Don't get any stupid ideas."
            An normal "I'm too worn out and tired for anything frisky. Maybe some other day."
            c "That's not what I was thinking about!"
            An smirk "Yes you were. Don't lie to me."
            An "Your face is all burning red."
            c "So is yours."
            An face "..."
            c "Wait, that sounded wrong."
            c "I didn't mean to say that..."
            An "Just get over here and I'll pretend you didn't say that."
            
            play sound "fx/undress.ogg"
            $ renpy.pause (1.0)
            nvl clear
            scene o3 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
                
            m "I took off my daily clothing and carefully settled into my bed next to Anna. It was big enough for us both in theory, but in practice, we ended up inches away from each other. It was a gap she didn't hesitate to close to press her softer underbelly into my side."
            m "I tried to turn away to make it less awkward for us both, but she would have none of it. Anna pulled and turned me towards herself, and kept me in place by the shoulders with both of her arms."
            m "She poked her nose into my upper chest, creating a hot spot with her breath, and shut her eyes."
            
            #Add some interaction dialogue here? Done.
            show anna sleep with dissolve
            An "Now you're all mine."
            An slsmirk "Mmmm, you produce a lot of body heat. Would be a shame to let it go to waste."
            c "I thought you said no frisky stuff."
            An "Do you see anything happening? I don't. Now shush."
            $ renpy.pause (2.0)
            show anna sleep with dissolve
            $ renpy.pause (1.0)
            An "I have to admit that, for someone so wussy and poorly fit for the wilderness, you're very cuddly."
            c "I guess you could add that to the list of things humans are better at."
            An slsmirk "I'll let you have this one."
            An "The overall score is still in our favor though."
            c "Just you wait. I might still surprise you."
            An sleep "We'll see."
            menu:
                "Scratch behind her frills":
                    m "With a mischievous grin, I reached out my free hand and started gently scratching the area between her horns and frills."
                    play sound "fx/purr.ogg"
                    m "I was rewarded by a purring sound, not unlike one of a very large cat. Her claws dug deeper into my skin, but thankfully not enough to hurt."
                    An slsmirk "I promise... if you tell anyone about this, I'll kill you."
                    c "Looks like I've found your weakness."
                    An sleep "You know, these sensitive spots are considered rather intimate among dragons."
                    c "Should I stop then?"
                    An "Did I tell you to?"
                    c "Good point."
                    m "For a couple more minutes, I silently continued with the scratching, until I felt drowsiness start to take over my mind."
                    m "I stopped my motions and looked down, resting my chin on her forehead."
                    c "Sleep well, Anna."
                    An "You too, [player_name]."
                    stop sound fadeout 2.5
                    hide anna with dissolve
                    nvl clear
                    m "Soon her breathing slowed down, and the purring stopped."
                    m "Face to face with the now peacefully smiling sleeping dragoness, I couldn't help but wonder what awaited us in the future."
                    m "I was confident that my other self would succeed in saving the humanity, but that was for another timeline. In a way, I was thankful that I had to stay here. The part of me that wanted a quiet life was happy."
                    m "Softly, I moved my hand away from Anna's head and placed it on her shoulder. For the first time in many months, I felt at peace."
                    stop music fadeout (2.0)
                    $ renpy.pause (2.0)
                    scene black with dissolveslow
                    
                    $ persistent.eckannaendingseena = "A"
                    show eckannaendingseenimga with dissolveslow
                    $ renpy.pause (1.5)
                    hide eckannaendingseenimga with dissolveslow
                    
                    play sound "fx/system.wav"
                    s "You've got the happy good ending and made Anna purr. Congratulations!"
                    if persistent.trueending == True:
                        s "Looks like you've already seen the true ending of the game. Would you like to explore this storyline further? \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
                        menu:
                            "Yes.":
                                jump eck_anna_amelyarc
                            "That would be enough reading, thanks.":
                                pass
                    else:
                        s "Just a reminder. You still have the humanity to save in another timeline, so don't let up yet. Though, those are the problems for \"the other you\" to solve. \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
                    
                    $ renpy.pause (2.0)
                    
                "Try to get some rest.":
                    m "I looked down, resting my chin on her forehead."
                    c "Sleep well, Anna."
                    An "You too, [player_name]."
                    hide anna with dissolve
                    nvl clear
                    m "Face to face with the now peacefully sleeping dragoness, I couldn't help but wonder what awaited us in the future."
                    m "I was confident that my other self would succeed in saving the humanity, but that was for another timeline. In a way, I was thankful that I had to stay here. The part of me that wanted a quiet life was happy."
                    m "Softly, I placed my hand on Anna's shoulder. For the first time in many months, I felt at peace."
                    stop music fadeout (2.0)
                    $ renpy.pause (2.0)
                    scene black with dissolveslow
                    
                    $ persistent.eckannaendingseena = "A"
                    show eckannaendingseenimga with dissolveslow
                    $ renpy.pause (1.5)
                    hide eckannaendingseenimga with dissolveslow
                    play sound "fx/system.wav"
                    s "You've got the happy good ending. Congratulations!"
                    if persistent.trueending == True:
                        s "Looks like you've already seen the true ending of the game. Would you like to explore this storyline further? \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
                        menu:
                            "Yes.":
                                jump eck_anna_amelyarc
                            "That would be enough reading, thanks.":
                                pass
                    else:
                        s "Just a reminder. You still have the humanity to save in another timeline, so don't let up yet. Though, those are the problems for \"the other you\" to solve. \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
                    
                    $ renpy.pause (2.0)
                    
            jump eck_anna_customcredits
                    
#   Hey again.
#   
#   Well, this is it for now. What will the future hold for [player_name] and Anna?
#   Who knows.
#   I might expand this mod later to include Amely's storyline + cover the heartbreak route better with a chance for recovery.
#   But that's for version 2.0, should it ever be made.
#
#   2.0 below this point.
# -----------------------------------------------------------------------------
# label eck_annasheartbreak_bak
#   m "I wasn't going to let her just walk away like that."
#   m "It was a huge misunderstanding between us, and I was determined to set things right."
#   m "A big part of me was also afraid for her safety. Anna was still very weak after the treatments. Going out all alone could be dangerous for her."
#   $ renpy.pause (2.0)
#   show anna cry with dissolvemed
#   m "It didn't take long for me to catch up with the weary dragoness. I quickly blocked her way urging her to stop."
#   An "What do you want from me?"
#   c "I wanted to apologize. I didn't mean to say that I will leave you, I don't know what I was thinking when I told you all that."
#   c "Please. Don't go."
#   An sad "We both know the truth, [player_name]. You will grow tired of me sooner or later, or my work will tear us apart."
#   An "This was never meant to last."
#   c "We've been through so much together. Do you want to just give up now?"
#   An disgust "Better now, then wait for you to get fed up, cause a massive stupid drama and leave."
#   An cry "You see how I am. Always assuming the worst about everyone around me."
#   An sad "Yet you want me to stay."
#   m "I placed my hand onto her upper chest and tried to give her a smile."
#   c "I want you to be happy, Anna."
#   An normal "How noble of you..."
#   m "Suddenly, I felt her muscles under my touch go limp."
#   # insert falling Anna
#   # insert body falling sound
#   # pan down
#   show anna slsad with dissolve
#   c "(She must have overstressed herself and collapsed. It is all my fault.)"
#   m "I sat down next to Anna and gently craddled her head on my lap. There was nothing I could do but wait for her to wake up."
#
#   nvl clear
#   
#   $ renpy.pause (2.0)
#   show eckclouds at Pan((150, 50), (0, 0), 12.0) with fade
#   $ renpy.pause (5.0)
#   m "Too occupied with my thoughts and worries, I had completely lost track of time. The sun had almost completely set, and the lamp posts started to light up for the night. It was getting late."
#   m "A chilly gust of the evening wind made me shiver. My clothes were never meant for anything but warm summer days. Thick, heavy clouds moving in closer from the darkening horizon marked the quick approach of a storm."
#   m "Far away from home, and with unconscious Anna in my arms, I was certain we'd get soaked by the rain."
#   nvl clear
#   
#   scene eckwildlands3 with dissolveslow
#   
#   show anna slsad with dissolve
#   An normal "What are you doing?"
#   c "Oh, good, you are awake."
#   An sad "I lost conscious, didn't I? Again, you get to see me at my worst."
#   c "It's alright. How are you feeling?"
#   An "Weak and stupid."
#
#   Nope, doesn't work. I don't like the tone, and the story is going nowhere. Gonna keep it here for anyone curious enough to datamine.
#   Also hey there, S3lvah! Please don't proofread the commented-out code and lines, they aren't worth it. Just saying.
#
#   Heartbreak/mend arc original plan:
#   1. Choice to sit there like a doofus or actually try to go after her.
#   2. Giving chace will not yeld any results at first (raptor lady is likely much faster anyway).
#   3. Remember her home address from the papers MC had seen in the hospital? Or be a creep and follow her. That's cool, too.
#   4. Get soaked while going there. *Insert thoughts about cheap symbolism of avoiding the very same rain in non-heartbreak path.*
#   5. Anna's door isn't locked. (ALL the implications.)
#   6. See Anna sprawled on her bed crying. A bottle of alcohol is nearby but not touched yet. Booze and medicine... yeah.
#   7. %scenes with options% (Use scoring system? Done.)
#   8. Outcomes:
#       - Failure (Anna casts MC away, her further fate unknown).
#       - Limited success (MC convinces her that they could still be friends and she's not alone.) Actually, no. At that point it's now or never.
#       - Success (Romance alt ending).
#   
#   
#   
#   Amely arc orignal plan (Romance endings only):
#   0. It should be optional.
#   1. Going to Adine together to thank her.
#   2. Meet Amely there.
#   3. Uncomfortable Anna causes suspicion. MC presses on.
#   4. Confession but no details about Amelia/Remy.
#   5. Option to adopt Amely.
#
#   I have no idea how to properly write children! At least dragon hatchlings aren't very talkative, and this is a VN.
#

label eck_anna_heartbreak:
    # Aka "Backgrounds Gallery: The Game". Scenery porn anyone?
    m "After all the trouble and hardship we'd been through, letting such a misunderstanding ruin everything between us was not an option. Determined to set things right, I quickly headed in the direction Anna took."
    m "A big part of me was also greatly concerned about her safety. She was still frail after the treatments, and being all alone could be dangerous for her, especially when under heavy stress."
    play soundloop "fx/steps/rough_gravel.wav"
    scene eckduskforest at Pan ((0, 360), (0,0), 8.0) with dissolveslow
    $ save_name = _("Anna 6B Heartbreak")
    m "Using her footprints on the soft dirt path, I managed to track and find her, but chose to stay a certain distance away and undetected. Anna never looked back or to the sides, though. A couple of times she stumbled over the tree roots sticking out from the ground but quickly regained her balance."
    scene eckdusktownroad at Pan((0, 220), (0, 220), 0.0) with dissolveslow
    m "I knew she felt terrible at that moment, and I wanted to rush in to comfort her, but I couldn't risk slipping and saying something stupid again. I had to be careful now and plan my approach properly."
    scene eckdarkpathway with dissolveslow

    $ renpy.pause (2.0)
    show eckclouds at Pan((150, 50), (0, 0), 12.0) with fade
    $ renpy.pause (3.0)
    m "Too distracted by keeping track of the dragoness, I didn't notice thick, heavy clouds taking over the evening sky, bringing with them an earlier starless night. Freezing cold heavy rain soon started, making me instantly regret my light clothing choices."
    stop soundloop fadeout 2.0
    $ renpy.pause (2.0)
    play soundloop "fx/eckrainloop.ogg"
    m "In a matter of seconds, I was completely soaked from head to toe, and gusts of strong chilling wind only made matters worse. For a time, I wondered if I was facing an actual risk of hypothermia."
    nvl clear
    hide eckclouds with fade
    $ renpy.pause (2.0)
    $ eckannahomeexploration1 = True
    $ eckannahomeexploration2 = True
    $ eckannahomeexploration3 = True
    
    scene eckannahouse at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    m "Eventually, Anna entered a blocky two-story concrete building. Despite the risk of catching a cold, I waited for a few minutes under a large tree before walking up to the front door. I was about to ring the bell when I noticed that the door wasn't locked."
    play sound "fx/door/handle.wav"
    scene eckannalivingroom at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    m "I walked inside without delay, happy to finally get away from the ugly weather. Now I had to find her to explain myself. I only hoped that she'd understand."
    stop music fadeout (2.0)
    stop soundloop fadeout 2.0
    $ renpy.pause (1.5)
    play sound "fx/door/door_close.ogg"
    $ renpy.pause (1.5)
    play music "mx/clocks.ogg"
    jump eck_anna_homeexploration
    
label eck_anna_homeexploration:
    scene eckannalivingroom at Pan((0, 250), (0, 250), 0.0) with dissolve
    menu:
        "Look around the living room." if eckannahomeexploration1:
            m "Tidy and spacious, if somewhat dusty, the living room had its cozy charm. I spotted a couple of books on the sofa. Their titles were a little too specific even for my level of knowledge, but it was something about stem cells."
            m "In the far corner stood a large shelf filled to the brim with assorted trophies, framed diplomas and other prizes of all shapes and colors. A thick layer of grey dust covered most surfaces. I even spotted a cobweb with a mean-looking spider in it."
            c "(Huh, she didn't exaggerate when she described the number of awards she'd won.)"
            $ eckannahomeexploration1 = False
            jump eck_anna_homeexploration
        "Search the bathroom." if eckannahomeexploration2:
            play sound "fx/door/handle.wav"
            scene eckannabath with dissolvemed
            m "Anna's bathroom was unsurprisingly average-sized, with sleek, simplistic furniture and fixtures. It actually reminded me a lot of my own, but in red."
            m "Stored in a wall cabinet were medical supplies, but out of all the pills I only recognized painkillers."
            c "(No trace of her, though.)"
            c "(It's probably for the best. I can't imagine how awkward it would've been to bump into her there of all places.)"
            $ eckannahomeexploration2 = False
            scene black with dissolve
            $ renpy.pause (2.0)
            jump eck_anna_homeexploration
        "Search the kitchen." if eckannahomeexploration3:
            play sound "fx/door/handle.wav"
            scene eckkitchenx2 with dissolvemed
            m "The kitchen had all the necessary furniture and equipment. However, most of it was in pristine new condition, showing that it was rarely used. The only exception was the coffee machine."
            c "(Looks like she's not a big fan of cooking at home.)"
            m "Considering how long she had been away from home, I decided against checking what was inside the fridge."
            $ eckannahomeexploration3 = False
            scene black with dissolve
            $ renpy.pause (2.0)
            jump eck_anna_homeexploration
        "Search the bedroom.":
            # bedroom bg
            m "Upon approaching the bedroom, I heard quiet sobs coming from behind the door. As quietly as I could, I entered the room."
            scene eckannabedroom with dissolvemed
            play sound "fx/door/handle.wav"
            jump eck_anna_confrontation
        "Leave.":
            $ renpy.pause (2.0)
            play sound "fx/door/handle.wav"
            jump eck_anna_heartbreakfailure
            
label eck_anna_confrontation:
    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    play music "mx/prophecy.ogg"
    $ anna5mood = 0
    scene eckannabedroom with dissolvemed
    show anna cryface with dissolve
    m "I found Anna sprawled over her bed, shaking with every sob she let out. Next to her on a bedside table stood a bottle of alcohol, opened but not yet touched."
    m "The moment I closed the door behind myself, however, she sharply turned her head to face me."
    play sound "fx/door/door_close.ogg"
    An disgust "How did you find my home? What are you doing here?"
    An cry "Did you follow me all the way to my apartment through the rain, you doofus? You're all soaked."
    c "Yes, I did. I couldn't leave you all alone, not like this."
    An sad "You'll catch a cold or worse, and I'll feel even more awful knowing it was all because of me."
    c "I'll be fine. It's pretty warm here."
    An "Don't lie to me. You're shivering."
    c "We can worry about my health later. Yours is far more important right now."
    An "How so?"
    c "The doctors agreed to release you only because I promised to look after you. It's not safe for you to be alone right now."
    An disgust "What do they know? I can take care of myself."
    An sad "I don't need anyone babysitting me like a hatchling."
    c "But what if you'll collapse or suddenly feel worse in some other way? Someone has to be there to help you."
    
    if persistent.remygoodending == False:
        c "I hate to think of the worst scenarios, but I'd rather make sure you are safe."
        
    else:
        m "A memory of hearing of Amelia's fate flashed before my eyes. The prospect of such a thing happening to Anna horrified me to the core."
        c "I'd never forgive myself if something terrible were to happen to you because I wasn't by your side when you needed it most."
        
    An face "You're just looking for an excuse to stay."
    c "I'm worried about you and your well-being."
    c "I also want to apologize for hurting you. Please, give me another chance."
    An cry "It's not about chances, [player_name]. For what you did for me, I'd be ready to overlook and forgive any stupid mistakes you can think of."
    c "Then what is it about?"
    An sad "It's about our future."
    An "Do you want to wait until everything blows up over something dumb like today, and we both walk away hating each other's guts for the rest of our lives?"
    An "If we're lucky, our work would consume us whole before that happens, and make us slowly drift apart until whatever we share would turn into indifference."
    An cry "This stupid affair of ours was never meant to last, anyway."
    menu:
        "Maybe... maybe you're right, Anna.":
            An disgust "Then why are you even here? To state the obvious?"
            jump eck_anna_heartbreakfailure
            
        "But we can make it last now.":
            $ anna5mood +=1
            c "We'll never find out if we won't try, and sadly, misunderstandings are often inevitable."
            c "But we've defeated your cancer, you don't have to worry about the police, and I'm not going to go back to the human world."
            c "We're free, Anna. Nothing stands in our way anymore."
            show anna sad with dissolve
            c "I understand that I messed up today. I didn't want to give you a reason to doubt us. I was just a little lost at how sudden and personal your question was."
            An "Whatever you say."
            c "No, really! I mean it."
            An "I know. But what you've said is true. You can't promise to tolerate me forever, and I will never change."
            An "This is who I am, [player_name]."
            c "And that is whom I grew to care about."
            
        "We can just be friends and still support each other.":
            c "It doesn't have to be an affair. I'd be glad to stay as your close friend."
            An sad "And then it would just take longer for you to drift away. Maybe it won't be as volatile when things go south, either."
            An "But, in the end, it would make no difference."
            
    An cry "You're so very naïve if you truly believe this would work. I was just like you once, thinking I could change things for the better, until the world taught me how everything really works."
    c "Maybe I'm being idealistic, but it's not about the world anymore. It's about the two of us."
    An sad "That hardly changes a thing."
    menu:
        "No. It changes everything.":
            $ anna5mood +=1
            c "We're the only ones who will decide how and where things will go now."
            c "I understand that you're afraid of getting hurt, and I just made it worse earlier today. I promise it won't happen again."
            An "You may say so now, but what will happen in a week or a month? How can you be so sure this whole affair won't come crashing down on us?"
            c "I can't predict the future, but I'll do my best."
            An "How wonderfully dramatic of you."
        "We have gone through so much together, yet you doubt me?":
            $ anna5mood -=1
            An disgust "You were the one who started this."
            An sad "Your uncertainty made me realize that if even a person like you can't tolerate me, what chances do I truly have?"
            c "I never said I can't tolerate you."
            An "You didn't have to state it openly. I understood exactly what you meant."
        "You might be right.":
            An cry "Then just go. You're only making everything harder than it has to be."
            jump eck_anna_heartbreakfailure
    
    c "I'm just asking you not to give up yet. There's still a way for us to fix this."
    An face "And what's the point? So that it could go to hell again later?"
    menu:
        "I'll be careful.":
            $ anna5mood -=1
            An disgust "I can see how well this worked out today."
            An cry "And if such small slip is enough to cause a rift between us, do you think it's even worth trying?"
            c "There's only one way to find out."
            An "I think we already did. It isn't."
        "I suppose it {i}is{/i} quite pointless...":
            An sad "See? Even you realize how futile this all is. Just go and don't look back."
            jump eck_anna_heartbreakfailure
        "You mean a lot to me.":
            $ anna5mood +=1
            c "I'll be completely honest with you. I don't have anyone else in this world. A few friends maybe, but nobody as close as you are to me."
            show anna sad with dissolve
            c "And if I lose you, I'll be all alone."
            An despair "Stop making it harder for me than it already is! Do you think I enjoy this?"
            An cry "In the end, parting now is something that should be done for both of our sakes, [player_name]. Once you look back at this in the future, you'll be thankful."
    
    c "But that won't make either of us feel any better. I can see that you don't want it to end here, and neither do I."
    An sad "You're way too stubborn for your own good."
    An cry "Go and find yourself another bleeding heart, someone nice and kind, who'll give you the care and happiness you deserve."
    An sad "No matter what you say, I can't give you any of those. Only drama, worries and endless problems to deal with. You'll be much better off if you keep your distance."
    An cry "Those people who warned you to stay away from me were right."
    m "Anna's head slumped listlessly onto her bed."
    show anna cryface with dissolve
    menu:
        "Stay where you are.":
            An "Just go. There's nothing left for you here to see, and I don't want to cry any more in front of you."
            jump eck_anna_heartbreakfailure
            
        "Sit down next to her.":
            m "Slowly, I walked up to the dragoness and sat down by her side."
            if anna5mood > 2:
                jump eck_anna_recoveryending
                
            elif anna5mood > 0:
                m "Reluctantly, she inched a little closer at first, but stopped half-way."
                An sad "I want to trust you, [player_name], but I can't."
                An cry "No matter how hard you'd try, those doubts will never go away."
                An sad "I appreciate everything you've done for me, and I will never forget it. But it would be best for us to go separate ways."
                m "I sighed."
                c "I guess some things are just never meant to be."
                An normal "Yeah. Don't worry about me. I'll be fine."
                An sad "I believe you'll find your happiness in this world as well. You're too much of a do-gooder to be alone for long."
                $ renpy.pause (2.0)
                c "Then... I guess this is goodbye, Anna."
                $ renpy.pause (2.0)
                An "Take care, [player_name]."
                jump eck_anna_heartbreakfailure
                
            else:
                An face "Don't bother trying to fix this mess, [player_name]."
                An sad "I'm grateful to you for saving my life. I'll never forget it. But you and I were never meant to become anything."
                m "I felt Anna shift as she used her strong hind legs to gently yet firmly push me away."
                An cry "Just go. You've already made it much harder for me than it had to be."
                c "Take care, Anna."
                An sad "Farewell, [player_name]."
                jump eck_anna_heartbreakfailure
                
        "Walk out and don't look back.":
            jump eck_anna_heartbreakfailure
            
            
label eck_anna_recoveryending:
    $ save_name = _("Anna 6B Recovery")
    c "But what about you? What's going to happen to you?"
    An "Don't concern yourself about it. I've been egoistic for long enough. Let me do something for someone else for once in my life."
    An "You won't care much anyway once you're gone."
    c "But I care right now. And I'm not abandoning you, no matter what."
    An face "You're so stubborn."
    c "This is who I am, Anna."
    $ annascenesfinished = 5
    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    play music "mx/eveningmelody.ogg"
    show anna slneutral with dissolve
    m "Reluctantly, she turned towards me and inched closer, shyly pressing against me."
    m "I placed my hand on her upper back and started stroking it in short gentle motions."
    show anna sleep with dissolve
    m "For a time we remained in complete silence. Anna's tensed up muscles slowly loosened and relaxed under my touch as she calmed down."
    $ annastatus = "good"
    $ renpy.pause (3.0)
    c "Anna, mind if I ask you something?"
    An "Yes?"
    $ renpy.pause (2.0)
    c "Can I..."
    $ renpy.pause (1.0)
    c "Can I stay with you?"
    $ renpy.pause (1.0)
    An normal "I'd love for you to stay."
    An smirk "I got used to having you after all, [player_name]."
    c "I got used to you too, Anna."
    $ renpy.pause (1.0)
    An normal "Maybe you and I have a chance after all."
    An sad "I feel so stupid right now. You've done so much for me, and I actually started to care, but then I nearly threw it all away over a damn response to a single stupid question I didn't even need to ask."
    c "It's my fault as well. It was important to you to get some reassurance, and I got confused and said something I shouldn't have."
    An normal "Looks like even a cunning ambassador like you can slip sometimes."
    c "Nobody's perfect. But we can learn from our mistakes and become better."
    An "Indeed, we can. You and I both."
    c "I hope all this stress didn't worsen your condition. Doctors said you need peace and quiet while you're recovering, but this whole situation was the exact opposite."
    An smirk "I'll be alright."
    m "She put her dainty hand on the wrist of my free arm and squeezed it."
    An sad "Promise me that if I ever try something dumb like that again, you'll stop me."
    c "I promise. I'll be there for you."
    
    $ renpy.pause (1.0)
    An normal "Thank you."
    $ renpy.pause (1.0)
    
    An "Your shirt is wet. You're still soaked."
    c "I told you, it's fine. Your apartment is warm enough."
    An smirk "No, that won't do."
    hide anna with dissolve
    play sound "fx/undress.ogg"
    m "Suddenly, she got off the bed and stood up face to face with me."
    show anna smirk with dissolve
    c "What are you doing?"
    An "Let's get those rags off you."
    c "Um, Anna, I don't think it's the best time for... {i}those{/i} kinds of activities."
    An face "That's not what I'm doing."
    An normal "We can't risk you getting sick, silly. The last thing I want right now is to worry about you dying from flu or pneumonia."
    An smirk "There's so much research and so many experiments you and I are yet to conduct, [player_name]. And now that you are a simple citizen, you're fair game without the need for council approval. You wouldn't say no to me, would you?"
    m "I gulped nervously."
    c "(I should've foreseen this.)"
    c "Um..."
    An face "The research part was just a joke, you wuss, no need to go pale."
    c "That's good to hear."
    An normal "Though, I'd love to study you some more and gather more data."
    An sad "But you don't owe me anything, and I don't expect you to agree to put up with that crap ever again."
    c "I wouldn't mind helping you and you only. Other scientists can complain all they want about the unfair competition."
    show anna normal with dissolve
    c "Maybe someday, we could run a few tests after the work hours if that won't get you into trouble with the law. We should double-check that before doing anything."
    An "I'd need a few weeks to fully recover and get off the sick list, too."
    An smirk "Speaking of which, you're still dressed up and soaked."
    c "And what am I supposed to do without clothes? I can't just walk around in my underwear."
    An "Are you ashamed of your human body? Thinking back to the test results, I can see why, though."
    c "It's not that. In human society, walking around undressed is considered extremely unbecoming, especially at someone else's home, and particularly if that someone is of the opposite gender."
    An normal "It wouldn't be a problem for me, if that's what you're concerned about."
    c "Of course it wouldn't. You live naked for your whole life, but I'm not used to that, you know."
    An smirk "You got used to me being naked rather fast, though. Actually, I don't remember hearing you ever complain about my lack of clothing, [player_name]."
    c "Um... well... I respect your traditions and ways of life?"
    An "Of course you do."
    An normal "And it's not my fault human skin is so sensitive, soft and fragile that you have to cover it at all times, which later developed into some weird customs."
    An face "You also like to radiate and waste body heat like you're trying to warm up the entire planet all by yourself."
    An normal "Anyway, I think we should go to bed. It's pretty late."
    c "Some rest {i}would{/i} be nice..."
    An smirk "Then make yourself comfortable. And since I'm feeling nice today, I'll let you lie down first."
    c "This bed is rather small. It might not be big enough for both of us. Maybe I should take the couch in the living room?"
    An sad "After all that's happened recently, I really don't want to sleep alone tonight."
    c "Alright. I'll try and take up as little space as possible, and you'll have to squeeze in somehow."
    An smirk "Don't try anything frisky."
    An normal "I'm far too tired and exhausted today. Maybe some other time."
    hide anna with dissolve
    
    $ renpy.pause (1.0)
    nvl clear
    
    m "As soon as I lay down close to the edge of the bed, Anna suddenly jumped onto it and stood over me, her hind legs planted at the sides of my abdomen."
    nvl clear
    
    show eckannarom2 at Pan ((580,608), (250,0), 12.0) with fade
    $ renpy.pause (5.0)
    m "She looked quite menacing from down below with all the claws and a predatory smirk on her face."
    c "Clever girl..."
    $ renpy.pause (2.0)
    scene eckannabedroom2 with dissolvemed
    show anna smirk with dissolve
    play sound "fx/undress.ogg"
    m "Slowly, she lowered herself right on top of me, pinning me down with most of her weight. Our eyes locked onto each other's for a few seconds. She wasn't as heavy as one might have expected, but enough to keep me in place."
    c "What are you doing?"
    show anna slsmirk with dissolve
    m "She rested her head on the pillow, right over my shoulder. Her voice was now but a whisper."
    An sleep "This is the only way for us to fit on this bed together."
    c "You had this planned all along, didn't you?"
    An slsmirk "Maybe I did. You're too warm and cuddly to miss out on."
    m "Anna pulled the blanket over both of us and shifted a little to settle down more comfortably. Her surprisingly smooth underbelly brushed against my skin."
    
    $ renpy.pause (1.5)
    
    show anna sleep with dissolve
    m "I felt that she still remained somewhat tense. Her muscles felt stiff, and she kept shifting slightly, as if unable to find a comfortable position."
    c "Anna, are you okay?"
    An slsad "I'm fine."
    m "I gave her neck a light rub."
    c "You don't need to hide anything from me."
    $ renpy.pause (1.5)
    An "You know, ever since you cured me, I was afraid to fall asleep. Every time I closed my eyes, I thought I'd wake up covered in tubes and wires again, and that this all would turn out to have been just a dream."
    An "Even now, everything feels so surreal. This is all just too good to be true after the crap my life had been throwing at me for the last years. What if it's an illusion my mind made up to cope with the imminent death?"
    An cryface "What if I'm still strapped to the hospital bed and doomed to die in a few days?"
    m "I felt her shudder and shiver. Gently, I placed one of my hands on her neck, and used the other arm to pull her close, hugging her tighter."
    c "It's real, Anna. You're safe, and you are not alone anymore."
    $ renpy.pause (1.0)
    An slneutral "Thank you."
    m "I turned my head to her muzzle and gave it a light peck."
    show anna slsmirk with dissolve
    c "Sleep well."
    An sleep "You too, [player_name]."
    hide anna with dissolve
    $ eckannahbrecoverpath = True
    
    m "Soon Anna's body relaxed as she fell asleep."
    m "Staring at the ceiling, listening to her slow, even breathing, I couldn't help but wonder what future awaited us here."
    m "Thoughts of humanity's fate still haunted my mind, but now they were more of a distant whisper. There was nothing I could do to help people back home, but I was certain that my other self would succeed."
    m "I looked at the raindrops streaming down the window glass outside, then turned back to Anna's muzzle and closed my eyes. After so many turbulent days and nights, I finally felt at peace."
    $ renpy.pause (2.0)
    stop music fadeout (2.0)
    scene black with dissolveslow
    $ persistent.eckannaendingseenb = "B"
    show eckannaendingseenimgb with dissolveslow
    $ renpy.pause (1.5)
    hide eckannaendingseenimgb with dissolveslow
    play sound "fx/system.wav"
    s "Phew. That was a close call, eh? But you've managed to recover and get the happy good ending for Anna and yourself. Congratulations!"
    if persistent.trueending == True:
        s "Looks like you've already seen the true ending of the game. Would you like to explore this storyline further? \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
        menu:
            "Yes.":
                jump eck_anna_amelyarc
            "That would be enough reading, thanks.":
                pass
    else:
        s "Just a reminder. You still have the humanity to save in another timeline, so don't let up yet. Though, those are the problems for \"the other you\" to solve. \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
    
    $ renpy.pause (2.0)
    jump eck_anna_customcredits
    
label eck_anna_heartbreakfailure:
    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    play music "mx/fragments.ogg"
    scene black with dissolveslow
    # sad music (dot) OGG
    m "With nothing else to say, I slowly walked out of Anna's home."
    m "There was simply no way for us to recover after such a misunderstanding, and I had finally realized that as well."
    $ renpy.pause (2.0)
    scene o3 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    m "I walked back to my apartment through the cold heavy rain, but I could barely feel its freezing touch."
    m "For hours, I just sat on a couch in the living room with lights off, wondering how things could've been had they turned out differently today."
    # rewrite the line above
    m "Trying to drown those thoughts in wine, I only succeeded in falling into a dark dreamless slumber."
    
    stop music fadeout (2.0)
    $ renpy.pause (2.0)
    scene black with dissolveslow
    
    $ persistent.eckannaendingseeni = "I"
    show eckannaendingseenimgi with dissolveslow
    $ renpy.pause (1.5)
    hide eckannaendingseenimgi with dissolveslow
    play sound "fx/system.wav"
    s "Well, that didn't work out, did it? You have saved Anna's life, but she's still heartbroken, and who knows how that would affect her in the long run."
    s "Do not fret though. Try a different approach, and you might just succeed. You could, of course, just settle for this outcome as well, but do you want to? I won't tell anyone if you reload. Promise. \n Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
    $ renpy.pause (2.0)
    jump eck_anna_customcredits2
#
#   Amely's arc below this point. Maybe, I should've separated the files. Maybe.
#   Grammar checker software can't even process it anymore. RIP me.
#   Well, this part should be the final touching bit for this mod I suppose.
#   
#   I mean I am not writing a book of "A life with Anna" or something. As tempting as it might be. This ending already feels longer than chapters 4 and 5 combined.
#   In hindsight, the line above is a bit prophetic.
#   

label eck_anna_amelyarc:
    $ save_name = _("Anna 7 Extra")
    $ renpy.pause (2.0)
    play music "mx/morningrise.ogg"
    $ renpy.pause (2.0)
    if eckannahbrecoverpath == True:
        scene eckannabedroom4 with dissolveslow
    else:
        scene o4 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
    
    #morning music I guess? Done.
        
    m "For once, my dreams didn't haunt me with images of home, or of the impending fiery doom looming over us all."
    if eckannahbrecoverpath == True:
        m "Staring at the unfamiliar ceiling and glimpses of furniture I could catch, I was confused for a moment, before memories of the day before flooded back into my sleepy mind."
        m "The lack of extra weight on top of my body meant that Anna was already up and about. She didn't bother waking me up, though, for some reason."
        c "(How did she even slip away without disturbing me?)"
    else:
        m "Staring at a now all-too-familiar ceiling, I almost forgot that I wasn't supposed to be alone at that moment. Slowly, memories of the day before surfaced once again within my sleep-addled mind."
        m "For a time, I remained motionless, slowly gathering enough strength to get up."
        c "(I wonder... Where did Anna go?)"
    m "My thoughts were interrupted by something warm and slippery traveling up my cheek."
    show anna smirk with dissolve
    m "I turned my head just in time to see Anna retracting her tongue while taking a step back."
    
    An "Get up, sleepyhead."
    c "What time is it? Seems very early."
    An normal "It's half past seven."
    c "I thought you were supposed to be on the sick list?"
    An sad "Force of habit. Normally, I go to work every day, you know."
    c "Well, now that you no longer need to rush your research, why not take some days off every now and then?"
    An disgust "And just slack off like some lounge-lizard, wasting my time and talent?"
    c "It will work wonders to lower your stress levels and fatigue, trust me. It might seem like you'd be working less, but you'll be more productive."
    show anna sad with dissolve
    c "Actually, I bet the PDAs have references to that research in the medical or social section."
    An normal "We should check it out when we get a chance. I might follow your advice if that's really what your data archives say."
    An smirk "Or is that suggestion just an excuse to spend more time with me?"
    c "Well, what if it is?"
    An "Then it's quite poorly concealed. I expected better from the cunning Ambassador [player_name]."
    An normal "Now, enough lying around like a log. Get up already."
    m "I rolled my eyes."
    c "Yes, ma'am."
    An smirk "Good little human."
    c "Aren't we past this?"
    m "Suddenly, she moved her face right up to mine and flicked her tongue over my nose before I could recoil in surprise."
    $ renpy.pause (1.0)
    An "How about this for motivation?"
    c "Alright, you win."
    hide anna with dissolve
    play sound "fx/undress.ogg"
    m "I slid off the bed and put on my daily clothes."
    $ renpy.pause (1.5)
    show anna normal with dissolve
    c "Do we have anything for breakfast?"
    
    if eckannahbrecoverpath == True:
        An sad "I've checked the fridge, and the food's all spoiled, so I have nothing to offer you."
        c "It's alright. We can just go to a café."
        An normal "You'll have to wait for a while. None of the places are open yet."
        An sad "In hindsight, maybe I shouldn't have awoken us so early."
        c "Want to do anything in the meantime?"
        An normal "I'm not used to having free time. We can read a book or watch that half-useless box."
        c "You mean the TV?"
        An face "What other box do you think you could watch? My microwave?"
        c "If I'm bored enough, I guess."
        An smirk "Oh, shut up."
        An sad "I don't know why I even bothered buying a TV back in the day. Most of the channels are complete crap."
        c "And what about that show about humans?"
        An "That nonsense? Do those deformed things look even remotely like humans to you?"
        c "The writing wasn't too bad from what I've heard."
        An "Do you want to see what's on right now?"
        c "Why not. There's still a chance it's something interesting."
        An face "I wouldn't count on that if I were you."
        $ renpy.pause (2.0)
        scene eckannalivingroom at Pan((0, 250), (0, 250), 0.0) with dissolveslow
        $ renpy.pause (2.0)
        show anna normal with dissolve
        m "We settled down side by side on a soft couch in the living room. Anna subtly wrapped her tail around my back."
        m "She grabbed the remote and pushed the red on-button. The TV's screen immediately lit up, revealing nothing but hissing grey static."
        
        An face "I forgot I cancelled my subscription a while ago."
        m "She pushed the same button again and tossed the remote onto the unoccupied sofa."
        An sad "Whatever."
        c "Reading books it is then. We don't exactly have many options around here."
        An normal "Let me find something not too complex for you."
        c "Is that supposed to be a provocation?"
        An smirk "Only if you want it to be."
        m "She got up and walked up to a shelf left from the main entrance door."
        An normal "I don't keep a lot of artistic literature. Most of my books are scientific in nature, and they are not for the feeble-minded."
        $ renpy.pause (2.0)
        An face "Everything is such a mess here."
        An sad "You know what, [player_name]? I hate this place. It reminds me of nothing but desperation, persecution and death."
        c "Perhaps then we could just go out for a walk? I don't think I've seen the town at such an early hour."
        An normal "It's nothing special. Streets are all empty, and everything is closed."
        An "But let's go. It's still better than this hole."
        
    else:
        An sad "We have some leftovers from yesterday, but it would be hardly enough if we split them."
        c "It's better than nothing. We could go to a café or buy more food later on."
        An normal "You'll have to wait for a while. None of the places are open yet."
        An sad "In hindsight, perhaps I shouldn't have awoken us so early."
        c "Maybe we could just go out for a walk? I don't think I've seen the town at such an early hour."
        An normal "It's nothing special. Streets are all empty, and everything is closed."
        c "It might still be an interesting experience."
        An "With my work schedule I've had it plenty of times by now. But we could go if you wanted."
        c "Well, first things first. It's time for breakfast."
        
        $ renpy.pause (1.5)
        scene eckkitchenx3 with dissolveslow
        $ renpy.pause (2.0)
        
        show anna normal with dissolve
        $ renpy.pause (2.0)
        An smirk "I can keep going without getting hungry much longer than you do, so I'll let you decide how to split the food."
        c "You have a larger appetite, and you're still recovering, though."
        An face "Stop worrying about me already. I'm not about to die anymore. I'll be fine."
        c "Hey, I'm just trying to make sure you feel welcome."
        show anna sad with dissolve
        c "You aren't used to someone actually caring how you feel, I know that, but at least let me try to lighten up your mood. I want to see you happy, after all."
        m "I opened the fridge and pulled out the plate with the remains of my dinner from the day before."
        c "How about I give you two thirds?"
        An "And leave you with such a meager, pathetic portion?"
        c "I don't really need more right now, so help yourself, Anna."
        An "Whatever."
        An slsad "..."
        An normal "Thank you."
        nvl clear
        hide anna with dissolve
        m "Anna was hesitant to touch her share at first, but quickly picked up the pace. It didn't take long to for us to finish off the remaining food supplies."
        $ renpy.pause (2.0)
        scene o4 at Pan((0, 250), (0, 250), 0.0) with dissolveslow
        $ renpy.pause (2.0)
        m "We returned to the living room and settled onto a couch. Anna subtly leaned her side against mine, but otherwise pretended to be more interested in the interior."
        show anna normal with dissolve
        c "(And she was poking fun at my poorly concealed intentions.)"
        An smirk "Your place might not be as fancy as mine, but it's so comfy."
        c "You sure it's the place that's comfortable?"
        An "Shh."
        c "Actually, I always wanted to see where you live."
        An sad "Maybe some other time. I... I really don't want to go there again."
        c "Is something wrong?"
        An "Too many bad memories and painful reminders."
        An normal "Maybe I should stay here. Just take whatever items I can't easily replace from my apartment and move in with you. I don't care what anyone else would think or say about it."
        c "That's an enormous commitment. Dates are one thing, but living together with someone is a whole different story. Are you sure you're ready for it?"
        An sad "I just want to get away from that place, if only for a time."
        An "..."
        An "I also liked not having to sleep alone anymore."
        An "You know, since the day you cured me, I was afraid to fall asleep. Every time I closed my eyes, I thought I'd wake up covered in tubes and wires again, and that this all would turn out to be just a dream."
        An normal "But, with you nearby, those thoughts and fears are gone."
        c "I'm glad I could help. You're welcome to stay here for as long as you need. I'll be happy to keep you company, as well."
        m "I felt Anna slowly rest her head on my shoulder. She let out a short, sharp breath."
        An "Won't it get in the way of your work? You told me you're the one responsible for handling PDA data analysis now."
        c "The ministry is in no rush. It takes them a while to process whatever I send even with the commentary provided, and those PDAs aren't going anywhere. In the grand scheme of things, a week or two of delays won't cause any harm, really."
        c "I could even make up a claim about observing the long-term effects of application of the cure, but I have a feeling they wouldn't believe me."
        An smirk "They aren't as smart as you think they are, [player_name]."
        c "Still, it would be wrong of me to abuse their trust. But if those two weeks won't be enough to fully get you back on your feet, I'll try to extend my leave."
        An normal "Don't worry, two weeks should be enough for me to get my strength back."
        c "That's good to hear. Let's see to it together."
        c "So, shall we go for a walk?"
        An "Yeah, enough sitting around."
        
    nvl clear
    stop music fadeout 2.0
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene town6 with dissolveslow
    play music "mx/soul.ogg"
    $ renpy.pause (2.0)
    show anna normal with dissolve
    
    c "Looks pretty empty."
    An face "I don't know what you were expecting to see at this hour."
    c "It seems that we've got the whole town for ourselves, then."
    An smirk "You could say that."
    c "It feels so different here compared to how it was back home. In the human world, you'd still meet plenty of people no matter the time of day, especially soldiers guarding the streets."
    An disgust "If people like Reza are the norm among your population, I can see why you need constant armed patrols."
    c "Things had really changed for the worse since that solar flare hit us." 
    show anna sad with dissolve
    c "Life there used to be much nicer, you know."
    An normal "You never told me much about the human world, besides the fact that your guys have a cure for cancer. I'm still surprised it worked so well for me, considering our biological differences."
    c "I could give you the general story of what happened to us, if you want."
    An "Go ahead. It's not like we have anything better to do."
    c "Alright. So years ago..."
    
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene town6 with dissolveslow
    show anna disgust with dissolve
    $ renpy.pause (2.0)
    
    c "...And this is why Reza and I were sent here for those generators. Our mission is... {i}was{/i} our city's best and probably only chance to survive and recover."
    An "What a mess. Your world is in ruins, and most of the humans are busy killing each other over petty gains instead of rebuilding."
    An face "And I thought our politicians are hardheaded and short-sighted."
    c "Our city might be the last bastion of human civilization as we knew it before the flare. We've lost contact with every other settlement we knew about."
    An disgust "So Reza wasn't just a murderous prick. He was an idealistic murderous prick with a noble agenda to save his species. How tragic. I almost feel bad for slitting his throat."
    c "He was still a person, you know. Good or bad, death is never pretty."
    An face "Knock it off. He had no such thoughts or regrets about his victims, and he didn't hesitate to murder other humans, either."
    An disgust "If I hadn't tackled you out of harm's way, you, and by extension I, would've been dead right now."
    An sad "It might be hard for a bleeding heart like you to realize, but sometimes you have to kill if you want to survive, or save people you care about."
    c "Maybe that's what he thought as well?"
    An rage "Unlike me, he had a choice to avoid bloodshed, but he decided to be a murderous piece of shit. It was you and me, or him. He dug his own grave, and I merely helped him into it."
    c "I'm sorry. I'm just trying to figure out why he did all of that. He was my friend once."
    An disgust "He didn't consider you a friend valuable enough not to point his gun at you and shoot."
    c "I know, and I'm thankful to you for saving me."
    An normal "Do you think your higher up guys were playing the double game all along? Considering how poorly we're prepared to deal with toys like the one Reza was using."
    
    if chap2receiptsuntaken == False:
        c "Now that you mention it... Reza had been buying lemons every single time he went to the grocery store."
        An face "And how are lemons connected to anything? It's just a dumb fruit."
        c "Naturally, he was reporting any progress the whole time during the official part of his visit."
        An "That still doesn't answer my question."
        c "On my first day here he sent me a letter as well. He said I'd understand how to read it. It took me some guesswork, but then I remembered how back in school we learned about using lemon juice to write hidden messages."
        An ntdespair "What?!"
        show anna rage with dissolve
        c "When you write something with lemon juice and let it dry, it becomes invisible to the naked eye. But if you then heat it up carefully, oxidization occurs and reveals the message."
        c "Now if you put together that fact, Reza's habit of buying lemons every time and the intense exchange of letters between him and the higher ups in the city..."
        An "Are you telling me that this whole time you guys were plotting behind our backs?!"
        c "I had nothing to do with it. I was always honest about my intentions as an ambassador here. I may have been their plan B in case Reza's gambit failed."
        An sad "So you were just a clueless pawn in their huge political game."
        c "I guess I was."
    else:
        c "I doubt they'd do that. It's too risky considering the possible political fallout in case of failure."
        An "Humans don't strike me as the kind that would avoid risks if the reward was good enough. I'd say it's still a possibility."
        c "It might be. We'll never know. With the connection to my world severed, we're stuck with nothing but speculations."
        
    An smirk "At least, in the end, I got to keep you."
    c "And I'm happy to have you."
    c "But at what price?"
    show anna normal with dissolve
    c "There are many innocent people back home who {i}need{/i} help, and I promised them I'd do my best to get some. But look where I ended up. Reza is dead, and I'm hopelessly stuck."
    An sad "There's nothing you can do for them now."
    m "I looked down to the ground and shook my head."
    c "It's not easy to just leave everything and everyone behind and pretend they don't exist anymore. Something that, at this point, might already be the case."
    An rage "Are you going to dwell on this for the rest of your life? Your ambassador's mission is over, [player_name]. It's all over. Your tears and self-loathing won't fix anything."
    c "I... I can't let it go, Anna. My species is going to go extinct, and I'm enjoying a luxurious life I was never meant to have."
    show anna sad with dissolve
    c "It feels so wrong."
    An "And what good will it do for them, you or anyone else if you continue to hurt yourself with those thoughts? For better or worse, their fate no longer depends on your mission. For them, you are dead and gone."
    An normal "You have to move on. If not for your own sake, do it for me."
    An sad "I know it won't be easy, but I will be there to give you any help you might need."
    show anna blush with dissolve
    m "Gently, I rested my arm on her shoulders, giving her a soft hug. She slowly leaned her head against mine."
    c "I will try my best. Thank you, Anna."
    An smirk "You're welcome."
    An normal "With how much I owe you, it's the least I can offer."
    c "Do you think the café is open already? We've been out for a while, I think."
    An "Let's go check."
    
    m "Suddenly, a familiar voice called us out."
    
    Br "Having fun, you two?"
    show anna sad flip at left with dissolve
    show bryce laugh b at right with easeinright
    Br smirk b "Good morning, [player_name] and Anna."
    if brycestatus == "bad":
        c "Hey, Bryce."
        if sebastiansaved == False:
            Br "Nice to see you, guys."
            c "Nice to see you too."
            c "You know, I never apologized to you for that mess up at the bar."
            Br laugh b "It's all good. You were stressed with how much was going on, and I am pretty impatient at times. Did you think I'd stay mad over something this silly?"
            c "Well, when you put it like that, I see your point."
            $ brycestatus = "neutral"
            Br smirk b "We are still friends, [player_name]."
            Br sad b "And I really don't want to lose another one."
            c "What are you doing here at this hour, anyway?"
        else:
            Br "Nice to see you, guys."
            c "Nice to see you too."
            c "You know, I never apologized to you for that mess up at the bar."
            Br laugh b "It's alright. You were stressed with how much was going on, and I am pretty impatient at times. Did you think I'd stay mad over something this silly?"
            Br smirk b "You also saved Seb's life, and I'm very grateful for that."
            c "I'm glad to hear that we're still good."
            $ brycestatus = "neutral"
            c "What are you doing here at this hour, anyway?"
    elif brycestatus == "abandoned":
        c "Hey, Bryce."
        if sebastiansaved == False:
            Br "Nice to see you, guys."
            c "Nice to see you too."
            c "You know, I never apologized to you for taking up your invitation. Too many things were going on at once."
            Br smirk b "It's alright. I was upset at first, but then I remembered how busy and heavily stressed you were."
            Br normal b "Maybe I hoped to see something between us which wasn't really there, too."
            c "Yeah, when you put it like that, I see your point."
            $ brycestatus = "neutral"
            Br "We're still good friends, [player_name]."
            Br sad b "And I really don't want to lose another."
            c "What are you doing here at this hour, anyway?"
        else:
            Br "Nice to see you, guys."
            c "Nice to see you too."
            c "You know, I never apologized to you for not calling back. Too many things were going on at once."
            Br smirk b "It's alright. I was upset at first, but then I remembered how busy and heavily stressed you were."
            Br normal b "Maybe I hoped to see something between us which wasn't really there, too."
            Br smirk b "Thanks for saving Seb, by the way. I am very grateful to you for that."
            c "I'm glad to hear that we're still good."
            $ brycestatus = "neutral"
            c "What are you doing here at this hour, anyway?"
    else:
        c "Hey, Bryce. What are you doing here at this hour?"
    if sebastiansaved == False:
        Br normal b "Going home from the night shift, of course. Naomi and I are the only ones left in my team after the Reza case, so we're seriously understaffed right now."
        Br "The police could really use your help, [player_name], but I know you're busy with other things."
        Br "And it doesn't look like we'll be getting new recruits anytime soon, either."
        An "Quite unfortunate. Reza killed everyone he could in his way."
    else:
        Br normal b "Going home from the night shift, of course. With Maverick gone, Seb, Naomi and I are the only ones left in my team. We were struggling during the Reza case already, and now we're seriously understaffed."
        Br "The police could really use your help, [player_name], but I know you're busy with other things."
        Br "And it doesn't look like we'll be getting new recruits anytime soon, either."
        An "Quite unfortunate. Looks like you will have to do with what you have."
        Br smirk b "At least, intentionally or not, [player_name] managed to get Sebastian out of harm's way that night."
        Br normal b "I had to give him a stern official warning for abandoning his post during the council investigation, but unofficially I made it clear that I was glad he stayed safe."
        Br sad b "I lost one friend that night. I don't know how I could've taken losing another."
        An normal flip "Yeah, there was no way Sebastian could've stopped Reza alone."
        c "I agree. No offense to Sebastian and his skills, but the odds were stacked massively against him."
        Br normal b "I know. Reza was armed and had no reservations about killing anyone standing in his way. Even other humans."
    
    c "He wasn't always like that. He was determined, yes, but not to the point of shooting and stabbing his way through to his goals."
    An disgust flip "Your world is a mess. Maybe that got to his head as well."
    Br "Maybe."
    Br laugh b "But you know what? Enough talking about past troubles. Let's go somewhere nice and have a chat over a beer or three."
    An normal flip "I prefer to keep my head clear."
    c "Isn't it a bit too early to be drinking?"
    Br smirk b "Well, it is technically evening for me now. I just finished my shift and crave something substantial."
    Br normal b "And you don't have to drink. I'm positive there's something you like on the menu."
    An smirk flip "I'll be fine with coffee. Just don't expect me to carry your drunk ass back home."
    show anna normal flip with dissolve
    if bryce1unplayed == False:
        if nodrinks == True:
            Br normal b "You won't leave me hanging this time, right, [player_name]?"
            c "Yeah, you're right. I shouldn't have run off like that. I'm sorry."
            Br smirk b "Don't worry, it was a long time ago."
            An normal flip "Well, I'm not helping you. Good luck dragging Bryce to his apartment by yourself."
            c "I think we'll be fine, really."
            An smirk flip "Don't overestimate yourself."
            c "I know my limits."
        else:
            Br "I can count on [player_name] if anything goes too far."
            An normal flip "I didn't know you were an alcoholic like him."
            c "Hey, it was just one night out!"
            Br laugh b "Which escalated into a drinking contest."
            An smirk flip "And who won?"
            c "We... we don't remember. I think it was a draw."
            An "You just can't win at anything, can you, [player_name]?"
            c "Oh, shut up."
    else:
        Br normal b "I can count on your aid, right, [player_name]?"
        c "Well, I doubt things will get that bad, but I suppose I can't just leave you hanging."
        Br smirk b "That's the spirit."
        An normal flip "Well, I'm not helping you. Good luck dragging Bryce to his apartment by yourself."
        c "I think we'll be fine, really."
        An smirk flip "Don't overestimate yourself."
        c "I know my limits."
    
    An normal flip "Well, let's go. We were heading for a café anyway."
    Br normal b "I see. My usual place is still closed, so lead the way. Just let me remove my badge."
    c "It's not like anyone can mistake you for someone else."
    An smirk flip "Yeah, I could recognize you from across town."
    $ renpy.pause (1.0)
    show bryce laugh with fade
    Br "But I can't let people get the impression that I'm drinking on duty!"
    An normal flip "Fair point."
    
    play sound "fx/steps/clean2.wav"
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene cafe with dissolvemed
    $ renpy.pause (2.0)
    play music "mx/jazzy.ogg"
    
    c "And here we are."
    
    play sound "fx/chair.wav"
    $ renpy.pause(1.2)
    
    show bryce normal at right with dissolve
    show anna normal flip at left with dissolve
    
    An "Ah yes, finally some food and coffee. I haven't had a good cup in weeks."
    Br "What stopped you?"
    An face flip "I was in the hospital. Didn't [player_name] tell you?"
    c "To be honest, it's our first meeting since the official investigation was closed."
    An sad flip "Oh."
    Br "I know you were ill because I had to assign someone to look after the PDAs. What exactly happened, though?"
    if sebastiansaved == False:
        pass
    else:
        Br "Sebastian looked like he knew something, but he was very vague when I asked him, and refused to give any details."
    An "Don't worry. It's all in the past now, anyway."
    Br stern "I see."
    An disgust flip "Can we expect our service today? I'm not seeing any other visitors, and the waiter is nowhere to be found."
    c "Give them time. The café has probably just opened."
    An face flip "Fine."
    
    show anna normal flip behind bryce with dissolve

    show bryce normal flip at Position (xpos = 0.35) with dissolve
    
    show adine normal b at right with easeinright
    
    Ad "Sorry for keeping you waiting, everyone! I was getting ready for the shift and wasn't expecting customers so early."
    Ad giggle b "Quite a company you've gathered here, [player_name]."
    c "Good morning, Adine."
    Br flirty flip "Hey there!"
    An sad flip "Hey. Can I make my order now?"
    Ad normal b "Of course! Nice to see you in good health, Anna. So, what would you like?"
    show bryce normal flip with dissolve
    An normal flip "I'll have a coffee and a big portion of the meat snacks."
    Br smirk flip "A large steak and a beer for me."
    show bryce normal flip with dissolve
    Ad "What about you, [player_name]?"
    $ eckannasamefood = False
    $ eckannasamefoodbr = False
    menu:
        "Scrambled eggs and bacon.":
            An smirk flip "How wonderfully mundane of you."
            c "It's simple and filling, what else to ask for?"
            Br smirk flip "Good point."
        "Steak.":
            $ eckannasamefoodbr = True
            Br normal flip "So, you've had a long night too, [player_name]?"
            An face flip "I was only released from the hospital yesterday, you dolt."
            Br smirk flip "Sounds like exactly the time for a happy reunion to make up for all the lost days. I bet you missed each other so much."
            show bryce laugh flip with dissolve
            c "Let's not go into this any further."
        "Meat snacks.":
            $ eckannasamefood = True
            if nofood == False:
                An smirk flip "Did my earlier cooking and sense of taste impress you so much you're trying to learn them? I could teach you a few things."
            else:
                An smirk flip "I see you don't want to turn down my sense of taste anymore. Good choice. I could teach you a few things."
            Br smirk flip "You have a rich learning experience ahead of you, [player_name]."
            An face flip "Shut up, Bryce."
        "Salad":
            An face flip "And I was wondering how come you needed to stuff your face so often."
            Br brow flip "Are you sure that's enough for you?"
            c "Yeah, I'm good. I don't need any more food for a light breakfast."
    Ad "Anything for drinks?"
    menu:
        "Coffee.":
            if eckannasamefood == True:
                An smirk flip "Good start. You may yet prove to be a capable student."
                Br smirk flip "I'm sure you won't disappoint her, [player_name], will you?"
                show anna face flip with dissolve
                c "Um... let's not go into this any further."
                Ad giggle b "One coffee coming right up."
            else:
                Ad "Got it. I'll be right back."
        "Soda.":
            Ad "Got it. I'll be right back."
        "Beer.":
            An smirk flip "I'm not carrying you back home, either."
            c "It's just a glass."
            Br smirk flip "This is some strong stuff, though."
            if eckannasamefoodbr == True:
                Br normal flip "You sure you can handle heavy food and alcohol early, [player_name]? I'm going to head home and retire to bed after this."
                Br smirk flip "Unless I'm not the only one."
                An face flip "Just stop."
                Ad giggle b "One beer it is. I'll be right back."
            else:
                Ad "Got it. I'll be right back."
        "Nothing, thanks.":
            Ad "Got it. I'll be right back."
    show adine normal b flip
    $ renpy.pause(0.3)
    hide adine with easeoutright
    
    show bryce normal at right with dissolve
    
    show anna normal flip with dissolve
    
    An sad flip "I still can't believe she's the one who saved my life."
    c "Looks and first impressions can be deceiving. You of all people should know, Anna."
    Br "Is there some story I'm not aware of? Not asking this as a chief of the police, but as a friend, you know."
    c "Let's just say that Adine played a huge role in curing Anna's terminal disease. I'll spare you the extra details. They aren't important, anyway."
    Br laugh "That girl is certainly something, eh, [player_name]?"
    c "She's a very nice person, and we've been good friends for a while."
    An "Yeah..."
    Br smirk "You know, I don't think I'd mind being more than friends with her."
    An face flip "You can't be serious."
    c "Not that I'm against it, but I doubt it would work out for you."
    Br normal "Aww. But I'd still love to try my chances someday."
    show anna normal flip with dissolve
    c "How are things at the police department, by the way?"
    Br stern "Everything seems to be back to how it used to be, with a few exceptions. It's a quiet town, and not much is normally going on in the area."
    Br "A few bad fellows there and there, but they are nothing serious. You know, the usual thieves and shoplifters."
    c "That's good to hear. Looks like you got the situation under control."
    Br smirk "Yeah. It's pretty calm currently, but we remain vigilant, of course. In our line of work, you can never know when trouble might arise, but right now it feels like we're finally catching a break."
    An "It might be quiet, but you should still take your work seriously."
    Br stern "We do, don't worry."
    
    show anna normal flip behind bryce with dissolve

    show bryce normal flip at Position (xpos = 0.35) with dissolve
    
    show adine normal b at right with easeinright
    
    m "Adine soon returned, balancing two trays on her wing arms with surprising precision. She settled them in front of Bryce and Anna and gently pushed the orders off her forelimbs onto the table with her muzzle."
    play sound "fx/dishes.wav"
    Ad "There you go. Enjoy!"
    Br wink flip "Thank you!"
    show bryce smirk flip with dissolve
    An sad flip "Thanks."
    Ad giggle b "[player_name], give me a moment. I'll bring yours."
    c "Sure thing."
    $ renpy.pause(0.5)
    show adine normal b flip
    $ renpy.pause(0.3)
    hide adine with easeoutright

    show anna normal flip with dissolve
    show adine normal b at right with easeinright
    
    Ad "And here's your order."
    play sound "fx/dishes.wav"
    c "Thank you, Adine."
    Ad "You're welcome."
    $ renpy.pause(0.5)
    show adine normal b flip with dissolve
    c "Wait a moment."
    Ad disappoint b "Is something wrong with the food?"
    c "No, it's all good. Anna and I just wanted to meet up with you when you have time after work. Will that be okay?"
    show adine normal b with dissolve
    An sad flip "[player_name] told me you were the one who came up with the idea about the cure. If not for that discovery, I wouldn't have been here today."
    An "..."
    An "I wanted to say thanks."
    Br brow flip "Wow. I never thought I'll ever see you being grateful to someone. I guess the world {i}was{/i} ending with that comet."
    An disgust flip "Nobody asked for your opinion, Bryce."
    Br laugh flip "What? I'm just making friendly jokes. Don't be so strung up."
    Ad giggle b "I'll be free this evening. You're all welcome to visit."
    show anna normal flip with dissolve
    c "Alright. I'll give you a call in advance."
    show bryce normal flip with dissolve
    Ad "Now you'll have to excuse me. Let me know if any of you need anything."
    
    $ renpy.pause(0.5)
    show adine normal b flip with dissolve
    $ renpy.pause(0.3)
    hide adine with easeoutright

    show bryce normal at right with dissolve
    
    Br "Sadly, I can't accompany you guys this evening. I have work to do."
    An sad flip "Nobody invited you to begin with."
    c "C'mon, Anna. You don't have to be that rude to people anymore. They are trying to be nice to you after all."
    An face flip "They aren't making it easy."
    Br smirk "She's already way friendlier than she used to be, [player_name]. You're making solid progress. Just give her time."
    An disgust flip "What's that supposed to mean?"
    c "So much for that progress."
    show anna normal flip with dissolve
    Br laugh "Yeah."
    An smirk flip "If you think you can just change the way I am, think again."
    c "I wouldn't dream of it."
    An "You better don't."
    show anna normal flip with dissolve
    Br smirk "I see you guys are doing well. Making the most of your time here, huh, [player_name]?"
    Br normal "Though, I suppose your ambassador's mission is pretty stressful after the Reza's incident, so I can't blame you for looking for a respite. The fallout probably took a while to settle, too, considering you're still here."
    c "Actually, I've lost my official status several weeks ago."
    Br stern "How so?"
    An sad flip "Long story short, the portal is defunct for good, and the council had no better idea than to strip [player_name] of all the benefits and support in this world."
    c "Hey, I still have my apartment. They also helped me with the job at the facility."
    An face flip "That's not much of a reward for saving our whole civilization."
    Br brow "So that comet was a real threat?"
    c "Yes. If Reza had gotten away with the generator or damaged it, it would've been all over."
    Br stern "Damn."
    An smirk flip "Thanks to me, however, he didn't."
    Br "You said the portal is broken. Did someone vandalize it again? I was sure it's guarded day and night. I had no reports about any incidents around that area, either."
    c "It's somewhat worse than that. The coordinates that were used to reach the human world are gone permanently."
    show anna normal flip with dissolve
    Br "Do you have any idea who might've done this?"
    c "I know for a fact who did it."
    Br brow "So why didn't you report that person?"
    c "Because she's dead. Izumi, that other human whose body was discovered in the facility after our confrontation with Reza, deleted the coordinates to prevent his escape."
    c "She wanted to save your people at all costs."
    Br sad "I see."
    Br smirk "But hey, now you will get to stay with us. I would've been sad to see you leave, [player_name]."
    An sad flip "You aren't the only one."
    Br "So what you two have is pretty serious, huh."
    An rage flip "That's none of your business."
    Br normal "If you need help with anything, [player_name], let me know."
    c "Sure."
    Br smirk "You too, Anna."
    An normal flip "Why are you so nice all out of sudden? Your guys didn't feel too bad when they raided my lab and home."
    Br normal "Hey, I was occupied by Reza's case day and night. I never ordered anything like that. The council must've taken initiative."
    An sad flip "I see."
    Br stern "We were always on your side. You can't consider me this stupid to mess up your work while we needed your help during the investigation."
    An "I guess I was wrong this time."
    c "Happens to all of us."
    Br laugh "It's all good."
    m "Bryce gulped down the rest his beer and set the glass down next to his now empty plate."
    Br normal "I need to go home and get some rest. I have a second shift this evening."
    An normal flip "Looks like I am not the only one to live at work."
    Br brow "Normally it doesn't get this bad, but with how understaffed we are, I have to cover two positions at once. We still need a flyer on duty, too."
    c "That sounds pretty rough. Good luck, Bryce."
    Br normal "Thanks. Here's my part of the tab and a tip for Adine."
    Br wink "Let her know it's from me."
    c "Sure."
    play sound "fx/chair.wav"
    Br smirk "Stay in touch, [player_name]."
    c "Hopefully, our next meeting will be sooner than in a few months."
    Br "Yep. I'll give you a call when I have time."
    An "Goodbye."
    
    $ renpy.pause(0.5)
    show bryce normal flip
    $ renpy.pause(0.3)
    hide bryce with easeoutright
    $ renpy.pause(1.7)
    hide anna with dissolve
    show anna normal with dissolve
    
    c "How are you feeling?"
    An face "Social interactions are exhausting. At least this one was much more pleasant than dealing with Damion."
    c "Yeah, he didn't look like someone fun to work with."
    An sad "You have no idea."
    An smirk "You know, since we are here and have nothing to do for the day, how about we have a rematch?"
    c "Rematch?"
    An face "That stupid trivia game."
    c "Alright, I'm in."
    An smirk "This time, make it five points and no draws. If we have the same score by the end of it, we'll just keep going until someone, and I know who, will slip."
    c "Deal."
    c "Hey, Adine!"
    show anna normal flip at left with dissolve
    show adine normal b at right with easeinright
    
    Ad "Do you need something?"
    c "Could you please bring that trivia game your café has?"
    Ad "I'll be right back. Should I take away those empty plates?"
    c "Yeah. Thank you. Could you also get the bill for Bryce's order? He had to leave early."
    Ad "Of course."
    play sound "fx/dishes.wav"
    $ renpy.pause(1.5)
    stop sound fadeout 1.0
    show adine normal b flip
    $ renpy.pause(0.3)
    hide adine with easeoutright
    $ renpy.pause(2.5)
    show adine normal b at right with easeinright
    
    play sound "fx/bg.wav"
    
    Ad giggle b "Here's your game. Have fun!"
    c "Thank you. This should take care of Bryce's tab, and this he asked me to pass to you as a tip."
    Ad "That's so nice of him. Thanks!"
    
    show adine normal b flip
    $ renpy.pause(0.3)
    hide adine with easeoutright
    
    hide anna with dissolve
    show anna normal with dissolve
    
    c "So, shall we begin?"
    An smirk "Want to make any bets?"
    c "How about this? If I win, you'll kiss me right here. In public."
    An rage "How about I introduce you to my claws instead, [player_name]?"
    An normal "But you know what? Fine. If I win, you'll let me run any experiments, studies and research I deem necessary on you. No complaining and no avoiding me."
    c "Can you really compare those two?"
    An normal "You're right."
    An smirk "I will also get to sleep in your bed in your apartment tonight and decide if I want to let you in or not."
    c "Hey! You're really pushing it."
    An face "Don't be such a wuss. If it makes you feel better, I'll settle for the second part alone."
    c "That sounds fair. Let's play then."
    An smirk "I'll go easy on you this time and let you start..."
    
    $ renpy.pause (2.0)
    scene black with dissolveslow
    $ renpy.pause (2.0)
    scene cafe with dissolveslow
    
    $ eckannagameoutcome = renpy.random.randint(1, 20)
    # I am NOT making up new questions and games, but I guess I could add a certain degree of random instead... 25% of winning sounds just about right.
    # Praise RNGesus!
    if eckannagameoutcome > 15:
        show anna rage with dissolve
        $ renpy.pause (2.0)
        An "How is this even possible?!"
        c "Looks like I win."
        An "No. This can't be happening. I can't seriously lose a game of trivia to a human."
        An ntdespair "Did you cheat?!" with hpunch
        c "Of course not. You can't even cheat in this game to begin with. Now, about my prize..."
        An sad "..."
        An blush "Fine."
        m "I smirked in triumph, but, at the same time, subtly glanced over the café. No other dragons were around, and even Adine was somewhere in the staff-only area. I didn't actually want to cause Anna any embarrassment."
        $ renpy.pause (1.0)
        m "Anna slowly stood up from her chair and moved her muzzle right up to my face."
        show anna embarrassed with dissolve
        $ renpy.pause (1.4)
        show anna blush with dissolve
        $ renpy.pause (0.4)
        show anna slblush with dissolve
        $ renpy.pause (0.2)
        m "Following brief hesitation, she quickly pushed her lips into mine. After getting over the shock, I returned the kiss while gently stroking the back of her head. I didn't anticipate her using tongue, though."
        $ renpy.pause (1.0)
        show anna embarrassed with dissolve
        m "After several long seconds, she broke off and sat back down onto her chair."
        $ renpy.pause (1.0)
        show anna blush with dissolve
        An "I hope you're happy, [player_name]."
        c "I am. Nobody was around to see us, and I haven't gotten to kiss you since that one night."
        An normal "You could've just asked instead of making it into a public spectacle."
        c "But what sort of fun new experience would that be?"
        An smirk "Good point."
    else:
        show anna smirk with dissolve
        $ renpy.pause (2.0)
        An "What a completely expected turn of events."
        c "Yeah. Congratulations and all that."
        An normal "I almost forgot how good it feels to beat someone, especially at their own little game."
        c "So I guess I'm sleeping on the couch tonight."
        An smirk "Who said that? I'm not letting any of that comfy body heat go to waste."
        An normal "I might even let you collect your prize if I feel nice enough. Without any audience, of course."
        c "Come to think of it, I haven't gotten to kiss you since that one night we had."
        An smirk "You could've just asked instead of making it into a bet for a game you can't hope to win."
        c "But what sort of fun new experience would that be?"
        An "Good point."
    
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene town4 at Pan((0, 0), (0, 0), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    play music "mx/serene.ogg"
    
    show anna normal with dissolve
    c "This is where Adine lives."
    An "I see her living conditions leave a lot to be desired."
    c "The house is pretty cozy on the inside despite how it looks. Though, I agree it could be better."
    $ renpy.pause (1.0)
    hide anna with dissolve
    play sound "fx/knocking1.ogg"
    $ renpy.pause (2.0)
    Ad "Give me a minute!"
    $ renpy.pause (2.0)
    play sound "fx/door/doorchain.ogg"
    $ renpy.pause (2.0)
    show adine normal b with dissolve
    
    Ad "Hey there, you two! Please, come in."
    
    scene cgamely at Pan ((0, 0), (580, 326), 8) with dissolvemed
    c "Oh, hi there."
    Am "Hello."
    $ renpy.pause(2.5)
    scene town4 at Pan((0, 0), (0, 0), 0.0) with dissolvemed
    show adine normal b at right with dissolve
    show anna sad flip at left with dissolve
    
    Ad "The orphanage wanted me to look after Amely this evening. It was a last-second call. I hope you don't mind."
    show anna ntdespair flip with dissolve
    $ renpy.pause (1.0)
    show anna blush flip with dissolve
    c "It's fine. She's kind of cute."
    An embarrassed flip "Yeah..."
    Ad giggle b "Don't try to pick her up by the belly or tail, and watch your legs. She likes to hunt and bite sometimes."
    An "My scales can take it."
    c "I doubt my skin can, though."
    An smirk flip "Too bad."
    
    $ renpy.pause (2.0)
    scene adineapt at Pan ((300, 300), (128,300), 3.0) with dissolveslow
    $ renpy.pause (1.5)
    
    show amely smnormal at Position (xpos = 0.85) with dissolve
    show adine normal b behind amely at Position (xpos = 0.7) with dissolve
    show anna normal flip behind amely at left with dissolve
    
    An "So this is your place. It's not as fancy as mine or [player_name]'s, but I guess it has some homey charm."
    Ad "Thanks. It's hard for me to keep it in order with my work schedule."
    An "I know what you mean. I had to pay janitor services to keep my apartment in order."
    Ad disappoint b "At least you can afford it with your position. I can hardly make ends meet."
    Ad normal b "Oh, I shouldn't be complaining. I'm sorry."
    c "It's okay. I know you don't have it easy."
    Ad giggle b "I still have enough time to practice my stunt flying sometimes, so I'm doing alright. You don't have to worry."
    Ad normal b "How's your recovery going, Anna?"
    An sad flip "I'm... fine. Thanks."
    Ad disappoint b "Is something wrong?"
    An "No. I'm just not used to people wanting to help me without some sort of ulterior motive or long-term goals."
    Ad giggle b "You have friends now, and this is what friends do."
    An "Let's hope I won't lose them."
    c "Don't be so sullen. We're here to thank Adine for her help and have some fun."
    An normal flip "You're right, [player_name]."
    c "We got some supplies on our way here as well. Mostly snacks, but they could still make an alright dinner."
    Ad disappoint b "I don't have much to offer."
    c "It's alright. We should have enough as it is."
    hide adine with dissolve
    hide anna with dissolve
    hide amely with dissolve
    
    m "It didn't take us long to set everything up for our get-together."
    m "Despite the limited space in Adine's apartment, we managed to find enough room to accommodate everyone."
    
    show amely smnormal at Position (xpos = 0.85) with dissolve
    show adine normal b behind amely at Position (xpos = 0.7) with dissolve
    show anna normal flip behind amely at left with dissolve
    
    An sad flip "Let's get this out of the way before everything else."
    An normal flip "Adine."
    Ad normal b "Yes?"
    An blush flip "Thank you for helping [player_name] find the cure for me. You saved my life when everyone else was ready to give up."
    An sad flip "I'm sorry for being such a pain to deal with in the past."
    Ad giggle b "It's fine. Don't worry about it."
    c "Hey, I didn't give up on you!"
    An normal flip "Shush."
    Ad normal b "You're welcome. I'm glad the cure worked, and many other people will be so happy to see their loved ones healthy, too."
    Ad "We didn't start on the best terms, but we could be friends if you want."
    An "I'm not a fan of emotionally laden words and terms. We barely know each other."
    Ad disappoint b "..."
    An embarrassed flip "But I'd be a fool to turn down someone who saved me from a slow death and expected nothing in return. I'm not used to having friends, but I want to see where life will take us."
    c "More new experiences for you, huh."
    An smirk flip "You could say that."
    Ad giggle b "You got me for a moment."
    c "You better watch out, Adine. She can be quite mischievous."
    An "You haven't seen anything yet."
    Ad "Should I be worried?"
    c "Yeah. Be afraid. Be very afraid."
    Ad normal b "I'll keep my guard up."
    show amely smnormal at Position (xpos = 0.15) with ease
    show amely smnormal flip with dissolve
    Ad "Seems like Amely likes you. I've never seen her approach a stranger so easily."
    c "Aw, look. She hugged your leg."
    An normal flip "Do you want something from me?"
    Am smnormal flip "Play?"
    An sad flip "I'm not very good with children. I can barely tolerate most adults, you know."
    Ad giggle b "Give it a try."
    An normal flip "Fine. What do you want to play?"
    Am smsad flip "..."
    Am smnormal flip "Hunt?"
    c "That sounds unsafe."
    An smirk flip "For you and your soft skin it is, [player_name]. She can't get through my scales, though."
    Ad normal b "She can. I have several bite and scratch marks."
    show anna face flip with dissolve
    Ad think b "I'm not sure if I should be worried that she considers me tasty."
    An sad flip "...Maybe some other time then, Amely."
    Am smsad flip "..."
    c "Can I pick her up on my lap?"
    Ad giggle b "That won't be a good idea. She doesn't like sitting in one place for long and might scratch or bite you. She doesn't want to let go of Anna's leg either, I see."
    An "This is getting awkward."
    c "I wonder why she likes you so much."
    An "I don't know."
    Ad normal b "Maybe it's because you're a runner like she is?"
    An "Perhaps."
    c "You are both red, too."
    c "Now when I think about it, you and Amely look really alike."
    An disgust flip "Are you trying to imply something?"
    c "It's just that you're so nervous around her. I couldn't help but notice it."
    An "..."
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    play music "mx/gravity.ogg"
    $ renpy.pause (2.0)
    An sad flip "When I told you that I don't deserve you or the chance you gave me, I meant something beyond my usual harsh attitude."
    Ad disappoint b "Don't say that. Everyone deserves their chance to live. It's a matter of making up for one's mistakes and learning to never do them again."
    An face flip "If only it were something that small. You won't be saying that after I finish my story."
    c "It can't be that bad. And you know that I have your back, no matter what."
    An sad flip "..."
    An "Thank you."
    Ad "So are you Amely's biological mother?"
    c "I doubt it. Anna, didn't you say that you only ever dated Maverick? Unless something bad happened outside of that."
    Ad sad b "What? That'd be horrible!"
    An rage flip "Who do you think I am? I pity any idiot who'd dare to try and do something like that to me, because that would be his last mistake."
    show adine disappoint b with dissolve
    c "...You know, I don't doubt that. Not sure why I was worried for a moment there."
    An sad flip "However, in a way, your guesswork isn't far from truth. Just not in the way you think."
    Ad think b "I don't understand."
    An face flip "You will soon. Have some patience."
    Ad annoyed b "Go on."
    c "Yeah, I'm not sure I follow either."
    show adine think b with dissolve
    An sad flip "Remember what I told you about my research for the cure?"
    c "Yes, the council shot you down because of questionable ethics."
    Ad "From what I've read in newspapers, that's a huge understatement."
    An "They never knew anything. All those articles were just an attempt to cash in on the controversy at my expense. There was a huge smear campaign against me started by some idiots with too much free time."
    Ad "How do I know you aren't lying?"
    An rage flip "Because police never released any actual information to the public. What you saw were nothing but empty speculations and made up nonsense."
    Ad disappoint b "I see. I'm sorry."
    An sad flip "You shouldn't be."
    An "Here's the truth about that experiment I was about to be prosecuted for. The most damning piece of evidence I had to get rid of was an egg."
    An "I could've smashed it or thrown it away in the forest..."
    show adine frustrated b with dissolve
    play sound "fx/eckadinegrowl.ogg"
    An "But ultimately I decided against those options. They were easy ones, but, unborn as it was, that egg still held a life. The hatchling was in the last stages of development, too."
    show adine disappoint b with dissolve
    An "So I chose the only other option I had and left it at someone's doorstep. I disguised it as an egg abandoned by its parents."
    c "Did you really experiment on unborn children?"
    Ad "That's a horrible thing to do."
    An disgust flip "You may not think much of me, but I have my standards. I wouldn't steep as low as taking away someone's unborn child for my own egoistic purposes."
    An normal flip "Instead, a whole different opportunity presented itself."
    An "I was given a dead body for an autopsy. A dragoness who supposedly froze to death during winter due to some accident. Normally I'd need permission from one's relatives to perform experiments on the body, but she had no friends, relatives or family."
    An "She was pregnant at the time but the eggs hadn't formed fully yet."
    Ad sad b "..."
    show adine frustrated b with dissolve
    An sad flip "Without my intervention they would've all died anyway."
    Ad "Was her name Amelia?"
    An "Yes."
    Ad "She was my friend!" with hpunch
    An "I doubt you'll care about my condolences."
    show adine disappoint b with dissolve
    An normal flip "I'll spare you the details, but I've managed to save and artificially grow only one egg."
    An "With specifically designed genes and splicing some of my own DNA into it, I was this close to creating a being with an immune system strong enough to fight cancer. For all I knew, I had already succeeded."
    Ad "I can't believe you toyed with an unborn life like that."
    Ad annoyed b "Don't you feel even the smallest tingle of shame?"
    An rage flip "Why should I? Not only did I save that hatchling, but my research could've helped thousands of others suffering from the same disease I had!"
    Ad "You did it all for yourself, didn't you?"
    An sad flip "My motives aren't important here."
    c "To be fair, she started her research before she was diagnosed with cancer. But this experiment went very far."
    An despair flip "I was desperate!"
    show adine disappoint b with dissolve
    show anna cry flip with dissolve
    Am smsad flip "..."
    Ad "I see."
    An sad flip "But then, the police was about to raid my place. I had no choice but to get rid of the egg."
    Ad annoyed b "Why? You could claim it as your own!"
    An face flip "Without any prior records about me ever being pregnant in my life?"
    show adine disappoint b with dissolve
    c "Well, you could've had claimed that you found it or something."
    An sad flip "Any half-witted investigator would've caught on those lies. And if they found out about the origin of this egg, what do you think would've happened to both it and me?"
    An "And we aren't talking about big softie Bryce and his team. Those thugs and bastards were sent by the council."
    c "I see. Amely would still have ended up in the orphanage, and you'd have died in prison."
    Ad "But why didn't you adopt her later? You just continued like nothing happened, without a single care in the world."
    An disgust flip "I only left my work to eat and sleep, all while being sabotaged and exploited. You can hardly call that a careless existence."
    An cry flip "Even if I wasn't so busy, I'd never have made a good parent anyway. I thought she would have no problems finding a happy family or whatever."
    c "But she didn't, and you never bothered to check on her."
    An sad flip "I was too busy being the public punching bag for months."
    An "And after it all blew over, how do you expect me to have been a single parent with the working schedule I had? I spent every hour from dawn to sunset in the lab working on projects."
    Ad disappoint b "I know how such a work schedule feels."
    An cry flip "It's not like I had enough time left to {i}live{/i} to raise her, anyway. I was working at a disadvantage against the clock as it was."
    Ad "I didn't think of that."
    An "Want to know what the worst part about this mess is? I failed. All that effort, all that time spent and sacrifices made – they were all for nothing."
    An "If not for you, [player_name] and the data from human PDAs, my dead body would've been rotting in the dirt by now."
    Ad sad b "Please don't talk like that. It wasn't all in vain. You saved an unborn life, even if for your own reasons."
    c "I agree. Amely is here only thanks to you. The research you were working on didn't come through, but it made you the person you are today, the person I grew to care about."
    show adine disappoint b with dissolve
    An sad flip "And what sort of life did I bring her to?"
    c "It's still better than death. You gave her a chance to live and be happy."
    Ad disappoint b "She never found a family, though, and spent those years in the orphanage. I'm looking after her whenever I can, but it's hardly enough."
    An face flip "Why does everything have to be so pointlessly tragic?"
    c "I guess this is how things are."
    c "What are we going to do next, though? I don't know if telling Remy is a good idea. Technically, he's the biological father, but such painful reminders might be too much for him."
    Ad "His life is already hard and lonely. Honesty isn't always the best policy..."
    c "Yeah. But Amely might become too old to be adopted soon, and we can't leave her like that."
    An "What a mess I've created."
    show anna sad flip with dissolve
    menu:
        "You should try and make it up to Amely.":
            stop music fadeout 2.0
            $ renpy.pause (2.0)
            play music "mx/hopefulAMELY.ogg"
            $ renpy.pause (2.0)
            c "Then why not fix it? You can take her in and make sure she'll grow up into a smart and lovely girl. She has your genes."
            show adine normal b with dissolve
            An face flip "How do you expect me to raise her on my own with the work schedule I have?"
            c "Remember what we talked about? You won't have to spend the whole day at the facility anymore, and I will be there for you, too."
            An sad flip "You're way too eager to fix my mistakes for me, [player_name]."
            if eckannahbrecoverpath == True:
                c "You know well that I'm not perfect myself. But together, we have better odds at setting things right for once."
            else:
                c "I promised to stay with you, remember? We'll walk this path together, like we did for the last several months."
            Ad "I'd be happy if you could do that for Amely. They will soon consider her too old for adoption, and I wouldn't want her to grow up without a family."
            c "And we could hire Adine to babysit for us if our work gets in the way."
            Ad giggle b "I don't know about that. Even if you take Amely in, there are still other children that need my help."
            c "You could quit your job as a waitress."
            Ad think b "Even though it doesn't pay, I like it. I get to meet new people like you, [player_name], and the conditions are nice."
            c "Like delivering packages in the middle of heavy storms?"
            Ad "Maybe I should quit that part, though."
            An "Ever since meeting you, [player_name], I'm finding myself involved in more and more commitments."
            c "I understand if you don't feel ready. I'm not certain myself if I can take on such an endeavor."
            Ad disappoint b "But you are her best chance for a normal life. In a few months, nobody is going to adopt her, and then she'll have to grow up without a family."
            An rage flip "Do you think it's easy for me to decide? I thought I was finally free to get away from stress and drama, but my life just can't let that happen."
            An sad flip "Yet, she is part me. She may be closer to a clone than a daughter, but I brought her into this world."
            c "If we aren't going to take this responsibility, nobody else will."
            An "I know."
            An "..."
            An normal flip "Fine. I will adopt her. I count on your help here, [player_name]."
            Ad giggle b "I'm so glad you've agreed!"
            Am smnormal flip "Home?"
            An normal flip "Yes, you are going to have a new home."
            c "Can we take her in now and fill out the papers tomorrow? I don't think any legal offices work at this hour."
            Ad giggle b "Of course. Thank you, you two, for giving her a family. I'm sure you will get along."
            Ad think b "Even though you weren't there when she hatched, I think she recognized you as her mother somehow."
            An embarrassed flip "It's possible. However, I have no idea how to be a parent."
            Ad giggle b "I'll help you. Feel free to ask any questions!"
            An sad flip "..."
            An normal flip "Thanks."
            c "It's getting late. We should head home before it gets completely dark."
            Ad disappoint b "Oh, right..."
            Ad normal b "Take care, everyone. If you need any help with Amely, don't hesitate to call me."
            c "Sure."
            $ eckannaadopt = True
            $ adinestatus = "good"
        "I think we better tell Remy.":
            stop music fadeout 2.0
            $ renpy.pause (2.0)
            play music "mx/chronos.ogg"
            $ renpy.pause (2.0)
            c "It might hurt him, but as a biological father, Remy has to know."
            Ad disappoint b "True. He wanted children, but with what happened to Amelia..."
            An face flip "He's going to kill me."
            c "He's a kind dragon, and if anything, you've saved Amely's life. Yes, you had your own motives, but I'm sure if you explain yourself he will understand your predicament."
            An "You know what they say. Beware the quiet ones."
            Ad "What about Vara? They're getting along so well, and I don't want her to lose her chance."
            c "He can look after them both. He might be a little clumsy when handling everyday objects, but I believe in him."
            An sad flip "As long as he won't be jailed for my murder."
            Ad giggle b "Don't be like that. Of course he won't hurt you."
            c "I agree. And I will be there to back you up, Anna."
            Ad normal b "So will I."
            An sad flip "Fine. Though I'd prefer to have someone like Bryce around during that meeting."
            c "We can invite him as well."
            Am smsad flip "No mother?"
            An "I am... not. I'm sorry, dear."
            show amely smsad flip at Position (xpos = 0.85) with ease
            show amely smsad with dissolve
            c "It's sad to see her like that, but I think this is better for everyone, her included."
            Ad disappoint b "I think so too. I'd have loved if you took in Amely, Anna, but I also realize that putting her into the hands of someone not yet ready isn't wise."
            An "My place is in the lab, working on research for the good of our whole civilization. I doubt I'll settle for a proper family any time soon."
            c "At least you have me by your side."
            An normal flip "For better or worse, for both of us."
            c "I guess it's settled, then."
            An "Yeah."
            Ad "I hope Remy will be alright."
            c "I hope so too."
            Ad normal b "He's so happy around children. Maybe being a father would actually help him overcome his depression."
            An "Maybe."
            An smirk flip "And if you two are going to hook up, I'm sure he'll be even happier."
            Ad giggle b "Oh, stop it. We're just good friends."
            An "That's how it always starts, you know."
            c "I don't think I like where this is going."
            An face flip "Shush. I'm trying to be friendly with someone, and you're not helping."
            Ad "There might be a lot to work on, but you're making progress, Anna."
            c "You have no idea how much effort it took me to get there."
            An smirk flip "Oh, shut up, both of you."
            c "Alright, alright."
            c "It's getting late. We should head home before it gets completely dark."
            Ad disappoint b "Oh, right..."
            Ad normal b "Take care, [player_name] and Anna."
            $ eckannaadopt = False
            $ adinestatus = "neutral"
    
    scene black with dissolvemed
    stop music fadeout 2.0
    $ renpy.pause (2.0)
    scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    play music "mx/tranquility.ogg"
    show anna normal with dissolve
    
    if eckannaadopt == True:
        show amely smnormal at Position (xpos = 0.55) with dissolve
    else:
        pass
    An "That was one crazy day."
    if eckannahbrecoverpath == True:
        c "Not as crazy as yesterday, thankfully."
        An "Yeah. I'm not sure I could take another one like that."
        c "Again, I'm sorry for hurting you and causing you grief with my thoughtless words."
        An smirk "We were both at fault there. And we both have learned a lot from it."
        c "A fair point. But let's not do that ever again."
        An "Agreed."
    else:
        c "And things had just started to calm down yesterday."
        An "I'm used to stress, you know. I'll be fine."
        c "Hopefully you'll at least be able to recover in peace. I don't want your condition to worsen because of constant worries and stress."
        An smirk "This is nothing compared to dealing with my work on a daily basis."
        c "Fair point."
        
    if eckannaadopt == True:
        Am "Explore!"
        hide amely with easeoutleft
        c "Wait. Where's she going?"
        An normal "Let her be. She's just getting familiar with her new surroundings. That's normal."
        c "Alright. We need to think how to accommodate her, though."
        An "You only have one bed, but it should be enough for us all until we get her a separate one."
        An sad "I never imagined myself to be a parent. It feels so odd to me."
        c "You aren't alone. Always remember that."
        An "Thank you."
    else:
        pass
    
    c "I guess it's time for us to go to bed. To be honest, I'm exhausted."
        
    if eckannahbrecoverpath == True:
        An normal "Your apartment feels so much better than mine. Not as fancy, but it brings much warmer thoughts and memories."
        c "I have a larger bed, too."
        An smirk "You don't expect that to stop me from enjoying your body heat, do you?"
        c "I had a feeling that wouldn't be the case."
    else:
        An normal "Do you want the spot by the wall this time?"
        c "I don't mind either way."
        An smirk "So, I assume no more trying to sleep on the couch away from me. Smart choice."
        c "Looking back, sleeping alone really isn't that nice."
    
    if eckannaadopt == True:
        An face "Just let me find Amely. We can't go to bed without her, can we?"
        c "I think I saw her whizzing towards the kitchen."
        An normal "Stay here. Your skin and clothing won't stop her sharp little claws and teeth."
        c "Okay."
        hide anna with easeoutleft
        $ renpy.pause (1.0)
        An "I'm not going to ask how, but {i}why{/i} did you climb that cupboard, Amely?"
        Am "Explore!"
        An "Come here, it's time for bed."
        show anna normal with dissolve
        show amely smnormal at Position (xpos = 0.55) with dissolve
    else:
        pass
    
    $ renpy.pause (2.0)
    scene o3 at Pan((0, 250), (0, 250), 0.0) with dissolvemed
    $ renpy.pause (2.0)
    play sound "fx/undress.ogg"
    $ renpy.pause (2.0)
    
    
    if eckannaadopt == True:
        m "We settled down face to face on my bed. Anna gathered Amely to her chest and held her in her arms, forming a sort of soft, comfy nest for her."
        m "Despite my expectations, the hatchling fell asleep almost immediately, never letting out as much as a sound."
        show anna normal with dissolve
        c "She's so cute."
        An "I know."
        An smirk "You sure turned my life upside down after saving it, huh, [player_name]?"
        c "That's what I am good at, I guess."
        An normal "I don't know if it's for good or ill yet, but I'm interested in giving it a try."
        c "I'm sure you'll like it."
        An smirk "But don't expect me to quit my work. I may reduce my hours and take some days of the week off, but that's where I'll draw the line."
        c "I wouldn't dream of more. Hopefully Adine will accept that babysitting offer. I don't want to leave Amely home alone."
        An normal "Dragon hatchlings are pretty self-sufficient. Show her the restroom and where to get food and water, and she'll be fine."
        An "Not that she doesn't need love or care. Just not constant supervision."
        c "That's neat. Human kids require a lot of babysitting. They're pretty noisy, too."
        An face "How did your kind even survive before you invented all that technology?"
        c "Good question. Maybe we just got lucky."
        $ renpy.pause (0.5)
        show anna normal with dissolve
        $ renpy.pause (1.5)
    else:
        m "We settled onto my bed, face to face. Anna put both of her arms on my shoulders and pressed herself against me."
        show anna normal with dissolve
        c "You know, you're pretty cuddly yourself. Your chest scales feel surprisingly smooth and warm."
        An smirk "Those are the softest ones I have. They're still stronger than your skin, though."
        c "I never doubted that."
        An normal "Tomorrow is going to be hell to get through. Normally I wouldn't be afraid of Remy, but in my weakened state he might get me."
        c "Don't worry. He'll give you an angry glance at worst and then rush off to Amely."
        An sad "I hope you're right."
        c "You have me and Adine to keep him from any rash actions. That's what friends are for."
        An normal "Thank you."
        $ renpy.pause (2.0)
    
    show anna sleep with dissolve
    $ renpy.pause (1.0)
    menu:
        "Cuddle.":
            if eckannaadopt == True:
                m "Being slow and gentle, I wrapped an arm around her shoulders and pulled her a little closer."
                m "I made sure not to disturb the sleeping Amely, but I doubted she would mind the extra cuddles."
                An brow "Be careful. Don't wake her up."
                c "I am careful. You two are simply adorable together."
            else:
                "I pulled her a little closer, her soft underside brushing against my skin. With gentle reverence, I ran my fingertips over her scales, stroking up and down her back."
                m "She moved her muzzle and opened her eyes to look into mine."
                show anna blush with dissolve
                c "No matter what, I'll always be here for you."
            show anna slblush2 with dissolve
            m "She took her time nuzzling my cheek, smiling warmly at me before resting her head back on the pillow."
            
            An smirk "You sure enjoy your time here, don't you, [player_name]?"
            c "I can't help it, especially with you around."
            An "I guess we still feel the same way."
            c "I guess we do."
        "Get some long-deserved rest.":
            pass
        "Give her a kiss.":
            if eckannagameoutcome > 15:
                c "Before we sleep, can I get another kiss?"
            else:
                c "Before we sleep, can I collect today's prize?"
            
            An slsmirk "Come and get it if you dare."
            show anna slblush with dissolve
            m "I moved my face closer to her muzzle and gently pressed my lips into hers. Subtly, she pushed back and slipped in her tongue, while I traced her head and horns with my fingers."
            m "We remained locked together for a time, until I slowly parted and inched away, taking a deep breath to replenish my nearly depleted oxygen."
            
            An smirk "You sure enjoy your time here, don't you, [player_name]?"
            c "I can't help it, especially with you around."
            An "I guess we still feel the same way."
            c "I guess we do."
    show anna sleep with dissolve
    c "Good night, Anna."
    An slblush2 "Good night, [player_name]."
    hide anna with dissolve
    
    if eckannaadopt == True:
        m "Soon, she fell asleep. For several minutes, I silently looked at Anna's peaceful features, and at Amely comfortably curled up in her arms. The only visible part of the hatchling from under the blanket was her little muzzle."
        m "I never expected to become a foster parent to a baby dragon, and I was nervous about the challenges such a commitment would bring."
        m "And yet I knew, deep inside, that we had little to worry about, as we could count on help from Adine and others on this long journey."
        m "With those thoughts, I let my eyes close and smiled."
        
        stop music fadeout (2.0)
        $ renpy.pause (2.0)
        scene black with dissolveslow
        
        $ persistent.eckannaendingseenc = "C"
        show eckannaendingseenimgc with dissolveslow
        $ renpy.pause (1.5)
        hide eckannaendingseenimgc with dissolveslow
        
    else:
        m "Soon enough, she fell asleep. For several minutes, I silently regarded Anna's peaceful features and wondered if we did the right thing that day."
        m "A part of my mind felt like we had just dodged our responsibilities and obligations towards Amely. Yet I knew that Anna wasn't prepared to take up the role of a parent, and I wasn't sure I was, either."
        m "On the other hand, Remy was the father, and he had the right to know the truth and be with his daughter. This could make them both happy. Maybe it was for the best of everyone in the end."
        m "With those thoughts, I shut my eyes and yawned, letting my body fully relax in Anna's soft embrace."
        c "(Maybe someday, she and I will be ready for it, too.)"
        
        stop music fadeout (2.0)
        $ renpy.pause (2.0)
        scene black with dissolveslow
        
        $ persistent.eckannaendingseend = "D"
        show eckannaendingseenimgd with dissolveslow
        $ renpy.pause (1.5)
        hide eckannaendingseenimgd with dissolveslow
    # This text above has officially been tamed. Yippee.
    m "Fin."
    play sound "fx/system.wav"
    s "Congratulations! You've made it to the finish line of the extended good ending for Anna. Quite a lot of reading, huh?"
    if eckannaadopt == True:
        s "You decided to convince Anna to make up for her past actions and adopt Amely. Was that a wise decision? Will she and you make good parents? Only time will tell."
        s "Your city is saved in another timeline, and you've settled down for a nice life in this one. Maybe it's not all that bad. I mean, if dinosaurs never went extinct, would humanity in the future even exist anymore?"
        s "Just some food for thought. Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
    else:
        s "You decided to tell Remy the truth about Amely. He'll likely make a good father, and who knows? Maybe that will help him and Adine get closer to each other."
        s "Your city is saved in another timeline, and you've settled down for a nice life in this one. Maybe it's not all that bad. I mean, if dinosaurs never went extinct, would humanity in the future even exist anymore?"
        s "Just some food for thought. Mod's endings seen: [persistent.eckannaendingseena] [persistent.eckannaendingseenb] [persistent.eckannaendingseenc] [persistent.eckannaendingseend] [persistent.eckannaendingseene] [persistent.eckannaendingseenf] [persistent.eckannaendingseeng] [persistent.eckannaendingseenh] [persistent.eckannaendingseeni]"
    jump eck_anna_customcredits
    
#   Over 1100 lines... damn, that's a lot...
#   I think I might've gotten sliiiiiightly carried away while working on this.
#   I wonder if the quality is as good as the first half though. I'd hate to overstay my welcome here after all and ruin the overall experience.
#   Then again, that's why it's optional.
#   Well, this is where everything ends. For real this time. See you soon in "EvilChaosKnight's better ending mod: The Electric Boogaloo: Bryce edition."
#   
#   It might be not the best name though... And "soon" might mean something like a month.
#   Has anyone tried the dragon cards mod yet btw? Any feedback? Just asking.