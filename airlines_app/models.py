
from django.db import models

# Create your models here.
class Flight(models.Model):

    DESTINATIONS = {
        'country': [
            ('israel', 'Israel'),
            ('london', 'London'),
            ('germane', 'Germany'),
            ('greece', 'Greece'),
            ('Australia','australia'),
            ('Austria', 'austria'),
            ('Bulgaria','bulgaria'),
            ('Czech Republic', "czech republic"),
            ('France', 'france'),
            ('Georgia','georgia'),
            ('Hong Kong', 'hong kong'),
            ('Hungary', 'hungary'),
            ('Italy', "italy"),
            ('Japan', 'japan'),
            ('Morocco', 'morocco'),
            ("Netherlands", "netherlands"),
            ("Portugal", "portugal"),
            ('Romania', "romania"),
            ('Russia',"russia"),
            ("United States", "united states"),
            ("United Kingdom", "united kingdom"),
            ("Thailand", "thailand"),
            ("Switzerland", "switzerland"),
            ("Spain", "spain"),
        ],
        'city': [
            ("Vienna", "vienna"),
            ("Sofia", "sofia"),
            ("Larnaca", "larnaca"),
            ("Prague", "prague"),
            ("Marseille", "marseille"),
            ("Paris", "paris"),
            ("Nice", "nice"),
            ("Tbilisi", "tbilisi"),
            ("Berlin", "berlin"),
            ("Frankfurt", "frankfurt"),
            ("Munich", "munich"),
            ("Athens", "athens"),
            ("Rhodes", "rhodes"),
            ("Hong Kong", "hong kong"),
            ("Budapest", "budapest"),
            ("Dublin", "dublin"),
            ("Milan", "milan"),
            ("Rome", "rome"),
            ("Venice", "venice"),
            ("Tokyo", 'tokyo'),
            ("Casablanca", "casablanca"),
            ("Marrakesh", "marrakesh"),
            ("Amsterdam", "amsterdam"),
            ("Lisbon", "lisbon"),
            ("Bucharest", "bucharest"),
            ("Moscow", "moscow"),
            ("Barcelona", "barcelona"),
            ("Madrid", "madrid"),
            ("Geneva", "geneva"),
            ("Zürich", "zürich"),
            ("Bangkok", "bangkok"),
            ("Phuket", "phuket"),
            ("London", "london"),
            ("Boston", "boston"),
            ("Las Vegas", "las vegas"),
            ("Los Angeles", "los angeles"),
            ("Miami", "miami"),
            ("Newark", "newark"),
            ("New York City", "new york city"),
            ("San Francisco", "san francisco"),
            ("Tel Aviv", 'tel aviv')
        ],
        "airport code": [

        ]

    }
    class Meta:
        db_table = 'flight'
        ordering = ['id']

    flight_num = models.CharField(max_length=256, db_column='flight number', null=False, blank=False)
    origin_country = models.C