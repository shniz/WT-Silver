

label summon_hermione:

    call play_sound("door")

    ### RANDOM CLOTHING EVENTS ###
    call hermione_random_clothing

    label hermione_requests:

    $ menu_x = 0.1
    $ menu_y = 0.5

    $ hide_transitions = False
    $ hermione_busy = True

    menu:
        "-Talk-":
            if not chitchated_with_her:
                if her_mood <= 7:
                    $ chitchated_with_her = True
                    call chit_chat
                    jump hermione_talk
                else:
                    her "I have nothing to say to you sir..."
                    jump hermione_requests
            else:
                jump hermione_talk

        "-Tutoring-" if not daytime and her_tutoring < 14: #13 is last level.
            if her_mood >=1 and her_mood < 3:
                her "I'm sorry, maybe tomorrow..."
                jump hermione_requests
            elif her_mood >=3 and her_mood < 10:
                her "I am not in the mood today..."
                jump hermione_requests
            elif her_mood >= 10 and her_mood < 20:
                her "Absolutely not, [genie_name]"
                her "I {i}might{/i} consider it once you've said sorry"
                jump hermione_requests
                # Question: What to do between 9 and 20? Only "jump l_tutoring_check"?
            elif her_mood >=20:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            else:
                jump l_tutoring_check

        "-Buy sexual favours-" if hermione_favors:
            if her_mood >=1 and her_mood < 3:
                her "I'm sorry, [genie_name], Maybe some other time..."
                jump hermione_requests
            elif her_mood >=  3 and her_mood < 10:
                her "I don't feel like it today..."
                her "Maybe in a couple of days..."
                jump hermione_requests
            elif her_mood >= 10 and her_mood < 20:
                her "No thank you...."
                jump hermione_requests
            elif her_mood >= 20 and her_mood < 30:
                her "After what you did, [genie_name]?"
                her "I don't think so..."
                jump hermione_requests
            elif her_mood >= 30 and her_mood < 40:
                her "You can't be serious!"
                jump hermione_requests
            elif her_mood >= 40:
                her "Is this some twisted joke to you, sir?!"
                her "After what you did I don't feel like doing this ever again!"
                jump hermione_requests
            else:
                jump hermione_requests_menu

        "-Wardrobe-":
            $ active_girl = "hermione"

            call load_hermione_clothing_saves

            call reset_wardrobe_vars
            call update_wr_color_list

            $ hide_transitions = True
            call her_main(xpos="wardrobe",ypos="base")
            call screen wardrobe

        #"-Ending \"Your whore\"-":
        #    $ public_whore_ending = False
        #    jump your_whore

        #"-Ending \"Public whore\"-":
        #    $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
        #    jump your_whore

        "-Dismiss her-":
            if daytime:
                if her_mood >=3 and her_mood < 7:
                    her "..............................."
                elif her_mood >=7:
                    her "*Humph!*..."
                else:
                    her "Oh, alright. I will go to classes then."
            else:
                if her_mood >=3 and her_mood < 7:
                    her "..............................."
                elif her_mood >=7:
                    her "Tch..."
                else:
                    her "Oh, alright. I will go to bed then."

            call play_sound("door")

            $ hermione_busy = True

            jump main_room



label hermione_requests_menu:
    if slytherin >= gryffindor or ravenclaw >= gryffindor or hufflepuff >= gryffindor:
        show screen hermione_main

        label silver_requests_root:
        menu:
            "-Personal favours-":
                label not_now_pf:
                python:
                    pf_menu = []
                    for i in hg_pf_list:
                        if i.imagination_level > imagination:
                            pf_menu.append(("{color=#858585}-A vague idea-{/color}","vague"))
                        else:
                            pf_menu.append((i.getMenuText(),i.start_label))
                    pf_menu.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(pf_menu)
                if result == "nvm":
                    jump silver_requests_root
                elif result == "vague":
                    call vague_idea
                    jump not_now_pf
                else:
                    $ renpy.jump(result)

            "{color=#858585}-Public requests-{/color}" if not daytime:
                show screen blktone
                with d3
                ">Public requests are available during the daytime only."
                hide screen blktone
                with d3
                jump silver_requests_root
            "-Public requests-" if daytime:
                if lock_public_favors:
                    her "Em... [genie_name]..."
                    her "I do not mind to keep selling you the favours..."
                    her "But only as long as we keep them private..."
                    jump silver_requests_root
                else:
                    label not_now_pr:
                    python:
                        pr_menu = []
                        for i in hg_pr_list:
                            if i.imagination_level > bdsm_imagination:
                                pr_menu.append(("{color=#858585}-A vague idea-{/color}","vague"))
                            else:
                                pr_menu.append((i.getMenuText(),i.start_label))
                        pr_menu.append(("-Never mind-", "nvm"))
                        result = renpy.display_menu(pr_menu)
                    if result == "nvm":
                        jump silver_requests_root
                    elif result == "vague":
                        call vague_idea
                        jump not_now_pr
                    else:
                        $ renpy.jump(result)

            "{color=#858585}-Public Shaming-{/color}" if not daytime:
                show screen blktone
                with d3
                ">Public Shaming events are available during the daytime only."
                hide screen blktone
                with d3
                jump silver_requests_root
            "-Public Shaming-"if daytime:
                label not_now_ps:
                python:
                    ps_menu = []
                    for i in hg_ps_list:
                        if i.imagination_level > bdsm_imagination:
                            ps_menu.append(("{color=#858585}-A vague idea-{/color}","vague"))
                        else:
                            ps_menu.append((i.getMenuText(),i.start_label))
                    ps_menu.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(ps_menu)
                if result == "nvm":
                    jump silver_requests_root
                else:
                    $ renpy.jump(result)

            "-Never mind-":
                jump hermione_requests


    else:
        show screen hermione_main
        with d3
        her "The Gryffindors are in the lead. I don't need to do this."
        jump hermione_requests



