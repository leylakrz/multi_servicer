import random

from _1 import GoogleProvider, YahooProvider, MSNProvide


class Command:
    providers = [GoogleProvider, YahooProvider, MSNProvide]

    def __new__(cls):
        return random.choice(cls.providers)()
