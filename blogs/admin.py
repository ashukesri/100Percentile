# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
#
from blogs.models import *
# from hunderedPercentile.models import *
#
admin.site.register(BlogPost)
admin.site.register(BlogImage)
admin.site.register(BlogPostDiscussion)