from rest_framework.routers import SimpleRouter
from .views import postviewset, UserviewSet

router = SimpleRouter()
router.register(r'posts', postviewset, basename='post')
router.register(r'users', UserviewSet, basename='user')

urlpatterns = router.urls
