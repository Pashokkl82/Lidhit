from rest_framework import generics, status
from rest_framework.response import Response
import phonenumbers
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
import datetime
from .models import *


class ListFormView(generics.ListAPIView):
    """Список  форм шаблонов"""
    def get(self, request, *args, **kwargs):  # pylint: missing-function-docstring, unused-argument
        email = request.query_params.get('email')
        try:
            validate_email(email)
        except ValidationError as e:
            print("bad email, details:", e)
        else:
            print("good email")
        phone = request.query_params.get('phone')
        my_number = phonenumbers.parse(phone, "RU")
        try:
            phonenumbers.is_valid_number(my_number)
        except ValidationError as e:
            print("bad phone, details:", e)
        else:
            print("good phone")
        date = request.query_params.get('data')
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        text = request.query_params.get('text')
        q = FormTemplate.objects.filter(fname1__in=request.query_params.keys(), fname2__in=request.query_params.keys(),
                                        fname3__in=request.query_params.keys(), fname4__in=request.query_params.keys())
        return Response(q[0].name, status=status.HTTP_200_OK)
