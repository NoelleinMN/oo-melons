"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty):                           # should not really have any __init__ because it's not meant to be used
        """Initialize melon order attributes."""

        self.species = species                                  # this should move down to each subclass below
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if self.species == "Christmas" and self.order_type == "international":
            base_price = base_price * 1.5
            if self.qty < 10:
                flat_fee = 3
                total = (1 + self.tax) * self.qty * base_price + flat_fee
            else: 
                total = (1 + self.tax) * self.qty * base_price
        
        elif self.species == "Christmas":
            base_price = base_price * 1.5
            total = (1 + self.tax) * self.qty * base_price

        elif self.order_type == "international":
            if self.qty < 10:
                flat_fee = 3
                total = (1 + self.tax) * self.qty * base_price + flat_fee
            else: 
                total = (1 + self.tax) * self.qty * base_price

        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"                                 # these are class attributes - and apply to ALL instances/objects in the class
    tax = 0.08


class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order purchased by the US Government."""

    order_type = "government"
    tax = 0.0
    passed_inspection = False 

    def mark_inspection(self, passed):
        """Record whether the melon order has passed inspection or not."""

        self.passed_inspection = passed


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):            #this init allows us to add in the new country_code attribute
        super().__init__(species, qty)                         #needs to refer to the superclass so that the # of arguments match up
        self.country_code = country_code
   
    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order0 = DomesticMelonOrder("Watermelon", 12)
order1 = InternationalMelonOrder("Honeydew", 5, "BRZ")
order2 = DomesticMelonOrder("Christmas", 2)
order3 = InternationalMelonOrder("Christmas", 4, "JPN")