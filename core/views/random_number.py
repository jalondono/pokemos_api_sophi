import requests
import time
from rest_framework import status
from django.http import JsonResponse

MAX_RETRIES = 3


def validate_min_max_values(min_value: int, max_value: int):
    """
    Validate that min_value is less than max_value, and both are not None
    """
    if min_value is None or max_value is None:
        return JsonResponse({"error": f"Min value and Max value are required"},
                            status=status.HTTP_400_BAD_REQUEST)
    if min_value > max_value:
        return JsonResponse({"error": f"Min value: {min_value} can not be greater than Max value: {max_value}"},
                            status=status.HTTP_400_BAD_REQUEST)


def random_number_view(request):
    """Create a new user in the system (This is a public view)"""
    if request.method == "GET":
        attempt_num = 0  # keep track of how many times we've retried
        while attempt_num < MAX_RETRIES:
            url = "http://www.randomnumberapi.com/api/v1.0/random"
            min_value = request.GET.get('min')
            max_value = request.GET.get('max')
            validate_min_max_values(min_value, max_value)
            url = f"{url}?min={min_value}&max={max_value}&count=1"
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                return JsonResponse({"random_number": data}, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                # You can probably use a logger to log the error here
                time.sleep(5)  # Wait for 5 seconds before re-trying
        return JsonResponse({"error": "Request failed"}, status=r.status_code)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
