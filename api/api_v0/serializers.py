from rest_framework import serializers
from django.utils import timezone

import random


class FortuneSerializer(serializers.Serializer):
    birth_date = serializers.DateField()
    blood_type = serializers.ChoiceField(['A', 'B', 'O', 'AB'])
    current_date = serializers.SerializerMethodField()
    fortune_range = serializers.SerializerMethodField(read_only=True)
    fortune = serializers.SerializerMethodField()
    fortune_min = 1
    fortune_max = 10

    def get_fortune_range(self, obj):
        return [self.fortune_min,  self.fortune_max]

    def get_current_date(self, obj):
        return timezone.localdate()

    def get_fortune(self, obj):
        seed = '%s%s%s' % (obj['birth_date'], obj['blood_type'], timezone.localdate())
        random.seed(seed)
        return random.choice(range(self.fortune_min, self.fortune_max + 1))
