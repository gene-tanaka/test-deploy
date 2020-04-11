def handle(data, client, secrets):
    print("Doing this!")
    assets = client.assets.list()
    print(f"Found {len(assets)} assets.")
    return {
        "success": True
    }