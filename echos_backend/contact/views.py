from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def send_contact_email(request):
    name    = request.data.get('name', '').strip()
    email   = request.data.get('email', '').strip()
    message = request.data.get('message', '').strip()

    if not name or not email or not message:
        return Response(
            {'error': 'All fields are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Email to Echos Production
        send_mail(
            subject=f'New Enquiry from {name} — Echos Production Website',
            message=f'Name:    {name}\nEmail:   {email}\n\nMessage:\n{message}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['echosproduction@gmail.com'],
            fail_silently=False,
        )

        # Auto-reply to the person who contacted
        send_mail(
            subject='We received your message — Echos Production',
            message=(
                f'Hi {name},\n\n'
                'Thank you for reaching out to Echos Production!\n'
                'We have received your message and will get back to you within 24 hours.\n\n'
                '"We don\'t just tell stories. We make them echo."\n\n'
                '— Team Echos Production\n'
                'echosproduction@gmail.com\n'
                '+91 63804 62274\n'
                'Risi House, 126, Anna Main Rd, MGR Nagar, Agaramthen, Chennai 600126'
            ),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False,
        )

        return Response({'success': True, 'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)

    except Exception as e:
        print(f'Email error: {e}')
        return Response(
            {'error': 'Failed to send email. Please try again or contact us directly.'},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
