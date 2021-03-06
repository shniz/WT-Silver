
screen room_back:
    if daytime:
        add "interface/map/room_bg1.png"
    else:
        add "interface/map/room_bg2.png"
    zorder 0

screen cg: #Used in tentacle event.
    tag cg_screen

    add cg_image

    zorder 4

screen ccg:
    tag cg_screen

    add "images/CG/"+ccg_folder+"/base.png"
    add "images/CG/"+ccg_folder+"/"+str(ccg1)+".png"
    add "images/CG/"+ccg_folder+"/"+str(ccg2)+".png"
    add "images/CG/"+ccg_folder+"/"+str(ccg3)+".png"

    zorder 4

screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    zorder 3

screen animation_feather: #Falling feather animation
    add "feather" xpos 360+140 ypos 140
    zorder 2

screen notes: #A bunch of notes poping out with a "win" sound effect.
    add "notes" xpos 320+140 ypos 330
    zorder 1

#################################################################
#########JJ  Flower production/dismissal  #######################
screen H_Flowers_in:  #  Hermione waves her wand and produces flowers
    add "flower_appear" xpos 198+140 ypos 233
    zorder 1

screen H_Flowers_out:  #  Hermione waves her wand and flowers vanish
    add "vanish_effect_flower" xpos 198+140 ypos 235
    zorder 5

screen G_Flowers_in:  #  Genie produces flowers
    add "bouquet_appear" xpos 198+140 ypos 235
    zorder 1

screen G_Flowers_out:  #  Genie flowers vanish
    add "vanish_effect_bouquet" xpos 198+140 ypos 235
    zorder 5



screen phoenix_food: #Phoenix's food.
    tag phoenix_food
    add "images/rooms/main_room/06_phoenix_food.png" xpos 490 ypos 49
    zorder 2


screen fireplace: #Used to display a fireplace in a different room. Not needed for main room. Included in screen "main_room".
    tag fireplace
    add "images/rooms/main_room/fireplace_w_shadow.png" at Position(xpos=693, ypos=277, xanchor="center", yanchor="center")
    zorder 1

screen fireplace_fire: #Used to display fire without the fireplace.
    tag fireplace_fire
    add "fireplace_fire" xpos 576 ypos 141 #xpos 576 ypos 141
    zorder 2

screen fireplace_glow:
    add "glow_effect" xpos 680 ypos 300 zoom 0.4 alpha 0.15
    zorder 3

$ width_offset = 140



screen desk: #Desk only!
    add "images/rooms/main_room/desk_with_shadow.png" at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")
    zorder 2

screen chair_left:
    add "images/rooms/main_room/chair_left_with_shadow.png" at Position(xpos=332, ypos=300, xanchor="center", yanchor="center")
screen chair_right:
    add "images/rooms/main_room/chair_right.png" at Position(xpos=793, ypos=300, xanchor="center", yanchor="center")
    zorder 1

#Mail
screen owl:
    tag owl

    if letter_queue_list != []: #Owl with letter.
        add "images/rooms/main_room/owl_01.png" at Position(xpos=455, ypos=270, xanchor="center", yanchor="center")
    else:
        add "images/rooms/main_room/owl_05.png" at Position(xpos=455, ypos=270, xanchor="center", yanchor="center")

screen package:
    add "images/rooms/main_room/owl_06" +str(room_deco)+ ".png" at Position(xpos=400, ypos=235, xanchor="center", yanchor="center")



screen dumbledore: # DUMBLEDORE AND HIS DESK.
    tag chibi_genie
    add "images/rooms/main_room/dum.png" at Position(xpos=370, ypos=336, xanchor="center", yanchor="center")

### EMO
screen thought: #Thinking emotion over a chibi.
    tag emo
    add "thought" xpos tt_xpos+140 ypos tt_ypos
    zorder 2




screen universal_walk:
    tag chibi_walk
    add universal_walk_image at universal_chibi_walk(u_walk_x, u_walk_x2, u_walk_speed, u_walk_y)


