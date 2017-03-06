from django.contrib.auth.models import User
from api import models







def register_customer(request):
    """
    Purpose: Register a user
    Author: @rtwhitfield84
    """

    data = request.POST

    new_user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        )

    models.Customer.objects.create(
        user=new_user,
        street_address=data['street_address'],
        city=data['city'],
        state=data['state'],
        zip_code=data['zip_code']
        )
