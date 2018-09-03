

label update_cho_uniform:
    hide screen cho_chang

    #Hair
    $ cho_hair         = "characters/cho/body/hair/hair_"+str(c_hair_style)+"_"+str(c_hair_color)+"_base.png"
    $ cho_hair_shadow  = "characters/cho/body/hair/hair_"+str(c_hair_style)+"_"+str(c_hair_color)+"_top.png"

    #Top
    $ cho_top            = "characters/cho/clothes/tops/base/"+str(c_top)+".png"

    #Bottom
    $ cho_bottom         = "characters/cho/clothes/bottoms/base/"+str(c_bottom)+".png"

    #Underwear
    $ cho_bra            = "characters/cho/clothes/underwear/base/"+str(c_bra)+".png"
    $ cho_onepiece       = "characters/cho/clothes/onepieces/base/"+str(c_onepiece)+".png"
    $ cho_panties        = "characters/cho/clothes/underwear/base/"+str(c_panties)+".png"
    $ cho_garterbelt     = "characters/cho/clothes/underwear/base/"+str(c_garterbelt)+".png"

    $ cho_neckwear       = "characters/cho/clothes/neckwear/"+str(c_neckwear)+".png"
    $ cho_gloves         = "characters/cho/clothes/gloves/"+str(c_gloves)+".png"
    $ cho_stockings      = "characters/cho/clothes/stockings/"+str(c_stockings)+".png"
    $ cho_robe           = "characters/cho/clothes/robe/"+str(c_robe)+".png"

    #Accessories
    $ cho_hat            = "characters/cho/accessories/hats/"+str(c_hat)+".png"

    return

#Hair equip.
label set_cho_hair(hair=None,color=None):
    hide screen cho_chang

    if hair != None:
        $ c_hair_style   = hair
    if color != None:
        $ c_hair_color   = color

    call update_cho_uniform
    show screen cho_chang

    return

#Hat equip.
label set_cho_hat(hat=""):
    hide screen cho_chang

    if cho_wear_hat and c_hat == hat:
        $ cho_request_wear_hat = False
        $ cho_wear_hat = False
    else:
        $ cho_request_wear_hat = True
        $ cho_wear_hat = True
        $ c_hat = hat

    call update_cho_uniform
    show screen cho_chang

    return

#Top equip.
label set_cho_top(top=""):
    hide screen cho_chang

    if cho_wear_top and c_top == top:
        $ cho_request_wear_top = False
        $ cho_wear_top = False
    else:
        $ cho_request_wear_top = True
        $ cho_wear_top = True
        $ c_top = top

    call update_cho_uniform
    show screen cho_chang

    return

#Bottom equip.
label set_cho_bottom(bottom=""):
    hide screen cho_chang

    if cho_wear_bottom and c_bottom == bottom:
        $ cho_request_wear_bottom = False
        $ cho_wear_bottom = False
    else:
        $ cho_request_wear_bottom = True
        $ cho_wear_bottom = True
        $ c_bottom = bottom

    call update_cho_uniform
    show screen cho_chang

    return

#Bra equip.
label set_cho_bra(bra=""):
    hide screen cho_chang

    $ cho_request_wear_bra = True
    $ cho_wear_bra = True
    $ c_bra = bra

    call update_cho_uniform
    show screen cho_chang

    return

#One-Piece equip.
label set_cho_onepiece(onepiece=""):
    hide screen cho_chang

    if cho_wear_onepiece and c_onepiece == onepiece:
        $ cho_request_wear_onepiece = False
        $ cho_wear_onepiece = False
    else:
        $ cho_request_wear_onepiece = True
        $ cho_wear_onepiece = True
        $ c_onepiece = onepiece

    call update_cho_uniform
    show screen cho_chang

    return

#Panties equip.
label set_cho_panties(panties=""):
    hide screen cho_chang

    $ cho_request_wear_panties = True
    $ cho_wear_panties = True
    $ c_panties = panties

    call update_cho_uniform
    show screen cho_chang

    return

#Garterbelt equip.
label set_cho_garterbelt(garter=""):
    hide screen cho_chang

    if cho_wear_garterbelt and c_garterbelt == garter:
        $ cho_request_wear_garterbelt = False
        $ cho_wear_garterbelt = False
    else:
        $ cho_request_wear_garterbelt = True
        $ cho_wear_garterbelt = True
        $ c_garterbelt = garter

    call update_cho_uniform
    show screen cho_chang

    return

#Neckwear equip.
label set_cho_neckwear(neck=""):
    hide screen cho_chang

    if cho_wear_neckwear and c_neckwear == neck:
        $ cho_request_wear_neckwear = False
        $ cho_wear_neckwear = False
    else:
        $ cho_request_wear_neckwear = True
        $ cho_wear_neckwear = True
        $ c_neckwear = neck

    call update_cho_uniform
    show screen cho_chang

    return

#Stockings equip.
label set_cho_stockings(stockings=""):
    hide screen cho_chang

    if cho_wear_stockings and c_stockings == stockings:
        $ cho_request_wear_stockings = False
        $ cho_wear_stockings = False
    else:
        $ cho_request_wear_stockings = True
        $ cho_wear_stockings = True
        $ c_stockings = stockings

    call update_cho_uniform
    show screen cho_chang

    return

