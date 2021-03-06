

label luna_init:

    if not hasattr(renpy.store,'luna_base') or reset_persistants or reset_luna_content:
        label reset_luna_base:

        #Body
        $ luna_base              = "characters/luna/body/base/base_01.png"
        $ luna_l_arm             = 1
        $ luna_r_arm             = 1
        $ luna_xpos              = 640
        $ luna_ypos              = 0
        $ luna_zorder            = 5
        $ luna_flip              = 1
        $ use_luna_head          = False

        #Hair
        $ luna_hair              = "characters/luna/body/hair/playful_blonde_base.png"
        $ luna_hair_shadow       = "characters/luna/body/hair/playful_blonde_top.png"
        $ lun_hair_style         = "playful"
        $ lun_hair_color         = "blonde"

        #Face
        $ luna_mouth             = "characters/luna/face/mouth/base.png"
        $ luna_eye               = "characters/luna/face/eyes/base.png"
        $ luna_eyebrow           = "characters/luna/face/brow/base.png"
        $ luna_pupil             = "characters/luna/face/pupil/blue/mid.png"
        $ luna_pupil_color       = "blue"

        $ luna_cheeks            = "characters/luna/face/extras/cheeks_blank.png"
        $ luna_tears             = "characters/luna/face/extras/tears_blank.png"
        $ luna_extra             = "characters/luna/face/extras/blank.png"
        $ luna_emote             = "characters/emotes/blank.png"

        $ changeCho("base","base","base","mid","blank","blank","blank","blank")

        #Cum
        $ luna_cum               = 1
        $ luna_wear_cum          = False
        $ luna_wear_cum_under    = False

        #Chibi
        $ luna_chibi_image       = "characters/luna/chibis/luna_stand.png"
        $ luna_chibi_stand       = "characters/luna/chibis/luna_stand.png"
        $ luna_chibi_blink       = "ch_lun blink_a"
        $ luna_chibi_blink_f     = "ch_lun blink_a_flip"
        $ luna_chibi_walk        = "ch_lun walk_a"
        $ luna_chibi_walk_f      = "ch_lun walk_a_flip"

        $ luna_chibi_xpos        = 500
        $ luna_chibi_ypos        = 250
        $ luna_chibi_xpos_name   = "base" #Memory of chibi position.
        $ luna_chibi_ypos_name   = "base" #Memory of chibi position.
        $ luna_chibi_zorder      = 3

        #CG
        $ hermione_kneel_leg     = False
        $ hermione_kneel_cock    = False


    if not hasattr(renpy.store,'lun_request_wear_top') or reset_persistants or reset_luna_content:
        label reset_luna_clothing:

        #Save State
        $ lun_request_wear_top              = True
        $ lun_request_wear_bra              = True
        $ lun_request_wear_bottom           = True
        $ lun_request_wear_panties          = True

        $ lun_request_wear_onepiece         = False
        $ lun_request_wear_garterbelt       = False

        $ lun_request_wear_neckwear         = False
        $ lun_request_wear_gloves           = False
        $ lun_request_wear_stockings        = False
        $ lun_request_wear_robe             = False

        $ lun_request_wear_hat              = False
        $ lun_request_wear_glasses          = False
        $ lun_request_wear_ears             = False
        $ lun_request_wear_makeup           = False
        $ lun_request_wear_accs             = False

        $ lun_request_wear_buttplug         = False
        $ lun_request_wear_piercings        = False
        $ lun_request_wear_tattoos          = False

        $ lun_request_wear_outfit           = False

        #Toggle
        $ luna_wear_top               = True
        $ luna_wear_bra               = True
        $ luna_wear_bottom            = True
        $ luna_wear_panties           = True

        $ luna_wear_onepiece          = False
        $ luna_wear_garterbelt        = False

        $ luna_wear_neckwear          = False
        $ luna_wear_gloves            = False
        $ luna_wear_stockings         = False
        $ luna_wear_robe              = False

        $ luna_wear_hat               = False
        $ luna_wear_glasses           = False
        $ luna_wear_ears              = False
        $ luna_wear_makeup            = False
        $ luna_wear_accs              = False
        $ luna_badges                 = False
        $ luna_wear_piercings         = False
        $ luna_wear_tattoos           = False

        $ luna_wear_outfit            = False



        #Top
        $ luna_top                 = "characters/luna/clothes/tops/base/top_1_r.png"
        $ lun_top                     = "top_1_r"
        $ lun_top_color               = "base"

        #Bottom
        $ luna_bottom              = "characters/luna/clothes/bottoms/base/skirt_1.png"
        $ lun_bottom                  = "skirt_1"
        $ lun_bottom_color            = "base"

        #Underwear
        $ luna_bra                 = "characters/luna/clothes/underwear/base/bra_basic.png"
        $ lun_bra                     = "bra_basic"
        $ lun_bra_color               = "base"

        $ luna_panties             = "characters/luna/clothes/underwear/base/panties_basic.png"
        $ lun_panties                 = "panties_basic"
        $ lun_panties_color           = "base"

        $ luna_onepiece            = "characters/luna/clothes/onepieces/blank.png"
        $ lun_onepiece                = "blank"
        $ lun_onepiece_color          = "base"

        $ luna_garterbelt          = "characters/luna/clothes/underwear/base/blank.png"
        $ lun_garterbelt              = "blank"
        $ lun_garterbelt_color        = "base"


        #Other Clothing
        $ luna_neckwear            = "characters/luna/clothes/neckwear/blank.png"
        $ lun_neckwear                = "blank"
        $ lun_neckwear_color          = "base"

        $ luna_accs_list           = []
        $ luna_accs                = "characters/luna/accessories/blank.png"

        $ luna_gloves              = "characters/luna/clothes/gloves/blank.png"
        $ lun_gloves                  = "blank"
        $ lun_gloves_color            = "base"

        $ luna_stockings           = "characters/luna/clothes/stockings/blank.png"
        $ lun_stockings               = "blank"
        $ lun_stockings_color         = "base"

        $ luna_robe                = "characters/luna/clothes/robe/blank.png"
        $ lun_robe                    = "blank"
        $ lun_robe_color              = "base"


        #Accessories
        $ luna_makeup_list         = []

        $ luna_hat                 = "characters/luna/accessories/hats/hair_base/blank.png"
        $ lun_hat                     = "blank"
        $ lun_hat_color               = "base"

        $ luna_glasses             = "characters/luna/accessories/glasses/base/blank.png"
        $ lun_glasses                 = "blank"
        $ lun_glasses_color           = "base"

        $ luna_ears                = "characters/luna/accessories/ears/blank.png"
        $ lun_ears                    = "blank"

        #Outfits
        $ luna_outfit_GLBL = None
        $ luna_temp_outfit = None

        call reset_lun_transparency



    # Luna Lists
    $ luna_arms_up_list  = ["top_cheer_r",
                            "ll_pyjama",
                            ]

    call luna_face_layers


    return

