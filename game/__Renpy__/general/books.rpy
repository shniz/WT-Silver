label __init_variables:


    ### Book Items ###

    if not hasattr(renpy.store,'Speedreading_1_ITEM'):
        $ Speedreading_1_ITEM = book_class(id="Speedreading_1", name="\"Copper book of spirit\"",             cost=40,  type="book", image="book_general",     chapters=2,  description=">This book contains various tips on speed reading. 2 chapters.", effect = ">New skill unlocked: a 1 out of 3 chance of completing an additional chapter when reading.")
        $ Speedreading_2_ITEM = book_class(id="Speedreading_2", name="\"Bronze book of spirit\"",             cost=60,  type="book", image="book_general",     chapters=4,  description=">This book contains various tips on speed reading. 4 chapters.", effect = ">New skill unlocked: a 2 out of 3 chance of completing an additional chapter when reading.")
        $ Speedreading_3_ITEM = book_class(id="Speedreading_3", name="\"Silver book of spirit\"",             cost=80,  type="book", image="book_general",     chapters=6,  description=">This book contains various tips on speed reading. 6 chapters.", effect = ">New skill unlocked: always complete an additional chapter when reading.")
        $ Speedreading_4_ITEM = book_class(id="Speedreading_4", name="\"Golden book of spirit\"",             cost=160, type="book", image="book_general",     chapters=8,  description=">This book contains various tips on speed reading. 8 chapters.", effect = ">You have mastered your spirit and from now on you can always complete two additional chapters when reading.")

        $ Speedwriting_1_ITEM = book_class(id="Speedwriting_1", name="\"Speedwriting for beginners\"",        cost=90,  type="book", image="book_general",     chapters=2,  description=">This book contains a bunch of very basic techniques used to improve one's ability to write quickly. 2 chapters.", effect = ">New skill unlocked: a 1 out of 3 chance of completing an additional chapter when doing paperwork.")
        $ Speedwriting_2_ITEM = book_class(id="Speedwriting_2", name="\"Speedwriting for amateurs\"",         cost=110, type="book", image="book_general",     chapters=4,  description=">This book contains intermediate techniques used to improve one's ability to write quickly. 4 chapters.", effect = ">New skill unlocked: a 2 out of 3 chance of completing an additional chapter when doing paperwork.")
        $ Speedwriting_3_ITEM = book_class(id="Speedwriting_3", name="\"Speedwriting for advanced writers\"", cost=130, type="book", image="book_general",     chapters=6,  description=">This book contains advanced techniques used to improve one's ability to write quickly. 6 chapters.", effect = ">New skill unlocked: always complete an additional chapter when doing paperwork.")
        $ Speedwriting_4_ITEM = book_class(id="Speedwriting_4", name="\"Speedwriting for experts\"",          cost=150, type="book", image="book_general",     chapters=8,  description=">This book contains expert techniques used to improve one's ability to read quickly. 8 chapters.", effect = ">You have become a true master of Speedwriting and from now on you shall always complete two additional chapters when doing paperwork.")

        $ Galadriel_I_ITEM    = fiction_book(id="Galadriel_I",    name="\"The Tale of Galadriel. Book I.\"",    cost=100, type="book", image="book_galadriel_1", chapters=20, description=">This book tells the story of an elven princess who defies the traditions of her people and chooses to forge her own destiny. Or does it? 20 chapters.", effect = ">Your imagination has improved.")
        $ Galadriel_II_ITEM   = fiction_book(id="Galadriel_II",   name="\"The Tale of Galadriel. Book II.\"",   cost=200, type="book", image="book_galadriel_2", chapters=20, description=">This book tells the story of an elven princess who defies the traditions of her people and chooses to forge her own destiny. Or does it? 20 chapters.", effect = ">Your imagination has improved.")
        $ Armchairs_ITEM      = fiction_book(id="Armchairs",      name="\"A game of Armchairs\"",               cost=300, type="book", image="book_chairs",      chapters=20, description=">An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape. 20 chapters.", effect = ">Your imagination has improved.")
        $ Dear_Wifu_ITEM      = fiction_book(id="Dear_Wifu",      name="\"My dear waifu\"",                     cost=300, type="book", image="book_waifu",       chapters=20, description=">Relive the glory of your high school days. Your step sister Shea, teacher Ms.Stevens or the mysterious library girl? Who will become your ultimate \"waifu\"? 20 chapters.", effect = ">Your imagination has improved.")





    $ Galadriel_I_ITEM.chapter_description = [
        "Galadriel - a gentle and gracious elven princess is introduced into the story.",
        "Galadriel's father - King Methis and his childhood friend Mofothelis are introduced into the story.",
        "King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis.",
        "Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle.",
        "King Methis dismisses her daughter's \"foolish\" complaints. Galadriel decides to run away.",
        "Galadriel manages to leave the royal residence at night unnoticed...",
        "King Methis is furious about his daughter's escape. He decides to personally lead the search party.",
        "Galadriel rides her mare \"white dove\" through the forest. The Princess enjoys her freedom... After a while she meets a rather handsome human nobleman on a horse...",
        "Galadriel rides alongside the nobleman. They exchange meaningless pleasantries. He makes her laugh. Suddenly the nobleman attacks the princess and knocks her out!...",
        "Galadriel comes about. To her horror she realizes that the nobleman is having his way with her. Galadriel is screaming for help but The handsome man keeps on raping her.",
        "Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously.",
        "After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop.",
        "Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen.",
        "A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage.",
        "Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food.",
        "Galadriel is starting to feel hopeful but it does not last. Soon she realizes what kind of establishment this is: a whorehouse.",
        "The elven princess is forced to work as a whore. She detests her new life but has very little choice.",
        "Galadriel gains popularity quickly. Humans, Dark Elves and even the occasional dwarf - she spreads her legs for everyone.",
        "The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel.",
        "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant. -End of book one-"
    ]

    $ Galadriel_II_ITEM.chapter_description = [
        "Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly.",
        "Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel.",
        "The Elven Princess-Whore knows nothing of the life outside the of walls of the brothel. But it does not affect her determination to escape.",
        "It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel.",
        "Galadriel soon gets lost in the vast city and is forced to spend the night on the street.",
        "Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly.",
        "The Pregnant Galadriel offers her company to a couple of filthy looking homeless men in exchange for food. She spends the night with them.",
        "Galadriel realizes that her live back in the brothel was a heaven compared to the live she's been leading for the past several days. She decides to return.",
        "Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back.",
        "Galadriel is, yet again, warm, clean and well fed. She is glad to be back and as popular as ever.",
        "Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now...",
        "A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him.",
        "The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her.",
        "The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask off.",
        "Galadriel recognizes the man as her father - King Methis. Only now he realizes that the pregnant whore he fucked for hours is his daughter.",
        # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
        "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face...",
        "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed.",
        "It takes the elven princess several minutes to realise that she was never pregnant. The entire adventure was nothing but a dream.",
        "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis.",
        "{size=-1}Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite. -The End-{/size}"
    ]

    $ Armchairs_ITEM.chapter_description = [
        "A family of noble northmen is introduced into the story.",
        "The royal family and the king are introduced into the story.",
        "Another family is introduced into the story.",
        "Some incest action between a brother and his sister, the queen, is taking place.",
        "Attempted child murder takes place. The kid barely survives and is now in a coma.",
        "Some more characters are introduced into the story.",
        "Some characters hatch an evil scheme against some other characters.",
        "The king gets poisoned and dies. Some more brother on sister incest takes place.",
        "A certain character you've been especially rooting for gets executed.",
        "Some new characters are introduced into the story.",
        "Some female characters get raped and then killed brutally.",
        "Some more members of the noble family of northmen find their untimely demise.",
        "Some more women get raped. Some of them manage to survive. (Surely only to get raped some more later,.",
        "The characters you hate clash in an epic battle against the characters you are rooting for.",
        "Most of the characters you hate survive the battle. Every single character you were rooting for is dead.",
        "Some more rapes take place, then some more murders... (You don't even care anymore...)",
        "A new group of characters is introduced into the story. You sort of starting to root for one of them.",
        "The character you were rooting for falls in love with a pretty girl.",
        "The character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well.",
        "A new race of half-frozen undead monsters is introduced into the story. To be continued..."
    ]


    $ book_list = silver_book_lib()
    $ book_list.read_books = [
        Speedreading_1_ITEM,
        Speedreading_2_ITEM,
        Speedreading_3_ITEM,
        Speedreading_4_ITEM
    ]
    $ book_list.write_books = [
        Speedwriting_1_ITEM,
        Speedwriting_2_ITEM,
        Speedwriting_3_ITEM,
        Speedwriting_4_ITEM
    ]
    $ book_list.fiction_books = [
        Galadriel_I_ITEM,
        Galadriel_II_ITEM,
        Armchairs_ITEM,
        Dear_Wifu_ITEM
    ]


    if not hasattr(renpy.store,'books'): #important!
        $ books = []

    return



