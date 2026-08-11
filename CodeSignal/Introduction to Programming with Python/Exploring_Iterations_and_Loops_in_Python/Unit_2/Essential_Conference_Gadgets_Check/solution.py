# Essential gadgets needed for the conference
essential_gadgets = ["laptop", "charger", "adapter", "USB drive"]
packed_items = ["laptop", "USB drive", "notebooks", "pens"]


for gadget in essential_gadgets:
    for packed in packed_items:
        if packed == gadget:
            # TODO: Found missing gadget, stop searching
            print("Packed missing gadget, stop searching.")
            break
    # TODO: Print missing gadget if there is one
    else:
        print("Missing gadget")
