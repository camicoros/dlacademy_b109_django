from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import CustomLoginView, CustomLogoutView, SignupView, ProfileView, ProfileEditView, AddFriendView, \
    CustomPasswordResetView, CustomPasswordResetViewDone, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

app_name = 'core'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
    path('edit-profile/<int:user_id>/', login_required(ProfileEditView.as_view()), name='edit_profile'),
    path('profile/<int:user_id>/add-remove-friend/', login_required(AddFriendView.as_view()), name='add_remove_friend'),

    # password reset
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', CustomPasswordResetViewDone.as_view(), name='password_reset_done'),
    path('password-reset/<str:uidb64>/<slug:token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
