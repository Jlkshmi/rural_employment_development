from django.urls import path

from management_app import views, adminviews, peopleviews, panchayathviews

urlpatterns = [
    # path('',views.intro,name='intro'),
    path('',views.landing_page,name='landing_page'),
    path('dash',views.dash,name='dash'),

    path('people_reg_page',views.people_reg_page,name='people_reg_page'),
    path('panchayat_reg_page',views.panchayat_reg_page,name='panchayat_reg_page'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_1,name='logout'),


#admin

    path('admin_view',adminviews.admin,name='admin_view'),
    path('user_list_view',adminviews.user_view,name='user_list_view'),
    path('panchayat_list_view',adminviews.panchayat_view,name='panchayat_list_view'),
    path('scheme_list_view',adminviews.scheme_view,name='scheme_list_view'),
    path('add_scheme',adminviews.add_schemes,name='add_scheme'),
    path('scheme_dlt/<int:id>/',adminviews.scheme_dlt,name='scheme_dlt'),
    path('feedback_view',adminviews.feedback_view,name='feedback_view'),
    path('feedback_reply/<int:id>/',adminviews.feedback_reply,name='feedback_reply'),
    path('job_application', adminviews.application_view, name='job_application'),
    path('status_change_1/<int:id>/', adminviews.status_change_1, name='status_change_1'),
    path('status_change_2/<int:id>/', adminviews.status_change_2, name='status_change_2'),
    path('notification',adminviews.notification,name='notification'),
    path('notification_view',adminviews.notification_view,name='notification_view'),
    path('noti_dlt/<int:id>/',adminviews.noti_dlt,name='noti_dlt'),
    path('apply_accept_view',adminviews.apply_accept_view,name='apply_accept_view'),


# people

    path('people',peopleviews.people,name='people'),
    path('user_profile',peopleviews.user_profile,name='user_profile'),
    path('user_delete/<int:id>/',peopleviews.user_delete,name='user_delete'),
    path('user_update/<int:id>/',peopleviews.user_update,name='user_update'),
    path('job_list_view',peopleviews.job_list_view,name='job_list_view'),
    path('apply_job/<int:id>/',peopleviews.job_apply,name='apply_job'),
    path('add_feedback',peopleviews.add_feedback,name='add_feedback'),
    path('reply_view',peopleviews.reply_view,name='reply_view'),
    path('application_reply',peopleviews.application_reply,name='application_reply'),
    path('noti_view',peopleviews.noti_view,name='noti_view'),

# panchayat
    path('panchayat',panchayathviews.panchayath,name='panchayat'),
    path('panchayat_profile',panchayathviews.panchayat_profile,name='panchayat_profile'),
    path('panchayat_update/<int:id>/',panchayathviews.panchayat_update,name='panchayat_update'),
    path('job_allotment',panchayathviews.job_allotment,name='job_allotment'),
    path('job_allotment_list',panchayathviews.job_allotment_list,name='job_allotment_list'),
    path('application_accept_view',panchayathviews.application_accept_view,name='application_accept_view'),
    path('work/<int:id>/',panchayathviews.work_asign,name='work'),
    path('work_view',panchayathviews.work_view,name='work_view'),
    path('work_update/<int:id>/',panchayathviews.work_update,name='work_update'),
    path('payment/<int:id>/',panchayathviews.payment,name='payment')

]