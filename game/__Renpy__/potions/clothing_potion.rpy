

### TRANSPARENCY POTION ###

label potion_scene_4: #Transparent uniform
    m "[hermione_name], I have another potion for you."
    call her_main("I'm not sure that I like these potions [genie_name].","normal","frown") from _call_her_main_5673
    call her_main("Especially after the time you tried to turn me into a cat.","annoyed","frown") from _call_her_main_5674
    m "To be fair I was trying to turn you into another girl..."
    call her_main("That's not much better [genie_name].","angry","angry") from _call_her_main_5675
    m "Isn't it?"
    call her_main("Well at least promise me that this one isn't going to embarrass me in the middle of class.","open","angryCl") from _call_her_main_5676
    call her_main("My reputation is suffering enough as it is. I don't need these constant potions causing me to transform in front of my peers.","annoyed","angryL") from _call_her_main_5677
    m "I promise that this potion won't affect your body in any way."
    call her_main("Well then what on earth is it going to do?","angry","angry") from _call_her_main_5678
    m "As always [hermione_name], you'll ha-"
    call her_main("Have to wait and see. I know.","normal","frown") from _call_her_main_5679
    
    call her_chibi("drink_potion","mid","base") from _call_her_chibi_176
    
    call nar(">Hermione quickly drinks the potion.") from _call_nar_596      #new
    call her_main("","open","angryCl") from _call_her_main_5680
    
    call her_chibi("stand","mid","base") from _call_her_chibi_177
    
    her "Can I go now?"
    m "Yes you may. 20 points to Gryffindor"
    call her_main("Thank you [genie_name].","open","closed") from _call_her_main_5681
    
    $ gryffindor += 20
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk("mid","leave",2) from _call_her_walk_118
    
    $ hermione_takes_classes = True
    if whoring <= 7:
        $ transparency = 0.8
    elif whoring <= 13:
        $ transparency = 0.6
    elif whoring <= 20:
        $ transparency = 0.4
    else:
        $ transparency = 0.2
    $ hermione_breasts = "characters/hermione/body/breasts/breasts_normal.png"
    $ transparent_quest = True
    jump day_main_menu

