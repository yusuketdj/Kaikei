from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from .forms import CustomerCreateForm, CustomerUpdateForm, ChoiceCreateForm, CustomerSearchForm
from . import forms
from .models import Customer, Choice

# Create your views here.
def index(request):
    return render(request, 'kaikei/index.html')

"""
class Text(LoginRequiredMixin, generic.TemplateView):
    template_name = 'kaikei/test.html'
"""

@login_required
def top(request):
    return render(request, 'kaikei/top.html')

"""
# def reception(request):
    return render(request, 'kaikei/reception.html')
"""

class CustomerList(generic.ListView):
    model = Customer

    def get_queryset(self):
        queryset = super().get_queryset()
        form = CustomerSearchForm(self.request.GET or None)
        if form.is_valid():
            customer_id = form.cleaned_data.get('customer_id')
            if customer_id:
                queryset = queryset.filter(Q(customer_id__icontains=customer_id))
        return queryset

"""
class IndexView(LoginRequiredMixin, generic.ListView):
    paginate_by = 5
    template_name = 'search/index.html'
    model = Post
    def post(self, request, *args, **kwargs):
        form_value = [
            self.request.POST.get('title', None),
            self.request.POST.get('text', None),
        ]
        request.session['form_value'] = form_value
        # 検索時にページネーションに関連したエラーを防ぐ
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()
        return self.get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        title = ''
        text = ''
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            text = form_value[1]
        default_data = {'title': title,  # タイトル
                        'text': text,  # 内容
                        }
        test_form = SearchForm(initial=default_data) # 検索フォーム
        context['test_form'] = test_form
        return context
    def get_queryset(self):
        # sessionに値がある場合、その値でクエリ発行する。
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            text = form_value[1]
            # 検索条件
            condition_title = Q()
            condition_text = Q()
            if len(title) != 0 and title[0]:
                condition_title = Q(title__icontains=title)
            if len(text) != 0 and text[0]:
                condition_text = Q(text__contains=text)
            return Post.objects.select_related().filter(condition_title & condition_text)
        else:
            # 何も返さない
            return Post.objects.none()
"""

"""
class WaitingCustomerList(generic.ListView):
    queryset = Customer.objects.filter(is_waiting=True)
"""

def waitingcustomer_list(request):
    context = {
        'waitingcustomer_list': Customer.objects.filter(is_waiting=True),
    }
    return render(request, 'kaikei/waitingcustomer_list.html', context)

class CustomerDetail(generic.DetailView):
    model = Customer

class CustomerUpdate(generic.UpdateView):
    model = Customer
    form_class = CustomerUpdateForm
    success_url = reverse_lazy('kaikei:top')

#def login(request):
    #return render(request, 'kaikei/login.html')

"""
#def choice_create(request):
    form = ChoiceCreateForm(request.POST or None)
    customer = Choice.objects.filter(customer__is_waiting=True)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('kaikei:accounts')
    
    context = {
        'form': form
    }
    return render(request, 'kaikei/choice_form.html', context)
"""

class ChoiceCreate(generic.CreateView):
    model = Choice
    # customer = Choice.objects.filter(customer__is_waiting=True)
    form_class = ChoiceCreateForm
    success_url = reverse_lazy('kaikei:accounts')

    # def get_queryset(self):
    #    return Choice.objects.filter(customer__is_waiting=True)

def accounts(request):
    choice = Choice.objects.last()
    context = {
        'choice': choice
    }
    #return render(request, 'kaikei/login/accounts.html', context)
    return render(request, 'kaikei/accounts.html', context)

class CustomerCreate(generic.CreateView):
    model = Customer
    form_class = CustomerCreateForm
    success_url = reverse_lazy('kaikei:top')