label door:
    hide screen main_room_menu
    
    $ summon_list = []
    $ summon_list.append(["snape", 0 if snape_busy else 1]) if snape_unlocked else 0
    $ summon_list.append(["hermione", 0 if hermione_busy else 1]) if hermione_unlocked else 0
    $ summon_list.append(["astoria", 0 if astoria_busy else 1]) if astoria_unlocked else 0
    $ summon_list.append(["cho", 0 if cho_busy else 1]) if cho_unlocked else 0
    $ summon_list.append(["tonks", 0 if tonks else 1]) if tonks_unlocked else 0
    $ summon_list.append(["susan", 0 if susan_busy else 1]) if susan_unlocked else 0
    $ summon_list.append(["luna", 0 if susan_busy else 1]) if susan_unlocked or luna_known else 0
    
    show screen door_menu
    
    $_return = ui.interact()
    
    hide screen door_menu
    
    if not door_examined and _return == "door":
        $ door_examined = True
        hide screen genie
        show screen chair_left #Empty chair near the desk.
        show screen chair_right
        call gen_chibi("stand","door","base")
        show screen desk
        with Dissolve(0.5)
        m "A sturdy looking door..."
        m "I wonder what's behind it."
        label examining_the_door:
        menu:
            "-Knock on the door-":
                show screen blktone8
                with d3
                call play_sound("knocking")
                "*Knock-knock-knock*"
                "..................."
                hide screen blktone8
                with d3
                m "No reply..."
                jump examining_the_door
            "-Put your ear on it-":
                show screen blktone8
                with d3
                ">You put your ear on the door and listen intently..."
                m "I don't hear anything."
                hide screen blktone8
                with d3
                jump examining_the_door
            "-Kick the door-":
                show screen blktone8
                with d3
                $ renpy.play('sounds/kick.ogg')
                pause.2
                with hpunch
                "*Thump!*"
                ".............................."
                hide screen blktone8
                with d3
                m "This door could take a thousand kicks like that and it still wouldn't break..."
                m "It doesn't look like it's locked though..."
                jump examining_the_door
            "-Leave it alone-":
                m "Who knows what kind of dangers could be lurking behind that door?"
                m "I think I'll let it be for now..."
                pass

        call gen_chibi("hide")
        hide screen chair_left #Empty chair near the desk.
        hide screen desk
        show screen genie
        with d3
        jump day_main_menu

        #"-Explore the Castle-" if door_examined:
        #    if map_unlocked:
        #        hide screen main_room_menu
        #        call screen map_screen
        #    else:
        #        m "I would almost certainly get lost without a map."
        #        m "Maybe there is one hidden somewhere in this room..."
        #        jump day_main_menu


    #Astoria
    elif astoria_busy and _return == "astoria":
        if daytime:
            call nar(">Astoria is taking classes.")
            jump day_main_menu
        else:
            call nar(">Astoria is already asleep.")
            jump night_main_menu
    elif not astoria_busy and _return == "astoria": #Summoning after intro events done.
        call play_music("chipper_doodle")
        jump summon_astoria


    #Susan
    elif _return == "susan" and susan_busy:
        if daytime:
            call nar(">Susan is taking classes.")
            jump day_main_menu
        else:
            call nar(">Susan is already asleep.")
            jump night_main_menu
    elif _return == "susan" and not susan_busy:
        jump summon_susan


    #Hermione
    elif _return == "hermione" and hermione_busy:
        if daytime:
            call nar(">Hermione is taking classes.")
            jump day_main_menu
        else:
            call nar(">Hermione is already asleep.")
            jump night_main_menu
    elif _return == "hermione" and not hermione_busy:
        jump summon_hermione



    #Luna
    elif luna_known and _return == "luna" and luna_busy:
        if daytime:
            call nar(">Luna is taking classes.")
            jump day_main_menu
        else:
            call nar(">Luna is already asleep.")
            jump night_main_menu
    elif luna_known and _return == "luna" and not luna_busy:
        if not luna_reverted:
            call play_music("dark_fog") # LUNA'S THEME (placeholder probably)
        else:
            call play_music("chipper_doodle") # LUNA'S THEME (placeholder probably)
        jump summon_luna


    #Cho
    elif _return == "cho" and cho_busy:
        if daytime:
            call nar(">Cho is taking classes.")
            jump day_main_menu
        else:
            call nar(">Cho is already asleep.")
            jump night_main_menu
    elif _return == "cho" and not cho_busy:
        call play_music("chipper_doodle") # CHO'S THEME (placeholder probably)
        jump cho_menu


    #Snape
    elif _return == "snape" and snape_busy:
        call nar(">Professor Snape is unavailable.")
        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu
    elif _return == "snape" and not snape_busy:
        call play_music("dark_fog") # SNAPE'S THEME
        jump summon_snape


    #Tonks
    elif _return == "tonks" and tonks_busy:
        call nar(">Tonks is unavailable.")
        if daytime:
            jump day_main_menu
        else:
            jump night_main_menu
    elif _return == "tonks" and not tonks_busy:
        jump summon_tonks
    
    elif _return=="Close":
        jump day_main_menu
    
    $ renpy.jump(_return)
    
screen door_menu:
    zorder 8
    add "images/backgrounds/desk.png"
    use close_button
    use map_screen
    use generic_character_select(summon_list, "-Summon-", 812, 23)
    