label __init_variables:
    # TODO: set to False before release
    $ DEBUG = True
return

label debug_menu:
    
    menu:
        "-Set Herm Clothes-":
            label debug_herm_clothes:
            show screen hermione_main
            python:
                o_menu = []
                for outfit in hg_outfits:
                    o_menu.append(("-"+outfit+"-",outfit))
                o_menu.append(("-Never mind-", "nvm"))
                selection = renpy.display_menu(o_menu)
            if selection == "nvm":
                call h_outfit_OBJ(None)
                hide screen hermione_main
                jump debug_menu
            else:
                call h_outfit_OBJ(hg_outfits[selection]) 
                jump debug_herm_clothes

        "-Load Clothes Saves-":
            $ hg_clothing.load('default')
            label debug_herm_clothes_saves:
            show screen hg_main_sc
            python:
                o_menu = []
                for key in hg_clothing_saves.keys():
                    o_menu.append(("-"+key+"-",key))
                o_menu.append(("-Never mind-", "nvm"))
                selection = renpy.display_menu(o_menu)
            if selection == "nvm":
                hide screen hg_main_sc
                jump debug_menu
            else:
                $ hg_clothing.load(selection)
                jump debug_herm_clothes_saves

        "-Never mind-":
            if daytime:
                jump day_main_menu
            else:
                jump night_main_menu