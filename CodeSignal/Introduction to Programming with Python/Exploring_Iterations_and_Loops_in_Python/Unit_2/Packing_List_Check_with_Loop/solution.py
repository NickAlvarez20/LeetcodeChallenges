# Suppose we have packed our bags for the trip and we are checking if we packed everything
packing_list = ["passport", "tickets", "camera", "clothes"]
packed_items = ["passport", "camera", "clothes"]

for item in packing_list:
    if item not in packed_items:
        print(f"Forgot to pack {item}")
        break
