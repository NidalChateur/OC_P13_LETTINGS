from django.shortcuts import render

from .add_log import add_log


def index(request):
    """Home page view

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
    Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
    vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum,
    eget consequat ipsum lobortis quis. Phasellus eleifend ex auctor venenatis tempus.
    Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi,
    pellentesque iaculis enim cursus in. Praesent volutpat porttitor magna,
    non finibus neque cursus id."""

    return render(request, "index.html")


def custom_404(request, exception):
    """activated when DEBUG=False"""

    error = f"404 error : {exception}"
    add_log(error_type="error", error_message=error)

    return render(request, "404.html", status=404)


def custom_500(request):
    """activated when DEBUG=False"""

    error = "500 error"
    add_log(error_type="error", error_message=error)

    return render(request, "500.html", status=500)


def check_500(request):
    """test 500 error view"""

    raise ValueError("Test 500 error !")
