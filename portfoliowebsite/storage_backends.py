from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static/images'
    default_acl = 'public-read'


class PublicMediaStorage(S3Boto3Storage):
    location = 'static/images/'
    default_acl = 'public-read'
    file_overwrite = False


class PrivateMediaStorage(S3Boto3Storage):
    location = 'static/images'
    default_acl = 'private'
    file_overwrite = False
    custom_domain = False