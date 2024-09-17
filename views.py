# views.py
from django.shortcuts import render
from .models import Person, LoginHistory
from .predictor import HeartAttackPredictor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

def predict_heart_attack(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            age = int(request.POST['age'])
            height = float(request.POST['height'])
            weight = float(request.POST['weight'])
            blood_pressure = float(request.POST['blood_pressure'])
            cholesterol_levels = float(request.POST['cholesterol_levels'])
            
            # Create a new Person object
            person = Person(
                name=name, 
                age=age, 
                height=height, 
                weight=weight, 
                blood_pressure=blood_pressure, 
                cholesterol_levels=cholesterol_levels
            )
            person.save()  # Save the person object to the database
            
            # Fetch previous Person records
            previous_persons = Person.objects.exclude(id=person.id)  # Exclude the newly added person

            # Use the HeartAttackPredictor class to make a prediction
            predictor = HeartAttackPredictor()
            prediction = predictor.predict(person)
            
            return render(request, 'result.html', {
                'prediction': prediction, 
                'person': person,  # Pass the newly created person object
                'previous_persons': previous_persons,  # Pass previous person records
            })
        except (KeyError, ValueError) as e:
            # Handle errors if any field is missing or invalid
            return render(request, 'index.html', {'error': 'Invalid input, please try again.'})
    
    return render(request, 'index.html')

@login_required
def login_history(request):
    history = LoginHistory.objects.filter(user=request.user).order_by('-login_time')
    return render(request, 'login_history.html', {'history': history})

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    LoginHistory.objects.create(user=user, login_time=timezone.now(), ip_address=ip_address)
