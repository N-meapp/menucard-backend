from django.shortcuts import render,redirect,HttpResponse
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status
# from django.contrib.auth import logout




# code for login validation
class LoginView(APIView):
    def post(self, request):
        # Get username and password from request
        username = request.data.get('username')
        password = request.data.get('password')
        
        # Check if the credentials are valid
        check = Login.objects.filter(username=username, password=password).first()

        if check:
            # If valid, serialize the login data
            serializer = LoginSerializer(check)
            
            # Set the session for the user
            request.session['user_id'] = check.id  # Assuming 'id' is the primary key of Login model
            request.session.modified = True  # Mark the session as modified
            request.session.save()
            print(f"Session saved with user_id: {request.session['user_id']}")

            return Response({
                "message": "Login successful",
                "user": request.session['user_id'],
            }, status=status.HTTP_200_OK)
        else:
            # If invalid, return an error message
            return Response({
                "message": "Check username and password",
            }, status=status.HTTP_401_UNAUTHORIZED)

# def test_session(request):
#         request.session['userid'] = 'user_id'
#         request.session.save()
#         value = request.session.get('userid', 'No session')
#         return HttpResponse(f"Session test value: {value}")




#   code for logout
class LogoutView(APIView):
    def post(self, request):
        # Safely access session data using get to avoid KeyError
        user_id = request.session.get('user_id')
        if user_id:
            print(f'Session found 😃 for user_id: {user_id}')
            # Clear the session
            request.session.flush()
            return Response({
                "message": "Logged out successfully"
            }, status=status.HTTP_200_OK)
        else:
            print('No active session found')
            return Response({
                "message": "No active session found"
            }, status=status.HTTP_400_BAD_REQUEST)

from django.http import HttpResponse




class LoginModelCreateView(APIView):
    def get(self,request):
        output = [{'name':output.name,
                   "password":output.password}
                   for output in Login.objects.all()]
        return Response(output)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# code for get and post menu items

