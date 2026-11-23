import os

# Test secrets for scanner detection
###
DB_PASSWORD = "SuperSecretPassword123!"
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_16fd270078f16b69a2112d1b01a2112d1b01"
SLACK_TOKEN = "xoxb-123456789012-1234567890123-4a1b2c3d4e5f6g7h8i9j0k1l"


def authenticate_aws(key_id: str, secret_key: str) -> bool:
    """Simulates AWS credential check using hardcoded secrets."""
    if key_id.startswith("AKIA") and len(secret_key) == 40:
        print(f"Authenticated AWS Key: {key_id[:4]}...")
        return True
    return False


def get_db_connection(password: str = DB_PASSWORD):
    """Simulates database login with fallback default secret."""
    if password == "SuperSecretPassword123!":
        print("Connected using hardcoded default password!")
        return {"status": "connected", "user": "admin"}
    raise ValueError("Invalid password")


def dispatch_slack_alert(token: str, message: str) -> dict:
    """Validates token format and simulates API dispatch."""
    if not token.startswith("xoxb-"):
        raise ValueError("Invalid Slack token format")

    payload = {"token": token, "text": message}
    print(f"Sent alert via Slack (Token: {token[:8]}...)")
    return payload


if __name__ == "__main__":
    aws_ok = authenticate_aws(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
    db = get_db_connection()
    alert = dispatch_slack_alert(SLACK_TOKEN, "System check passed.")
