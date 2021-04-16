import os

DEFAULT_FILE_STORAGE = 'mypage.aws.utils.MediaStorage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')  # 環境変数を指定
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')  # 環境変数を指定

AWS_STORAGE_BUCKET_NAME = 'mypagemedia'  # Amazon S3 のバケット名
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # キャッシュの有効期限（最長期間）= 1日
}
AWS_QUERYSTRING_AUTH = False  # URLからクエリパラメータを削除

AWS_S3_URL = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
MEDIA_URL = f'https://{AWS_S3_URL}/media/'
