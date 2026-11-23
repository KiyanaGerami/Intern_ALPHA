MIN_VERSION = "3.9"


def in_virtualen(prefix, base_prefix):
    return prefix != base_prefix

def check_version(version_text):
    parts = tuple(int(x) for x in version_text.split(".")[:2])
    if parts >= tuple(int(x) for x in MIN_VERSION.split(".")):
        return "ok"
    hint = "uv python install 3.14"
    return f"too old, run: {hint}"

def describe_interpreter(version, path):
    text = f"interpreter: Python {version} at {path}"
    return text

