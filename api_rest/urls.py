from rest_framework.routers import DefaultRouter

from api_rest.views import ReceiptsViewSet, CommentariesViewSet


router = DefaultRouter()
router.register(r"receipts", ReceiptsViewSet)
router.register(r"commentaries", CommentariesViewSet)

urlpatterns = []

urlpatterns += router.urls