label hermione_talk:
    menu:
        "-Working-":
            label working_menu:
            menu:
                "-Work as a maid-" if daytime and hg_outfit_maid_ITEM.unlocked:
                    jump job_1

                "-Work as a maid-" if daytime and not hg_outfit_maid_ITEM.unlocked:
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a maid-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Work as a cheerleader for Gryffindor-" if daytime and (hg_cheer_g_ITEM.unlocked or hg_cheer_g_sexy_ITEM.unlocked):
                     jump job_3

                "-Work as a cheerleader for Gryffindor-" if daytime and not (hg_cheer_g_ITEM.unlocked or hg_cheer_g_sexy_ITEM.unlocked):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a cheerleader for Gryffindor-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Work as a cheerleader for Slytherin-" if daytime and (hg_cheer_s_ITEM.unlocked or hg_cheer_s_sexy_ITEM.unlocked):
                    jump job_4

                "-Work as a cheerleader for Slytherin-" if daytime and not (hg_cheer_s_ITEM.unlocked or hg_cheer_s_sexy_ITEM.unlocked):
                    m "(I'll need an outfit for hermione if I want her to work.)"
                    jump working_menu

                "{color=#858585}-Work as a cheerleader for Slytherin-{/color}" if not daytime:
                    "This job is only available during the day."
                    jump working_menu

                "-Never mind-":
                    jump hermione_talk

        "-Ask for a new student-" if hat_known and not luna_known:
            call luna_init
            $ luna_known = True
            jump hat_intro_2

        "-Talk about the ministry letter-" if letter_curse_complaint_OBJ.read and not astoria_unlocked:
            #You tell Hermione about the curses.
            if snape_on_the_lookout: #Already talked to Snape.
                $ hermione_finds_astoria = True
                $ days_without_an_event = 0 #So the event won't happen right after.
            if hermione_on_the_lookout:
                call her_main("I'm still looking for that student, [genie_name]!","open","closed")
                call her_main("Trust in me, I will find that slytherin scum!","angry","angry")
                jump hermione_talk
            $ hermione_busy = True
            $ hermione_on_the_lookout = True
            jump letter_intro_hermione

        "-Address me only as-":
            menu:
                "-Sir-":
                    $ genie_name = "Sir"
                    jump genie_change
                "-Dumbledore-":
                    $ genie_name = "Dumbledore"
                    jump genie_change
                "-Professor-":
                    $ genie_name = "Professor"
                    jump genie_change
                "-Old man-":
                    $ genie_name = "Old man"
                    jump genie_change
                "-Genie-":
                    if her_whoring >=5:
                        $ genie_name = "Genie"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-My Lord-":
                    if her_whoring >=7:
                        $ genie_name = "My Lord"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Darling-":
                    if her_whoring >=10:
                        $ genie_name = "Darling"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Lord Voldemort-":
                    if her_whoring >=15:
                        $ genie_name = "Lord Voldemort"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Daddy-":
                    if her_whoring >=20:
                        $ genie_name = "Daddy"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Master-":
                    if her_whoring >=20:
                        $ genie_name = "Master"
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if temp_name == "":
                        $ genie_name = "Sir"
                        jump genie_change
                    if her_whoring >=20:
                        $ genie_name = temp_name
                        jump genie_change
                    else:
                        jump genie_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-From now on I will refer to you as-":
            menu:
                "-Miss Granger-":
                    $ hermione_name = "Miss Granger"
                    jump hermione_change
                "-Girl-":
                    $ hermione_name = "Girl"
                    jump hermione_change
                "-Good Girl-":
                    if her_whoring >=5:
                        $ hermione_name = "Good Girl"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slave-":
                    if her_whoring >=10:
                        $ hermione_name = "Slave"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Princess-":
                    if her_whoring >=10:
                        $ hermione_name = "Princess"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Whore-":
                    if her_whoring >=15:
                        $ hermione_name = "Whore"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Little Girl-":
                    if her_whoring >=15:
                        $ hermione_name = "Little Girl"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Slytherin Slut-":
                    if her_whoring >=18:
                        $ hermione_name = "Slytherin Slut"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Mudblood-":
                    if her_whoring >=20:
                        $ hermione_name = "Mudblood"
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Custom Input-":
                    $ temp_name = renpy.input("(Please enter the name.)")
                    $ temp_name = temp_name.strip()
                    if hermione_name == "":
                        $ hermione_name = "Miss granger"
                    if her_whoring >=20:
                        $ hermione_name = temp_name
                        jump hermione_change
                    else:
                        jump hermione_change_fail
                "-Never mind-":
                    jump hermione_talk

        "-Start the Ending-" if her_dress_wearable: #Starts the ending of the game.
            jump start_end_events

        "-Never mind":
            jump hermione_requests


label genie_change:
    call her_main("Ok, from now on I'll call you [genie_name].","base","base")
    jump hermione_talk

label genie_change_fail:
    call her_main("I'm not calling you that!","scream","angryCl")
    jump hermione_talk

label hermione_change:
    if her_whoring >= 20:
        call her_main("You can call me whatever you want, [genie_name]!","base","glance")
    else:
        call her_main("Sure, [genie_name]. I like that name.","base","base")
    jump hermione_talk

label hermione_change_fail:
    call her_main("I'm not letting you call me that!","scream","angryCl")
    jump hermione_talk
