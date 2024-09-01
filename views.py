from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count, Sum

# Create your views here.
from .models import CompanyModel, ContactModel, OrderModel
from .serializers import CompanySerializer, ContactSerializer, OrderSerializer

class SummaryView(APIView):
    def get(self, request):
        orders = OrderModel.objects.values_list("contact_id__company_id__name", "contact_id__first_name", "contact_id__last_name").annotate(order_count=Count("order_id", distinct=True), total_order=Sum("total"))
        # print(orders)
        return Response("Ishita", status=status.HTTP_200_OK)

