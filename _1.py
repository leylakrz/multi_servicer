from abc import ABC


class Runner(ABC):
    def run(self, service, arg):
        return getattr(self, f"send_{service.lower()}")(arg)

    def send_sms(self, phone_number: str) -> str:
        return f"sms sent by {type(self).__name__}. args: {phone_number}"

    def send_mms(self, phone_numbers: list[str]) -> str:
        return f"mms sent by {type(self).__name__}. args: {phone_numbers}"

    def send_email(self, email: str) -> str:
        return f"email sent by {type(self).__name__}. args: {email}"


class GoogleProvider(Runner):
    pass


class YahooProvider(Runner):
    pass


class MSNProvide(Runner):
    pass


class Command:
    providers = {
        "google": GoogleProvider,
        "yahoo": YahooProvider,
        "msn": MSNProvide,
    }

    def __new__(cls, provider):
        return cls.providers[provider]()

# Command(provider="google").run("MMS", "phone_number")
# Command(provider="yahoo").run("email", "email@email.email")