label reset_lun_transparency:

    $ lun_top_transp       = 1
    $ lun_bottom_transp    = 1

    $ lun_bra_transp       = 1
    $ lun_onepiece_transp  = 1
    $ lun_panties_transp   = 1
    $ lun_garter_transp    = 1

    $ lun_gloves_transp    = 1
    $ lun_stockings_transp = 1
    $ lun_robe_transp      = 1

    $ lun_outfit_transp    = 1

    return



label luna_progress_init:

    # Update 1.3
    if not hasattr(renpy.store,'luna_known') or reset_persistants or reset_luna_content:

        #Stats
        $ lun_whoring = 0
        $ lun_mood = 0

        $ luna_gold = 0
        $ lun_skirt_level = 1
        $ lun_top_level = 1

        $ lun_dom = 0
        $ lun_sub = 0
        $ lun_corruption = 0
        $ lun_arousal = 0

        #Flags
        $ hat_known = False
        $ luna_known = False
        $ luna_busy = False
        $ luna_unlocked = False
        $ luna_wardrobe_unlocked = False

        $ luna_herm_talk = False
        $ luna_reverted = False
        $ luna_addicted = False

        $ days_to_luna = 0

        #Names
        $ lun_genie_name = "Old man"
        $ luna_name = "Miss Lovegood"

    return
