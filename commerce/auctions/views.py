from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ListingForm
from .models import User, Listing, Category

# from .utils import formParser

def index(request):
    # Put all the active listing here
    print(request.session['watchlist'])
    listings = Listing.objects.order_by('-created_at')
    return render(request, "auctions/index.html", {"listings": listings, "request": request})


def listing_page(request, item_id):
    listing_details = Listing.objects.get(id=item_id)
    return render(request, "auctions/listing_page.html", {"listing": listing_details})


def create_listing(request):
    form = ListingForm()
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listed_by = User.objects.get(username=request.user)
            category = Category.objects.get(id=form.cleaned_data["category"].id)
            listing = Listing(item_name=form.cleaned_data["item_name"],
                              starting_price=form.cleaned_data["starting_price"],
                              listed_by=listed_by,
                              image=form.cleaned_data["image"],
                              description=form.cleaned_data["description"],
                              category=category)
            listing.save()
            # print(form.cleaned_data["item_name"])
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/create_listing.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def watchlist_add(request, item_id):
    if 'watchlist' in request.session:
        request.session['watchlist'].append(int(item_id))
        request.session.modified = True
    else:
        request.session['watchlist'] = []
        request.session['watchlist'].append(int(item_id))
        request.session.modified = True

    return HttpResponseRedirect(reverse("index"))


def watchlist_remove(request, item_id):
    item_id = int(item_id)
    request.session['watchlist'].remove(int(item_id))
    request.session.modified = True
    return HttpResponseRedirect(reverse("index"))