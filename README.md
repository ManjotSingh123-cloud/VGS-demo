# VGS Demo

## Follow steps to run demo

#### 1. Install Python if not already installed, and install python request module

#### 2. Sign for a VGS Account here: https://dashboard.verygoodsecurity.com/ and 

#### 3. Gather vault_id, https_proxy_username and https_proxy_password from VGS account and update info in Config.py file.

#### 4. Get sandbox.pem file content from https://www.verygoodsecurity.com/docs/code-samples and save in file sandbox.pem. Add path of file to config.py.

    a. This key will be used for https proxy when testing reveal function.

### Redact and Reveal snippets demo

#### 1. Create Inbound and Outbound Routes as follow:
   
    a. Create Inbound Route for credit card info with upstream host as https://echo.apps.verygood.systems. 

    b. In Inbound Route, Add redact conditions for json data and fields `card_number` and `card_cvc`. Refer inbound_route_json_data.yaml file for configuration
   
    c. Create Outbound Route for Credit card info with upstream host as https://echo.apps.verygood.systems. 
   
    d. In Outbound Route, Add reveal conditions for json data and fields `card_number` and `card_cvc`. Refer outbound_route_json_data.yaml file for configuration
   
#### 2. Test redact and reveal operations for json data using run_demo_1.py. There are two steps in run_demo_1

    a. Update Card variable with card_number and card_cvc you want to test with and run step_1 to redact these feilds. (you can comment step 2 for now)
   
    b. As Step 1 completes successfully, it will return aliased card_number and card_cvc. That means card_number and card_cvc is now redacted and aliased values are sent to upstream host. 
   
    c. Update the card_alias variable with aliased values returned by Step 1 and  run Step 2. Successfully completion of Step 2 will return the original card_number and card_cvc, revealing the aliased versions.
   
    d. You can check the logs in https://dashboard.verygoodsecurity.com/ to see the requests sent by Step 1 and Step 2.
   
### VGS Collect Demo 
    
    a. Setup 'Vault ID' and 'Environment' fields in  vgs-collect-example/creit-card-example.html.
    
    b. Please note that VGS Collect demo will use inbound route created above.
    
    c. Open vgs-collect-example/creit-card-example.html using browser.
    
    d. Fill the information and submit. The result section will show the aliased card info.

### Stripe API Demo

#### 1. Create Inbound and Outbound routes to test Stripe API. 

    a. Refer configuration files inbound_route_stripe.yaml and outbound_route_stripe.yaml to set host and filter conditions.
    
#### 2. Test redact and reveal operations to integrate with Stripe API using run_demo_2.py
    
    a. Go to https://stripe.com/docs/api/tokens/create_card and gather card token details (card number, cvc, exp_month, exp_year, and stripe api key for test.
    
    b. Update stripe api key in config.py file
    
    c. Update Card variable with info from Step 7.a and run step_1 to redact these feilds. (you can comment step 2 for now)
    
    d. As Step 1 completes successfully, it will return aliased card number and card cvc. That means card number and card cvc is now redacted and aliased values are sent to upstream host. 
    
    e. Update the card_alias variable with aliased values returned by Step 1 and  run Step 2. Successfully completion of Step 2 will return the original card_number and card_cvc, revealing the aliased versions.

