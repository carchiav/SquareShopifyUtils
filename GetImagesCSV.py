from square.client import Client
from SquareUtilities import getAllCatalogObjects
import os

client = Client(
    access_token=os.environ['SQUARE_ACCESS_TOKEN'],
    environment='production')

allObjects = getAllCatalogObjects("ITEM")

######################### Now there is a list of all of the objects: allObjects
namesandimgs = []
counter = 0
while counter < len(allObjects):
  print("Getting image for object number " + str(counter+1)+", Name: " + allObjects[counter]['item_data']['name'])
  counter2 = 0
  while counter2 < len(allObjects[counter]['item_data']['variations']):
    print("Variation number " + str(counter2+1))
    ##print(allObjects[counter]['item_data']['variations'][counter2]['item_variation_data'])
    currName = allObjects[counter]['item_data']['name']
    currVar = allObjects[counter]['item_data']['variations'][counter2]['item_variation_data']['name']
    if 'image_ids' in allObjects[counter]['item_data']['variations'][counter2]['item_variation_data']:
      currImgId = allObjects[counter]['item_data']['variations'][counter2]['item_variation_data']['image_ids'][0]
    else:
      currImgId = "none"
    
    if currImgId == "none":
      currImg = "none"
    else:
      currImgInfo = client.catalog.batch_retrieve_catalog_objects(
        body = {
            "object_ids": [
              currImgId
              ],
      "include_related_objects": False
        }
      )
      ##print(currImgInfo)
      currImg = currImgInfo.body['objects'][0]['image_data']['url']
    
    tempnameandimg = [currName,currVar,currImg]
    ##print(tempnameandimg)
    namesandimgs.append(tempnameandimg)
    counter2+=1
  counter+=1

counter = 0


##############################
print("Total number of variations: " + str(len(namesandimgs)))
with open('images.csv', 'w') as f:
    f.write('Name, Variation, ImageURL')
    f.write('\n')
    for line in namesandimgs:
        f.write(line[0])
        f.write(',')
        f.write(line[1])
        f.write(',')
        f.write(line[2])
        f.write('\n')