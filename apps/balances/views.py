from django.shortcuts import redirect, render
from ..login_reg.models import User
from ..user_dash.models import Home
from .models import Transaction


# Create your views here.
def index(request):
    this_user = User.objects.get(id=request.session['uid'])
    context = {
        "user": this_user,
        "home_members": this_user.home.members.all().exclude(id=this_user.id),
    }
    return render(request, 'balances/index.html', context)

def post(request):
    if request.method == "GET":
        return redirect('/balances/')

    this_user = User.objects.get(id=request.session['uid'])

    user_ids = request.POST.getlist('splits')
    amount = float(request.POST['amount']) / float(len(user_ids) + 1)


    for user_id in user_ids:
        Transaction.objects.create(payor=this_user, payee=User.objects.get(id=user_id),\
            amount=amount, store=request.POST['store'], description=request.POST['notes'])

    return redirect('/balances/')

def get_transactions(request, user_id):
    this_user = User.objects.get(id=request.session['uid'])
    owed = 0

    transactions = Transaction.objects.all().filter(payee__id=request.session['uid']).filter(payor__id=user_id) |\
        Transaction.objects.all().filter(payor__id=request.session['uid']).filter(payee__id=user_id)    

    for transaction in transactions:
        if transaction.payee == this_user:
            owed -= transaction.amount
        else:
            owed += transaction.amount

    context = {
        "this_user": this_user,
        "other_user": User.objects.get(id=user_id),
        "transactions": transactions,
        "owed": owed,
    }
    return render(request, 'balances/table-partial.html', context)

def all_paid(request, user_id):
    transactions = Transaction.objects.all().filter(payee__id=request.session['uid']).filter(payor__id=user_id) |\
        Transaction.objects.all().filter(payor__id=request.session['uid']).filter(payee__id=user_id)    

    for transaction in transactions:
        transaction.delete()
    
    return redirect('/balances/')

def remove_txn(request, txn_id):
    this_txn = Transaction.objects.get(id=txn_id)
    if request.session['uid'] == this_txn.payor.id or request.session['uid'] == this_txn.payee.id:
        this_txn.delete()

    return redirect('/balances/')
