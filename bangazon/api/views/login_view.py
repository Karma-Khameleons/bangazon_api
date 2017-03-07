from django.contrib.auth.models import User
from rest_framework import  generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
from api import models

class LoginView(generics.RetrieveAPIView):
	permission_classes = (AllowAny,)

	error_messages = {
	'invalid': "Invalid username or Password",
	'disabled': "Sorry, this account is suspended",
	}

	def _error_response(self, message_key):
		data = json.dumps({
			'success': False,
			'message': self.error_messages[message_key],
			'user_id': None,
		})

	@csrf_exempt
	def post(self,request):
	    permission_classes = (AllowAny,)

	    req_body = json.loads(request.body.decode())
	    username = req_body['username']
	    password = req_body['password']
	    user = authenticate(username=username, password=password)

	    success = False
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            data = json.dumps({
	                'success': True,
	                'username': user.username,
	                'email': user.email,
	            })
	            return HttpResponse(data, content_type='application/json')

	        return HttpResponse(self._error_response('disabled'), content_type='application/json')
	    return HttpResponse(self._error_response('invalid'), content_type='application/json')

