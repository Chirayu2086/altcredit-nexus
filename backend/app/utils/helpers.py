def validate_consent(token: str) -> bool:
    """Mock AA consent validation"""
    return token and token.startswith("mock-aa-") or token == "demo-consent"
