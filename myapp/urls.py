from django.urls import path
from .views import *

urlpatterns = [
    path("", myfunction),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('aboutus/', aboutus, name='aboutus'),
    path('contactus/', contactus, name='contactus'),
    path('employee/', employee, name='employee'),
    path('student/', student, name='student'),
    path('adminhome/', adminhome, name='adminhome'),
    path('register_view/', register_view, name='register_view'),
    path('login_view/', login_view, name='login_view'),
    path('viewstudent/', viewstudent, name='viewstudent'),
    path('viewemployee', viewemployee, name='viewemployee'),
    path('employeeprofile', employeeprofile, name='employeeprofile'),
    path('studentprofile', studentprofile, name='studentprofile'),
    path('postmarks/', postmarks, name='postmarks'),
    path('studentresults', studentresults, name='studentresults'),
    path('profile', profile, name='profile'),
    path('viewresult',viewresult,name='viewresult'),
    path('results', results, name='results'),
    path('feepayments', feepayments, name='feepayments'),
    path('logout', logout, name='logout'),
    path('student/<str:username>/', student_profile, name='student_profile'),
    path('student/<str:username>/fee_payments/', student_fee_payments, name='student_fee_payments'),
    path('view_employee/', view_employee, name='view_employee'),
    path('std_profile/', std_profile, name='std_profile'),
    path('save_student/', save_student, name='save_student'),
    path('getresult/', getresult, name='getresult'),
    path('checkmarks/',checkmarks,name='checkmarks'),
    path('checkstudent/',checkstudent,name="checkstudent"),
    path('checkpayments/',checkpayments,name="checkpayments"),
    path('courses/',courses, name="courses"),
    path("addcourse",addcourse,name="addcourse" ),
    path("insertcourse",insertcourse, name="insertcourse"),
    path("ticket",ticket, name="ticket"),
    path("viewticket",viewticket, name="viewticket"),
    path('send_email/', send_email, name='send_email'),
    path('student__profile/', student__profile, name='student__profile'),
]