from django.shortcuts import render

def subjectbb(request):
    return render(request, 'subjectBB.html')

def subjectReview(request):
    return render(request, 'subject_review.html')
