from django.shortcuts import render, redirect

# def basket_list(request):
#     context = {}
#     return render(request, 'treasure/cart.html', context=context)

# def basket_list(request):
#     context = {}
#     return render(request, 'treasure/cart.html', context=context)

def add_to_basket(request, bookTitle):
    if request.method == "POST":
        if not request.session.get('basket'):
            request.session['basket'] = list()
        else:
            request.session['basket'] = list(request.session['basket'])

    item_exist = next((item for item in request.session['basket'] if item["bookID"] == request.POST.get('bookID') and item["bookTitle"] == bookTitle), False)

    add_data = {
        'bookID': request.POST.get('bookID'),
        'qty': request.POST.get('qty'),
        'bookTitle': bookTitle,
    }

    if not item_exist:
        request.session['basket'].append(add_data)
        request.session.modified = True
    return redirect(request.POST.get('url_from'))

def remove_from_basket(request, bookTitle):
    if request.method == "POST":
        for item in request.session['basket']:
            if item['bookTitle'] == bookTitle and item['bookID'] == request.POST.get('bookID'):
                item.clear()


        while {} in request.session['basket']:
            request.session['basket'].remove({})
        if not request.session['basket']:
            del request.session['basket']

        request.session.modified = True

    return redirect(request.POST.get('url_from'))

def delete_basket(request):
    if request.session.get('basket'):
        del request.session['basket']
    return redirect(request.POST.get('url_from'))
