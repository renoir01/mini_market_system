from django.http import JsonResponse

def api_root(request):
    return JsonResponse({'message': 'Welcome to the API root endpoint'})