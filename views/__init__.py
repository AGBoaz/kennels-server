#get related
from .animal_requests import get_all_animals, get_single_animal
from .location_requests import get_all_locations, get_single_location
from .customer_requests import get_all_customers, get_single_customer
from .employee_requests import get_all_employees, get_single_employee

#post related
from .animal_requests import create_animal
from .customer_requests import create_customer
from .employee_requests import create_employee
from .location_requests import create_location

#delete related
from .animal_requests import delete_animal
from .customer_requests import delete_customer
from .employee_requests import delete_employee
from .location_requests import delete_location

#put related
from .animal_requests import update_animal
from .customer_requests import update_customer
from .employee_requests import update_employee
from .location_requests import update_location


