from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from .models import Student, FeePayment,Ticket


# Create your views here.
def myfunction(request):
    return render(request, "index.html")


def aboutus(request):
    return render(request, 'aboutus.html')

from django.shortcuts import render

def courses(request):
    # Your view logic here
    return render(request, 'courses.html')



def contactus(request):
    return render(request, 'contactus.html')


def login(request):
    return render(request, 'login.html')


def viewstudent(request):
    return render(request, 'viewstudent.html')


def viewemployee(request):
    return render(request, 'viewemployee.html')


from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Register.objects.filter(Q(username=username, password=password)).values()

        if username == 'admin' and password == 'admin':
            return render(request, 'adminhome.html',)  # Assuming the URL name for the admin page is 'admin_page'
        elif len(username) == 4 and user:
            userid = username;
            return render(request, 'employee.html',{'userid':userid})  # Assuming the URL name for the user page is 'user_page'
        elif user:
            request.session["sid"] = username
            sid = username
            return render(request, 'student.html',{'sid':sid})  # Assuming the URL name for the user page is 'user_page'
        return render(request, 'login.html', {'error_message': 'Invalid username or password.'})

    # If request method is not POST, render login page
    return render(request, 'login.html')


class Employee:
    pass


def view_employee(request):
    employee = None
    if request.method == 'GET':
        employee_id = request.GET.get('employee_id')
        if employee_id:
            try:
                employee = Employee.objects.get(id=employee_id)
            except Employee.DoesNotExist:
                pass
    return render(request, 'employees/view_employee.html', {'employee': employee})


def employee(request):
    # Add any logic needed for the employee page here
    return render(request, 'employee.html')


def adminhome(request):
    # Add any logic needed for the employee page here
    return render(request, 'adminhome.html')


def student(request):
    # Add any logic needed for the employee page here
    return render(request, 'student.html')


def register(request):
    # Add any logic needed for the employee page here
    return render(request, 'registration.html')


def employeeprofile(request):
    # Add any logic needed for the employee page here
    return render(request, 'employeeprofile.html')


def studentprofile(request):
    students = StudentProfile.objects.all()
    print(students)  # Add this line for debugging
    return render(request, 'studentprofile.html', {'students': students})


def studentresults(request):
    # Add any logic needed for the employee page here
    return render(request, 'studentresults.html')


def postmarks(request):
    # Add any logic needed for the employee page here
    courses = Course.objects.all()

    return render(request, 'postmarks.html',{'courses': courses})


from django.shortcuts import render, redirect
from .models import Mark  # Import your Marks model
from django.contrib import messages


def profile(request):
    id = request.session["sid"]
    users = StudentProfile.objects.filter(studentId=id).values()
    #print(user)
    # Add any logic needed for the employee page here
    return render(request, 'profile.html', {"users": users})
def employee(request):
    id = request.session["sid"]
    users = EmployeeProfile.objects.filter(employeeId=id).values()
    return render(request, 'employeeprofile',{"users": users})

def feepayments(request):
    # Add any logic needed for the employee page here
    id=request.session["sid"]
    payment =FeePayment.objects.filter(studentId=id)
    return render(request, 'feepayments.html',{"payment":payment})


def results(request):
    # Add any logic needed for the employee page here
    return render(request, 'results.html')


def logout(request):
    return render(request, 'base.html')


def student_profile(request, username):
    student = get_object_or_404(Student, username=username)
    return render(request, 'student_profile.html', {'student': student})


def student_fee_payments(request, username):
    student = get_object_or_404(Student, username=username)
    fee_payments = FeePayment.objects.filter(student=student)
    return render(request, 'student_fee_payments.html', {'fee_payments': fee_payments})


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        city = request.POST['city']

        allowed_domains = ['@gmail.com', '@yahoo.com', '.in']
        if not any(domain in email for domain in allowed_domains):
            message = 'Invalid email domain. Allowed domains: @gmail.com, @yahoo.com, .in'
            return render(request, 'registration.html',{'message':message})

        # print(username, email, password, confirm_password)
        user = Register(username=username, email=email, password=password, city=city)
        user.save()
        messages.info(request, 'Account created Successfully!')
        return render(request, 'login.html')


from .models import Student


def std_profile(request):
    students = StudentProfile.objects.all()
    print(students)  # Add this line for debugging
    return render(request, 'studentprofile.html', {'students': students})

