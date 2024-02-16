import base64
import hashlib
import hmac

SECRET_KEY = "8gBm/:&EnhH.1/q"  # merchant key for UAT


def generate_signature(message: str):
    secret_key = SECRET_KEY

    # Encode the message and secret key for proper handling
    message_bytes = message.encode("utf-8")
    secret_key_bytes = secret_key.encode("utf-8")

    # Create the HMAC object with SHA256 algorithm
    h = hmac.new(secret_key_bytes, message_bytes, hashlib.sha256)

    # Generate the digest (binary) and encode it to base64
    digest = h.digest()
    base64_encoded_hash = base64.b64encode(digest).decode("utf-8")

    # Print the base64 encoded hash
    return base64_encoded_hash
