

label hg_pf_LetsHaveSex: #LV.7 (Whoring = 18 - 20)
    hide screen hermione_main
    with d3

    $ menu_x = 0.5 #Menu is moved to the middle.
    $ menu_y = 0.5 #Menu is moved to the middle.

    if hg_pf_SuckIt_OBJ.points == 0:
        m "{size=-4}(Should I ask her to have sex with me?){/size}"
        menu:
            "\"(Yes, let's do it!)\"":
                pass
            "\"(Not right now.)\"":
                jump silver_requests
    
    $ genie_chibi_xpos = -70 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "sex_ani"

    call bld

    if whoring < 18:
        m "[hermione_name]..."
        m "Why don't you come over here and I pound your pussy for a bit..."
        g9 "With my cock!"
        jump too_much

    #First Event.
    if hg_pf_LetsHaveSex_OBJ.points == 0:
        m "[hermione_name]?"
        call her_main("[genie_name]?","base","base")
        m "The favour I will be buying from you today..."
        call her_main(".......?","base","base")
        m "How should I put this delicately...?"
        call her_main("Is it sex, [genie_name]?","base","suspicious")
        m "Well, yes. How did you...?"

        call her_main("Not a terribly difficult deduction all things considered...","base","glance")
        m "You don't mind then?"
        call her_main("Of course, I mind, [genie_name]!","upset","closed")
        her "I am not a prostitute!"
        m "But you'll do it anyway??"
        call her_main("\"Gryffindor\" is falling behind again...","open","closed")
        her "What choice do I have...?"
        m "Great!"

        label your_ass:
        hide screen hermione_main
        call blkfade

        stop music fadeout 1.0
        call gen_chibi("hide")
        call her_chibi("hide")

        call her_head(".............","upset","closed")
        call her_head("!!!!!!!!!!!!!!!","angry","wide")
        m "Relax, [hermione_name]. I'm Just gonna take off your panties."
        call her_head("..............","angry","angry")
        m "Are you ready?"
        call her_head("No...","annoyed","annoyed")
        m "Good girl."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide")

        call gen_chibi("hide")
        call her_chibi("hide")
        hide screen genie
        show screen chair_left
        show screen g_c_u

        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","normal","worriedCl")
            show screen ccg

        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc


        call play_music("playful_tension") # SEX THEME.

        #FUCKING
        g4 "Your pussy... It's so tight."
        call her_head("................","normal","worriedCl")
        m "You alright?"
        call her_head("A-ha... It's too big...","angry","base",tears="soft")
        call her_head("You will rip me apart, [genie_name]!")
        m "Nonsense! My cock is of a regular size."
        m "It's not my fault that you are so tiny."
        call her_head("......................","normal","worriedCl")

        menu:
            "\"You should be ashamed of yourself!\"":
                #$ ccg2 = 20
                call her_head("I am not ashamed, [genie_name]!","normal","worriedCl")
                call her_head("I am doing this for the sake my house!")
                call her_head("To help my--")
                call her_head("ah-ha-a...","open","worriedCl")
                call her_head("My classmates depend on me... ah-a...")
                m "Are you sure that's the only reason?"
                call her_head("I don't know--","normal","worriedCl")
                call her_head("ah-a...","open","worriedCl")
                call her_head("I don't know what you mean, [genie_name].","angry","down_raised")
                m "It seems to me that you are enjoying this a little bit too much."
                #$ ccg2 = 21
                call her_head("I'm not, [genie_name]!","angry","down_raised")
                m "Really?"
                call her_head("......................","normal","worriedCl")
                m "Then why is your pussy so wet?"
                call her_head("....................a-ha.{image=textheart}","open","worriedCl")
                m "Admit it, you enjoy getting fucked by your [genie_name]!"
                #$ ccg2 = 25
                call her_head("I do not!","normal","worriedCl")
                m "Stubborn girl..."
                call her_head("Aha...{image=textheart}","open","worriedCl")
            "\"So... What's new in your life?\"":
                #$ ccg2 = 14
                call her_head("...[genie_name]?","open","base")
                m "Just trying to have a polite conversation."
                #$ ccg2 = 17
                call her_head("Ah-ah... But... ah...","open","base")
                m "Any news from your folks?"
                call her_head("My parents?","angry","worriedCl",emote="05")
                call her_head("[genie_name], please, I cannot talk...","open","worriedCl")
                m "Why not? Enjoying this too much?"
                call her_head("I am not... ah...{image=textheart}","open","worriedCl")
                m "I think you are."
                call her_head("I am only doing this for the points, [genie_name]...","open","worriedCl")
                m "Oh, I see..."
                m "So you are like a prostitute then."
                call her_head("What?","angry","base")
                m "Well I pay you to have sex with me. How would you call that?"
                call her_head("...........","angry","down_raised")
                #$ ccg2 = 19
                call her_head("I am not a prostitute...","open","worriedCl")
                call her_head("Why are you being so mean to me, [genie_name]?","angry","base",tears="soft")
                m "I think you like it when I'm mean."
                call her_head("I do not!","mad","worried",tears="soft")
                m "Really? Then why is your pussy so wet?"
                call her_head("Not because of that!","angry","down_raised")
                m "If you say so..."
                #$ ccg2 = 20
                call her_head("A-ah...{image=textheart}","open","worriedCl")
                call her_head("I am... ah...{image=textheart} not a prostitute...","shock","worriedCl")
            "\"......................................................\"":
                #$ ccg2 = 14
                call her_head("A-ha... ah...","open","worriedCl")
                m "*Panting!*"
                call her_head("Ah... ha-aha...","open","worriedCl")
                m "Oh..."
                call her_head("Ah-ah...","open","worriedCl")
                m "......................"
                call her_head("Ah... ah...","open","worriedCl")
                call her_head("Ah... [genie_name]?","open","base")
                m "What is it?"
                #$ ccg2 = 17
                call her_head("Ah... Do you.... like it?","open","worriedCl")
                m "Do I like drilling your super-tight pussy?"
                m "Very much so, [hermione_name]. Why?"
                call her_head(".....................","normal","worriedCl")
                call her_head("Ah... You just got so quiet...","open","worriedCl")
                m "Just enjoying the moment, [hermione_name]."
                m "What about you? You alright?"
                call her_head("Ah... yes...","open","worriedCl")
                call her_head("It hurts a little though, ah...","open","base")
                call her_head("Your penis is too big... ah...","open","worriedCl")
                m "Hm..."
                m "You need me to slow down or something?"
                #$ ccg2 = 20
                call her_head("No, [genie_name]... You don't have to...","open","base")
                call her_head("Please, don't mind me... Enjoy your moment.","normal","worriedCl")
                call her_head("I will... ah... Get used to it eventually... ah...")
                m "As you say, [hermione_name]."
                #$ ccg2 = 21
                call her_head("Ah-a...{image=textheart}","open","worriedCl")
                m "Yes, this is great!"

        call her_head("Ah-ah...{image=textheart}","open","worriedCl")

        if daytime:
            m "Going to classes after this?"
        else:
            m "Going to bed after this?"
        #$ ccg2 = 22

        call her_head("Yes, ah...{image=textheart}","open","worriedCl")
        call her_head("If I'll be able to walk...")
        g4 "Ght! {image=textheart} Yes, you always say the right things, [hermione_name]!"
        call her_head("Ah...{image=textheart} ah...{image=textheart}{image=textheart}","shock","worriedCl")
        with hpunch
        #$ ccg2 = 24
        call her_head("{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart}{image=textheart}{image=textheart}","scream","wide")
        m "Huh? You alright?"
        call nar(">Hermione's legs are shaking...")
        m "[hermione_name]?"
        #$ ccg2 = 28
        call her_head("{image=textheart}{image=textheart}{image=textheart}I think I'm cumming, [genie_name]!{image=textheart}{image=textheart}{image=textheart}","scream","wide")
        g9 "Tch... You nasty slut!"
        #$ ccg2 = 29
        call her_head("AAH! I can't hold it!","silly","dead")
        g4 "You need to be punished for being such a slut!"
        call nar(">You tighten your grip on Hermione's buttocks and start to fuck her fiercely!")
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        #$ ccg2 = 30
        call her_head("NO! STOP! PLEASE!","scream","wide")
        g4 "Who told you you could cum, slut? This is your punishment!"
        call her_head("[genie_name], no, ah-a!{image=textheart}","open","worriedCl")
        #$ ccg2 = 31
        call her_head("Ah-a...{image=textheart}I will go insane!{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
        g4 "{size=+7}Grragh!{/size}"
        hide screen bld1
        with d3
        call ctc

        #$ ccg2 = 32
        call her_head("No...{image=textheart} ah...{image=textheart}","silly","ahegao")
        #$ ccg2 = 33
        call her_head("I think I will...{image=textheart} pass out...{image=textheart}")
        g4 "ARGH! YOU WHORE!"

        menu:
            "-Cum all over Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                call cum_block
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                call set_u_ani("sex_cum_out_ani")
                $ g_c_u_pic = "sex_cum_out_ani"
                $ ccg3 = "s3"
                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 42
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                hide screen bld1
                call ctc

                call set_u_ani("sex_cum_out_blink_ani")
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                m "Well, that was rather intense..."
                #$ ccg2 = 28
                call her_head("*heavy panting*","open_wide_tongue","ahegao")
                m "You alright?"
                call her_head("Ah... yes...","silly","dead")
                #$ ccg2 = 29
                call her_head("My legs are still shaking...")
                hide screen bld1
                with d3
                call ctc
                call blkfade

                hide screen ccg
                $ face_on_cg = False
                call h_update_hair

                if daytime:
                    call her_head("But I think I will be able to make it to my classes...","silly","dead",xpos="base",ypos="base")
                else:
                    call her_head("But I think I will be able to make it to the common room...","silly","dead",xpos="base",ypos="base")

                m "Good."
                m "Did you enjoy getting fucked by your [genie_name]?"
                call her_head("[genie_name], I am only doing this for my house.","grin","ahegao")
                m "Seriously? Still?"
                call her_head("Could I just get paid now... please?","open","worriedCl")

            "-Cum inside Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                call cum_block
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                call set_u_ani("sex_cum_in_ani")
                $ g_c_u_pic = "sex_cum_in_ani"
                $ ccg3 = "s1"
                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 41
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                hide screen bld1
                with d3
                call ctc
                $ g_c_u_pic = "images/animation/23_cum_19.png"
                #$ ccg2 = 40
                call her_head("You came inside of me...","silly","dead")
                g9 "I sure did."
                hide screen bld1
                with d3
                call ctc
                call blkfade

                hide screen ccg
                $ face_on_cg = False
                call h_update_hair

                call her_head("But...","silly","dead",xpos="base",ypos="base")
                m "What?"
                call her_head("What if I get pregnant?","shock","worriedCl")
                m "Nah, you will be alright..."
                call her_head("How do you know, [genie_name]?","shock","worriedCl")
                m "We witchers are infertile."
                call her_head("Witchers?","open","worriedCl")
                m "Sure... You are a witch, that make me a witcher, right?"
                m "And everyone knows that witchers are infertile..."
                call her_head("[genie_name], you make no sense...","angry","base")
                call her_head("Can I please just get paid now...?")

    #Second time event.
    elif hg_pf_LetsHaveSex_OBJ.points == 1:
        m "[hermione_name], are you keeping your pussy wet and ready for me?"
        call her_main("[genie_name]!","scream","angryCl")
        m "Just say \"I do\" and come over here, [hermione_name]."
        call her_main("...........","open","base")
        call her_main("I do....","angry","down_raised")
        hide screen hermione_main
        jump your_ass

    #Third time event.
    elif hg_pf_LetsHaveSex_OBJ.points >= 2:
        m "[hermione_name]..."
        m "Last night I had a dream..."
        g9 "You were lying on my desk and I was fucking your tight pussy like a madman..."
        if whoring >= 24:
            call her_main("In that dream, [genie_name]...","soft","ahegao",xpos="right",ypos="base")
        else:
            call her_main("In that dream, [genie_name]...","upset","closed",xpos="right",ypos="base")
        if whoring <= 23:
            call her_main("Did I happen to receive 65 house points afterwards?","angry","angry")
            g9 "Why yes, you did, [hermione_name]."
        else:
            call her_main("Did you cum inside me or not?","smile","baseL")
            g9 "I'm not sure [hermione_name], care to find out?"
        call her_main("...............................","disgust","glance")
        her "Let me just take my panties off..."
        stop music fadeout 1.0
        hide screen hermione_main
        call blkfade

        # SEX
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","scream","wide")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie

        call gen_chibi("hide")
        call her_chibi("hide")
        $ g_c_u_pic = "sex_ani"
        show screen chair_left
        show screen g_c_u

        if use_cgs:
            hide screen candlefire
            $ face_on_cg = True
            $ ccg_folder = "herm_sex"
            $ ccg1 = "blank"
            $ ccg2 = "blank"
            $ ccg3 = "blank"
            call her_head("","open","worriedCl")
            show screen ccg

        hide screen blktone
        hide screen bld1
        hide screen blkfade
        with fade
        call ctc

        call play_music("playful_tension") # SEX THEME.


        call her_head("Ah...{image=textheart}","open","worriedCl")
        m "Your pussy feels a bit looser today..."
        #$ ccg2 = 4
        call her_head("Does it...{image=textheart} ah...?{image=textheart}","open","worriedCl")
        #$ ccg2 = 5
        call her_head("That's all because of you [genie_name]...{image=textheart}","shock","worriedCl")
        #$ ccg2 = 6
        call her_head("You are ruining my little pussy with your monstrous penis...{image=textheart}","silly","ahegao")
        g4 "Agh, you whore!"
        #$ ccg2 = 10
        call her_head("Ah...{image=textheart}{image=textheart}","silly","ahegao")
        m "Yes! Do you like it when I fuck you like this?"
        call her_head("Yes, [genie_name]...","base","glance")
        menu:
            g4 "..."
            "\"Be sweet but passionate.\"":
                m "Yes, you're liking this?"
                #$ ccg2 = 14
                call her_head("I do, [genie_name]... ah...{image=textheart}","open","closed")
                m "Good girl!"
                m "Just relax and take my cock!"
                call her_head("Yes... ah...{image=textheart}","open","closed")
                m "All the way in... all the way..."
                call her_head("Ah...{image=textheart}{image=textheart}","open","worriedCl")
                m "Yes, my little princess..."
                #$ ccg2 = 15
                call her_head("What?","angry","wide")
                call her_head("No, please don't call me that... ah...{image=textheart}","angry","down_raised")
                call her_head("My daddy used to call me his little princess when I was little...")
                m "Well, right now I am your daddy!"
                #$ ccg2 = 16
                call her_head("Ah...{image=textheart} ah-ah...{image=textheart}{image=textheart}","soft","ahegao")
                m "And you are my little princess-slut!"
                #$ ccg2 = 17
                call her_head("Ah...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","grin","dead")
            "\"Be mean to her!\"":
                m "Yes, you slut!"
                m "I bet you love every second of this!"
                call nar(">You pick up the pace.")
                #$ ccg2 = 17
                call her_head("Ah...{image=textheart} [genie_name]...","open","worriedCl")
                m "You nasty slut!"
                call her_head("Ah...{image=textheart} ah-a...{image=textheart}","shock","worriedCl")
                m "You are a disgrace, [hermione_name]!"
                #$ ccg2 = 18
                call her_head("Ah-ah...{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
                m "Your parents sent you here to study, not to screw your teachers, you disgusting cunt!"
                #$ ccg2 = 19
                call her_head("Ah-a...{image=textheart} But I am only doing this--","shock","worriedCl")
                m "Nobody cares why you are doing this, cocksucker!"
                m "Look at what you've become!"
                m "Butt-naked, on your professor's old cock, like a cheap whore!"
                #$ ccg2 = 20
                call her_head("Ah...{image=textheart} No...{image=textheart} stop saying...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
                call nar(">You pick up the pace some more.","start")
                $ g_c_u_pic = "sex2_ani"
                call nar(">The room fills up with rhythmical sound of a flesh hitting flesh...","end")
                m "You let me molest you... You suck my cock..."
                m "What are you after that I ask you!?"
                #$ ccg2 = 21
                call her_head("................","grin","dead")
                call her_head("Ah...{image=textheart} ah....{image=textheart}{image=textheart}{image=textheart}","shock","worriedCl")
                call her_head(".......................","angry","down_raised")
                call her_head("{size=-5}I am a whore...{/size}")
                m "Yes! That's exactly what you are!"

        #$ ccg2 = 22
        call her_head("Ah... ah... ah...","angry","down_raised")
        call her_head("[genie_name], you think you could... ah...")
        m "What?"
        call her_head("Could you spank me a little... ah...?","silly","worried",cheeks="blush",tears="soft")
        g4 "Gladly!"

        call slap_her

        #$ ccg2 = 24
        call her_head("Aa-a-ah!{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft")
        m "You liked that one, huh?"

        call slap_her

        #$ ccg2 = 28
        call her_head("Ah..!{image=textheart} Yes!{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        m "And some more!"

        call slap_her

        #$ ccg2 = 29
        call her_head("Ahh! Yes!","silly","worried",cheeks="blush",tears="soft")
        call nar(">You notice that every time you slap the girl's butt, her pussy clutches your cock tightly for a second...","start")
        ">You love the sensation..."
        ">You unleash another series of slaps on Hermione's ass-cheeks."
        call nar(">Every single one met with a gasp of excitement from the girl.","end")
        #$ ccg2 = 30

        call slap_her
        call slap_her
        call slap_her
        call slap_her
        call slap_her

        #$ ccg2 = 31
        call her_head("Aah!!!{image=textheart}{image=textheart}{image=textheart} IT HURTS!{image=textheart}{image=textheart}{image=textheart}","silly","worried",cheeks="blush",tears="soft")
        #$ ccg2 = 32
        call her_head("It hurts...{image=textheart}{image=textheart}{image=textheart} It hurts...{image=textheart}{image=textheart}{image=textheart}","silly","ahegao")
        m "Hm?"
        m "Why your legs are shaking, [hermione_name]?"
        m "Are you cumming?"
        #$ ccg2 = 33
        call her_head("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","silly","dead")
        m "Well, I think I will follow your example then."
        call her_head("..............","silly","dead")
        call nar(">You start fucking Hermione with renewed determination!")
        #$ ccg2 = 34
        call her_head("Ah! No! I can't...{image=textheart} I...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","shock","baseL",cheeks="blush",tears="soft")
        m "Shut it whore!"
        g4 "Argh!"

        menu:
            "-Cum inside of Hermione-":
                with hpunch
                g4 "{size=+7}Argh, TAKE THIS!!!{/size}"
                call cum_block
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ ccg3 = "s1"
                $ g_c_u_pic = "sex_cum_in_ani"
                call cum_block
                call ctc
                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 33
                call her_head("!!!","silly","dead")
                #$ ccg2 = 38
                call her_head("AH! IT'S FILLING ME UP!{image=textheart}{image=textheart}{image=textheart}")
                g4 "I'm Not done yet, bitch!"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                call cum_block
                call her_head("AH! MY BELLY!","shock","baseL",cheeks="blush",tears="soft")
                g4 "{size=+5}SLUT!{/size}"

                hide screen bld1
                with d3
                call ctc



                $ g_c_u_pic = "images/animation/23_cum_19.png"

                #$ ccg2 = 40
                m "Well, this was pretty great..."
                call her_head("Ah...{image=textheart}","silly","dead")
                m "You alright there, slut? Ehm, I mean, [hermione_name]."
                call her_head("Yes... I...","silly","dead")
                #$ ccg2 = 41
                call her_head("I feel so full...","open_wide_tongue","ahegao")
                call her_head("!!!","scream","wide")
                call her_head("You came inside of me, [genie_name]!")
                m "I sure did."
                call her_head("You shouldn't have...","open","worriedCl")
                m "Didn't you enjoy it?"
                call her_head("....maybe.","grin","dead")
                #$ ccg2 = 42
                call her_head("I think I came several times...","soft","ahegao")
                call blkfade

                $ face_on_cg = False
                call h_update_hair

                call her_head("Maybe you are right, [genie_name], and I shouldn't worry so much.","angry","wink",xpos="base",ypos="base")
                if whoring <= 23:
                    call her_head("Can I get my payment now?")

            "-Cum all over Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                call cum_block
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                $ ccg3 = "s3"

                call cum_block
                call ctc

                $ uni_sperm = True
                $ u_sperm = "characters/hermione/face/auto_08.png"
                #$ ccg2 = 30
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","silly","dead")
                g4 "{size=+5}You whore! Take this!{/size}"
                call her_head("{size=+5}!!!{/size}","silly","worried",cheeks="blush",tears="soft")
                hide screen bld1
                with d3
                call ctc


                $ g_c_u_pic = "sex_cum_out_blink_ani"
                m "Well, that was pretty great..."
                #$ ccg2 = 31
                call her_head("Ah...{image=textheart}","silly","worried",cheeks="blush",tears="soft")
                m "You alright there, slut?"
                call her_head("Yes... I...","silly","dead")
                m "Didn't you enjoy this?"
                #$ ccg2 = 29
                call her_head("....I think so...","grin","dead")
                call ctc
                call blkfade

                $ face_on_cg = False
                call h_update_hair

                call her_head("I think I came several times, [genie_name]...","soft","ahegao",xpos="base",ypos="base")
                if whoring <= 23:
                    call her_head("Can I get my payment now?","angry","wink")
                $ uni_sperm = False #Sperm layer is not displayed in hermione screen.


    $ face_on_cg = False
    call h_update_hair

    hide screen ccg
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen chair_left
    hide screen desk
    if not daytime:
        show screen candlefire

    call her_chibi("stand","desk","base")
    call gen_chibi("hide")
    show screen genie
    pause.1
    hide screen blktone
    hide screen bld1
    call hide_blkfade
    pause.5

    call bld
    stop music fadeout 4.0
    if whoring < 24:
        m "Yes, [hermione_name]. 65 points to the \"Gryffindor\" house."
        $ gryffindor +=65
    call her_main("Thank you, [genie_name]...","soft","baseL",xpos="right",ypos="base")

    if whoring < 21: #Adds points till 21.
        $ whoring +=1

    if hg_pf_LetsHaveSex_OBJ.points == 0:
        $ new_request_29_heart = 1
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 1 #Event hearts level (0-3)
    if hg_pf_LetsHaveSex_OBJ.points == 1:
        $ new_request_29_heart = 2
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 2 #Event hearts level (0-3)
    if hg_pf_LetsHaveSex_OBJ.points >= 2:
        $ new_request_29_heart = 3
        $ hg_pf_LetsHaveSex_OBJ.hearts_level = 3 #Event hearts level (0-3)

    $ hg_pf_LetsHaveSex_OBJ.points += 1

    jump end_hg_pf  #Resets screens. Hermione walks out. Resets Hermione.
