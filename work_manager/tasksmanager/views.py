from django.shortcuts import render


def index(request):
    my_variable = "Hello world!"
    years_old = 15
    array_city_capitale = ["Paris", "London", "Washington"]
    return render(request, 'en/public/index.html', {
        "my_var": my_variable,
        "years": years_old,
        "array_city": array_city_capitale
    })

def connection(request):
    return render(request, 'en/public/connection.html')