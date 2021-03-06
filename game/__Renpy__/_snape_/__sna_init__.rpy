

label snape_init:

    if not hasattr(renpy.store,'snape_chibi_flip') or reset_persistants:
        $ snape_xpos = 525
        $ snape_ypos = 0
        $ snape_zorder = 5
        $ snape_flip = 1
        $ use_snape_head            = False

        $ s_sprite = "characters/snape/main/snape_01.png"

        $ snape_head_xpos = 540
        $ snape_head_ypos = 380
        $ snape_head_zorder = 8

        $ snape_chibi_xpos=610
        $ snape_chibi_ypos=210
        $ snape_speed = 2.0
        $ snape_chibi_flip = 1
        $ snape_chibi_zorder = 2

        $ snape_chibi_stand = "characters/snape/chibis/snape_stand.png"
        $ snape_chibi_walk = "snape_walk"

    return



label snape_progress_init:

    if not hasattr(renpy.store,'snape_busy') or reset_persistants:

        ###SNAPE STATS###
        $ snape_busy = False #When True, you can't summon Snape.

        $ sna_support = 0 #Controls how much points is awarded to SLYTHERIN daily.
        $ snape_events = 0 #Get's +1 point every time a special event with Snape happens.
        $ sna_dates_counter = 0
        $ sna_friendship = 0 #Get's +1 after every evening spent is Snape's company.
        $ sna_friendship_maxed = False

        $ wine_intro_done = False
        $ sna_wine_counter = 0




        ### SNAPE EVENTS ###
        $ snape_against_hermione = False #Turns True after event_01. Activates event_11 when hanging out with Snape next time.
        $ snape_against_hermione_02 = False #Turns True after event_09. Activates second event when hanging out with Snape.


        ### CHITCHATS WITH SNAPE ###
        $ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night.

        $ chitchat_event_01_happened = False
        $ chitchat_event_02_happened = False
        $ chitchat_event_03_happened = False
        $ chitchat_event_04_happened = False
        $ chitchat_event_05_happened = False
        $ chitchat_event_06_happened = False
        $ chitchat_event_07_happened = False


        ### SPECIAL DATES WITH SNAPE ###
        $ snape_unlocked = False
        $ hanging_with_snape = False #Removed! Not in use anymore!

        $ date_with_snape_02_happened = False #Second date with Snape. They decide to de-throne Hermione.
                                      #Turns true after event_09

    #if not hasattr(renpy.store,'ADD') or reset_persistants:

    return
