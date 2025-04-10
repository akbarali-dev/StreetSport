from django.urls import path
from .views import (StadiumCreateView, MyStadiumsListView, StadiumAddManagerView, StadiumConfirmView,
                    AdminStadiumDeleteView, AdminStadiumEditView, StadiumCountViewSet,
                    ActiveStadiumsListView, StadiumBookingCreateView, BookingsListView,
                    ConfirmPaymentByManagerView)

urlpatterns = [
    path('create/', StadiumCreateView.as_view(), name='stadium-create'),
    path('list/', MyStadiumsListView.as_view(), name='get-my-stadium'),
    path('add-manager/', StadiumAddManagerView.as_view(), name='stadium-add-manager'),
    path('<str:stadium_id>/confirm/', StadiumConfirmView.as_view(), name='confirm-stadium'),
    path('<str:pk>/admin-edit/', AdminStadiumEditView.as_view(), name='admin-action-edit'),
    path('<str:pk>/admin-delete/', AdminStadiumDeleteView.as_view(), name='admin-action-delete'),
    path('count/', StadiumCountViewSet.as_view(), name='admin-stadion-count'),
    path('booking-stadiums/', StadiumBookingCreateView.as_view(), name='booking-stadiums'),
    path('booking-stadiums-list/', BookingsListView.as_view(), name='booking-stadium-list'),
    path('dont-booking-stadiums/', ActiveStadiumsListView.as_view(), name='dont-booking-stadiums'),
    path('<uuid:booking_id>/confirm-payment/', ConfirmPaymentByManagerView.as_view(), name='confirm-payment'),
]
