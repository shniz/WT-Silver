label store_init:

    #Update 1.3
    if not hasattr(renpy.store,'clothing_store_intro_done') or reset_persistants:

        #Shop
        $ order_placed = False #TRUE when and order has been placed on an item.
        $ days_in_delivery = 0 # +1 day, every day since the orer has been made (when order_placed = True).
        $ days_in_delivery2 = 0 # +1 day, every day since the orer has been made (when order_placed = True).
        $ package_is_here = False # Turns true when days_in_delivery >= 5. Package is displayed.


        $ tentacle_owned = False #Quest item. Not the scroll you buy from the store.

        $ outfit_is_worked_on = False
        $ store_intro_done = False
        $ book_store_intro_done = False
        $ clothing_store_intro_done = False

    return
