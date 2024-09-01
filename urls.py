from django.urls import path, include

from .views import SummaryView

appname="mailer"

urlpatterns = [
    path("", SummaryView.as_view()),
]