from rest_framework.routers import DefaultRouter
from core.api.views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'tables', TableViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'menucategories', MenuCategoryViewSet)
router.register(r'photos', PhotoViewSet)


