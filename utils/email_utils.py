# main function that actually sends the email.
from django.core.mail import send_mail

# render_to_string takes a Django template (like an HTML file)
#  and fills it with context variables, returning a rendered HTML string
from django.template.loader import render_to_string


# strip_tags removes all HTML tags from a string.
from django.utils.html import strip_tags


# Imports Django project’s settings (like EMAIL_BACKEND, DEFAULT_FROM_EMAIL, etc.) so you can use them in the function.
from django.conf import settings




def send_vendor_registration_notification_to_admin(vendor):
    """
    Send email to admin when a new vendor registers
    """
    subject = 'A new vendor has registered: {vendor.vendor_name}'


    domain = getattr(settings, 'SITE_DOMAIN', 'http://127.0.0.1:8000')

    admin_url = f"{domain}/admin/vendor/vendor/"
    vendor_detail_url = f"{domain}/admin/vendor/vendor/{vendor.id}/change/"

    html_message = render_to_string('emails/admin_vendor_notification.html', {
        'vendor': vendor,
        'vendor_user': vendor.vendor_user,
        'admin_url': admin_url,
        'vendor_detail_url': vendor_detail_url,
        'domain': domain,
                         })
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(
            subject=subject,
                 #   The body of the email 
                message = plain_message, 
                #   The email address to send the email
                from_email = from_email, 
                #   A list of recipients, here just [settings.ADMIN_EMAIL]
                 recipient_list= [settings.ADMIN_EMAIL], 
                #   The HTML body of the email.
                  html_message=html_message,
                  # If sending fails, raise an exception instead of silently ignoring it.
                  fail_silently=False)
        
        return True
    except Exception as e:
        print(f"Error sending admin notification: {e}")
        return False
    


def send_vendor_approval_notification(vendor,approved = True):
    """
    Send email to vendor about approval status
    """
    subject = 'Congratulations! Your vendor account has been approved'
    html_message = render_to_string('emails/vendor_approved.html', {'vendor': vendor})
    plain_text = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(subject,plain_text, from_email, [vendor.vendor_user.email], html_message=html_message,
                  fail_silently=False)
        return True
    except Exception as e:
        print(f"Error sending vendor approval notification: {e}")
        return False


def send_vendor_rejection_notification(vendor):
    """
    Send email to vendor about rejection status
    """
    subject = 'Sorry! Your vendor account has been rejected'
    html_message = render_to_string('emails/vendor-rejection.html', {'vendor': vendor})
    plain_text = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL

    try:
        send_mail(subject,plain_text, from_email, [vendor.vendor_user.email], html_message=html_message,fail_silently=False)
        return True
    except Exception as e:
        print(f"Error sending vendor rejection notification: {e}")
        return False