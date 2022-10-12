from rest_framework import serializers
from categories.models import Category
from family_member.models import FamilyMember
from rest_framework.response import Response
from rest_framework import status

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    belongs_to_profile = serializers.StringRelatedField(
        source="belongs_to_profile.user.username"
    )
    category_name = serializers.CharField(source="category.name")
    category = serializers.StringRelatedField(source="category.id")

    # Inspiration from:
    # https://stackoverflow.com/questions/62847000/write-an-explicit-update-method-for-serializer
    def update(self, instance, validated_data):
        """
        Used for updating task form
        """
        task = Task.objects.get(id=instance.id)

        # If payload has no title (only containing info about status) and status id Done.
        if (
            validated_data.get("title") is None
            and validated_data.get("status") is "Done"
        ):
            # Someone needs to be assigned to task make "Done"
            if task.assigned is None:
                # TODO: Return a http status code
                print("No one is assigned")
            else:
                assigned_family_member = FamilyMember.objects.get(id=task.assigned.id)
                # If user remove task done. Assigned family member will loose star points and 1 closed task
                if task.status == "Done":
                    task.status = "Todo"
                    assigned_family_member.closed_tasks = (
                        assigned_family_member.closed_tasks - 1
                    )
                    # A family member can't have negative scores on their scoreboard. If negative, set to 0
                    if assigned_family_member.closed_tasks < 0:
                        assigned_family_member.closed_tasks = 0
                    assigned_family_member.star_points = (
                        assigned_family_member.star_points - task.star_points
                    )
                    if assigned_family_member.star_points < 0:
                        assigned_family_member.star_points = 0
                # When a task is marked as done.
                # Assigned family member will gain star points and 1 point will be added to closed task.
                # 1 point will be removed from ongoing tasks.
                else:
                    task.status = "Done"
                    assigned_family_member.closed_tasks = (
                        assigned_family_member.closed_tasks + 1
                    )
                    assigned_family_member.star_points = (
                        assigned_family_member.star_points + task.star_points
                    )
                    assigned_family_member.ongoing_tasks = (
                        assigned_family_member.ongoing_tasks - 1
                    )

                assigned_family_member.save()
                task.save()

        # If payload has no title ans status (only containing info about assignment).
        elif (
            validated_data.get("title") is None and validated_data.get("status") is None
        ):
            familyMember = FamilyMember.objects.get(name=validated_data.get("assigned"))
            # If a family member is assigned. Remove assigne and subtract ongoing tasks by 1
            if task.assigned is not None:
                task.assigned = None
                familyMember.ongoing_tasks = familyMember.ongoing_tasks - 1

                if familyMember.ongoing_tasks < 0:
                    familyMember.ongoing_tasks = 0
            # Assign current family member on task and add ongoing tasks by 1
            else:
                task.assigned = validated_data.get("assigned")
                familyMember.ongoing_tasks = familyMember.ongoing_tasks + 1

            familyMember.save()

        else:  # Is update in Form
            task.title = validated_data.get("title")
            task.category = Category.objects.get(
                name=validated_data.get("category")["name"]
            )
            task.end_date = validated_data.get("end_date")
            task.description = validated_data.get("description")
            task.star_points = validated_data.get("star_points")
            if validated_data.get("assigned") is not None:
                familyMember = FamilyMember.objects.get(
                    name=validated_data.get("assigned")
                )
                task.assigned = familyMember
                familyMember.ongoing_tasks = familyMember.ongoing_tasks + 1
                familyMember.save()

        task.save()
        return task

    # Override create to be able to change familymember score if is assigned at create form
    def create(self, validated_data):
        task = Task.objects.create(
            title=validated_data.get("title"),
            category=Category.objects.get(name=validated_data.get("category")),
            creator=validated_data.get("creator"),
            belongs_to_profile=validated_data.get("belongs_to_profile"),
            end_date=validated_data.get("end_date"),
            description=validated_data.get("description"),
            star_points=validated_data.get("star_points"),
        )

        if validated_data.get("assigned") is not None:
            familyMember = FamilyMember.objects.get(name=validated_data.get("assigned"))
            task.assigned = familyMember
            familyMember.ongoing_tasks = familyMember.ongoing_tasks + 1
            familyMember.save()
        task.save()
        return task

    class Meta:
        model = Task
        fields = [
            "id",
            "belongs_to_profile",
            "title",
            "creator",
            "category",
            "category_name",
            "end_date",
            "description",
            "star_points",
            "assigned",
            "status",
        ]
