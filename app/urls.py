from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm

urlpatterns = [
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(),name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    # path('profile/', views.profile, name='profile'),
    path('profile/',auth_views.LoginView.as_view(template_name='app/profile.html',authentication_form=LoginForm),name='profile'),
    
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('mobile/', views.mobile, name='mobile'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
     
    # path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'), 
    
    path('checkout/', views.checkout, name='checkout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
