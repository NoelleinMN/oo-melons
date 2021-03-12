"""Classes for melon orders."""

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    
    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    country_code = country_code
    order_type = "international"
    tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

order0 = DomesticMelonOrder("Watermelon", 12)
order1 = InternationalMelonOrder("Honeydew", 18, "BRZ")