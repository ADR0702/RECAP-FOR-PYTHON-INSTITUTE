class Phone:

    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    
    def type_number(self):
        self.number=int(input("type 10 digit number to call:\n"))
    
    def call(self):
        print(f"Calling {self.number} from {self.brand} {self.model}")


brand_and_no=Phone("Nokia", "6310")

brand_and_no.type_number()
brand_and_no.call()
