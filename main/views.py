from django.shortcuts import render, redirect, get_object_or_404
from django.http import (
    HttpResponse, HttpResponseRedirect, JsonResponse
)
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.core import serializers
from django.utils.html import strip_tags

from .models import Product  
from .forms import ProductForm  
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

# ============ Utilities ============

def is_ajax(request):
    """Deteksi request AJAX dari header."""
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest' or \
           (request.headers.get('Accept') or '').startswith('application/json')

def _own_or_404(user, id):
    """Ambil product milik user; jika tidak ada -> 404-like (None)."""
    try:
        return Product.objects.get(pk=id, user=user)
    except Product.DoesNotExist:
        return None


# ============ Pages ============

def show_main(request):
    """Halaman utama grid produk (AJAX akan ambil data dari show_json)."""
    context = {
        'npm': '2406348710',
        "class": "PBP-C", 
        "last_login": request.COOKIES.get('last_login', '-'),
    }
    return render(request, "main.html", context)


@login_required
def create_product(request):
    """Halaman form create (server-rendered, opsional untuk tugas AJAX)."""
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.name = strip_tags(product.name or '')
            product.description = strip_tags(product.description or '')
            product.size = strip_tags(product.size or '')
            product.category = strip_tags(product.category or '')
            product.save()
            messages.success(request, "Produk berhasil dibuat.")
            return redirect("main:show_main")
        messages.error(request, "Form tidak valid.")
    return render(request, "create_product.html", {"form": form})


def show_product(request, id):
    """Halaman detail produk (server-rendered)."""
    product = get_object_or_404(Product, pk=id)
    try:
        product.product_views = (product.product_views or 0) + 1
        product.save(update_fields=["product_views"])
    except Exception:
        pass
    return render(request, "product_detail.html", {"product": product})


@login_required
def edit_product(request, id):
    """Halaman edit produk (server-rendered). Hanya pemilik."""
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST":
        if form.is_valid():
            p = form.save(commit=False)
            p.name = strip_tags(p.name or '')
            p.description = strip_tags(p.description or '')
            p.size = strip_tags(p.size or '')
            p.category = strip_tags(p.category or '')
            p.save()
            messages.success(request, "Produk berhasil diperbarui.")
            return redirect("main:show_product", id=str(product.id))
        messages.error(request, "Form tidak valid.")
    return render(request, "edit_product.html", {"form": form, "product": product})


@login_required
def delete_product(request, id):
    """Hapus produk (server-rendered via link). Hanya pemilik."""
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    messages.success(request, "Produk dihapus.")
    return redirect("main:show_main")


# ============ Auth (pages) ============

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Response AJAX
            if is_ajax(request):
                resp = JsonResponse({
                    "ok": True,
                    "username": user.username,
                    "redirect": reverse("main:show_main"),
                })
            else:
                resp = HttpResponseRedirect(reverse("main:show_main"))

            resp.set_cookie('last_login', str(user.last_login or 'Just now'))
            return resp
        
        if is_ajax(request):

            err = "Username/password salah"
            try:
                errs = form.non_field_errors() or []
                if not errs:
                    errs = sum([v for k,v in form.errors.items()], [])
                if errs:
                    err = errs[0]
            except Exception:
                pass
            return JsonResponse({"ok": False, "error": err}, status=400)

        messages.error(request, "Username/password salah")
        return render(request, "login.html", {"form": form})

    return render(request, "login.html", {"form": form})



def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save()  

            if is_ajax(request):
                return JsonResponse({
                    "ok": True,
                    "username": user.username,
                    "redirect": reverse("main:login")
                })
            messages.success(request, "Registrasi berhasil. Silakan login.")
            return redirect("main:login")

        if is_ajax(request):
            try:
                all_errs = []
                for _, errs in form.errors.items():
                    for e in errs:
                        all_errs.append(str(e))
                msg = all_errs[0] if all_errs else "Registrasi gagal. Periksa kembali isian."
            except Exception:
                msg = "Registrasi gagal. Periksa kembali isian."
            return JsonResponse({"ok": False, "error": msg}, status=400)

        messages.error(request, "Registrasi gagal. Periksa kembali isian.")
        return render(request, "register.html", {"form": form})

    # GET
    return render(request, "register.html", {"form": form})


def logout_user(request):
    logout(request)
    if is_ajax(request):
        resp = JsonResponse({"ok": True, "redirect": reverse("main:login")})
    else:
        resp = HttpResponseRedirect(reverse("main:login"))
    resp.delete_cookie('last_login')
    return resp


# ============ Data Endpoints (JSON / XML) ============

def show_json(request):
    """List semua product sebagai JSON untuk grid AJAX."""
    products = Product.objects.all().order_by('-created_at') if hasattr(Product, 'created_at') else Product.objects.all()
    data = []
    for p in products:
        data.append({
            "id": str(p.id),
            "name": p.name,
            "description": p.description,
            "thumbnail": p.thumbnail,
            "price": p.price,
            "stock": p.stock,
            "size": getattr(p, "size", None),
            "category": getattr(p, "category", None),
            "is_featured": getattr(p, "is_featured", False),
            "product_views": getattr(p, "product_views", 0),
            "created_at": (p.created_at.isoformat() if getattr(p, "created_at", None) else None),
            "user_id": getattr(p.user, "id", None),
        })
    return JsonResponse(data, safe=False)


