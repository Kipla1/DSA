def update_shopping_cart(cart, action):
    product_id = action.get("product_id")
    
    if action["type"] == "add":
        if product_id in cart:
            cart[product_id] += action["quantity"]
        else:
            cart[product_id] = action["quantity"]
    elif action["type"] == "remove":
        if product_id in cart:
            del cart[product_id]
    elif action["type"] == "change":
        if "quantity" in action:
            if action["quantity"] > 0:
                cart[product_id] = action["quantity"]
            else:
                # If quantity is 0 or negative, remove the item
                if product_id in cart:
                    del cart[product_id]
    
    return cart