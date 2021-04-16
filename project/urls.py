from django.urls import path
from . import views
urlpatterns = [
    path('list/', views.list, name="list"),
    path('update/<int:project_id>', views.update, name="update"),
    path('<int:project_id>/', views.detail, name="detail"),
    path('post/', views.post, name="post"),
    path('com/<int:com_id>/', views.comdel, name="comdel"),
    path('list/<int:cat_id>', views.cat_filter, name="catfilter"),
    path('apply/<int:project_id>', views.apply, name="apply"),
    path('managelist/', views.managelist, name="managelist"),
    path('team/<int:project_id>', views.team, name="team"),
    path('done/<int:project_id>', views.done, name="done"),
    path('accept/<int:project_id>/<int:apply_id>', views.accept, name="accept"),
    path('reject/<int:project_id>/<int:apply_id>', views.reject, name="reject"),
]
