from django.urls import path
from .views import SignInView,SignUpView,IndexView, add_answer, upvote_answer, signout_view
urlpatterns = [
    path("",SignInView.as_view(),name="signin"),
    path("logout",signout_view,name="signout"),
    path("register",SignUpView.as_view(),name="signup"),
    path("index",IndexView.as_view(),name="index"),
    path("questions/<int:id>/answer/add", add_answer, name='add-answer'),
    path("answer/<int:id>/upvote", upvote_answer, name="upvote-answer"),
]
