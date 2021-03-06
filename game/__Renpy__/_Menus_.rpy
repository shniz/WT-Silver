

### Universal Menus ###

#List Menu #Customizable
screen list_menu(menu_items, title, toggle1="", toggle2="", toggle3="", toggle4=""):
    $ items_shown=4
    zorder 5

    #Close Button.
    use close_button

    #Up Button.
    imagebutton:
        xpos 825
        ypos 240
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not current_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")

    #Down Button.
    imagebutton:
        xpos 825
        ypos 292
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if current_page < math.ceil((len(menu_items)-1)/items_shown):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")

    #Main Store Window.
    imagemap:
        xsize 638
        ysize 544
        xalign 0.5
        yalign 0.5

        ground "interface/store/"+interface_color+"/items_panel.png"
        hover "interface/store/"+interface_color+"/items_panel_hover.png"

        if toggle1 != "": #Top left
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle1_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319, 31, 115, 22) clicked Return("toggle1")
            add toggle1_image xpos 322 ypos 30 zoom 0.8
            text "{size=10}" + toggle1 + "{/size}" xpos 342 ypos 35

        if toggle2 != "": #Borrom left
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle2_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319, 31+20, 115, 22) clicked Return("toggle2")
            add toggle1_image xpos 322 ypos 30+22 zoom 0.8
            text "{size=10}" + toggle2 + "{/size}" xpos 342 ypos 35+20

        if toggle3 != "": #Top right
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle3_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319+114, 31, 115, 22) clicked Return("toggle3")
            add toggle1_image xpos 322+115 ypos 30 zoom 0.8
            text "{size=10}" + toggle3 + "{/size}" xpos 342+115 ypos 35

        if toggle4 != "": #Borrom right
            $ toggle1_image = "interface/general/"+interface_color+"/check_true.png" if toggle4_bool else "interface/general/"+interface_color+"/check_false.png"
            hotspot (319+114, 31+20, 115, 22) clicked Return("toggle4")
            add toggle1_image xpos 322+115 ypos 30+22 zoom 0.8
            text "{size=10}" + toggle4 + "{/size}" xpos 342+115 ypos 35+20

        hbox:
            xpos 5
            ypos 30
            xsize 300
            ysize 41
            text title xalign 0.5 yalign 0.5 size 16 bold 0.2

        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                if menu_items[i].unlockable == False: #Unlockables are shown but aren't buyable/clickable
                    hotspot (12, 86+90*(i-(current_page*items_shown)), 540, 90) clicked Return(menu_items[i])
                use list_menu_item(menu_items[i], 77+90*(i-(current_page*items_shown)))


screen list_menu_item(menu_item, ypos=0):
    frame:
        background #00000000
        xpos 12
        ypos ypos
        xsize 530
        ysize 100

        $ image_zoom = get_zoom(menu_item.get_image(), 82, 81)

        vbox:
            xpos 0
            ypos 1
            xsize 82
            ysize 81
            add menu_item.get_image() xalign 0.5 yalign 0.5 zoom image_zoom

        vbox:
            xpos 100
            ypos 5
            xsize 440
            ysize 22
            text menu_item.get_name() size 16 yalign 0.5

        vbox:
            xpos 100
            ypos 35
            xsize 430
            ysize 55
            text menu_item.get_description() size 12

        text menu_item.get_buttom_right() xalign 1.0 yalign 1.0