### MISC SCREENS
screen bld1:
    tag bld
    add "interface/bld.png"
    zorder 3

screen ctc:
    add "ctc4"
    zorder 9

screen points: #House points screen.
    add "interface/points/TopUI_Bar.png" at Position(xpos=0+140, ypos=1)
    hbox:
        spacing 10 xpos 177 ypos 11
        text "{size=-5}[ravenclaw]{/size}"
    hbox:
        spacing 10 xpos 286 ypos 11
        text "{size=-5}[slytherin]{/size}"
    hbox:
        spacing 10 xpos 392 ypos 11
        text "{size=-5}[gryffindor]{/size}"
    hbox:
        spacing 10 xpos 505 ypos 11
        text "{size=-5}[hufflepuff]{/size}"
    hbox: ### DAYS COUNTER ###
        spacing 10 xpos 615 ypos 10
        text "{size=-3}[day]{/size}"
    hbox: ### GOLD COUNTER ###
        spacing 10 xpos 730 ypos 10
        text "{size=-4}[gold]{/size}"
    zorder 2


screen gift:
    zorder 6
    add "interface/frames/"+str(interface_color)+"/reward_background.png" at Position(xalign=0.5, yalign=0.547)
    add the_gift at Position(xalign=0.5, yalign=0.5)


label give_reward(text="",gift=""):

    $ renpy.play('sounds/win2.mp3')
    show screen notes
    with d9
    hide screen notes
    with d3

    if gift!="":
        $ the_gift = gift
    else:
        $ the_gift = "interface/icons/box_blue_2.png"

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    $ reward_text = text

    show screen gift
    show screen blktone5
    with d3

    menu:
        "[reward_text]"
        "-Done Reading-":
            pass

    hide screen gift
    hide screen blktone5
    with d3

    $ menu_y = 0.5 #return to default menu align

    return


screen clothing_unlock:
    zorder 6
    add "interface/store/"+str(interface_color)+"/clothing_panel_B.png" at Position(xalign=0.5, ypos=100)
    add mannequin_preview xalign 0.47 ypos 52 zoom 0.6/scaleratio

label unlock_clothing(text="",item=None):

    $ renpy.play('sounds/win2.mp3')
    show screen notes
    with d9
    hide screen notes
    with d3

    if item != None:
        $ mannequin_preview = item.get_image()
    else:
        $ mannequin_preview = "interface/icons/outfits/mannequin_1.png"

    $ menu_x = 0.5
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.

    show screen clothing_unlock
    show screen blktone5
    with d3

    menu:
        "[text]"
        "-Done Reading-":
            pass

    hide screen clothing_unlock
    hide screen blktone5
    with d3

    $ item.unlocked = True

    $ menu_y = 0.5 #return to default menu align

    return




screen blkfade:
    zorder 6
    add "interface/blackfade.png"

screen whitefade:
    zorder 6
    add "interface/whitefade.png"

screen blktone:
    tag blktone
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone2:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.2)

screen blktone5: #For narrator. (label nar) #Don't add tag blktone!
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.8)

screen whitetone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/white.jpg", 0.8)

screen white:
    zorder 3
    add "interface/white.jpg"

screen emo: #Character talking off screen.
    #zorder 3
    add "emo8" at Position(xpos=840, ypos=100, xanchor=0, yanchor=0)

### DUEL ###
screen snape_defends:
    add "ch_sna defend" at Position(xpos=-90+140, ypos=-5)
    zorder 2

### DAMAGE ###

screen minus_0:
    add "minus_0" at Position(xpos=780, ypos=120)
screen minus_50:
    add "minus_50" at Position(xpos=780, ypos=120)
screen minus_100:
    add "minus_100" at Position(xpos=780, ypos=120)

screen minus_300:
    add "minus_300" at Position(xpos=780, ypos=120)
screen minus_400:
    add "minus_400" at Position(xpos=780, ypos=120)
screen minus_500:
    add "minus_500" at Position(xpos=780, ypos=120)


#GENIE HEALTH LOSS
screen minus_0_genie:
    add "minus_0" at Position(xpos=450, ypos=120)
