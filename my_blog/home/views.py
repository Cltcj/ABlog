from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
# from home.models import ArticleCategory,Article
from django.http.response import HttpResponseNotFound

class IndexView(View):
    """首页广告"""

    def get(self, request):
        """提供首页广告界面"""
        return render(request, 'index.html')