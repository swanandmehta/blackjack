class Account:

    def __init__(self, **kwargs):
        self.bal = int(kwargs.get("bal"))

    def get_bal(self):
        return self.bal
