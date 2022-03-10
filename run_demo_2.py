import utils

card = {
    'card[number]': '4242424242424242',
    'card[exp_month]': '3',
    'card[exp_year]': '2023',
    'card[cvc]': '314'
}


# Step 1
print("---Test Reveal VGS Echo with Application content type: form---")
#utils.redact_vgs_echo_form(card)


# Step 2
card_alias = {
    'card[number]': 'tok_sandbox_bvoKZzGcQLZRWWspUvxokr',
    'card[exp_month]': '3',
    'card[exp_year]': '2023',
    'card[cvc]': 'tok_sandbox_wqXWDSa5JaX9j2PUDPpk2C'
}

print("---Test Reveal Stripe API--")
utils.reveal_stripe_api(card_alias)