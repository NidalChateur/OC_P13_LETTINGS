# pylint: disable=no-member

from django.shortcuts import render

from home.add_log import add_log

from .models import Letting


def index(request):
    """List view

    Aenean leo magna, vestibulum et tincidunt fermentum,
    consectetur quis velit.
    Sed non placerat massa. Integer est nunc,
    pulvinar a tempor et, bibendum id arcu.
    Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae;
     Cras eget scelerisque"""

    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}

    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Detail view

    Cras ultricies dignissim purus, vitae hendrerit ex varius non.
    In accumsan porta nisl id eleifend. Praesent dignissim,
    odio eu consequat pretium, purus urna vulputate arcu,
    vitae efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta.
    Maecenas auctor, est ut luctus congue, dui enim mattis enim,
    ac condimentum velit libero in magna. Suspendisse potenti. In tempus a nisi sed laoreet.
    Suspendisse porta dui eget sem accumsan interdum.
    Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
    In tristique mauris eu velit fermentum, tempus pharetra est luctus.
    Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
    Mauris condimentum auctor elementum. Donec quis nisi ligula.
    Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet."""

    try:
        the_letting = Letting.objects.get(id=letting_id)
        context = {
            "title": the_letting.title,
            "address": the_letting.address,
        }

        return render(request, "lettings/letting.html", context)

    except Letting.DoesNotExist:
        error = f"Letting.DoesNotExist : Letting id n°{letting_id} does not exist !"
        add_log(error_type="exception", error_message=error)

        return render(request, "404.html", {"error": error})

    except ValueError:
        error = f"ValueError : Field id expected a number but got {letting_id}"
        add_log(error_type="exception", error_message=error)

        return render(request, "404.html", {"error": error})