#Robe equip.
label set_cho_robe(robe=""):
    hide screen cho_chang

    if cho_wear_robe and c_robe == robe:
        $ cho_request_wear_robe = False
        $ cho_wear_robe = False
    else:
        $ cho_request_wear_robe = True
        $ cho_wear_robe = True
        $ c_robe = robe

    call update_cho_uniform
    show screen cho_chang

    return


## Equip Outfit
label set_cho_outfit(outfit):
    hide screen cho_chang
    with d3
    call cho_outfit(outfit)
    pause .5
    show screen cho_chang
    with d5
    return

label cho_outfit(outfit):
    hide screen cho_chang

    if outfit == None:
        $ cho_request_wear_outfit = False
        $ cho_wear_outfit = False
    else:
        $ cho_wear_outfit = True

        $ cho_request_wear_top = True
        $ cho_wear_top = True

        $ cho_outfit_GLBL = outfit

        if cho_outfit_GLBL.hair_layer != "":
            $ c_hair_style = cho_outfit_GLBL.getHairLayers()
            $ c_hair_color = 1
        if cho_outfit_GLBL.top_layers != []:
            $ cho_request_wear_hat = True
            $ c_hat = cho_outfit_GLBL.getTopLayers()

    call load_cho_clothing_saves
    call update_cho_uniform
    show screen cho_chang

    return


label set_cho_clothing(outfit=""):
    hide screen cho_chang

    if outfit in ["uniform"]: #Remove outfit
        $ c_top                 = "top_1"
        $ c_bra                 = "bra_sport"
        $ c_panties             = "panties_sport"

        if cho_quidd_points <= 1:
            $ c_bottom              = "skirt_1"
        elif cho_quidd_points == 2:
            $ c_bottom              = "skirt_2"
        else:
            $ c_bottom              = "skirt_3"

        call load_cho_clothing_saves

    if outfit == "quidditch":
        #Temporary way of doing outfits for Cho for now
        $ c_robe                = "quidditch"
        $ c_top                 = "sweater"
        $ c_bra                 = "bra_sport"
        $ c_panties             = "panties_sport"
        $ c_gloves              = "quidditch"

        if cho_quidd_points == 0:
            $ c_bottom              = "pants_yoga_long"
        elif cho_quidd_points == 1:
            $ c_bottom              = "skirt_1"
        elif cho_quidd_points == 2:
            $ c_bottom              = "skirt_2"
        else:
            $ c_bottom              = "skirt_3"

        $ cho_wear_top = True
        $ cho_wear_bottom = True
        $ cho_wear_robe = True
        $ cho_wear_bra = True
        $ cho_wear_panties = True
        $ cho_wear_gloves = True

        $ cho_wear_accs = False
        $ cho_wear_stockings = False

    call update_cho_uniform

    return


label load_cho_clothing_saves:

    #Uniform & Underwear
    if cho_request_wear_top:
        $ cho_wear_top          = True
    else:
        $ cho_wear_top          = False

    if cho_request_wear_onepiece:
        $ cho_wear_onepiece     = True
    else:
        $ cho_wear_onepiece     = False

    if cho_request_wear_bra:
        $ cho_wear_bra          = True
    else:
        $ cho_wear_bra          = False

    if cho_request_wear_bottom:
        $ cho_wear_bottom       = True
    else:
        $ cho_wear_bottom       = False

    if cho_request_wear_panties:
        $ cho_wear_panties      = True
    else:
        $ cho_wear_panties      = False

    if cho_request_wear_garterbelt:
        $ cho_wear_garterbelt   = True
    else:
        $ cho_wear_garterbelt   = False

    #Other Clothing
    if cho_request_wear_neckwear:
        $ cho_wear_neckwear     = True
    else:
        $ cho_wear_neckwear     = False

    if cho_request_wear_accs:
        $ cho_wear_accs    = True
    else:
        $ cho_wear_accs    = False

    if cho_request_wear_gloves:
        $ cho_wear_gloves       = True
    else:
        $ cho_wear_gloves       = False

    if cho_request_wear_stockings:
        $ cho_wear_stockings    = True
    else:
        $ cho_wear_stockings    = False

    if cho_request_wear_robe:
        $ cho_wear_robe         = True
    else:
        $ cho_wear_robe         = False

    #Head Accessories
    if cho_request_wear_hat:
        $ cho_wear_hat          = True
    else:
        $ cho_wear_hat          = False

    if cho_request_wear_glasses:
        $ cho_wear_glasses      = True
    else:
        $ cho_wear_glasses      = False

    if cho_request_wear_ears:
        $ cho_wear_ears         = True
    else:
        $ cho_wear_ears         = False

    if cho_request_wear_makeup:
        $ cho_wear_makeup       = True
    else:
        $ cho_wear_makeup       = False

    if cho_request_wear_piercings:
        $ cho_wear_piercings    = True
    else:
        $ cho_wear_piercings    = False

    if cho_request_wear_tattoos:
        $ cho_wear_tattoos      = True
    else:
        $ cho_wear_tattoos      = False

    return