def show_json_by_id(request, id):
    """Detail product by id (JSON) untuk halaman detail AJAX (kalau dipakai)."""
    try:
        p = Product.objects.select_related('user').get(pk=id)
    except Product.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)

    data = {
        "id": str(p.id),
        "name": p.name,
        "description": p.description,
        "thumbnail": p.thumbnail,
        "price": p.price,
        "stock": p.stock,
        "size": getattr(p, "size", None),
        "category": getattr(p, "category", None),
        "is_featured": getattr(p, "is_featured", False),
        "product_views": getattr(p, "product_views", 0),
        "created_at": (p.created_at.isoformat() if getattr(p, "created_at", None) else None),
        "user_id": getattr(p.user, "id", None),
        "user_username": getattr(p.user, "username", None),
    }
    return JsonResponse(data)


def show_xml(request):
    qs = Product.objects.all()
    return HttpResponse(serializers.serialize('xml', qs), content_type='application/xml')


def show_xml_by_id(request, id):
    qs = Product.objects.filter(pk=id)
    if not qs.exists():
        return HttpResponse('<error>Not Found</error>', content_type='application/xml', status=404)
    return HttpResponse(serializers.serialize('xml', qs), content_type='application/xml')


# ============ AJAX CRUD (Create / Update / Delete) ============

@login_required
@require_POST
def add_product_ajax(request):
    """Create via AJAX (dari modal)."""
    name = strip_tags(request.POST.get("name") or "")
    description = strip_tags(request.POST.get("description") or "")
    thumbnail = request.POST.get("thumbnail") or ""
    price = request.POST.get("price") or 0
    stock = request.POST.get("stock") or 0
    size = strip_tags(request.POST.get("size") or "")
    category = strip_tags(request.POST.get("category") or "")
    is_featured = (request.POST.get("is_featured") == "on")

    product = Product(
        name=name,
        description=description,
        thumbnail=thumbnail,
        price=price or 0,
        stock=stock or 0,
        size=size,
        category=category,
        is_featured=is_featured,
        user=request.user,
    )
    product.save()
    return JsonResponse({"ok": True, "id": str(product.id)}, status=201)


@login_required
@require_POST
def update_product_ajax(request, id):
    """Update via AJAX (hanya pemilik)."""
    product = _own_or_404(request.user, id)
    if not product:
        return JsonResponse({"ok": False, "error": "Not found"}, status=404)

    if "name" in request.POST:
        product.name = strip_tags(request.POST.get("name") or product.name)
    if "description" in request.POST:
        product.description = strip_tags(request.POST.get("description") or product.description)
    if "thumbnail" in request.POST:
        product.thumbnail = request.POST.get("thumbnail") or product.thumbnail
    if "price" in request.POST:
        product.price = request.POST.get("price") or product.price
    if "stock" in request.POST:
        product.stock = request.POST.get("stock") or product.stock
    if "size" in request.POST:
        product.size = strip_tags(request.POST.get("size") or product.size)
    if "category" in request.POST:
        product.category = strip_tags(request.POST.get("category") or product.category)
    if "is_featured" in request.POST:
        product.is_featured = (request.POST.get("is_featured") == "on")

    product.save()
    return JsonResponse({"ok": True, "id": str(product.id)})


@login_required
@require_POST
def delete_product_ajax(request, id):
    """Delete via AJAX (hanya pemilik)."""
    product = _own_or_404(request.user, id)
    if not product:
        return JsonResponse({"ok": False, "error": "Not found"}, status=404)
    product.delete()
    return JsonResponse({"ok": True})


# ============ AJAX Auth (Login / Register / Logout) ============

@require_POST
def api_login(request):
    username = request.POST.get("username") or ""
    password = request.POST.get("password") or ""
    user = authenticate(request, username=username, password=password)
    if not user:
        return JsonResponse({"ok": False, "error": "Username/password salah"}, status=400)
    login(request, user)
    response = JsonResponse({
        "ok": True,
        "username": user.username,
        "redirect": reverse("main:show_main"),
    })
    response.set_cookie('last_login', str(user.last_login or 'Just now'))
    return response


@require_POST
def api_register(request):
    from django.contrib.auth.models import User
    username = request.POST.get("username") or ""
    password1 = request.POST.get("password1") or request.POST.get("password") or ""
    password2 = request.POST.get("password2") or password1

    if not username or not password1:
        return JsonResponse({"ok": False, "error": "Semua field wajib diisi"}, status=400)
    if password1 != password2:
        return JsonResponse({"ok": False, "error": "Konfirmasi password tidak cocok"}, status=400)
    if User.objects.filter(username=username).exists():
        return JsonResponse({"ok": False, "error": "Username sudah dipakai"}, status=400)

    User.objects.create_user(username=username, password=password1)
    return JsonResponse({
        "ok": True,
        "username": username,
        "redirect": reverse("main:login")
    })


@require_POST
def api_logout(request):
    logout(request)
    resp = JsonResponse({"ok": True, "redirect": reverse("main:login")})
    resp.delete_cookie('last_login')
    return resp

def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)
    
@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user
        
        new_product = Product(
            name=name, 
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()
        
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)