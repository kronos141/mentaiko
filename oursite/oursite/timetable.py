from django.shortcuts import render

def timetable(request):
    return render(request, 'timetable.html')

def timetable_popup(request):
    return render(request, 'timetable_popup.html')
