from rest_framework import serializers
from career.models import JobCategory, Job, City

__author__ = 'beam'


class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City


class JobSerializer(serializers.ModelSerializer):
    city = serializers.RelatedField()
    category = JobCategorySerializer()

    class Meta:
        model = Job
        exclude = (
            'creation_date', 'employer', 'status', 'user', 'mailer',
        )
