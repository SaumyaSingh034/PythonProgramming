class Cart:
    ItemsInCart = 0

    def add_to_cart(self, items_to_add):
        if items_to_add < 0:
            print("Cannot add a negative number of items.")
        elif items_to_add > 0:
            Cart.ItemsInCart +=  items_to_add
            print("{} items added. Total in cart {}".format(items_to_add, Cart.ItemsInCart))
            if(Cart.ItemsInCart > 5):
                print("Cart limit exceeded.")

obj = Cart()
obj.add_to_cart(2)
obj.add_to_cart(-1)