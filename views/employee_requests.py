EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis",
        "address": "54 Sycamore Avenue",
        "locationId": 2
    },
    {
        "id": 2,
        "name": "loooong dog",
        "address": "54 Sycamore Avenue",
        "locationId": 2
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


def create_employee(employee):
    """creates one employee
    """
    # Get the id value of the last employee in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the employee dictionary
    employee["id"] = new_id

    # Add the employee dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee