from django.shortcuts import render

def post_list(request):
    return render(request, 'newblog/post_list.html', {})
