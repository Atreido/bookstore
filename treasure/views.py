from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Books, News, Comments, Categories, Orders, User, UserDetails
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib import messages
# from django.views.generic import ListView

def get_categories():
    all= Categories.objects.all().order_by('category')
    return {'catList': all[:8], 'extendList': all[9:]}


def check_password(username, password):
    try:
        user = User.objects.get(username=username)
        return user.check_password(password)
    except User.DoesNotExist:
        return False

def index(request):
    books = Books.objects.all().order_by("title")
    context = {"basket_list": request.session.get('basket'), 'books': books}
    context.update(get_categories())
    
    return render(request, 'treasure/index.html', context=context)

def register(request):
    if request.method == 'GET':
        context = {"basket_list": request.session.get('basket'), }
        return render(request, 'treasure/register.html', {'form': context})
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['password']
        pwdr = request.POST['repeat-password']
        users = User.objects.all()
        flag = True
        for user in users:
            if name == user.username:
                flag = False
                message = "Registration is not successfull! Such username alredy exists"
                return render(request, 'treasure/register.html', {"basket_list": request.session.get('basket'), 'message': message})
            elif email == user.email:
                flag = False
                message = "Registration is not successfull! Such email is alredy registered"
                return render(request, 'treasure/register.html', {"basket_list": request.session.get('basket'), 'message': message})
            elif pwd != pwdr:
                flag = False
                message = "Registration is not successfull! Entered paswords do not match"
                return render(request, 'treasure/register.html', {"basket_list": request.session.get('basket'), 'message': message})
        if flag:
            if pwd == pwdr:
                min_length = 8
                if len(pwdr) < min_length:
                    message = f"Password does not meet the requirements - it must be at least {min_length} characters long."
                    return render(request, 'treasure/register.html',
                                  {"basket_list": request.session.get('basket'), 'message': message})

                # check for digit
                elif sum(c.isdigit() for c in pwdr) < 1:
                    message = "Password does not meet the requirements - it must contain at least 1 number."
                    return render(request, 'treasure/register.html',
                              {"basket_list": request.session.get('basket'), 'message': message})
                # check for uppercase letter
                elif not any(c.isupper() for c in pwdr):
                    message = "Password does not meet the requirements - it must contain at least 1 uppercase letter."
                    return render(request, 'treasure/register.html',
                                  {"basket_list": request.session.get('basket'), 'message': message})
                # check for lowercase letter
                elif not any(c.islower() for c in pwdr):
                    message = "Password does not meet the requirements - it must contain at least 1 lowercase letter."
                    return render(request, 'treasure/register.html',
                              {"basket_list": request.session.get('basket'), 'message': message})
                else:
                    securePass = make_password(pwdr)
                    new_comment = User(username=name, email=email, password=securePass, is_superuser=0, is_staff=0,
                                       is_active=1)
                    new_comment.save()
                    return redirect('index')



def logout_view(request):
    logout(request)
    return redirect('index')


def shop(request):
    show = request.GET.get('show')
    sorter = request.GET.get('sort')
    if sorter == 'title':
        books = Books.objects.all().order_by('title')
    elif sorter == 'titleDsc':
        books = Books.objects.all().order_by('-title')
    elif sorter == 'author':
        books = Books.objects.all().order_by('author')
    elif sorter == 'authorDsc':
        books = Books.objects.all().order_by('-author')
    elif sorter == 'price':
        books = Books.objects.all().order_by('price')
    elif sorter == 'priceDsc':
        books = Books.objects.all().order_by('-price')
    else:
        books = Books.objects.all()

    if show == "12":
        paginator = Paginator(books, 12)
    elif show == "10":
        paginator = Paginator(books, 10)
    elif show == "8":
        paginator = Paginator(books, 8)
    elif show == "5":
        paginator = Paginator(books, 5)
    elif show == "3":
        paginator = Paginator(books, 3)
    else:
        paginator = Paginator(books, 12)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"basket_list": request.session.get('basket'), 'books': page_obj, 'sort': sorter}
    context.update(get_categories())
    
    return render(request, 'treasure/shop-grid.html', context)

