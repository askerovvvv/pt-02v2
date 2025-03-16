from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import DepartmentModelViewSet, ItemViewSet, NoteListCreateApiView

router = DefaultRouter()
router.register("", DepartmentModelViewSet)

urlpatterns = [
    path('department/', include(router.urls)),
    path('item/', ItemViewSet.as_view({
        "get": "list",
        "post": "create"
    })),
    path("note/", NoteListCreateApiView.as_view())
]


