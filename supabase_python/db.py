from insert import add_application
from read import get_all_applications, get_application_by_email
from update import update_application
from delete import delete_application

# print("\n1. Adding a new application...")
# add_application()

# print("\n2. Fetching all applications...")
# get_all_applications()

print("\n3. Fetching application by email...")
get_application_by_email("ujjwal@invact.com")

# print("\n4. Updating salary for an application...")
# update_application("john.doe@example.com", "14 LPA")

# print("\n5. Deleting an application...")
# delete_application("john.doe@example.com")
