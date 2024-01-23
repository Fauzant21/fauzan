from django.urls import path
from .import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    #path('tentang-kami', views.tentang, name='tentang'),
    #path('Hubungi Kami', views.kontak, name='kontak'),
    path('Hubungi Kami', views.KontakView.as_view(), name='kontak'),
    path('profil-kami', views.profil, name='profil'),
    path('pemesanan-kami', views.pemesanan, name='pemesanan'),
    path('checkout', views.CheckoutView.as_view(), name='checkout'),
    path('cari', views.cari, name='cari'),


    path('<slug:slug>', views.kategori, name='kategori'),
    path('<slug:kategori_slug>/<slug:slug>', views.produk, name='produk'),
]
