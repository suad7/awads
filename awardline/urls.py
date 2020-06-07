from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'home'),
    url(r'^project/(\d+)', views.project, name = "project"),
    url(r'^add/project',views.new_project, name= 'add_project'),
    url(r'^profile',views.profile, name= 'profile'),
    url(r'^user/(?P<username>\w+)', views.user_profile, name = "user_profile" ),
    # url(r'^profile',views.profile, name= 'profile'),
    url(r'^search/', views.search, name='search'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