def search(request):
    query = request.GET.get('query')
    findbooks = Books.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    paginator = Paginator(findbooks, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"basket_list": request.session.get('basket'), 'books': page_obj}
    context.update(get_categories())
    
    return render(request, 'treasure/shop-grid.html', context=context)


def contact(request):
    context = {"basket_list": request.session.get('basket') }
    context.update(get_categories())
    
    return render(request, 'treasure/contact.html', context=context)


def order_complete(request):
    context = {"basket_list": request.session.get('basket')}
    context.update(get_categories())

    return render(request, 'treasure/order_complete.html', context=context)

def bookDetails(request, id=None):
    bookdetails = get_object_or_404(Books, title=id)
    categories = Categories.objects.all()
    comments = Comments.objects.all().order_by("-publish_date")
    rate = 0
    i = 0
    irated = 0
    for comment in comments:
        if comment.posted_id == bookdetails.id:
            if int(comment.rating) != 0:
                rate += int(comment.rating)
                irated += 1
            i += 1
    avg = 0 if i < 1 else rate/irated
    avg = round(avg, 1)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['message']
        pdate = timezone.now()
        rating = request.POST['star']
        if name == "" or email == "":
            message = "Please check name and email"
            context = {"basket_list": request.session.get('basket'), "details": bookdetails, "comments": comments, "categories": categories, "avgrate": avg,
                       "iter": i, "errMsg": message, "iterRated": irated}
            context.update(get_categories())
            
            return render(request, 'treasure/product-details.html', context=context)

        else:
            new_comment = Comments(name=name, email=email, comment=comment, publish_date=pdate, rating=rating, posted_id = bookdetails.id, user_id=1)
            new_comment.save()
            context = {"basket_list": request.session.get('basket'), "details":bookdetails, "comments": comments, "categories":categories, "avgrate": avg, "iter": i, "iterRated": irated}
            context.update(get_categories())
            
            return render(request, 'treasure/product-details.html', context=context)
    else:
        context = {"basket_list": request.session.get('basket'), "details": bookdetails, "comments": comments, "categories": categories, "avgrate": avg, "iter": i, "iterRated": irated}
        context.update(get_categories())
        
        return render(request, 'treasure/product-details.html', context=context)

def category(request, name=None):
    ctgry = get_object_or_404(Categories, category=name)
    books = Books.objects.filter(fk_category=ctgry)
    paginator = Paginator(books, 12)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"basket_list": request.session.get('basket'), 'books': page_obj}
    context.update(get_categories())
    
    return render(request, 'treasure/shop-grid.html', context=context)

def cart(request):
    session_data = request.session.get('basket')
    id_set = []
    qty = []
    prices = []

    if session_data != None:
        for elem in session_data:
            id_set.append(elem['bookID'])
            qty.append(elem['qty'])

    ordered = Books.objects.filter(id__in=id_set)

    for product in ordered:
        prices.append(product.price)

    subtotal = [float(qty[i]) * float(prices[i]) for i in range(len(prices))]

    objects = zip(ordered, qty, subtotal)

    total = sum(subtotal)
    context = {"basket_list": session_data, "objects":objects, "total": total}
    context.update(get_categories())
    
    return render(request, 'treasure/cart.html', context=context)

def checkout(request):
    userdata = []

    if request.user.is_authenticated:
        userdata = User.objects.get(username=request.user.username)

    session_data = request.session.get('basket')
    id_set = []
    qty = []
    prices = []

    if session_data != None:
        for elem in session_data:
            id_set.append(elem['bookID'])
            qty.append(elem['qty'])

    ordered = Books.objects.filter(id__in=id_set)

    for product in ordered:
        prices.append(product.price)

    subtotal = [float(qty[i]) * float(prices[i]) for i in range(len(prices))]
    objects = zip(ordered, qty)
    total = sum(subtotal)

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        region = request.POST['region']
        zipcode = request.POST['zipcode']
        notes = request.POST['notes']

        order = Orders.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone=phone,
            address=address,
            city=city,
            region=region,
            zip=zipcode,
            notes=notes,
        )
        for booklist in ordered:
            order.orderedBook.add(booklist.id)

        del request.session['basket']

        context = {"basket_list": request.session.get('basket'), "userdata": userdata, "objects": objects,
                   "total": total}
        context.update(get_categories())
        return redirect('order_complete')

    context = {"basket_list": request.session.get('basket'), "userdata": userdata, "objects": objects, "total": total}
    context.update(get_categories())
    
    return render(request, 'treasure/checkout.html', context=context)

