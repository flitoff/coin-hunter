import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone


# =========================
# COIN HUNTER CONFIGURATION
# =========================

MAX_PRICE_GBP = 300

SEARCH_PROFILES = [
    {
        "name": "Spanish Cob",
        "query": "spanish cob",
        "max_price": MAX_PRICE_GBP,
    },
    {
        "name": "8 Reales Cob",
        "query": "8 reales cob",
        "max_price": MAX_PRICE_GBP,
    },
    {
        "name": "Shipwreck Silver",
        "query": "shipwreck silver coin",
        "max_price": MAX_PRICE_GBP,
    },
    {
        "name": "Spanish Colonial Silver",
        "query": "spanish colonial silver coin",
        "max_price": MAX_PRICE_GBP,
    },
    {
        "name": "Portuguese Silver",
        "query": "portuguese silver coin",
        "max_price": MAX_PRICE_GBP,
    },
]


HIDDEN_FIND_PROFILES = [
    "old spanish silver coin",
    "unknown silver coin",
    "old hammered silver coin",
    "pirate silver coin",
    "old colonial silver coin",
]


def check_supabase_connection():
    url = os.environ.get("SUPABASE_URL")
    secret_key = os.environ.get("SUPABASE_SECRET_KEY")

    if not url:
        raise RuntimeError("SUPABASE_URL is missing")

    if not secret_key:
        raise RuntimeError("SUPABASE_SECRET_KEY is missing")

    endpoint = f"{url.rstrip('/')}/rest/v1/listings?select=id&limit=1"

    request = urllib.request.Request(
        endpoint,
        headers={
            "apikey": secret_key,
            "Accept": "application/json",
        },
        method="GET",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))

            print("Supabase connection: OK")
            print(f"Database response: {len(data)} row(s)")

    except urllib.error.HTTPError as exc:
        error_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Supabase HTTP error {exc.code}: {error_body}"
        ) from exc

    except urllib.error.URLError as exc:
        raise RuntimeError(
            f"Supabase connection failed: {exc.reason}"
        ) from exc


def run_hunter():
    now = datetime.now(timezone.utc)

    print("=" * 50)
    print("COIN HUNTER")
    print("=" * 50)
    print(f"Scan started: {now.isoformat()}")
    print()

    print("DATABASE")
    check_supabase_connection()
    print()

    print("MAIN SEARCH PROFILES")
    for profile in SEARCH_PROFILES:
        print(
            f"- {profile['name']} | "
            f"query='{profile['query']}' | "
            f"max £{profile['max_price']}"
        )

    print()
    print("HIDDEN FINDS")
    for query in HIDDEN_FIND_PROFILES:
        print(f"- {query}")

    print()
    print("Status: monitoring engine ready.")
    print("eBay API connection will be enabled after credentials are approved.")


if __name__ == "__main__":
    run_hunter()
