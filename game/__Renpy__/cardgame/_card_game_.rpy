label setup_deck(opppent_deck): 
    python:
        player_deck = []
        for card in playerdeck:
            card.playercard = True
            player_deck.append(card)
        enemy_deck = []
        for card in opppent_deck:
            card.playercard = False
            enemy_deck.append(card)
        reset_table_cards()
    return
    
label cardgame:
    show screen card_battle(player_deck,enemy_deck)
    $ _return = ui.interact()

    if _return in player_deck:
        $ selectcard = player_deck.index(_return)
        $ response_card = "NewTurn"
        return "NewTurn"
    
    elif _return == "Close":
        $ selectcard = -1
        hide screen card_battle
        $ response_card = "Close"
        return "Close"

    else:
        if not selectcard == -1:
            
            $ y = int(math.floor(int(_return)/3))
            $ x = int(_return)-(y*3)
            
            $ table_cards[x][y] = player_deck[selectcard]
            $ table_cards[x][y].playercard = True
            $ del player_deck[selectcard]
            $ selectcard = -1
            $ update_table(x,y)
            
            pause
            if (len(player_deck) == 0 or len(enemy_deck) == 0):
                $ response_card = "EndGame"
                hide screen card_battle
                return "EndGame"
            call enemy_turn
            $ response_card = "AfterEnemy"
            if (len(player_deck) == 0 or len(enemy_deck) == 0):
                $ response_card = "EndGame"
                hide screen card_battle
                return "EndGame"
            return "NewTurn"
        else:
            $ response_card = "NewTurn"
            return "NewTurn"
        
label enemy_turn:
    python:
        high_score = 0
        high_score_card = None
        high_score_pos = 0
        
        for card in enemy_deck:
            tuple_my = card.getAIScore(table_cards)
            if tuple_my[0] > high_score:
                high_score = tuple_my[0]
                high_score_pos = tuple_my[1]
                high_score_card = card
                
        y = int(math.floor(int(high_score_pos)/3))
        x = int(high_score_pos)-(y*3)
        del enemy_deck[enemy_deck.index(high_score_card)]
        table_cards[x][y] = high_score_card        
        table_cards[x][y].playercard = False
        update_table(x,y)
    return
          
screen card_battle(l_playerdeck, l_enemydeck):
    imagemap:
        ground "images/cardgame/card_table.png"
        hover "images/cardgame/card_table_hover.png"
        
        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y] == None:
                    hotspot (383+105*x, 60+124*y, 105, 124) clicked Return(str(x+y*3))
                else:
                    use cardrender(table_cards[x][y], 383+105*x, 60+124*y)
   
    for i in range(0, len(l_playerdeck)):
        if not selectcard == i:
            use cardrender(l_playerdeck[i], 20,60+70*i, True)
    
    if not selectcard == -1:
        use cardrender(l_playerdeck[selectcard], 60,60+70*selectcard)
        
    for i in range(0, len(l_enemydeck)):
        use cardrender(l_enemydeck[i], 950,60+70*i)
        
    use close_button
        
screen cardrender(card, xpos_card, ypos_card, interact=False, return_value=None):
    if return_value == None:
        $ return_value = card
    frame:
        xpos xpos_card -4
        ypos ypos_card -4
        xsize card_width*cardzoom
        ysize card_height*cardzoom
        background #00000000


        if interact:
            imagebutton:
                idle card.get_card_image()
                hover card.get_card_hover()
                action Return(return_value)
        else:
            add card.get_card_image()
        
        if card.playercard:
            add playerboarder zoom cardzoom
        else:
            add enemyboarder zoom cardzoom
        add "images/cardgame/dots.png" zoom cardzoom
        
        $ lefttext = "{size=18}"
        $ righttext = "{/size}"
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.topvalue)+righttext xalign 0.5 yalign -0.05
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.buttomvalue)+righttext xalign 0.5 yalign 1.05
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.rightvalue)+righttext xalign 1.0 yalign 0.5
        
        hbox:
            xsize card_width*cardzoom
            ysize card_height*cardzoom
            text lefttext+str(card.leftvalue)+righttext xalign 0.00 yalign 0.5
            
screen start_deck:
    zorder 9
    for i in range(0, len(playerdeck)):
        use cardrender(playerdeck[i],250+125*i,200, interact=False)