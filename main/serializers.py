from rest_framework import serializers
from models import Profile, Category, Badge, Activity, Agent


class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ('name', 'icon')


class CategorySerializer(serializers.ModelSerializer):
    badge = BadgeSerializer()

    class Meta:
        model = Category
        fields = ('name', 'badge')


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='profile_user.username', read_only=True)
    email = serializers.CharField(source='profile_user.email', read_only=True)
    first_name = serializers.CharField(source='profile_user.first_name', read_only=True)
    last_name = serializers.CharField(source='profile_user.last_name', read_only=True)
    badges = BadgeSerializer(many=True)
    interests = CategorySerializer(many=True)

    class Meta:
        model = Profile
        fields = ('interests', 'username', 'phoneNumber', 'picture', 'email', 'first_name', 'last_name', 'badges')


class AgentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='profile.first_name', read_only=True)
    last_name = serializers.CharField(source='profile.last_name', read_only=True)

    class Meta:
        model = Agent
        fields = ('phoneNumber', 'website', 'first_name', 'last_name')


class ActivitySerializer(serializers.ModelSerializer):
    agent = AgentSerializer()
    category = CategorySerializer()
    class Meta:
        model = Activity
        fields = ('name', 'description', 'location', "userCount", 'startDate', 'endDate', 'price', 'isActivity', 'agent', 'category', 'image')

