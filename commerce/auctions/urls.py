from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create-listing/", views.create_listing, name="create-listing"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<item_id>", views.listing_page, name="listing_page"),
    path("watchlist/add/<item_id>", views.watchlist_add, name="watchlist_add"),
    path("watchlist/remove/<item_id>", views.watchlist_remove, name="watchlist_remove")
]
