from django.shortcuts import render

# Create your views here.

def index(request):
    MeetUps = [
        {
            'title': 'A First Meetup', 
            'location': 'New York', 
            'slug':'a-first-meetup'
        },

        {
            'title': 'A Second Meetup', 
            'location': 'Paris', 
            'slug':'a-second-meetup'
        }

    ]
    return render(request, 'MeetUps/index.html', {
        'show_MeetUps': True,
        'MeetUps': MeetUps
    })

def meetup_detials(request):
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
    }
    return render(request, 'MeetUps/meetup-details.html',{
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description']
    })