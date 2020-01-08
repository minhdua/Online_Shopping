import stripe
stripe.api_key = 'sk_test_b59L8medGYT3RWvLvT8dGSpX007YcDepjQ'

charge = stripe.Charge.create(
  amount=1000,
  currency='usd',
  source='tok_visa',
  receipt_email='jenny.rosen@example.com',
)
