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


# Searches designed to find badly described / unidentified coins
HIDDEN_FIND_PROFILES = [
    "old spanish silver coin",
    "unknown silver coin",
    "old hammered silver coin",
    "pirate silver coin",
    "old colonial silver coin",
]


def run_hunter():
    now = datetime.now(timezone.utc)

    print("=" * 50)
    print("COIN HUNTER")
    print("=" * 50)
    print(f"Scan started: {now.isoformat()}")
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
