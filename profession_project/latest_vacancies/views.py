import requests
from django.shortcuts import render


def latest_vacancies_page(request):
    # Replace 'YOUR_HH_API_KEY' with your actual HeadHunter API key
    hh_api_key = 'YOUR_HH_API_KEY'

    # Specify the profession for IT vacancies
    profession = 'С++'

    # Specify the number of vacancies to retrieve
    vacancies_count = 10

    # Construct the API endpoint URL
    api_url = f'https://api.hh.ru/vacancies?area=1&specialization=1.221&per_page={vacancies_count}&page=0&order_by=publication_time'

    # Make the API request
    response = requests.get(api_url, headers={'User-Agent': 'YourAppName/1.0', 'HH-User-Key': hh_api_key})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        vacancies = response.json()['items']

        # Prepare data for rendering
        context = {'vacancies': vacancies}

        # Render the template with the retrieved vacancies
        return render(request, 'latest_vacancies.html', context)
    else:
        # Handle errors here (e.g., log the error, display an error message)
        error_message = f"Error {response.status_code}: Unable to fetch vacancies from HeadHunter API."
        return render(request, 'error.html', {'error_message': error_message})
