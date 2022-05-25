from django.urls import path
from app1 import views


urlpatterns = [
    path("post_family/<str:name>/<int:dni>", views.post_family),
    path("get_family/<int:id>", views.get_family),
    path("all_family/", views.all_family),

]

