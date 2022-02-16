from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from ipware.ip import get_client_ip
import logging


logging.basicConfig(filename="tests.log", level=logging.DEBUG)


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    print("user {} logged in through page {}".format(user.username))


@receiver(user_login_failed)
def log_user_login_failed(sender, credentials, request, **kwargs):
    print("user failed to log in")


@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs ):
    print("user logged out")


def IPCatcher(request):
    ip = get_client_ip(request)
    if ip is not None:
        print("We have an IP address for user")
        print(ip)
        logging.basicConfig(filename='log_recording.txt',
                            level=logging.DEBUG, format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.DEBUG('This is working')

    else:
        print("we don't have an IP address for user")