class MenuItemsList(APIView):
    def get(self, request):
        # Filter Menu_items where waiting is not 'null'
        menu_items = Menu_items.objects
        serializer = MenuItemsSerializer(menu_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# code for get and post order

class OrderItemsList(APIView):
    def get(self, request):
        # First get the new orders and accepted/picked orders
        new_orders = Order.objects.filter(result='pending').order_by('-result')
        picked_orders = Order.objects.filter(result='placed').order_by('-result')

        # Combine the two querysets, new orders first and picked orders next
        all_orders = list(new_orders) + list(picked_orders)

        # Serialize the orders
        serializer = OrderSerializer(all_orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

# code for get and post category items

class CategoryItemsList(APIView):
    def get(self, request):
        category_items = Category.objects.all()
        serializer = CategoryItemsshowSerializer(category_items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        category = Category.objects.all()
        test = Category.objects.filter(Category_name=request.data.get('Category_name'))
        if test:
            return Response({"message":"already exist"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = CategoryItemsshowSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# code for cancel order

class DeleteOrderIfNull(APIView):
    def get(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
            # Serialize the order and return it
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Order.DoesNotExist:
            return Response({"message": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
            order = Order.objects.get(pk=pk)
            # Check if the `status` field (or any other field) is `None`
            if order.result == "pending":  # Replace 'status' with the actual field you're checking
                order.delete()
                return Response({"message": "Order deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "Order cannot be deleted ."}, status=status.HTTP_400_BAD_REQUEST)
            
# code for change food number 
class Food_order_updation(APIView):
    def get(self, request,id=None):
        order_items = Order.objects.all()
        serializer = OrderSerializer(order_items, many=True)
        return Response(serializer.data)

    def patch(self, request, id):
        try:
            # Fetch the instance to be updated
            food_item = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Extract the 'hide' field from the request data
        food = request.data.get('quantity')
        
        # Debug: Check if the hide value is being received
        print(f"Received 'quantity' value: {food}")

        if food_item.result == "pending":
            # Update only the 'hide' field of the model
            food_item.quantity = food
            food_item.save()

            # Return the updated data
            serializer = OrderSerializer(food_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # No 'hide' field provided, return error message
            return Response({'detail': 'order is already picked.'}, status=status.HTTP_400_BAD_REQUEST)


# code for filter category and show correct items when search for corresponding category

class CategoryFiltering(APIView):
    def post(self, request):
        # Print the full request body to check what is being received
        print(f"Request data: {request.data}")

        # Get the category from the request body
        cate = request.data.get('category', None)
        print(f"Category from request: {cate}")  # Debug print

        if cate is None:
            return Response({"message": "Category not provided."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
            # Filter by category
                cat = Menu_items.objects.filter(category=cate)

                if not cat.exists():
                    return Response({"message": f"No items found for category '{cate}'."}, status=status.HTTP_404_NOT_FOUND)
            
                serializer = MenuItemsSerializer(cat, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# code for update,delete the menu items

class Update_menu(APIView):
    def get(self,request,id=None):
        datas=Menu_items.objects.all()
        serializer=MenuItemsSerializer(datas,many=True)
        return Response(serializer.data)
    def put(self, request, id):
        try:
        # Fetch the existing item or return 404 if it doesn't exist
            menu = Menu_items.objects.get(id=id)
        except Menu_items.DoesNotExist:
            return Response({"error": "Menu item not found."}, status=status.HTTP_404_NOT_FOUND)

    # Pass partial=True to allow partial updates
        serializer = MenuItemsSerializer(menu, data=request.data, partial=True)
    
    # Check if the provided data is valid
        if serializer.is_valid():
        # Save the updated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
        # If invalid, return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,id):
        item_remove = get_object_or_404(Menu_items, id=id)
        if item_remove:
            item_remove.delete()
            return Response({"message": "deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message":"cant delete"} , status=status.HTTP_400_BAD_REQUEST)  

class Update_hide(APIView):
    def put(self, request, id):
        try:
            # Fetch the instance to be updated
            menu_item = Menu_items.objects.get(id=id)
        except Menu_items.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Extract the 'hide' field from the request data
        hide_value = request.data.get('hide')
        
        # Debug: Check if the hide value is being received
        print(f"Received 'hide' value: {hide_value}")
        menu_item.hide = hide_value
        menu_item.save()    
        if hide_value is not None:
            # Update only the 'hide' field of the model
            

            # Return the updated data
            serializer = MenuItemsSerializer(menu_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # No 'hide' field provided, return error message
            return Response({'detail': 'Hide value is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
# code for editing category

class Category_update(APIView):
    def get(self,request,id=None):
        datas=Category.objects.all()
        serializer=CategoryItemsshowSerializer(datas,many=True)
        return Response(serializer.data)
    def put(self, request, id):
        try:
        # Fetch the existing item or return 404 if it doesn't exist
            menu = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"error": "Category item not found."}, status=status.HTTP_404_NOT_FOUND)

    # Pass partial=True to allow partial updates
        serializer = CategoryItemsshowSerializer(menu, data=request.data, partial=True)
    
    # Check if the provided data is valid
        if serializer.is_valid():
        # Save the updated data
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
        # If invalid, return the errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        category = Category.objects.get(id=id)
        category.delete()
        return Response({"message": "deleted successfully."}, status=status.HTTP_204_NO_CONTENT)    



class Update_order_placing(APIView):
    def get(self, request, id=None):
        # Retrieve all orders
        menu_items = Order.objects.all()
        serializer = OrderSerializer(menu_items, many=True)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            # Fetch the instance to be updated by its ID
            result_item = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        
        # Extract the field to update (e.g., 'result') from the request data
        result_value = request.data.get('result')

        # Debug: Check if the 'result' field is being received
        print(f"Received 'result' value: {result_value}")

        if result_value is not None:
            # Update only the 'result' field of the model
            result_item.result = result_value
            result_item.save()

            # Return the updated data
            serializer = OrderSerializer(result_item)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:

       # No 'hide' field provided, return error message
            return Response({'detail': 'hide value is required.'}, status=status.HTTP_400_BAD_REQUEST)