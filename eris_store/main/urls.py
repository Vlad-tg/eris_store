from django.urls import path, re_path, include
from . import views
from django.contrib.auth.views import LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.contrib.auth import views as auth_views
from .filter_laptop import FilterLaptopView
from .views import (
    AllView,
    CategoryDetailView,
    CartView,
    AddToCartView,
    DeleteFromCartView,
    ChangeQTYView,
    CheckoutView,
    MakeOrderView,
    LoginView,
    CreateAccountView,
    CategoryFilterLaptopsView,
    SearchViews,
    TestSearchProductView,
    AddStarRatingView,
    SendCommentViews,
    VerificationView,
    RandomProductERMAView,
    RandomView

)

urlpatterns = [
    path('', AllView.as_view(), name='all'),
    path('search-product-test/', TestSearchProductView.as_view(), name='search_product_test'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('filter-laptop/', FilterLaptopView.as_view(), name='filter_laptop'),
    path('filter-laptop-category/', CategoryFilterLaptopsView.as_view(), name='filter_laptop_category'),
    path('search/', SearchViews.as_view(), name='search_all'),
    path('products/<slug>/', views.product_rating, name='base_product'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-gty-cart/<str:slug>/', ChangeQTYView.as_view(), name='change_gty_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
    path('create_account/', CreateAccountView.as_view(), name='create_account'),
    path('account/', views.account_view, name='account'),
    path('change_information/', views.change_information_view, name='change_information'),
    path('change_icon/', views.change_icon_view, name='change_icon'),
    path('change_sequence/', views.change_sequence_view, name='change_sequence'),
    path('add-rating/', views.AddStarRatingView.as_view(), name='add_rating'),
    path('post-comment/', views.post_comment, name="post_comment"),
    path('products/<slug>/comment/', views.leave_comment_and_rating_views, name="leave_comment_rating"),
    path('send-comment/', SendCommentViews.as_view(), name="send_comment"),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
    path('random-product/', RandomView.as_view(), name='random_product'),
    path('random-product-erma/', RandomProductERMAView.as_view(), name='random_product_erma'),
    path('promo-code/', views.promo_cod_view, name='promo_code'),


    path('accounts/password_reset/',
         PasswordResetView.as_view(template_name='main/reset_password/password_reset_form.html'),
         name='password_reset'),
    path('accounts/password_change/done/',
         PasswordResetDoneView.as_view(template_name='main/reset_password/password_reset_done.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='main/reset_password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done/',
         PasswordResetCompleteView.as_view(template_name='main/reset_password/password_reset_complete.html'),
         name='password_reset_complete'),
]





