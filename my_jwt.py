import jwt
from datetime import datetime, timedelta

def generate_token(user):
    exp_time = datetime.utcnow() + timedelta(hours=1)
    
    # Define the token's payload with the user's ID and expiration time
    payload = {
        'user_id': user,
        'exp': exp_time,
    }
    
    # Generate the token with a secret key
    token = jwt.encode(payload, 'secret_key', algorithm='HS256')
    claims = jwt.decode(token,key="secret_key",algorithms=['HS256', ])
    return claims