label read_book_menu:
    hide screen desk_menu

    python:
        item_list = []
        if toggle1_bool:
            item_list.extend(book_list.fiction_books)
        if toggle2_bool:
            item_list.extend(book_list.write_books)
        if toggle4_bool:
            item_list.extend(book_list.read_books)

        item_list = list(filter(lambda x: (x.unlocked == True and x.done==False), item_list))

    show screen list_menu(item_list, "Read Books", toggle1="Fiction Books", toggle2="Educat. Books", toggle4="Effic. Books")
    with d1

    $ _return = ui.interact()

    hide screen list_menu

    if isinstance(_return, item_class):
        $ book_choice = _return
        jump handle_book_selection

    elif _return == "Close":
        $ current_page = 0
        jump day_main_menu

    elif _return == "toggle1":
        $ toggle1_bool = not toggle1_bool
    elif _return == "toggle2":
        $ toggle2_bool = not toggle2_bool
    elif _return == "toggle3":
        $ toggle3_bool = not toggle3_bool
    elif _return == "toggle4":
        $ toggle4_bool = not toggle4_bool

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump read_book_menu


label handle_book_selection:
    $ the_gift = book_choice.get_image()
    show screen gift
    with d3
    "[book_choice.description]"
    if book_choice.done:
        if book_choice.id == "Armchairs":
            m "Why would I want to do this to myself again?"
        else:
            ">You already finished this one."
        hide screen gift
        jump read_book_menu
    else:
        hide screen gift
        jump check_book_order


