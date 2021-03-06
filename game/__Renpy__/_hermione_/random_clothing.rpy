

#Door Events (Hermione wears random clothing.)

label hermione_random_clothing:
    call load_hermione_clothing_saves

    $ hermione_costume = False
    $ hermione_wear_top         = True
    $ hermione_wear_bottom      = True

    $ random_number = renpy.random.randint(1, 10)

    # Rainy and Thundery Weather.
    if weather_gen >= 5:

        if random_number in [1,2,3,4,5]: #50% chance

            #One time event.
            if not hg_accs_wool_g_ITEM.unlocked and not hermione_door_event_happened:
                $ hg_accs_wool_g_ITEM.unlocked = True
                $ hermione_door_event_happened = True #Hermione won't greet you again.

                $ hermione_wear_neckwear    = True
                $ hermione_wear_gloves      = True
                $ hermione_wear_stockings   = True
                $ h_neckwear = "scarf_striped_g"
                $ h_gloves = "gloves_wool_short_g"
                $ h_stockings = "stockings_striped_g"

                call update_her_uniform
                call her_chibi("stand","mid","base")
                pause.2
                call her_main("","base","base",xpos="base",ypos="base")
                call ctc

                m "..."
                m "[hermione_name],..."
                m "What's with all these clothes you are wearing?"

                call her_main("[genie_name], it's raining outside! I don't want to get a cold.","open","base")
                m "It's not raining in here..."
                call her_main("Yes, but it's a bit cold, [genie_name], and my...","soft","baseL",cheeks="blush")

                if her_whoring < 11:
                    call her_main("I better not mention it...","disgust","down",cheeks="blush")
                elif her_whoring < 18:
                    call her_main("{size=-5}People can see my... my nipples...{/size}","disgust","down",cheeks="blush")
                else:
                    call her_main("I can't have my nipples poking out all the time, [genie_name]! It's distracting!","annoyed","angryL")

                call her_main("","soft","base")
                pause.2
                m "Alright,... It looks cute on you."
                m "You can keep it on for now."
                call her_main("Thank you, [genie_name].","base","base")

                $ h_request_wear_top = True
                $ h_request_wear_bottom = True
                $ h_request_wear_neckwear = True
                $ h_request_wear_gloves = True
                $ h_request_wear_stockings = True

                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_accs_wool_g_ITEM)


            elif not hg_muggle_cold_ITEM.unlocked and not hermione_door_event_happened:
                $ hg_muggle_cold_ITEM.unlocked = True
                $ hermione_door_event_happened = True #Hermione won't greet you again.

                $ h_request_wear_stockings = True

                $ hermione_wear_neckwear    = False
                $ hermione_wear_gloves      = False
                $ hermione_wear_stockings = True
                $ h_top = "normal_pullover"
                $ h_bottom = "skirt_belted_mini"
                $ h_stockings = "stockings_pantyhose"

                call update_her_uniform
                call her_chibi("stand","mid","base")
                pause.2
                call her_main("","base","base",xpos="base",ypos="base")
                call ctc

                m "New outfit?"
                call her_main("Yes, [genie_name]. I brought it with me from home. It's a bit too cold for just my normal uniform...","open","baseL")
                call her_main("Do you like it?","soft","base")
                g9 "I do, [hermione_name]. It's cute."
                $ her_mood -= 10

                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_ITEM)

            elif her_whoring >= 5 and hg_muggle_cold_ITEM.unlocked and not hg_muggle_cold_sexy_ITEM.unlocked and not hermione_door_event_happened:
                $ hg_muggle_cold_sexy_ITEM.unlocked = True
                $ hermione_door_event_happened = True #Hermione won't greet you again.

                $ h_request_wear_stockings = True

                $ hermione_wear_neckwear    = False
                $ hermione_wear_gloves      = False
                $ hermione_wear_stockings   = True
                $ h_top = "normal_pullover_sexy"
                $ h_bottom = "skirt_belted_micro"
                $ h_stockings = "stockings_pantyhose"

                call update_her_uniform
                call her_chibi("stand","mid","base")
                pause.2
                call her_main("","base","base",xpos="base",ypos="base")
                call ctc

                m "That's quite the cute outfit, [hermione_name]."
                call her_main("Thank you, [genie_name]. I made some changes to the old one...","open","baseL")
                call her_main("Do you like it?","soft","base")
                g9 "Very much so, [hermione_name]. I love the breast window."
                $ her_mood -= 10

                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_cold_sexy_ITEM)

            elif not hg_muggle_rainy_ITEM.unlocked and not hermione_door_event_happened:
                $ hg_muggle_rainy_ITEM.unlocked = True
                $ hermione_door_event_happened = True #Hermione won't greet you again.

                $ aftersperm = True
                $ hermione_wear_neckwear    = False
                $ hermione_wear_gloves      = False
                $ h_top = "normal_sweater"
                $ h_bottom = "pants_jeans_long"

                call update_her_uniform
                call her_chibi("stand","mid","base")
                pause.2
                call her_main("","disgust","down",xpos="base",ypos="base")
                call ctc

                m "Damn girl. You look drenched..."
                call her_main("I'm sorry, [genie_name], but... It's raining cats and dogs out there!","open","base")
                call her_main("I couldn't find my robe so I just put on a sweater and some jeans...","open","baseL")
                call her_main("I hope you don't mind my uniform not being up for standards. I didn't want it to get wet.","disgust","down")
                m "It's fine, [hermione_name]."
                g9 "Besides, I wouldn't mind seeing you in jeans more often!"
                call her_main("Thank you, [genie_name].","normal","baseL")
                $ her_mood -= 10

                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_rainy_ITEM)



        #Hermione wears a robe.
        else:

            $ hermione_wear_robe = True
            call update_her_uniform

            call her_chibi("stand","mid","base")

            if her_mood > 1:
                call her_main("","annoyed","baseL",xpos="base",ypos="base")
            else:
                call her_main("","base","base",xpos="base",ypos="base")

            if not h_request_wear_robe:
                pause.5 #Shows Hermione with robe for a bit.

    # Clear Weather.
    else:
        if daytime and random_number in [1,2,3,4,5]: #50% chance:

            if not hg_muggle_hot_ITEM.unlocked and not hermione_door_event_happened and her_whoring >= 5:
                $ hg_muggle_hot_ITEM.unlocked = True
                $ hermione_door_event_happened = True #Hermione won't greet you again.

                $ hermione_wear_neckwear    = False
                $ hermione_wear_gloves      = False
                $ hermione_wear_stockings   = True
                $ h_top = "normal_waitress_top"
                $ h_bottom = "pants_jeans_short"
                $ h_stockings = "stockings_cute"

                call update_her_uniform
                call her_chibi("stand","mid","base")

                pause.2
                call her_main("","base","base",xpos="base",ypos="base")
                call ctc

                g4 "(Wow! Look at her!)"
                g9 "That's quite a sexy outfit, [hermione_name]!"
                if her_whoring < 11:
                    call her_main("Uhm... Thanky you, [genie_name].","soft","baseL")
                    call her_main("I normally don't wear something like this.","open","base")
                    call her_main("(Showing so much cleavage...)","disgust","down",cheeks="blush")
                    call her_main("But the weather is just too hot today.","base","baseL")
                    g9 "You should wear this more often!"
                else:
                    call her_main("Thanky you, [genie_name].","base","glance")

                #Unlocks rewards.
                call unlock_clothing(text = ">New clothing items for Hermione have been unlocked!", item = hg_muggle_hot_ITEM)


    #Resets her clothing.
    call her_chibi("stand","mid","base")
    pause.2
    call load_hermione_clothing_saves
    call update_her_uniform

    #Hermione greeting.
    if her_mood >= 1:

        call set_her_face(change="all")
        call her_main(xpos="base",ypos="base")
        if her_mood >=1 and her_mood < 3:
            ">Looks like Hermione is still a little upset with you..."
        elif her_mood >=3 and her_mood < 10:
            ">Hermione is upset with you."
        elif her_mood >=10 and her_mood < 20:
            ">Hermione is very upset with you."
        elif her_mood >=20 and her_mood < 40:
            ">Hermione is her_mood at you."
        elif her_mood >=40 and her_mood < 50:
            ">Hermione is very her_mood at you."
        elif her_mood >=50 and her_mood < 60:
            ">Hermione is furious at you."
        elif her_mood >=60:
            ">Hermione hates your guts."

    else: #Not mad.
        call set_her_face(change="all")
        if not hermione_door_event_happened:
            call her_main("Yes, [genie_name]?",xpos="base",ypos="base")
        else:
            call her_main(xpos="base",ypos="base")

    return
