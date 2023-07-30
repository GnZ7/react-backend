from django.http import Http404, JsonResponse
from customers.models import Customer
from customers.serializer import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def customers(request):
    
    if request.method == 'GET': # invocar serializer y devolver clientes
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response({'customers': serializer.data})
    elif request.method == 'POST':  # Agregar elemento
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(): # comprobar si la información nueva es válida
            serializer.save()
            return Response({'customer': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, satus=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(['GET', 'POST', 'DELETE'])
def customer(request, id):
    # si el cliente buscado no existe, responde con un 404
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(data)
        return Response({'customer': serializer.data})
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_410_GONE)
    elif request.method == 'POST':  # Modificar elemento existente (update)
        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'customer': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
