from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.carrieres, name="carrieres"),
    path('<int:pk>', views.carriere, name="carriere"),
    path('details/', views.carrieresDetails, name="carrieres_details"),
    path('details/iframe', views.carrieresIframe, name="carrieres_iframe"),
    path('add/', views.addCarriere, name="add_carriere"),
    path('edit/<int:pk>', views.editCarriere, name="edit_carriere"),
    path('delete/<int:pk>', views.deleteCarriere, name="delete_carriere"),
    path('confirm/<int:pk>', views.confirmCarriere, name="confirm_carriere"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
