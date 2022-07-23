from rest_framework import serializers
from model_name.models import classroom

# class MyProductSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = MyProduct
#         fields = ('id',
#                   'name',
#                   'product_code',
#                   'visibility',
#                   'currency_type',
#                   'price',
#                   'requester_ip',
#                   'created_date')


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = classroom
        fields = ('room_no', 'status', 'course_id', 'capacity', 'projector',
                  'ac', 'computer', 'desks', 'whiteboard', 'count', 'type')

