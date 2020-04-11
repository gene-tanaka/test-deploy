def handle(data, client, secrets):
    assets = client.assets.list()
    print(f"Found {len(assets)} assets.")
    return {
        "success": True
    }