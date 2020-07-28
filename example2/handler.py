import time

def handle(data, client):
    print("Hello anders. Will sleep a bit now...")
    time.sleep(1.0)
    print("Did sleep. Will sleep some more, but first, print another line")
    print("Here it is.")
    time.sleep(1.0)
    print("Ok, I'm done now. Fetching an asset")
    asset = client.assets.retrieve(external_id = "my_special_asset")
    time.sleep(1.0)
    print("Slept again.")
    return {
        "result": 4.0 * data["value"],
        "assetName": asset.name,
    }
