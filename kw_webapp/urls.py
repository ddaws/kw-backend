from django.conf.urls import patterns, url, include
from django.contrib.auth.forms import AdminPasswordChangeForm
from kw_webapp.views import Logout, Review, Register, RecordAnswer, Dashboard, ReviewSummary, UnlockLevels, UnlockRequested, ForceSRSCheck, About, Contact, \
    Settings, AllLevels, LevelVocab, ToggleVocabLockStatus
from django.contrib.auth.decorators import login_required
from kw_webapp.forms import UserLoginForm


urlpatterns = patterns('',
    url(r'^$', login_required(Dashboard.as_view()), name="home"),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'registration/login.html', 'authentication_form': UserLoginForm}, name="login"),
    url(r'^register/$', Register.as_view(), name="register"),
    url(r'^logout/$', login_required(Logout.as_view()), name="logout"),
    url(r'^review/$', login_required(Review.as_view()), name="review"),
    url(r'^summary/$', login_required(ReviewSummary.as_view()), name="summary"),
    url(r'^record_answer/$', login_required(RecordAnswer.as_view()), name="record_answer"),
    url(r'^unlocks/$', login_required(UnlockLevels.as_view()), name="unlocks"),
    url(r'^levelunlock/$', login_required(UnlockRequested.as_view()), name="do_unlock"),
    url(r'^force_srs/$', login_required(ForceSRSCheck.as_view()), name="force_srs"),
    url(r'^about/$', login_required(About.as_view()), name='about'),
    url(r'^contact/$', login_required(Contact.as_view()), name='contact'),
    url(r'^vocabulary/$', login_required(AllLevels.as_view()), name='vocab'),
    url(r'^vocabulary/(?P<level>\d{1,2})/$', login_required(LevelVocab.as_view()), name='vocab_level'),
    url(r'^togglevocab/$', login_required(ToggleVocabLockStatus.as_view()), name='toggle_vocab_lock'),
    url(r'^settings/$', login_required(Settings.as_view()), name='settings'),
)

