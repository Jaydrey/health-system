from random import randrange
from rest_framework import serializers

from customuser.models import CustomUser
from .models import LabReagent, LabTestResult, LabTestRequest, LabTestCategory, LabTestProfile, LabEquipment, EquipmentTestRequest, PublicLabTestRequest

class LabReagentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabReagent
        fields = '__all__'

class LabTestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestProfile
        fields = '__all__'

class PublicLabTestRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicLabTestRequest
        fields = '__all__'

class LabEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabEquipment
        fields = '__all__'

class LabTestProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestProfile
        fields = '__all__'        

class LabTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestResult
        fields = '__all__'

class EquipmentTestRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentTestRequest
        fields = '__all__'

class LabTestRequestSerializer(serializers.ModelSerializer):
    patient_first_name = serializers.ReadOnlyField(source='patient_ID.first_name')
    patient_last_name = serializers.ReadOnlyField(source='patient_ID.second_name')
    class Meta:
        model = LabTestRequest
        fields = "__all__"
        read_only_fields = ("id", "sample_id")


    def sample_code():
        sp_id = ""
        while True:
            random_number = [randrange(0,10000) for _ in range(4) ]
            sp_id = f"SP-{random_number}"
            lab_req = LabTestRequest.objects.filter(sample_id=sp_id)
            if not lab_req.exists():
                break

        return sp_id
    
    
    def create(self, validated_data: dict):
        sp_id = ""
        while True:
            random_number = "".join([str(randrange(0,9)) for _ in range(4) ])
            sp_id = f"SP-{random_number}"
            lab_req = LabTestRequest.objects.filter(sample_id=sp_id)
            if not lab_req.exists():
                break

        validated_data["sample_id"] = sp_id
        return super().create(validated_data)


    def to_representation(self, instance: LabTestRequest):

        data = super().to_representation(instance)
        if instance.requested_by:
            try:
                user: CustomUser = CustomUser.objects.get(id=data.get("requested_by"))
                data["requested_name"] = user.get_fullname()
            except Exception as e:
                pass

        return data


class LabTestCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LabTestCategory
        fields = '__all__'
