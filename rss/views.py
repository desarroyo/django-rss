from django.contrib.auth.models import User, Group
from .models import Rss
from rest_framework import viewsets
from rss.serializers import UserSerializer, GroupSerializer, RssSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.db.models import F
import json
import copy

import feedparser
from bs4 import BeautifulSoup
import dateutil.parser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET'])
def rss_list(request):
    """
    List rss
    """
    if request.method == 'GET':
        rss = Rss.objects.all()
        serializer = RssSerializer(rss, many=True)
        return Response(serializer.data)    

@api_view(['GET'])
def rss_list_categoria(request, categoria):
    """
    List rss
    """
    try:
        rss = Rss.objects.filter(categoria=categoria)
    except Rss.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RssSerializer(rss, many=True)
        NewsFeed = feedparser.parse(serializer.data[0]['url'])
        ni=dict()

        for noticia in NewsFeed.entries:
        	if ('tags' in noticia) and noticia.tags[0] and (noticia.tags[0].term not in ni) :
        		ni[noticia.tags[0].term] = [];

	        n = dict()

	        n["title"] = str(BeautifulSoup(noticia.title)).replace("\xa0"," ")
	        n["summary"] = str(BeautifulSoup(noticia.summary)).replace("\xa0"," ")
	        n["published"] = str(dateutil.parser.parse(noticia.published))
	        n["author"] = noticia.author
	        n["media_content"] = noticia.media_content[0]["url"] if ('media_content' in noticia) else ''
	        n["link"] = noticia.link

       		ni[noticia.tags[0].term].append(n)


        #print(serializer.data[0]['url'])

        return Response(ni)

@api_view(['GET'])
def rss_list_fuente(request, fuente):
    """
    List rss
    """
    try:
        rss = Rss.objects.filter(fuente=fuente)
    except Rss.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RssSerializer(rss, many=True)
        return Response(serializer.data)        


@api_view(['GET'])
def rss_detail(request, pk):
    """
    Retrieve rss.
    """
    try:
        rss = Rss.objects.get(pk=pk)
    except Rss.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RssSerializer(rss)
        return Response(serializer.data)        

class RssViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    serializer_class = RssSerializer

    def list(self, request,):
        queryset = Rss.objects.filter()
        serializer = RssSerializer(queryset, many=True)
        return HttpResponse(json.dumps(serializer.data), content_type="application/json")#HttResponse(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Rss.objects.filter()
        rss = get_object_or_404(queryset, pk=pk)
        serializer = RssSerializer(rss)
        return HttpResponse(serializer.data, content_type="application/json")#HttResponse(serializer.data)

class RssInformadorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Rss.objects.all()[:1]
    serializer_class = RssSerializer    