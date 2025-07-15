import hashlib
import requests

def check_password_breach(password):
    # Hash password using SHA-1
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]

    # Query the Have I Been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return -1  # API failed

        hashes = (line.split(':') for line in response.text.splitlines())
        for hash_suffix, count in hashes:
            if hash_suffix == suffix:
                return int(count)

        return 0  # Not found in breaches

    except Exception:
        return -1  # Network or other error
