def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    """ for value in kwargs.values():
        print(value, end=" ") """
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.", "sany", "|||", street="368 Fake st.", city="Mirpur", state="USM", zip="6300")