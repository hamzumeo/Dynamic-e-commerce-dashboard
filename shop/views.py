from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from .models import Product, CartItem


def home_view(request):
    context = {
        "welcome_message": "Welcome to ShopSmart – your smart way to shop online."
    }
    return render(request, "shop/home.html", context)


def product_list_view(request):
    query = request.GET.get("q", "").strip()
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query)
        )

    paginator = Paginator(products, 12)  # 12 products per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "query": query,
    }
    return render(request, "shop/products.html", context)


@login_required
def cart_view(request):
    cart_items = CartItem.objects.select_related("product").filter(user=request.user)
    context = {
        "cart_items": cart_items,
    }
    return render(request, "shop/cart.html", context)


@login_required
def profile_view(request):
    user = request.user
    context = {
        "user_obj": user,
    }
    return render(request, "shop/profile.html", context)
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("/accounts/login/")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})

