from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.db.models import Q

# import datetime
from datetime import datetime, date, timedelta
from .forms import *
# from datetime import date, timedelta
# Create your views here.
def search(request):
    query=request.POST.get('search','')
    if query:
        queryset = (Q(title__icontains=query)) | (Q(details__icontains=query)) | (Q(category__icontains=query))
        results = Post.objects.filter(queryset).distinct()
    else:
        results = []
    context = {
        'results':results
    }
    return render(request, 'post_manage/search.html', context)

def filter(request):
    post=Post.objects.all()
    dateform = TimeRangeForm()
    if request.method == 'POST':
        age_from=request.POST['age_from']
        age_to=request.POST['age_to']
        dateform = TimeRangeForm(data=request.POST)
        student= True if request.POST.get('student') else False

        results = []
        count=0

        # if dateform.is_valid():
        #     start_date = dateform.cleaned_data.get('start_date')
        #     end_date = dateform.cleaned_data.get('end_date')

        # print(start_date, end_date)
        # date_filter_queryset = Post.objects.filter(created_at__range=[start_date, end_date+timedelta(days=1)])

        # date_filter_queryset = Post.objects.filter(created_at__range=[start_date, end_date])
        # student=request.POST['student']
        # results_get = Post.objects.all()
        # print(results_get__age)
        # sub = Post.objects.all()
        # post = sub.age.all()
        # print(sub.age)
        # results = Post.objects.filter(queryset).distinct()
        # print(results)
        # if age_from:
        #     queryset = Post.objects.filter(age__gte=age_from)
        #     if age_to:
        #         queryset = queryset.filter(age__lte=age_to)

        # startdate = datetime.now()
        # enddate = startdate + timedelta(days=6)

        # difference_date=startdate-enddate
        # d = datetime.timedelta(difference_date).strftime("%A, %B %e, %Y")
        # print(type(difference_date))
        # print(datetime(year=0, month=0, day=6))

        # date_range= Post.objects.filter(created_at__range=[startdate, enddate])
        # date_range= Post.objects.filter(created_at__range=[startdate, enddate])
        # print(startdate-enddate)

        query=request.POST.get('search','')
        # results = []
        # print(query.lower())
        if (len(query) > 0):
            queryset = (Q(title__icontains=query)) | (Q(details__icontains=query))
            results = Post.objects.filter(queryset).distinct()

            # blogs = Post.objects.filter(title=title).values_list('id', flat=False)
            ls_title = list(Post.objects.values_list('title', flat=True))
            ls_details = list(Post.objects.values_list('details', flat=True))
            count_title=0
            for i in ls_title:
                for j in i.split():
                    if query.lower()==j.lower():
                        count_title = count_title+1

            count_details=0
            for i in ls_details:
                for j in i.split():
                    if query.lower()==j.lower():
                        count_details = count_details+1

            # print(count_title+count_details)
            count = count_title+count_details
            # for i in ls_details:
            #     print(i)
            # keyword_ls = []
            # for keyword in query.split(' '):
            #     keyword_ls += list(Post.objects.filter(title__icontains=query))
            #     keyword_ls += list(Post.objects.filter(details__icontains=query))
            # print(len(keyword_ls))
            if student:
                results=results.filter(student=True)
            if age_from:
                results = results.filter(age__gte=age_from)
            if age_to:
                results = results.filter(age__lte=age_to)

            # if dateform.exist():
            #     print("True")
            if dateform.is_valid():
                start_date = dateform.cleaned_data.get('start_date')
                end_date = dateform.cleaned_data.get('end_date')
                if start_date and end_date:
                    results = results.filter(created_at__range=[start_date, end_date + timedelta(days=1)])
            # end_date = dateform.cleaned_data.get('end_date')
            # print(type(dateform))

            # if dateform.is_valid():
            #     start_date = dateform.cleaned_data.get('start_date')
            #     end_date = dateform.cleaned_data.get('end_date')
            #
            #     results = results.filter(created_at__range=[start_date, end_date + timedelta(days=1)])



        elif student:
            queryset = Post.objects.filter(student=True)
            results = queryset

            if dateform.is_valid():
                start_date = dateform.cleaned_data.get('start_date')
                end_date = dateform.cleaned_data.get('end_date')
                if start_date and end_date:
                    results = results.filter(created_at__range=[start_date, end_date + timedelta(days=1)])

            # if dateform.is_valid():
            #     start_date = dateform.cleaned_data.get('start_date')
            #     end_date = dateform.cleaned_data.get('end_date')
            #
            #     results = results.filter(created_at__range=[start_date, end_date+timedelta(days=1)])

        elif age_from:
            queryset = Post.objects.filter(age__gte=age_from)
            if age_to:
                queryset = queryset.filter(age__lte=age_to)
                if dateform.is_valid():
                    start_date = dateform.cleaned_data.get('start_date')
                    end_date = dateform.cleaned_data.get('end_date')
                    if start_date and end_date:
                        queryset = queryset.filter(created_at__range=[start_date, end_date + timedelta(days=1)])

            results = queryset

        elif dateform.is_valid():
            start_date = dateform.cleaned_data.get('start_date')
            end_date = dateform.cleaned_data.get('end_date')
            if start_date and end_date:
                queryset = Post.objects.filter(created_at__range=[start_date, end_date+timedelta(days=1)])
                results = queryset

    context = {
        'results':results,
        'count': count,
        'dateform':dateform,
    }

        # elif age_to:
        #     results=results_get.filter(age__lte=age_to)
        # if subject or class_in:
        #     queryset=(Q(subject__name__icontains=subject)) & (Q(class_in__name__icontains=class_in))
        #     results = Post.objects.filter(queryset).distinct()
        #     if available:
        #         results=results.filter(available=True)
        #     if salary_from:
        #         results=results.filter(salary__gte=salary_from)
        #     if salary_to:
        #         results=results.filter(salary__lte=salary_to)
        # else:
        #     queryset = []
        # context={
        #     'results':queryset
        # }
        # context={
        #     'results_get':results_get
        # }
    return render(request, 'post_manage/search.html', context)


def post_list(request):
    return render(request, 'post_manage/post_list.html')

class PostListView(ListView):
    template_name='post_manage/post_list.html'
    queryset=Post.objects.all()
    model=Post
    context_object_name='posts'
    dateform = TimeRangeForm()
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = context.get('object_list')
        context['dateform'] = self.dateform
        return context

# def postlist(request):
#     post = Post.objects.all()

class PostDetailView(DetailView):
    model=Post
    template_name='post_manage/post_detail.html'
