from django.urls import path

from persons.views import PersonViews, get_persons_with_sales_opportunity

urlpatterns = [
    path("", PersonViews.as_view(), name="persons"),
    path("sales-opportunity", get_persons_with_sales_opportunity, name="sales opportunity"),
]
