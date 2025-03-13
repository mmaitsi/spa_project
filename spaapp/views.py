from django.shortcuts import render

# Home page view
def index(request):
    return render(request, 'index.html')

# About page view
def about(request):
    return render(request, 'about.html')

# Contact page view
def contact(request):
    return render(request, 'contact.html')

# Price page view
def price(request):
    return render(request, 'price.html')

# Appointment page view
def appointment(request):
    return render(request, 'appointment.html')

# Service page view
def service(request):
    return render(request, 'service.html')

# Team page view
def team(request):
    return render(request, 'team.html')

# Testimonial page view
def testimonial(request):
    return render(request, 'testimonial.html')

# Opening hours page view
def opening(request):
    return render(request, 'opening.html')
