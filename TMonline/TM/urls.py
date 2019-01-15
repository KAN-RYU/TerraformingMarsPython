from django.urls import path, re_path
from TM.views import TmList, TmDetail, TmGrid

app_name = 'TM'

urlpatterns = [
        path('', TmList.as_view(), name='index'),
        re_path(r'^(?P<pk>\d+)/$', TmDetail.as_view(), name='detail'),
        path('grid/', TmGrid.as_view(), name='grid'),
]
