from django.shortcuts import render
from django.http import HttpResponse , JsonResponse, StreamingHttpResponse
from django.http.request import QueryDict
from django.views.decorators.http import require_http_methods
from django.template import loader
from django.views.generic import View, TemplateView, ListView
from .models import TableName
import json, csv



from django.core.paginator import Page, Paginator

    # name = models.CharField(max_length=128, blank=True, null=True)
    # price = models.IntegerField(blank=True, null=True)
    # link = models.CharField(max_length=512, blank=True, null=True)
    # pic_path = models.CharField(max_length=64, blank=True, null=True)



# 这个应该没啥用
class BookListView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('success')

# 这个应该没啥用
class AddBookView(View):
    def get(self, request, *args, **kwargs):
        return  render(request, 'add_article.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get("title")
        content = request.POST.get("content")
        args = request.POST.getlist("tags")
        print(title,content,args)
        return HttpResponse("success")
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("你请求的方法不存在！")

# 这个应该没啥用
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        content = {
            'phone': "111111"
        }
        return content



# 这个应该没啥用
def add_article(request):
    articles = []
    for x in range(0, 102):
        article = Article(title='标题：%s' % x, content='内容：%s' % x)
        articles.append(article)
    # article = Article(title='标题：', content='内容：')
    # article.save()
    # articles.append(article)
    # print(article)
    # print(articles)
    Article.objects.bulk_create(articles)
    return HttpResponse("插入成功")




# 这个是关键
class ArticleListView(ListView):
    model = TableName #数据库表格名称
    template_name = 'article_list.html'
    context_object_name = 'articles'
    #这个是提交给html的变量
    # 也就是说，类视图里面是context_object_name
    # html则是articles.
    # 两者完全对应
    paginate_by = 10
    # ordering = 'create_time'



    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_page = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_page = range(1, current_page)
        else:
            left_has_more = True
            left_page = range(current_page-around_count, current_page)
        if current_page >= num_page-around_count-1:
            right_page = range(current_page+1, num_page+1)
        else:
            right_has_more = True
            right_page = range(current_page+1, current_page+3)
        return {
            'left_pages': left_page,
            'right_pages': right_page,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
        }


    def get_context_data(self,  **kwargs):
        context = super(ArticleListView, self).get_context_data(**kwargs)
        # print("*"*20)
        # print(context)
        # print("*"*20)
        paginator = context.get('paginator')
        # print(paginator.count)
        # print(paginator.num_pages)
        # print(paginator.page_range)
        page_obj = context.get('page_obj')
        # print(page_obj.has_next())
        # print(page_obj.next_page_number)
        paginator_data = self.get_pagination_data(paginator, page_obj)
        context.update(paginator_data)
        print("dir(context)=",dir(context))
        return context

    # def get_queryset(self):
    #     return Article.objects.filter(id__lte=9)

