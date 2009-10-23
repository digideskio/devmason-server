from django.conf.urls.defaults import *
from .utils import Resource
from . import handlers

urlpatterns = patterns('',
    url(r'^$',
        Resource(handlers.ProjectListHandler),
        name = 'project_list'
    ),
    url(r'^(?P<slug>[\w-]+)$',
        Resource(handlers.ProjectHandler),
        name = 'project_detail'
    ),
    url(r'^(?P<slug>[\w-]+)/builds$',
        Resource(handlers.ProjectBuildListHandler),
        name = 'project_build_list'
    ),
    url(r'^(?P<slug>[\w-]+)/builds/(?P<build_id>\d+)$',
        Resource(handlers.BuildHandler),
        name = 'build_detail'
    ),
    url(r'^(?P<slug>[\w-]+)/builds/latest$',
        Resource(handlers.LatestBuildHandler),
        name = 'latest_build'
    ),
    url(r'^(?P<slug>[\w-]+)/tags$',
        Resource(handlers.ProjectTagListHandler),
        name = 'project_tag_list'
    ),
    url(r'^(?P<slug>[\w-]+)/tags/(?P<tags>[^/]+)/latest$',
        Resource(handlers.ProjectLatestTaggedBuildHandler),
        name = 'latest_tagged_build'
    ),
    url(r'^(?P<slug>[\w-]+)/tags/(?P<tags>.*)$',
        Resource(handlers.TagHandler),
        name = 'tag_detail'
    ),
)