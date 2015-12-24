from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from main.forms import UserForm, ProfileForm
from models import Profile, Activity, Category
from rest_framework.response import Response
from serializers import ProfileSerializer, ActivitySerializer, CategorySerializer

# class ProfileViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Profile.objects.all().order_by('-date_joined')
#     serializer_class = ProfileSerializer


@api_view(['GET'])
def profile_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def profile_detail(request):
    try:
        user = request.user
        profile = Profile.objects.get(profile_user=user)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny, ])
def all_activities(request):
    try:
        activity = Activity.objects.all().order_by("-startDate")
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitySerializer(activity, many=True, read_only=True)
        return Response(serializer.data)



@api_view(['GET'])
@permission_classes([AllowAny, ])
def activitiesFromCategory(request, category):
    try:
        mcategory = Category.objects.filter(name=category).all()[0]
        activity = mcategory.activity_set.all()
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def activities(request):
    try:
        user = request.user
        profile = Profile.objects.get(profile_user=user)
        interests = profile.interests.all()
        activity =[]
        for interest in interests:
            for active in interest.activity_set.all():
                activity.append(active)
        activity.sort(key=lambda x: x.startDate, reverse=True)
    except Activity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActivitySerializer(activity[::-1], many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny,])
def categories(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@csrf_exempt
def register(request):
    data = {"operation": "error"}
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                first_name = request.POST.get('first_name')
                last_name = request.POST.get('last_name')
                email = request.POST.get('email')
                telephone = request.POST.get('phoneNumber')
                interest = request.POST.get('interest').split(",")
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name
                                                , last_name=last_name)
                interests = []
                for name in interest:
                    category = Category.objects.filter(name=name)[0]
                    interests.append(category)
                profile = Profile.objects.create(profile_user=user, phoneNumber=telephone)
                if interests and interests != [""]:
                    profile.interests.add(*interests)
                profile.save()
                data = {"operation": "done"}
                return JsonResponse(data)
            except Exception, e:
                pass

    return JsonResponse(data)
