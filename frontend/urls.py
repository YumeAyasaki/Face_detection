from django.urls import path

from .views import LoginView, RegisterView, HomeView, FaceDetectionView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("face/", FaceDetectionView.as_view(), name="face_detection"),
]