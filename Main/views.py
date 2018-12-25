from django.shortcuts import render

def main_page(request):
    return render(request, 'Main_Page.html',)