def emp_profile(request):
    employee = None
    saved = False
    if request.method == 'GET':
        employee_id = request.GET.get('employee_id')
        if employee_id:
            try:
                employee = EmployeeProfile.objects.get(id=employee_id)
            except EmployeeProfile.DoesNotExist:
                pass
    return render(request, 'employeeprofile.html', {'employee': employee, 'saved': saved})

def save_student(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        if student_id:
            try:
                student = Student.objects.get(id=student_id)
                # Update student details or perform any necessary actions here
                # For example, you could set a 'saved' flag on the student object
                student.saved = True
                student.save()
            except Student.DoesNotExist:
                pass
    return redirect('studentprofile.html')


def checkmarks(request):
    if request.method == "POST":
        id = request.POST.get("studentId")
        cn1 = request.POST.get("courseName1")
        cr1 = request.POST.get("credits1")
        gp1 = request.POST.get("gradePoints1")
        grade = request.POST.get("grade1")
        fid = request.POST.get("FacultyId")
        fname = request.POST.get("FacultyName")
        print(id, gp1, cn1, cr1, gp1, grade,fid,fname)

        # Create and save instances of the Course model
        mark = Mark(studentId=id, course_name=cn1, credits=cr1, grade_points=gp1, grade=grade,Correctedbyfacultyid = fid ,CorrectedbyfacultyName=fname)
        mark.save()
        messages.info(request, "Marks Posted Successfully")
        # Redirect or render a response
        return redirect('postmarks')
    else:
        # Handle GET requests
        return render(request, 'postmarks.html')


def getresult(request):
    result = Mark.objects.all()
    return render(request, "getresult.html", {"result": result})


def viewresult(request):
    student_id = request.session["sid"]  # Assuming you pass studentId as a query parameter
    result = Mark.objects.filter(studentId=student_id)
    return render(request, 'getresult.html', {'result': result})


def checkstudent(request):
    if request.method == "POST":
        studentId = request.POST["studentId"]
        fullName = request.POST["fullName"]
        branch = request.POST["branch"]
        yearOfStudy = request.POST["yearOfStudy"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        address = request.POST["address"]
        print(studentId, fullName, branch, yearOfStudy, email, contact, address)
        student = StudentProfile(studentId=studentId,
                                 full_name=fullName,
                                 branch=branch,
                                 year_of_study=yearOfStudy,
                                 email=email,
                                 contact=contact,
                                 address=address
                                 )
        if student:
            messages.info(request, "Profile update SucessFully")
            student.save()
            return redirect('profile')
        else:
            messages.info(request, "Profile  not updated")
            return redirect('profile')


def checkpayments(request):
    if request.method == "POST":
        studentId = request.session["sid"]
        payment_type = request.POST["payment_type"]
        amount = request.POST["amount"]
        print(payment_type, amount)
        student = FeePayment(studentId=studentId, payment_type=payment_type, amount=amount)

        if student:
            messages.info(request, "Payment sucessfully")
            student.save()
            return redirect('feepayments')
        else:

            messages.info(request, "Payment unsucessfull")
            return redirect('feepayments')

def addcourse(request):
    return render(request,"addcourse.html")

def insertcourse(request):
  if request.method=="POST":
    dept=request.POST["dept"]
    year = request.POST["year"]
    Ayear = request.POST["Ayear"]
    semester = request.POST["semester"]
    ccode = request.POST["ccode"]
    ctitle = request.POST["ctitle"]

    course=Course(department=dept,academicyear=Ayear,semester=semester,Year=year,coursecode=ccode,coursetitle=ctitle)

    Course.save(course)
    message = "Course added"
    return render(request,"addcourse.html",{"msg":message})

def ticket(request):
    if request.method == "POST" :
        ticket = request.POST.get("ticket")
        studentid = request.POST.get("studentid")

        tickets= Ticket(ticket=ticket,studentid=studentid)
        tickets.save()
    return render(request,"ticket.html")

def viewticket(request):
    tickets = Ticket.objects.all()
    return render(request,"viewticket.html",{"tickets":tickets})

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

def send_email(request):
    if request.method == 'POST':
        # Get data from the form
        id = request.POST.get('id')
        text = request.POST.get('text')

        # Construct your email message
        subject = f"Email from {id}"
        message = f"Sir, I am {id}.\n{text}"

        # Send the email
        send_mail(subject, message, 'feedbackpfsd@gmail.com', ['hemanthhlr.7979@gmail.com'])

        # Optionally, you can redirect to a success page
        return HttpResponse('Email sent successfully!')
    else:
        return render(request, "mail.html")


def student__profile(request):
    return render(request,"adminstudentview.html")


