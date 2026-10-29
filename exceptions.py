
"""Custom exceptions used across SentinelKit."""


class ScanTargetError(Exception):
    """Raised when a scan target cannot be reached or resolved."""

    def __init__(
        self,
        target: str,
        reason: str,
        suggestion: str = "Verify the target and try again.",
    ):
        self.target = target
        self.reason = reason
        self.suggestion = suggestion

        message = (
            f"Scan target error: {target}\n"
            f"Reason: {reason}\n"
            f"Suggested action: {suggestion}"
        )

        super().__init__(message)


class APIKeyMissingError(Exception):
    """Raised when a required API key is not set in the environment."""

    def __init__(
        self,
        key_name: str,
        suggestion: str = "Set the required API key in your environment.",
    ):
        self.key_name = key_name
        self.suggestion = suggestion

        message = (
            f"API configuration error: Missing '{key_name}'.\n"
            f"Suggested action: {suggestion}"
        )

        super().__init__(message)
