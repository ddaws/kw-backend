from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt import views as jwtviews
from api.views import ReviewViewSet, VocabularyViewSet, ReadingViewSet, LevelViewSet, ReadingSynonymViewSet, \
    FrequentlyAskedQuestionViewSet, AnnouncementViewSet, UserViewSet, ContactViewSet, ProfileViewSet, ReportViewSet, \
    MeaningSynonymViewSet

router = DefaultRouter()
router.register(r'review', ReviewViewSet, base_name="review")
router.register(r'profile', ProfileViewSet, base_name='profile')
router.register(r'vocabulary', VocabularyViewSet, base_name="vocabulary")
router.register(r'report', ReportViewSet, base_name="report")
router.register(r'reading', ReadingViewSet, base_name="reading")
router.register(r'level', LevelViewSet, base_name="level")
router.register(r'synonym/reading', ReadingSynonymViewSet, base_name="reading-synonym")
router.register(r'synonym/meaning', MeaningSynonymViewSet, base_name="meaning-synonym")
router.register(r'faq', FrequentlyAskedQuestionViewSet, base_name='faq')
router.register(r'announcement', AnnouncementViewSet, base_name='announcement')
router.register(r'user', UserViewSet, base_name='user')
router.register(r'contact', ContactViewSet, base_name='contact')

urlpatterns = router.urls + [
    url(r'^auth/login/', jwtviews.obtain_jwt_token),
    url(r'^auth/', include('djoser.urls.base', namespace="auth"))
]

