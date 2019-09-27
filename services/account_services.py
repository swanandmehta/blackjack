# This service will deal with player account
import random

from entity import account


def get_account(min_bal, max_bal):
    """
    This will create Account using min bal and max bal
    :param min_bal: int
    :param max_bal: int
    :return: Account
    """
    bal = random.uniform(min_bal, max_bal)
    account_details = account.Account(bal=bal)
    return account_details


