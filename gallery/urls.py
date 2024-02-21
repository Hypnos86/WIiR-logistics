from django.urls import path
from gallery.views import GalleryListView

app_name = 'gallery'
urlpatterns = [
<<<<<<< HEAD
    path('', GalleryListView.as_view(), name='galleryList')
=======
    path('', GalleryListView.as_view(), name='galleryList'),

>>>>>>> 17099ceb532e315c9c8d4063c785f67955ad4583
]