screen minus_50_genie:
    add "minus_50" at Position(xpos=450, ypos=120)
screen minus_100_genie:
    add "minus_100" at Position(xpos=450, ypos=120)

screen minus_300_genie:
    add "minus_300" at Position(xpos=450, ypos=120)
screen minus_400_genie:
    add "minus_400" at Position(xpos=450, ypos=120)
screen minus_500_genie:
    add "minus_500" at Position(xpos=450, ypos=120)

#GENIE HEALTH GAIN
screen plus_300:
    add "plus_300" at Position(xpos=450, ypos=120)



### HANGING WITH SNAPE ###

screen with_snape:
    add "images/rooms/main_room/with_snape.png" at Position(xpos=140, ypos=0)
    tag hanging_with_snape
    zorder 3

screen with_snape_animated:
    add "genie_toast_goblet" at Position(xpos=140, ypos=0)
    tag hanging_with_snape
    zorder 3



screen c_scene: #Snape Classroom Scene
    tag gc
    add "images/CG/scene_01.png" xpos 140 ypos 0
    zorder 4



screen ch_hotdog:
    add "ch_hem hotdog" xpos -70 ypos 10 #Desk sex ani.
    zorder 0


screen s_head: #Snape. Head.
    tag head
    add s_sprite xpos tt_xpos+140 ypos tt_ypos # x = 330, Right bottom corner: y = 340
    zorder 8

screen s_head2: #Snape. Head.
    tag head
    add s_sprite xpos snape_head_xpos+140 ypos snape_head_ypos # x = 330, Right bottom corner: y = 340
    zorder 8


label teleport(position=None):
    if position == "genie":
        $ teleport_xpos = genie_chibi_xpos+75
        $ teleport_ypos = genie_chibi_ypos-15
        $ teleport_zorder = 3
    elif position == "hermione":
        $ teleport_xpos = hermione_chibi_xpos+45
        $ teleport_ypos = hermione_chibi_ypos-80
        $ teleport_zorder = 3
    elif position == "desk":
        $ teleport_xpos = 320
        $ teleport_ypos = 160
        $ teleport_zorder = 1
        show screen desk


    $ renpy.play('sounds/magic4.ogg')
    show screen whitefade
    with d1

    hide screen whitefade
    with d1

    show screen blkfade
    with d1

    hide screen blkfade
    show screen heal_animation
    with d3

    #stop music fadeout 1

    hide screen heal_animation
    show screen teleport_animation
    with d5

    hide screen teleport_animation
    with d5
    pause 1

    return

screen teleport_animation:
    add "teleport_ani" xalign 0.5 xpos teleport_xpos ypos teleport_ypos+60 zoom 0.5
    zorder teleport_zorder

screen heal_animation:
    add "heal_ani" xalign 0.5 xpos teleport_xpos ypos teleport_ypos zoom 0.5
    zorder teleport_zorder



### ENDING UNIVERSAL 01 ###
screen end_u_1:
    tag ending
    add "interface/blackfade.png"
    add end_u_1_pic at Position(xpos=140,ypos=0)
    zorder 2

### ENDING UNIVERSAL 02 ###
screen end_u_2:
    tag ending
    add "interface/blackfade.png"
    add end_u_2_pic at Position(xpos=140,ypos=0)
    zorder 2

### ENDING UNIVERSAL 03 ###
screen end_u_3:
    add end_u_3_pic at Position(xpos=140,ypos=0)
    zorder 2

### ENDING UNIVERSAL 04 ###
screen end_u_4:
    add end_u_4_pic at Position(xpos=140,ypos=0)
    zorder 2




screen credits_chibi: # ONE CHIBI
    zorder 5
    add dermo at Position(xpos=420, ypos=140)


screen credits_chibi2: # TWO CHIBIs
    zorder 5
    add dermo at Position(xpos=290, ypos=140)

screen uni_cr: # UNIVERSAL CREDITS CHIBI
    zorder 5
    add dermo at Position(xpos=xder+140, ypos=yder)





