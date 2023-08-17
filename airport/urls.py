from rest_framework.routers import SimpleRouter


router = SimpleRouter()
# router.register(r"news", NewsViewSet, basename="airport")


urlpatterns = router.urls

app_name = "airport"
