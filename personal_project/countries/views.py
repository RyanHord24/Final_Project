from django.http import JsonResponse
from .models import Country

def Get_country(request, id):
    try:
        country = Country.objects.get(id=id)
        return JsonResponse({
            "id": country.id,
            "name": country.name,
        })
    except Country.DoesNotExist:
        return JsonResponse({"error": "Country not found"}, status=404)

