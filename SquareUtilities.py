from square.client import Client
import os

def getAllCatalogObjects(itemType):
    counter = 0
    counter2 = 0
    allObjects = [] ##List of all CatalogObjects of itemType
    client = Client(
        access_token=os.environ['SQUARE_ACCESS_TOKEN'],
        environment='production')
    result = client.catalog.list_catalog(
        types = itemType
    )

    if result.is_success():
        print(counter+1)
        while counter2 < len(result.body['objects']):
            allObjects.append(result.body['objects'][counter2])
            counter2+=1
        counter+=1
    elif result.is_error():
        print(result.errors)
    while result.cursor != None:
        result = client.catalog.list_catalog(
            cursor = result.cursor,
            types = "ITEM"
        )
        if result.is_success():
            print(counter+1)
            counter2 = 0
            while counter2 < len(result.body["objects"]):
                allObjects.append(result.body['objects'][counter2])
                counter2+=1
            counter+=1
        elif result.is_error():
            print(result.errors)
            break
    return allObjects
