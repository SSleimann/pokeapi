import jwt

from datetime import timedelta

from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def create_token_jwt(user):
    secret_key = settings.SECRET_KEY
    exp_date = timezone.now() + timedelta(days=3)

    payload = {
        'user': user.username,
        'exp': exp_date,
        'type': '_email_confirmation'
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    
    return token


def send_user_verify_email(user_pk):
    """Send account verification link to given user."""
    user = get_user_model().objects.get(pk=user_pk)
    verification_token = create_token_jwt(user)
    
    subject = 'Account Verification'
    from_email = '<noreply@api.com>'
    
    content = render_to_string(
        'email/email_verify.txt',
        {'token': verification_token, 'user': user}
    )
    
    msg = EmailMessage(subject, content, from_email, [user.email])
    msg.send(fail_silently=False)