label potion_scene_4_2: #Scene where Hermione comes back after classes angry and confused at having her uniform made transparent
    $ transparent_quest = False
    call play_sound("door") from _call_play_sound_201 #Sound of a door opening.
    call her_chibi("stand","mid","base") from _call_her_chibi_178
    
    show screen bld1
    if whoring <= 7: #Very angry and embarrassed
        call nar(">Hermione bursts into your office.") from _call_nar_597
        call her_main("How could you [genie_name]!","angry","base",tears="soft") from _call_her_main_5682
        call her_main("I am the laughing stock of the entire school!","angry","base",tears="soft") from _call_her_main_5683
        call her_main("Now everyone knows what I look like naked!","mad","worriedCl",tears="soft_blink") from _call_her_main_5684
        m "Tell me about what happened."
        call her_main("Tell you about what happened? I'm never speaking to you again.","angry","base",tears="soft") from _call_her_main_5685
        $ mad += 20
        $ transparency = 1
        # $ hermione_breasts = "characters/hermione/body/breasts/"+outfit.breast_layer+".png"
        # This is bugged and causes a crash. Things don't go catistrophically wrong without this line, so I've edited it out until you can fix it.
    elif whoring <= 13: #Mildly aggravated
        call nar(">Hermione comes into your office quickly without knocking.") from _call_nar_598
        call her_main("Again?","angry","worriedCl",emote="05") from _call_her_main_5686
        m "What's this about [hermione_name]?"
        call her_main("Why would you make my clothes invisible again?","open","base") from _call_her_main_5687
        m "Why not?"
        call her_main("Ugh, you're such a pig.","annoyed","worriedL") from _call_her_main_5688
        m "Tell me about what happened."
        call her_main("...","normal","worriedCl") from _call_her_main_5689
        call her_main("Fine, but I expect an extra 10 points.","open","base") from _call_her_main_5690
        m "As you wish."
        call her_main("Well I started off with potions class as usual when I started to feel like all eyes were on me.","disgust","glance") from _call_her_main_5691
        m "I wonder why."
        call her_main("As I was saying I was completing potions class and felt like everyone wouldn't take their eyes off of me.","annoyed","angryL") from _call_her_main_5692
        call her_main("I didn't think anything of it until I was approached by Professor Snape at the end of the lesson.","annoyed","annoyed") from _call_her_main_5693
        call her_main("He normally criticises me during potions class. Stuff like getting dosages wrong, things that I know are correct.","annoyed","worriedL") from _call_her_main_5694
        m "Back to the story [hermione_name]."
        call her_main("Well when he commented that he liked my outfit I was suspicious. I thought that perhaps he was talking about my shirt until I looked down and saw that everything was see through.","disgust","glance") from _call_her_main_5695
        call her_main("But I just ignored him, finished class and ran here.","annoyed","angryL") from _call_her_main_5696
        m "You just finished class?"
        call her_main("Of course, I can't afford to miss potions class. I'm doing poorly enough without missing class.","annoyed","annoyed") from _call_her_main_5697
        m "Well fair enough. You may go now."
        call her_main("Hmmph. Goodbye [genie_name].","annoyed","worriedL") from _call_her_main_5698

    elif whoring <= 20: #Slightly aroused
        call nar(">Hermione enters your office") from _call_nar_599
        call her_main("Can you at least warn me next time?","open","suspicious") from _call_her_main_5699
        m "Well, that'd take away from the suspense wouldn't it?"
        call her_main("Hmmmm, well at least ask what I'm doing before you give me the potion.","open","worriedL") from _call_her_main_5700
        m "Why, what did you have to do today that was so important?"
        call her_main("I had to give a speech for languages!","angry","worried") from _call_her_main_5701
        call her_main("Do you have any idea how inappropriate it was giving a speech on morality in front of the entire class-","open","closed") from _call_her_main_5702
        call her_main("{size=+5}As my clothes became transparent!{/size}","angry","worried") from _call_her_main_5703
        m "Well I imagine it depends on what side of morality you were arguing."
        call her_main("It doesn't matter.","open","closed") from _call_her_main_5704
        m "Are you sure that you didn't enjoy it?"
        call her_main("How could I. I had to stand there as my friends and peers all saw me naked.","annoyed","suspicious") from _call_her_main_5705
        m "You finished your speech?"
        call her_main("Certainly, I had to make sure that everyone knew my views on morality.","soft","base") from _call_her_main_5706
        m "Well I'm sure they have a crystal clear view of it now."
        call her_main("Hmmph, are you done?","annoyed","angryL") from _call_her_main_5707
        m "Yes, you may go now."
        call her_main("Good bye [genie_name].","open","base") from _call_her_main_5708
        
    else: #Highly aroused (doesn't even acknowledge that her clothes are see-through)
        call nar(">Hermione enters the office casually.") from _call_nar_600
        m "Hello [hermione_name], how was your day today?"
        call her_main("Fine [genie_name]. Why do you ask?","base","base") from _call_her_main_5709
        m "No reason. Anything unusual happen today?"
        call her_main("Hmmmm, now that you mention it I suppose that boys in class were a little more forward than usual.","open","worriedL") from _call_her_main_5710
        m "How so?"
        call her_main("Well nothing serious, just small stuff like calling me names, groping me.","soft","baseL") from _call_her_main_5711
        m "Groping you? What on earth could have provoked them to do that?"
        call her_main("I don't know [genie_name]. I can't imagine any reason that I would be attracting attention today...","base","base") from _call_her_main_5712
        m "You're getting off on this aren't you?"
        call her_main("...","smile","baseL") from _call_her_main_5713
        call her_main("I've never been so turned on in my life. Having all eyes on me. Having every boy imagine doing unspeakable things to me.","soft","ahegao") from _call_her_main_5714
        call her_main("Snape made me stand out the front of class after I talked back to him.","base","down") from _call_her_main_5715
        call her_main("I think that I orgasmed just from the looks people gave me.","grin","dead") from _call_her_main_5716
        m "Well done [hermione_name]. You're becoming quite the slut."
        call her_main("Thank you [genie_name]. Is that all?","base","glance") from _call_her_main_5717
        m "Yes, you can go now slut."
        call her_main("{image=textheart}","smile","baseL") from _call_her_main_5718
        
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    $ transparency = 1
    call update_her_uniform from _call_update_her_uniform_97
    
    call her_walk("mid","leave",2) from _call_her_walk_119
    
    $ hermione_sleeping = True
    jump night_main_menu
    
    
    