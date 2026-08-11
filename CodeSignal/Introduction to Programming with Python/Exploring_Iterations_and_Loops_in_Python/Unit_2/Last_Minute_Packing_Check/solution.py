packed_items = ["tickets", "camera", "passport", "notebook", "clothes"]
# TODO: Once you've found the passport, no need to rummage anymore
for item in packed_items:
    print("Rummaging...")
    if item == "passport":
        print("Found it!")
        break
