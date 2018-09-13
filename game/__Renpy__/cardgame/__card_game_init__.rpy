label __init_variables:
    python:
        selectcard = -1
        cardzoom = 0.1
        
        if not hasattr(renpy.store,'playercolor_r'):
            playercolor_r = 0.5
            playercolor_g = 0.5
            playercolor_b = 1
            enemycolor_r = 1
            enemycolor_g = 0.5
            enemycolor_b = 0.5    
        
        table_cards = [[None for x in range(0,3)] for y in range(0,3)] 
        
        card_width = get_witdh("images/cardgame/cheerl.png")
        card_height = get_height("images/cardgame/cheerl.png")
        
        playerboarder = playerTint("images/cardgame/sides.png")
        enemyboarder = enemyTint("images/cardgame/sides.png")
        
        cheer1 = card_new(          imagepath="images/cardgame/cheerl.png",
                                    topvalue = 2,
                                    buttomvalue = 3,
                                    rightvalue = 3,
                                    leftvalue = 1,
                                    title="cheerleader 1")
                                    
        bikini = card_new(          imagepath="images/cardgame/bikini5.0.png",
                                    topvalue = 4,
                                    buttomvalue = 3,
                                    rightvalue = 2,
                                    leftvalue = 3,
                                    title="Bikini version 5.0")
                                    
        nightdress = card_new(      imagepath="images/cardgame/NightlyDress.png",
                                    topvalue = 2,
                                    buttomvalue = 3,
                                    rightvalue = 4,
                                    leftvalue = 3,
                                    title="Nightly Dress")
                                    
        nightdressbreast = card_new(imagepath="images/cardgame/NightlyDressBreastCover.png",
                                    topvalue = 3,
                                    buttomvalue = 4,
                                    rightvalue = 5,
                                    leftvalue = 3,
                                    title="Nightly Dress Dont look")
                                    
        snapeandelf = card_new( imagepath="images/cardgame/SnapeAndElf.png",
                                    topvalue = 2,
                                    buttomvalue = 4,
                                    rightvalue = 5,
                                    leftvalue = 1,
                                    title="Snape and elf")
        
        normalcl = card_new(        imagepath="images/cardgame/NormalCl.png",
                                    topvalue = 2,
                                    buttomvalue = 4,
                                    rightvalue = 3,
                                    leftvalue = 2,
                                    title="Normal Hermione")
        
        genieforest = card_new(     imagepath="images/cardgame/GenieForest.png",
                                    topvalue = 4,
                                    buttomvalue = 2,
                                    rightvalue = 3,
                                    leftvalue = 3,
                                    title="Genie Forest")
        
        hermione_cheer_en1 = card_new(playercard=False)
        hermione_cheer_en2 = card_new(playercard=False)
        hermione_cheer_en3 = card_new(playercard=False)
        hermione_cheer_en4 = card_new(playercard=False)
        hermione_cheer_en5 = card_new(playercard=False)
        
        if not hasattr(renpy.store,'unlocked_cards'):
            unlocked_cards = [normalcl, cheer1, genieforest, nightdressbreast, snapeandelf]
            
        if not hasattr(renpy.store,'deck_unlocked'):
            deck_unlocked = False
            deck_mail_send = False
         
        if not hasattr(renpy.store,'playerdeck'):
            playerdeck = [normalcl, cheer1, genieforest, nightdressbreast, snapeandelf]
        
        enemydeck = [hermione_cheer_en1 ,hermione_cheer_en2 ,hermione_cheer_en3,hermione_cheer_en4,hermione_cheer_en5]
        
        