#Clothing Menu #Customizable
screen clothing_menu(menu_items, character, preview):
    $ items_shown=3
    zorder 5

    #Close Button.
    use close_button

    #Up Button.
    imagebutton:
        xpos 725
        ypos 240
        idle "interface/general/"+interface_color+"/button_arrow_up.png"
        if not current_page <= 0:
            hover "interface/general/"+interface_color+"/button_arrow_up_hover.png"
            action Return("dec")

    #Down Button.
    imagebutton:
        xpos 725
        ypos 292
        idle "interface/general/"+interface_color+"/button_arrow_down.png"
        if current_page < math.ceil((len(menu_items)-1)/items_shown):
            hover "interface/general/"+interface_color+"/button_arrow_down_hover.png"
            action Return("inc")

    #Left Button (Bottom right of screen).
    imagebutton:
        xpos 977
        ypos 544
        idle "interface/general/"+interface_color+"/button_arrow_left.png"
        if character >= character_choice_list[1]:
            hover "interface/general/"+interface_color+"/button_arrow_left_hover.png"
            action Return("left")

    #Right Button (Bottom right of screen).
    imagebutton:
        xpos 1029
        ypos 544
        idle "interface/general/"+interface_color+"/button_arrow_right.png"
        if character < character_choice_list[-1]:
            hover "interface/general/"+interface_color+"/button_arrow_right_hover.png"
            action Return("right")

    #Bag of Gold Icon
    if preview != None:
        imagebutton:
            xpos 705
            ypos 490
            if gold >= preview.cost:
                idle  "interface/general/gold_bag.png"
                hover "interface/general/gold_bag_hover.png"
            else:
                idle  grayTint("interface/general/gold_bag.png")
                hover grayTint("interface/general/gold_bag.png")
            action Return("buy") #Buys whatever is currently previewed (item_choice)


    #Main Store Window.
    imagemap:
        xpos 0
        ypos 0

        if preview == None:
            ground "interface/store/"+str(interface_color)+"/clothing_panel_main.png"
            hover "interface/store/"+str(interface_color)+"/clothing_panel_main_hover.png"
        else:
            ground "interface/store/"+str(interface_color)+"/clothing_panel_full.png"
            hover "interface/store/"+str(interface_color)+"/clothing_panel_full_hover.png"

            #Item Information Display Panel.
            text preview.get_name() xpos 83 ypos 458 size 16
            text preview.get_description() xpos 85 ypos 490 size 12
            text preview.get_type() xpos 509 ypos 458 size 16

            for i in range(0,len(preview.get_items() )):
                $ row = i % 3
                $ col = i % 2
                text "+"+preview.get_items()[i] xpos 511+(80*col) ypos (490+(12*row)) size 12

            text preview.get_wait_time() xpos 83 ypos 557 size 16
            text preview.get_cost() xpos 509 ypos 557 size 16

        #Mannequin Display Panels.
        for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
            if i < len(menu_items):
                hotspot( 70+(227*(i-(current_page*items_shown))) , (107) , 175 , 284 ) clicked Return(menu_items[i])

                add menu_items[i].get_image() xpos (-7+(227*(i-(current_page*items_shown)) )) ypos 30 zoom 0.6/scaleratio

        #Large Mannequin Preview.
        if preview != None:
            add preview.get_image() xpos 600 ypos 0 zoom 1.0/scaleratio
        else:
            add "interface/icons/outfits/mannequin_"+str(character)+".png" xpos 600 ypos 0 zoom 1.0/scaleratio



#Character Select Menu #Customizable
screen character_select_menu(character_list=[], menu_text="menu name", xposition=24, yposition=52):

    imagemap:
        xpos xposition
        ypos yposition
        xsize 198
        ysize 548

        ground "interface/stat_select/"+str(interface_color)+"/ground_character_screen_"+str(wardrobe_color)+".png"
        hover "interface/stat_select/"+str(interface_color)+"/hover_character_screen_"+str(wardrobe_color)+".png"

        vbox:
            xpos 11
            ypos 31
            xsize 173
            ysize 41
            text menu_text xalign 0.5 yalign 0.5  size 14

        for i in range(0,len(character_list)):
            $ row = i // 2
            $ col = i % 2

            $ button_image = im.FactorScale(get_head_icon(character_list[i][0]), 0.4) if character_list[i][1] == 1 else grayTint(im.FactorScale(get_head_icon(character_list[i][0]), 0.4))



            hotspot(13+(90*col), 87+(92*row), 83, 85) clicked Return(character_list[i][0])

            add button_image xpos (90*col) ypos 92+(92*row)





### Menu Init ###

init -2 python:

    def grayTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(1.1, 1.1, 1.1))

    def yellowTint(image):
        return im.MatrixColor( image,  im.matrix.tint(1.2, 1.1, 0.7))

    toggle1_bool = True
    toggle2_bool = True
    toggle3_bool = True
    toggle4_bool = True

    def get_head_icon(name):
        return "interface/icons/head/head_"+str(name)+"_1.png"

    def get_zoom(image, xsize, ysize):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]

        if x > y:
            return xsize / x
        else:
            return ysize / y
