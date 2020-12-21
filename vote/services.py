from django.contrib.contenttypes.models import ContentType

from .models import Vote


def upvote(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    vote, created = Vote.objects.get_or_create(
        content_type=obj_type, object_id=obj.id, user=user
    )
    return vote


def downvote(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    Vote.objects.filter(content_type=obj_type, object_id=obj.id, user=user).delete()
