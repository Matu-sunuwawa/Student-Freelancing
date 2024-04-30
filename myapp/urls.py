from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import LoginView, RegistrationView, HomePageView, GuestPageView, CartPageView, CartDeleteView, CartUpdateView, CheckoutPageView, SubmitInfo, Searchpage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('guestpage/', GuestPageView.as_view(), name='guestpage'),
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('searchpage/', Searchpage.as_view(), name='searchpage'),
    path('cartpage/', CartPageView.as_view(), name='cartpage'),
    path('delete_list/<str:pk>/', CartDeleteView.as_view(), name='delete_list'),
    path('update_cart_list/', CartUpdateView.as_view(), name='update_cart_list'),
    path('checkout/', CheckoutPageView.as_view(), name='checkout'),
    path('editinfo/', SubmitInfo.as_view(), name='editinfo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
