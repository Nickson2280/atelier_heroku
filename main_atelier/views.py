import datetime

from django.shortcuts import render, redirect
from .models import Category, Service, Events
from .forms import UserMessagesForm

# Create your views here.


def main(request):
    if request.method == 'POST':
        form = UserMessagesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    special_categories = Category.objects.filter(is_visible=True).filter(is_special=True).order_by('order_category')
    for item in special_categories:
        item.service = Service.objects.filter(category=item.pk)

    categories = Category.objects.filter(is_visible=True).filter(is_special=False).order_by('order_category')
    for item in categories:
        item.service = Service.objects.filter(category=item.pk)

    events = Events.objects.filter(event_date__gte=datetime.date.today())

    user_messages_form = UserMessagesForm()

    return render(request, 'index.html', context={'categories': categories,
                                                  'special_categories': special_categories,
                                                  'events': events,
                                                  'form': user_messages_form})
