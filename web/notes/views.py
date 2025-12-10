from django.shortcuts import render, redirect
from .models import Note

def home(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        body = request.POST.get("body", "").strip()

        # Only create if title is not empty
        if title:
            Note.objects.create(title=title, body=body)

        # Redirect to avoid form resubmission on refresh
        return redirect("home")

    # GET request → just list notes
    notes = Note.objects.order_by("-created_at")
    return render(request, "notes/home.html", {"notes": notes})

