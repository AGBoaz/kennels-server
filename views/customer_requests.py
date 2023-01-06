CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanay"
    },
    {
        "id": 2,
        "name": "green duck"
    }
]

def get_all_customers():
    """gets all the customers
    """
    return CUSTOMERS


def get_single_customer(id):
    """gets one customer
    """
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer