from django.shortcuts import render


# Create your views here.
def profile(request):
    return render(request, 'profile.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def mr(request):
    return render(request, 'mr.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def songs(request):
    return render(request, 'songs.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def likes(request):
    return render(request, 'likes.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def followings(request):
    return render(request, 'followings.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def followers(request):
    return render(request, 'followers.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def comments(request):
    return  render(request, 'comments.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})


def track_detail(request):
    return  render(request, 'track_detail.html', {'range': range(10), 'sl_range': range(3), 'sfw_range': range(8), 'sfi_range': range(3)})