### LOLA ###

screen l_head: #Screen that shows a full sprite of HERMIONE.
    tag head
    zorder 8
    add lola_body xpos lx+140 ypos ly
    add lola_face xpos lx+140 ypos ly
    if l_blush:
        add "characters/misc/lola/blush.png" xpos lx+140 ypos ly
    if l_things:
        add "characters/misc/lola/things.png" xpos lx+140 ypos ly
    if l_question:
        add "characters/misc/lola/question.png" xpos lx+140 ypos ly
    if l_drop:
        add "characters/misc/lola/drop.png" xpos lx+140 ypos ly
    if l_hearts:
        add "characters/misc/lola/hearts.png" xpos lx+140 ypos ly
    if l_exclamation:
        add "characters/misc/lola/exclamation.png" xpos lx+140 ypos ly
    if l_tears:
        add "characters/misc/lola/tears.png" xpos lx+140 ypos ly



### CGs ###
screen snape_groping:
    add "images/CG/scene_01.png"
    zorder hermione_chibi_zorder

screen snape_facial:
    add "images/CG/scene_03.png"
    zorder hermione_chibi_zorder

screen snape_sex:
    add "images/CG/scene_04.png"
    zorder hermione_chibi_zorder

screen dual_hand_job:
    add "images/CG/scene_02.png"
    zorder hermione_chibi_zorder

screen blkback:
    zorder 1
    add "interface/blackfade.png"

screen sccg:
    add "interface/blackfade.png"
    add sc_cg_base xpos sccgxpos ypos sccgypos
    add sc_cg_image_1 xpos sccgxpos ypos sccgypos
    add sc_cg_image_2 xpos sccgxpos ypos sccgypos
    add sc_cg_image_3 xpos sccgxpos ypos sccgypos

    zorder 6



### Menu Screens ###

#Close Button.
screen close_button(offsetx = 0, offsety = 0, close_var=lambda : "Close"):
    imagebutton:
            xpos 1028-offsetx
            ypos 11-offsety
            idle "interface/general/"+interface_color+"/button_close.png"
            hover "interface/general/"+interface_color+"/button_close_hover.png"
            action Return(close_var())


init python:###THANKS TO CLEANZO FOR WRITING THIS CODE

    def cg(image):
        global cg_image
        ###HIDE OLD SCREEN
        renpy.hide_screen("cg")
        #renpy.with_statement(Dissolve(0.5))
        if image is not None:
            cg_image = image
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cg")
        renpy.with_statement(Dissolve(0.5))

    def ccg(layer1=None, layer2=None, layer3=None):
        global ccg1
        global ccg2
        global ccg3

        if layer1 is not None:
            ccg1 = layer1
        if layer2 is not None:
            ccg2 = layer2
        if layer3 is not None:
            ccg3 = layer3
        renpy.show_screen("ccg")
        renpy.with_statement(Dissolve(0.5))


    def sc34CG(scene=None, image1=None, image2=None, image3=None):
        global sc_cg_base
        global sc_cg_image_1
        global sc_cg_image_2
        global sc_cg_image_3
        ###HIDE OLD SCREEN
        renpy.hide_screen("sccg")
        renpy.hide_screen("blkfade")
        #renpy.with_statement(Dissolve(0.5))
        if scene is not None:
            sc_cg_base = "images/CG/sc34/"+str(scene)+"/base_1.png"
        if image1 is not None:
            sc_cg_image_1 = "images/CG/sc34/"+str(scene)+"/A_"+str(image1)+".png"
        else:
            sc_cg_image_1 = "blank.png"
        if image2 is not None:
            sc_cg_image_2 = "images/CG/sc34/"+str(scene)+"/B_"+str(image2)+".png"
        else:
            sc_cg_image_2 = "blank.png"
        if image3 is not None:
            sc_cg_image_3 = "images/CG/sc34/"+str(scene)+"/C_"+str(image3)+".png"
        else:
            sc_cg_image_3 = "blank.png"
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("sccg")
        renpy.with_statement(Dissolve(0.5))
