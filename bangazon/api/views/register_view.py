from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from api import models




class RegisterView(generics.RetrieveAptView):
    permission_classes = (AllowAny,)

    error_messages = {
    'invalid': 'Please enter a valid username or password',
    'disabled': 'Sorry, account suspended'
    }

    def _error_response(self, message_key):
        data = json.dumps({
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
            })

        @csrf_exempt
    def post(self, request):
        permission_classes = (AllowAny,)
        """
        Purpose: Register a user
        Author: @rtwhitfield84
        """

        # data = request.POST
        req_body = json.loads(request.body.decode())
        new_user = User.objects.create_user(
            username=req_body['username'],
            email=req_body['email'],
            password=req_body['password'],
            first_name=req_body['first_name'],
            last_name=req_body['last_name'],
            )

        # models.Customer.objects.create(
        #     user=new_user,
        #     street_address=data['street_address'],
        #     city=data['city'],
        #     state=data['state'],
        #     zip_code=data['zip_code']
        #     )
