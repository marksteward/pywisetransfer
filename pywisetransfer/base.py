from apiron import Service


class Base(Service):

    client = None

    def __init__(self, *args, **kwargs):
        if "client" in kwargs and Base.client != kwargs["client"]:
            Base.client = kwargs["client"]
        if Base.client and Base.client.environment == "live":
            Base.domain = "https://api.transferwise.com"
        else:
            Base.domain = "https://api.sandbox.transferwise.tech"

    @property
    def required_headers(self):
        if self.client:
            return {"Authorization": f"Bearer {self.client.api_key}"}
        return {}
