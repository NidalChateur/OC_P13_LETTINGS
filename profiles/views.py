# pylint: disable=no-member

from django.shortcuts import render

from home.add_log import add_log

from .models import Profile


def index(request):
    """List view

    Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
    sed consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
    massa dolor cursus neque, quis dictum lacus d"""

    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}

    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Detail view

    Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
    laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
    dolor id facilisis fringilla, eros leo tristique lacus,
    it. Nam aliquam dignissim congue.
    Pellentesque habitant morbi tristique senectus et netus et males"""

    try:
        the_profile = Profile.objects.get(user__username=username)
        context = {"profile": the_profile}

        return render(request, "profiles/profile.html", context)

    except Profile.DoesNotExist:
        error = f"Profile.DoesNotExist : User with username {username} does not exist !"
        add_log(error_type="exception", error_message=error)

        return render(request, "404.html", {"error": error})
