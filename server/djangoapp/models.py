from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default=' ')
    description = models.CharField(
        null=False, max_length=300, default=' ')

    def __str__(self):
        return 'Name:' + self.name + ',' + \
            'Description:' + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'Suv'
    WAGON = 'Wagon'
    STYLE_CHOICES = [
        (SEDAN, 'Sedan'),
        (WAGON, 'Wagon'),
        (SUV, 'Suv')
    ]

    make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    dealerId = models.IntegerField()
    model = models.CharField(null=False, max_length=30)
    style = models.CharField(
        null=False,
        max_length=20,
        choices=STYLE_CHOICES,
        default=SUV
    )
    year = models.DateField(default=now)

    def __str__(self):
        return "Make: " + str(self.make) + "," + "\n DealerId: " + str(self.dealerId) + "," + "\n Model: " + self.model + "," + "\n Style: " + self.style + "," + "\n Year: " + str(self.year)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, state, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state (st)
        self.st = st
        # Dealer state
        self.state = state
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data


class DealerReview:
    def __init__(self, id, name, dealership, review, purchase, purchase_date, car_make, car_model, car_year, sentiment):
        self.id=id
        self.name = name
        self.dealership = dealership
        self.review = review
        self.purchase = purchase
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment

    def __str__(self):
        return "Review: " + self.review
