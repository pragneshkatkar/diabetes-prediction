from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import pickle
import pandas as pd

model = pickle.load(open("C:\Users\pragn\diabetes_prediction\Diabetes.pkl", "rb"))

from main.models import Doctor, Feedback, Prediction, UsersAddress

# Create your views here.

@api_view(['POST', 'PUT'])
def signup_view(request):
    if request.method == 'POST':
		# email = request.data['email']
		# check = User.objects.filter(email=email).exists()
		# if check:
		# 	return Response({'message': 'Email already exists'})
        user = User.objects.create_user(
            first_name=request.data['first_name'],
            last_name=request.data['last_name'],
            email=request.data['email'],
            password=request.data['password'],
            username=request.data['username']
        )
        user.save()
        return Response()
    elif request.method == 'PUT':
        user = User.objects.get(id=request.data['user_id'])
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.username = request.data['username']
        user.save()
        return Response()

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        print(request.user)
        response = Response()
        email = request.data['username']
        password = request.data['password']
        username_exists = User.objects.filter(email=email).exists()
        print(username_exists)
        status = 'Invalid Username'
        if username_exists:
            user = authenticate(request, username=email, password=password)
            print(user)
            if user is not None:
                login(request, user)
                # payload = jwt_payload_handler(user)
                # token = jwt_encode_handler(payload)
                # response.set_cookie(key='token', value=token, httponly=True)
                status = 'Successful'
                # is_mfa_user = EmployeeCompany.objects.filter(user_id=request.user.id).last().is_mfa_user
                # if not is_mfa_user:
                request.session['username'] = user.email
                request.session['user_id'] = user.id
                response.data = {
                    'status': status,
                }
            else:
                status = 'Incorrect Password'
                response.data = {
                    'status': status,
                }
        return response

@api_view(['POST', 'GET'])
def predict_view(request):
    response = Response({'flash': False, 'message': 'Invalid request'})
    if request.method == 'POST':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        name = request.data['name']
        no_of_pregnancies = request.data['no_of_pregnancies']
        glucose = request.data['glucose']
        blood_pressure = request.data['blood_pressure']
        skin_thickness = request.data['skin_thickness']
        insulin = request.data['insulin']
        bmi = request.data['bmi']
        diabetes_pedigree_function = request.data['diabetes_pedigree_function']
        age = request.data['age']
        row_df = pd.DataFrame([pd.Series([no_of_pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age])])
        prediction=model.predict_proba(row_df)
        output='{0:.{1}f}'.format(prediction[0][1], 2)
        output = str(float(output)*100)+'%'
        # if output>str(0.5):
        #     return render_template('result.html',pred=f'You have chance of having diabetes.\nProbability of having Diabetes is {output}')
        # else:
        #     return render_template('result.html',pred=f'You are safe.\n Probability of having diabetes is {output}')
        # # prediction
        prediction = Prediction.objects.create(
            user_id=user,
            name=name,
            number_of_pregnancies=no_of_pregnancies,
            glucose=glucose,
            blood_pressure=blood_pressure,
            skin_thickness=skin_thickness,
            insulin=insulin,
            bmi=bmi,
            age=age,
            model1_prediction=str(output),
            # model2_prediction=False,
            # model3_prediction=False,
            # model4_prediction=False,
            result=str(output)
        )
        prediction.save()
        response = Response({'flash': True, 'message': 'Prediction added successfully'})
    return response

@api_view(['PUT'])
def user_details_view(request):
    response = Response({'flash': False, 'message': 'Invalid request'})
    if request.method == 'PUT':
        user_id = request.session['user_id']
        user = User.objects.get(id=user_id)
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.save()
        address = UsersAddress.objects.filter(user_id=user).last()
        print(request.data['zipcode'])
        if address is not None:
            address.address = request.data['address']
            address.city = request.data['city']
            address.state = request.data['state']
            address.country = request.data['country']
            address.zip_code = request.data['zipcode']
            address.save()
        else:
            address = UsersAddress.objects.create(
                user_id=user,
                address=request.data['address'],
                city=request.data['city'],
                state=request.data['state'],
                country=request.data['country'],
                zip_code=request.data['zipcode']
            )
            address.save()
        response = Response({'flash': True, 'message': 'User details updated successfully'})
    return response



@api_view(['POST', 'PUT'])
def doctor_view(request):
    if request.method == 'POST':
		# email = request.data['email']
		# check = User.objects.filter(email=email).exists()
		# if check:
		# 	return Response({'message': 'Email already exists'})
        doctor = Doctor()
        doctor.name = request.data['name']
        doctor.email = request.data['email']
        doctor.degree = request.data['degree']
        doctor.contact_number = request.data['contact_number']
        doctor.is_active = request.data['is_active'] == "on"
        doctor.save()
        return Response()
    elif request.method == 'PUT':
        doctor = Doctor.objects.get(id=request.data['doctor_id'])
        doctor.name = request.data['name']
        doctor.degree = request.data['degree']
        doctor.contact_number = request.data['contact_number']
        doctor.email = request.data['email']
        doctor.is_active = request.data['is_active']
        doctor.save()
        return Response()
        
        

@api_view(['POST', 'GET'])
def feedback_view(request):
    user_id = request.session['user_id']
    if request.method == 'POST':
        feedback = Feedback()
        feedback.user_id = request.user
        feedback.feedback = request.data['feedback']
        feedback.save()
    return Response()