from django.shortcuts import render
from testapp.utils import dropbox_list_folder

def index(request):
    if request.user.is_authenticated:
        folder_contents = dropbox_list_folder(request.user)
    else:
        folder_contents = None
    context = {
        "folder_contents": folder_contents,
    }
    return render(request, "index.html", context)
