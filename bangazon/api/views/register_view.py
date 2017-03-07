from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
import json
from api import models




class RegisterView(generics.RetrieveAPIView):
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
        # new_user = authenticate(username=new_user['username'], password=new_user['password'])
        models.Customer.objects.create(
            user=new_user,
            street_address=req_body['street_address'],
            city=req_body['city'],
            state=req_body['state'],
            zip_code=req_body['zip_code']
            )
        success = False
        if new_user is not None:
            if new_user.is_active:
                login(request, new_user)
                data = json.dumps({
                    'success': True,
                    'username': new_user.username,
                    'email': new_user.email,
                })
                return HttpResponse(data, content_type='application/json')

            return HttpResponse(self._error_response('disabled'), content_type='application/json')
        return HttpResponse(self._error_response('invalid'), content_type='application/json')