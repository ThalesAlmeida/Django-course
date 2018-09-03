from django.urls import path
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete

from .views import PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete


urlpatterns = [
    # FUNCTION BASED VIEWS
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="persons_update"),
    path('delete/<int:id>/', persons_delete, name="persons_delete"),

    # CLASS BASED VIEWS
    path('personlist/', PersonList.as_view(), name='person-list'),
    path('persondetail/<pk>/', PersonDetail.as_view(), name='person-detail'),
    path('personcreate/', PersonCreate.as_view(), name='person-create'),
    path('personupdate/<pk>/', PersonUpdate.as_view(), name='person-update'),
    path('persondelete/<pk>/', PersonDelete.as_view(), name='person-delete'),
]