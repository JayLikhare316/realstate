from django.urls import path ,reverse
from . import views

urlpatterns = [
    path('', views.masterlogin, name='login'),
    path('category', views.category, name='category'),
    path('addcategory', views.addcategory, name='addcategory'),
    path('deletecategory/<int:id>', views.deletecategory, name='deletecategory'),
    path('editcategory/<int:id>', views.editcategory, name='editcategory'),
    path('addsubcategory/<int:id>', views.addsubcategory, name='addsubcategory'),
    path('deletesub/<int:id>', views.deletesub, name='deletesub'),
    path('editsub/<int:id>', views.editsub, name='editsub'),

]
