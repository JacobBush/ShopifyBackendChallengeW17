# Jacob Bush, University of Waterloo, 2017
#
# Made for Shopify
# Developer Intern - Winternship 2018
# Back End Development Problem
#
# Created and Tested in Python 3.6.0

import urllib.request, json 

# define a function to query the API
def get_page(base_url, page_number):
    # url is base_url combined with page_number
    combined_url = base_url + "?page=" + str(page_number)
    #get the data as a dictionary
    with urllib.request.urlopen(combined_url) as url:
        data = json.loads(url.read().decode())
    #return dictionary
    return data

def valid_customer_field (customer, field, constraints):
    # will validate an individual customer over a field/
    # field is a possible key in customer (ex. "name", "email", etc.)
    # constraints are the constraints imposed on the field - will be
    # all of ["required", "type", "length"] as per the assignment specifications.


    if ((field in customer) and (customer[field])):
        # field was provided
        print("field provided")
    else:
        # field was not provided - check if was required
        if (constraints["required"]):
            # field was required and not provided - this is an invalid field
            return False
    
    # We have checked all constraints for the field - the field is valid
    return True

def get_invalid_customers (customers, validations):
    # will return a dictionary of invalid customers, as per the specied id, invalid fields format.

    # All invalid customers will be stored in a list
    invalid_customers = [];

    #loop over the customers
    for customer in customers:
        # we will gather all of the invalid fields in an array
        invalid_fields = []

        for validation in validations:
            # We loop over each validation to ensure that the conditions are met
            for field in validation:
                constraints = validation[field]
                if not valid_customer_field (customer, field, constraints):
                    invalid_fields.append(field)
        
        if (invalid_fields):
            # There are some invalid fields - this customer is invalid
            invalid_customer_data = {"id" : customer["id"], "invalid_fields": invalid_fields}
            invalid_customers.append(invalid_customer_data)

    return invalid_customers

# URL to API
endpoint_url = 'https://backend-challenge-winter-2017.herokuapp.com/customers.json'

# Here we get the 1st page of user data
# Could be looped to get all pages
data = get_page(endpoint_url , 1)

invalid_customers = get_invalid_customers(data["customers"], data["validations"])
print (invalid_customers)
