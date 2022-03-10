import utils

card = {
    'card_number': '4242424242424242',
    'card_cvc': '314'
}

# Step 1
print("---Test Redact VGS Echo with Application Content type = JSON ---")
#utils.redact_vgs_echo_json(card)

# Step 2
card_alias = {
    'card_number': 'tok_sandbox_bvoKZzGcQLZRWWspUvxokr',
    'card_cvc': 'tok_sandbox_wqXWDSa5JaX9j2PUDPpk2C'
}

print("---Test Reveal VGS Echo with Application Content type = JSON ---")
utils.reveal_vgs_echo_json(card_alias)
