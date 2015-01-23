from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^hello/', 'article.views.hello'),
    #url(r'^hello_template/', 'article.views.hello_template'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^articles/', include('article.urls')),
)
