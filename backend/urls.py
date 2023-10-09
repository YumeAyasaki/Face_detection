from django.urls import path

from .views import login_user, logout_user, upload_image, register_user, face_detection

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("upload/", upload_image, name="upload"),
    path("register/", register_user, name="register"),
    path("face/", face_detection, name="face_detection")
]