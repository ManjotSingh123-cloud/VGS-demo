import requests
import os

from config import HTTPS_PROXY_USERNAME, HTTPS_PROXY_PASSWORD, VAULT_ID, STRIPE_API_KEY, SANDBOX_KEY


def set_proxy():
    os.environ['HTTPS_PROXY'] = "https://{}:{}@{}.sandbox.verygoodproxy.com:8080".format(
        HTTPS_PROXY_USERNAME, HTTPS_PROXY_PASSWORD, VAULT_ID
    )


def redact_vgs_echo_json(data):

    inbound_url = "https://{}.sandbox.verygoodproxy.com/post".format(VAULT_ID)
    response = requests.post(
        inbound_url,
        json=data
    )
    print(response.text)


def reveal_vgs_echo_json(data):

    set_proxy()
    response = requests.post(
        'https://echo.apps.verygood.systems/post',
        json=data,
        verify=SANDBOX_KEY)
    print(response.text)


def redact_vgs_echo_form(data):

    inbound_url = "https://{}.sandbox.verygoodproxy.com/post".format(VAULT_ID)
    response = requests.post(
        inbound_url,
        data=data
    )
    print(response.text)


def reveal_vgs_echo_form(data):

    set_proxy()
    response = requests.post(
        'https://echo.apps.verygood.systems/post',
        data=data,
        verify='certs/sandbox.pem')
    print(response.text)


def reveal_stripe_api(data):

    set_proxy()
    response = requests.post(
        'https://api.stripe.com/v1/tokens',
        data=data,
        auth=(STRIPE_API_KEY, ''),
        verify=SANDBOX_KEY
    )

    print(response.text)

