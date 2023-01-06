EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    },
    {
        "id": 2,
        "name": "loooong dog"
    }
]

def get_all_employees():
    """gets all the employees
    """
    return EMPLOYEES


def get_single_employee(id):
    """gets one employee
    """
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee