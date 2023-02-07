import veg_menu as veg
import nonveg_menu as nonveg

def food_item(menu,item):
    if menu=="veg_menu":
        print("3 items are available in Veg")
        if item=="tomato_soup":
            print(veg.tomato_soup())
        elif item=="veg_soup":
            print(veg.veg_soup())
        elif item=="garlic_soup":
            print(veg.garlic_soup())
        else:
            print("No food item available")
    if menu=="nonveg_menu":
        print("3 items are available in NonVeg")
        if item=="chicken_curry":
            print(nonveg.chicken_curry())
        elif item=="chicken_fry":
            print(nonveg.chicken_fry())
        elif item=="chicken_biryani":
            print(nonveg.chicken_biryani())
        else:
            print("No food item available")
 #enter food menu and item name

print(food_item("veg_menu","tomato_soup"))