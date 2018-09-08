from pymongo import MongoClient
import datetime

client = MongoClient("184.73.76.65", 27017);

db = client.imageDatabase

collection = db.imageCollection

#returns a array of the images, each one is a dictonary, is SAFE for client side
def getRisks():

    counter = 0
    returnValue = [] 

    for post in collection.posts.find():
        returnValue.append(post)
        counter += 1

    return returnValue

#returns an array of the posts, each one is a dictonay, however only the nessary client info is included, is NOT safe
def getRisksBasicInfo():
    
    returnValue = []
    for post in collection.posts.find():
        value = {
            "riskType" : post["riskType"]
            "location" : post["location"]
        }
        returnValue.append(value)
    
    return returnValue

# adds a post to the database
def addRisk(imageFileName, location, riskType, userPosted, userId):
    if collection == None:
        print("[DatabaseManager] Database was not set up right yet")
        print("[DatabaseManager] Fix this ^ Rahual")
        return

    dataUploaded = datetime.date

    if userPosted == None:
        userId = "None"

    post = {
        "imageFileName": str(imageFileName),
        "location": str(location),
        "riskType" : str(riskType),
        "flagged": "false"
        "userPosted" : str(userPosted),
        "userName" : str(userId)
    }

    posts = collection.posts
    post_id = posts.insert_one(post).inserted_id

    print("[DatabaseManager] Thing added")

#find the data about a certain image, is safe for clientside
def findRisk(location):
    posts = collection.posts
    post = posts.find_one({"location" : location})

    if post == None:
        print("[DataBaseManager] No post found with location " + location)

    data = {
        imageFileName : str(post[imageFileName])
        location : str(location)
        riskType : str([postriskType])
        flagged : str(post[flagged])
    }

#finds ALL data about a certain image, is NOT safe for clientside
def findAllData(location):

    posts = collection.posts
    post = posts.find_one({
        "location" : location
    })

     if post == None:
        print("[DataBaseManager] No post found with location " + location)


def flagRisk(imageFileName):

    posts = collection.posts
    image = posts.find_one({"imageFileName" : imageFileName})

    if image == None:
        print("[DatebaseManager] Image was not found")
        return

    collection.update_one({'_id': imageId}, {"flagged": "true"}, upsert=False)

    print("[DatabaseManager] Flagged image ")


def count():
    return collection.posts.count

#getImages()

#print("End")