label check_book_order:
    if book_choice in book_list.read_books:
        if (book_choice.id == "Speedreading_1") or (book_choice.id == "Speedreading_2" and book_list.isDone("Speedreading_1")) or (book_choice.id == "Speedreading_3" and book_list.isDone("Speedreading_2")) or (book_choice.id == "Speedreading_4" and book_list.isDone("Speedreading_3")):
            jump reading_book

    if book_choice in book_list.write_books:
       if (book_choice.id == "Speedwriting_1") or (book_choice.id == "Speedwriting_2" and book_list.isDone("Speedwriting_1")) or (book_choice.id == "Speedwriting_3" and book_list.isDone("Speedwriting_2")) or (book_choice.id == "Speedwriting_4" and book_list.isDone("Speedwriting_3")):
            jump reading_book

    if book_choice in book_list.fiction_books:
        if (book_choice.id == "Galadriel_II" and book_list.isDone("Galadriel_I")):
            jump reading_book
        elif book_choice.id != "Galadriel_II":
            jump reading_book

    m "Reading books out of order won't do me any good."

    jump read_book_menu


label reading_book:
    stop music fadeout 2.0
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...

    if fire_in_fireplace:   #Shows Genie reading a book near the fireplace.
        hide screen chair_right
        hide screen genie
        show screen reading_near_fire
        with d3
    else:                   #Shows Genie reading a book near the window.
        hide screen chair_right
        hide screen genie
        show screen reading
        with d3

    if raining:
        ">You read a book called [book_choice.name], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book_choice.name]..."

    if cheat_reading:
        if book_choice in book_list.get_edu():
            $ book_choice.progress = book_choice.chapters
        elif book_choice in book_list.get_fic():
            label cheat_reading_loop:
                call read_chapter
                if book_choice.progress < book_choice.chapters:
                    jump cheat_reading_loop
        jump book_complete
    else:
        call read_book

        if _return == "DONE":
            jump book_complete

        call book_speed_check
        $ speed_check = _return
        if speed_check >= 1:
            if speed_reading == 1:
                ">Implementing some tricks you picked up in the \"Speed reading for dummies\" book allows you to save time and keep on reading."
            if speed_reading == 2:
                ">Implementing speed reading techniques allows you to save time and keep on reading."
            if speed_reading == 3:
                ">Implementing speed reading techniques allows you to save time and keep on reading."
            if speed_reading > 3:
                ">Implementing advanced speed reading techniques lets you blaze through the book."
            call read_book

        if _return == "DONE":
            jump book_complete

        if speed_check == 2:
            call read_book

        if _return == "DONE":
            jump book_complete

        if raining:
            if not fire_in_fireplace:
                ">The rain outside of the tower calms your mood and you feel like keeping on reading..."
                ">You try to keep on reading but after a while you realise that the air in your chambers is too damp for your liking."
            else:
                ">The rain outside of your tower calms your mood and you feel like keeping on reading..."
                call read_book

        if _return == "DONE":
            jump book_complete

        ">There are still some chapters left."

    if fire_in_fireplace:
        show screen done_reading_near_fire
        hide screen reading_near_fire
    else:
        show screen done_reading
        hide screen reading

    if daytime:
        jump night_start
    else:
        jump day_start


