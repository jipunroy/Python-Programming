def outer():
    name = "Rahim"

    def inner():
        print(name)

    inner()

outer()