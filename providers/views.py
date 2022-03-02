from django.shortcuts import render
from .serializers import ServiceAreaSerializer
from .models import ServiceArea
from users.models import CustomUser
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from shapely.geometry import Point, Polygon
import json


def check_if_point_in_polygom(point, coordinates):
    poly = Polygon(coordinates)
    return point.within(poly)


class ServiceAreaList(APIView):
    def get(self, request, format=None):
        snippets = ServiceArea.objects.all()
        serializer =ServiceAreaSerializer(snippets, many=True)
        return Response(serializer.data)


class ServiceAreaCreateDetail(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = ServiceAreaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckServiceArea(APIView):
    pass


class ServiceAreaUpdateDetail(APIView):
    def get_object(self, tk):
        try:
            return ServiceArea.objects.get(polygon_name=tk)
        except ServiceArea.DoesNotExist:
            raise Http404
    def put(self, request, tk, format=None):
        snippet = self.get_object(tk)
        serializer = ServiceAreaSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAreaDeleteDetail(APIView):
    def get_object(self, tk):
        try:
            return ServiceArea.objects.get(polygon_name=tk)
        except ServiceArea.DoesNotExist:
            raise Http404
    def delete(self, request, tk, format=None):
        snippet = self.get_object(tk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




