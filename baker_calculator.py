#`full_boxes`**: Kitne poore boxes pack honge? (`//` use karein)
#**`leftover_cupcakes`**: Packing ke baad kitne cupcakes akand/bach jayenge? (`%` use karein)
#**`boxes_cost`**: Total boxes ki kitni keemat bani? (`*` use karein)
#**`leftovers_cost`**: Baches hue cupcakes ki kitni keemat bani? (`*` use karein)
#**`total_bill`**: Total kitna bill bana? (`+` use karein)

#In sab ko calculate karke f-strings ke zariye print karein. Code VS Code mein run karke mujhe output share karein!
total_required_box = 65
per_box_cupcakes = 8
Price_box = 15
one_cupcake_price = 2

full_boxes = total_required_box // per_box_cupcakes
leftover_cupcakes = total_required_box % per_box_cupcakes
boxes_cost = full_boxes * 15
leftovers_cost = leftover_cupcakes * one_cupcake_price
total_bill = boxes_cost + leftovers_cost

print(f"Full Boxes: {full_boxes}.")
print(f"Leftover Cupcakes: {leftover_cupcakes}")
print(f"Boxes Cost: {boxes_cost}")
print(f"Leftovers Cost {leftovers_cost}")
print(f"Total Bill: {total_bill}")