init python:
   
    def playerTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(playercolor_r, playercolor_g, playercolor_b))
    def enemyTint(image):
        return im.MatrixColor( image, im.matrix.desaturate() * im.matrix.tint(enemycolor_r, enemycolor_g, enemycolor_b))
      
    def get_image_size(image):
        myDisplayable = im.Image(image)
        myRender = renpy.render(myDisplayable, 800, 600, 0, 0)
        sizes = myRender.get_size()
        x = sizes[0]
        y = sizes[1]
        
        return (x,y)
    
    def get_hex_string(red, green, blue):
        red = str(hex( int( math.ceil( red*255))))[2:]
        if not len(red) == 2:
            red = "0"+red
        green = str(hex(int(math.ceil( green * 255))))[2:]
        if not len(green) == 2:
            green = "0"+green
        blue = str(hex(int(math.ceil( blue * 255))))[2:]
        if not len(blue) == 2:
            blue = "0"+blue
        return "#" + red + green + blue
    
    def get_witdh(image):   
        return get_image_size(image)[0]
        
    def get_height(image):
        return get_image_size(image)[1]    
    
    def reset_table_cards():
        for y in range(0,3):
            for x in range(0,3):
                table_cards[x][y] = None
        return
        
    def check_winner():
        playerpoints = len(player_deck)

        for y in range(0,3):
            for x in range(0,3):
                if table_cards[x][y].playercard:
                    playerpoints += 1
        return playerpoints > 5
    
           
    def update_table(new_card_x, new_card_y):
        if  not new_card_y == 0 and not table_cards[x][y-1] == None and table_cards[x][y].topvalue >= table_cards[x][y-1].buttomvalue:
            table_cards[x][y-1].playercard = table_cards[x][y].playercard
            
        if not new_card_y == 2 and not table_cards[x][y+1] == None and table_cards[x][y].buttomvalue >= table_cards[x][y+1].topvalue:
            table_cards[x][y+1].playercard = table_cards[x][y].playercard
            
        if  not new_card_x == 0 and not table_cards[x-1][y] == None and table_cards[x][y].leftvalue >= table_cards[x-1][y].rightvalue:
            table_cards[x-1][y].playercard = table_cards[x][y].playercard
            
        if not new_card_x == 2 and not table_cards[x+1][y] == None and table_cards[x][y].rightvalue >= table_cards[x+1][y].leftvalue:
            table_cards[x+1][y+1].playercard = table_cards[x][y].playercard
            
    def add_card_to_deck(title):
            for card in unlocked_cards:
                if title == card.title:
                    card.copies += 1
                     
    class card_new(object):
        playercard = True
        imagepath = "images/cardgame/cheerl.png"
        title = "Cheerleader BaseCard"
        description = "She will cheer for you all the way up the wand"
        copies = 0
        textcolor = "{color=#8f939b}"
        
        topvalue = 0
        buttomvalue = 1
        rightvalue = 2
        leftvalue = 3
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def get_card_image(self):
            return im.Scale(self.imagepath, card_width*cardzoom, card_height*cardzoom)
        def get_card_hover(self):
            return im.MatrixColor(im.Scale(self.imagepath, card_width*cardzoom, card_height*cardzoom),im.matrix.brightness(0.12))
            
        def get_title(self):
            return self.textcolor+self.title+"{/color}"
        def get_amount(self):
            return self.textcolor+"amount: " + str(self.copies)+"{/color}"
        def get_description(self):
            return self.textcolor+self.description+"{/color}"
            
        
                    
        def getAIScore(self, table_of_cards):
            high_score = 0
            position = 0
            wallscore = 2
            getcardscore = 9
            for y in range(0,3):
                for x in range(0,3):
                    score = 0
                    if table_cards[x][y] == None:
                        if  not y == 0:
                            if not table_cards[x][y-1] == None and self.topvalue > table_cards[x][y-1].buttomvalue:
                                score += getcardscore
                            else:
                                score += self.topvalue
                        else:
                            score += wallscore
                        if not y == 2:
                            if not table_cards[x][y+1] == None and self.buttomvalue > table_cards[x][y+1].topvalue:
                                score += getcardscore
                            else:
                                score += self.buttomvalue
                        else:
                            score += wallscore
                        if  not x == 0:
                            if not table_cards[x-1][y] == None and self.leftvalue > table_cards[x-1][y].rightvalue:
                                score += getcardscore
                            else:
                                score += self.leftvalue
                        else:
                            score += wallscore
                        if not x == 2:
                            if not table_cards[x+1][y] == None and self.rightvalue > table_cards[x+1][y].leftvalue:
                                score += getcardscore
                            else:
                                score += self.rightvalue
                        else:
                            score += wallscore
                            
                        if score > high_score:
                            high_score = score
                            position = x + y * 3
            return [high_score, position]