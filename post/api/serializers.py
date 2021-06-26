from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.http import request
from rest_framework import serializers
from post.models import Post, Images

from datetime import datetime, timezone
from datetime import date
from django.utils.timesince import timesince

from rest_framework.fields import CurrentUserDefault


class PostUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('id', 'username', 'email', 'first_name')




class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'image', 'post')



class PostSerilaziers(serializers.ModelSerializer):

    images = PostImageSerializer(source='images_set', allow_null=True, many=True, required=False)
    
    time_since_pub = serializers.SerializerMethodField()
    post_user = PostUserSerializer(read_only=True)


    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'posting_date', 'updatind_date', 'active']

 
    

    
    def get_time_since_pub(self, obj):
        now = datetime.now(timezone.utc)
        pub_date = obj.posting_date
        
        time_delta = timesince(pub_date, now)
        return time_delta
      

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        # 
        post = Post.objects.create(cat=validated_data.get('cat', 'no-cat'), title=validated_data.get('title', 'no-title'), city=validated_data.get('city', 'no-city'), price=validated_data.get('price', 'no-price'), text=validated_data.get('text', 'no-text'), post_user_id=1)
        for image_data in images_data.getlist('image'):
            Images.objects.create(post=post, image=image_data)
        return post


    def clear_existing_images(self, instance):
        for post_images in instance.images_set.all():
            post_images.image.delete()
            post_images.delete()
            

    def update(self, instance, validated_data):
        # instance.updatedAt = datetime.datetime.now()
        images = self.context.get('view').request.FILES
        print(images)
        if images:
            self.clear_existing_images(instance)  # uncomment this if you want to clear existing images.
            post_image_model_instance = [Images(post=instance, image=image) for image in images.getlist('image')]
            Images.objects.bulk_create(
                post_image_model_instance
            )
        # instance.save()
        return super().update(instance, validated_data)
    







    def validate_posting_date(self, tarihdegeri):
        today = date.today()
        if tarihdegeri > today:
            raise serializers.ValidationError('Yükləmə tarixi düzgün deyil')
        return tarihdegeri

    
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Başlıq çox kiçikdir. Ən az 5 hərf istifadə edilməlidir')

        elif len(value) > 20:
            raise serializers.ValidationError('Başlıq çox uzundur. Ən çox 20 hərf olmalıdır.')

        return value

    