def news(request):
    allnews = News.objects.all().order_by("-published_date")
    paginator = Paginator(allnews, 6)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)
    context = {"basket_list": request.session.get('basket'), 'allNews': page_obj}
    context.update(get_categories())
    
    return render(request, 'treasure/news.html', context=context)

def newsDetails(request, title=None):
    newsdetails = get_object_or_404(News, title=title)
    context = {"basket_list": request.session.get('basket'), 'newsdetails': newsdetails}
    context.update(get_categories())
    
    return render(request, 'treasure/news-details.html', context=context)

def compare(request):
    context = {"basket_list": request.session.get('basket')}
    context.update(get_categories())
    
    return render(request, 'treasure/compare.html', context=context)

def wishlist(request):
    context = {"basket_list": request.session.get('basket')}
    context.update(get_categories())
    
    return render(request, 'treasure/wishlist.html', context=context)

@login_required
def account(request):
    global selected
    users = User.objects.all()
    for find in users:
        if find.username == request.user.username:
            selected = find
            break
    checkExist = UserDetails.objects.filter(user_id=selected.id).exists()
    if request.method == 'POST':
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        email = request.POST['email']
        crntPwd = request.POST['current-pwd']
        newPwd = request.POST['new-pwd']
        cnfrmPwd = request.POST['confirm-pwd']
        chkPwd = check_password(request.user.username, crntPwd)
        User.objects.filter(username=request.user).update(email=email)

        if checkExist:
            obj = UserDetails.objects.get(user_id=selected.id)
            obj.firstname = firstname
            obj.lastname = lastname
            obj.save()
            message = "Профіль оновлено"
            context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}
        else:
            addExtra = UserDetails(user_id=selected.id, firstname=firstname, lastname=lastname)
            addExtra.save()

            context = {"basket_list": request.session.get('basket'), 'UserDetails': selected}

        if chkPwd and newPwd == cnfrmPwd:
            min_length = 8
            if len(newPwd) < min_length:
                message = "Password does not meet the requirements - it must be at least %s characters long."
                context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}
            # check for digit
            elif sum(c.isdigit() for c in newPwd) < 1:
                message = "Password does not meet the requirements - it must contain at least 1 number."
                context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}
            # check for uppercase letter
            elif not any(c.isupper() for c in newPwd):
                message = "Password does not meet the requirements - it must contain at least 1 uppercase letter."
                context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}
            # check for lowercase letter
            elif not any(c.islower() for c in newPwd):
                message = "Password does not meet the requirements - it must contain at least 1 lowercase letter."
                context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}
            else:
                newPass = make_password(newPwd)
                User.objects.filter(username=request.user).update(password=newPass)
                message = "Пароль оновлено"
                context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}
        elif chkPwd and newPwd != cnfrmPwd:
            message = "Введені паролі не співпадають"
            context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}
        elif not chkPwd and newPwd != "":
            message = "Поточний пароль введено не вірно"
            context = {"basket_list": request.session.get('basket'), 'UserDetails': selected, "message": message}

        context.update(get_categories())
        
        return render(request, 'treasure/my-account.html', context=context)




    context = {"basket_list": request.session.get('basket'), 'UserDetails': selected}
    context.update(get_categories())
    
    return render(request, 'treasure/my-account.html', context=context)



def order_complete(request):
    context = {"basket_list": request.session.get('basket'), }
    context.update(get_categories())
    
    return render(request, 'treasure/order-complete.html', context=context)

def faq(request):
    context = {"basket_list": request.session.get('basket'), }
    context.update(get_categories())
    
    return render(request, 'treasure/faq.html', context=context)
