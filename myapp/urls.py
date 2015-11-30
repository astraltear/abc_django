from django.conf.urls import include, url, patterns


'''
urlpatterns = [
    url(r'^$', 'myapp.views.myapp1'),
    url(r'^hello/$', 'myapp.views.hello'),
    url(r'^hello_template/$', 'myapp.views.hello_template'),
]
'''

urlpatterns = patterns('myapp.views',
                       url(r'^$', 'myapp1'),
                       url(r'^art/$', 'myapp2'),
                       url(r'^hello/$', 'hello'),
                       url(r'^hello_template/$', 'hello'),
                       )