label book_speed_check:
    if speed_reading == 1: #33% chance
        if renpy.random.randint(1, 3) == 1: #Success.
            return 1
    if speed_reading == 2: #66% chance
        if renpy.random.randint(1, 3) > 1: #Success.
            return 1
    if speed_reading == 3: #100% chance
        return 1
    if speed_reading > 3: #Double 100% chance
        return 2
    return 0



label read_book:
    if book_choice.progress >= book_choice.chapters:
        return "DONE" #prevents cases where book is done but read_book was called
    call read_chapter
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    if book_choice in book_list.get_edu():
        $ renpy.say(None,">You've completed \"chapter [book_choice.progress]\" of the book.")
    if book_choice in book_list.get_fic():
        $ renpy.say(None,">You've completed \"chapter "+str(book_choice.progress/2)+"\" of the book.")
    if book_choice.progress >= book_choice.chapters:
        return "DONE" #this is here to indicate completeing a book without escapeing the call otherwise renpy would treat a jump or call as a recursive action
    return


label read_chapter:
    $ book_choice.progress += 1
    if book_choice in book_list.get_fic():
        if book_choice.id == "Dear_Wifu":
            call waifu
        else:
            $tmp_desc = book_choice.getChapterDesc()
            "[tmp_desc]"
            if book_choice.progress < book_choice.chapters:
                $ book_choice.progress += 1
                $tmp_desc = book_choice.getChapterDesc()
                "[tmp_desc]"
    return


label book_complete:
    if fire_in_fireplace:
        show screen done_reading_near_fire
    else:
        show screen done_reading

    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">That was the last chapter, You finished the entire book."

    if book_choice.id == "Dear_Wifu":
        jump waifu_completed
    elif book_choice.id == "Armchairs":
        g4 "What a pile of garbage! I hate the guy who wrote this crap!"
        m "Although all those rapes gave me a few ideas..."
        $ bdsm_imagination += 1
    else:
        $ imagination += 1

    if book_choice in book_list.read_books:
        $ speed_reading += 1
    if book_choice in book_list.write_books:
        $ speed_writing += 1

    $ book_choice.done = True

    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    "[book_choice.effect]" # ex. ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.."
    hide screen notes


    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else:
        jump day_start


#Scrolls

label read_scroll_menu:
    hide screen desk_menu

    python:
        item_list = []
        if toggle1_bool:
            item_list.extend(scroll_list_A)
        if toggle2_bool:
            item_list.extend(scroll_list_B)
        if toggle3_bool:
            item_list.extend(scroll_list_C) #Silver Scrolls.

        item_list = list(filter(lambda x: x.unlocked == True , item_list))

    show screen list_menu(item_list, "Scrolls", toggle1="Volume I", toggle2="Volume II", toggle3="Silver", toggle4="Comments")
    with d1

    $ _return = ui.interact()

    hide screen list_menu

    if isinstance(_return, item_class):
        call read_scroll(_return)

    elif _return == "Close":
        $ current_page = 0
        jump day_main_menu

    elif _return == "toggle1":
        $ toggle1_bool = not toggle1_bool
    elif _return == "toggle2":
        $ toggle2_bool = not toggle2_bool
    elif _return == "toggle3":
        $ toggle3_bool = not toggle3_bool
    elif _return == "toggle4":
        $ toggle4_bool = not toggle4_bool
        if toggle4_bool == True:
            $ commentaries = True
        else:
            $ commentaries = False

    elif _return == "inc":
        $ current_page += 1
    elif _return == "dec":
        $ current_page += -1

    jump read_scroll_menu


label read_scroll(scroll):
    $ the_gift = "images/misc/extras/"+str(scroll.scroll_image)+".png"
    show screen gift
    with d3

    if commentaries:
        python:
            for comment in scroll.comments:
                if scroll in scroll_list_C:
                    renpy.say(sil,comment)
                else:
                    renpy.say(a1,comment)
    call ctc

    hide screen gift
    with d3

    jump read_scroll_menu
