# -*- coding: utf-8 -*-
"""
Event Object Sketch for PCT Project
"""
import datetime
import json

class Event:
    data = {}
    eventName = ""
    organizer = ""
    participants = ""
    description = ""
    tags = [] #array of strings for now
    registrationRequired= False
    
    #https://pypi.python.org/pypi/pyzipcode
    #using this package will allow us to only get address and Zip code
    #then the zip code will find their city and state for us! (Yet to implement)
    location = ""
    address = ""
    city = ""
    zipCode = ""
    
    #https://docs.python.org/3/library/datetime.html
    #each timeDate class has attributes year, month, day, hour, minute, second, microsecond, tzinfo
    #can reference them like startTime.year, startTime.month, ect.
    startTime = 0
    endTime  = 0
    duration = endTime - startTime #overloaded operator
    
    cost = 0.00
    minCost = 0.00
    maxCost = 0.00
    refundPolicy = False
    
    subOrganizers = []
    sponsors = []
    
    #removed anything to do with links, that will be in the HTML I presume.
    
    #Don't know how these will be used yet
    ID = 123
    otherIDs = "asdf"
    

    '''Constructor with all the required fields needed'''
    def __init__(self, name, organ, parti, desc, regReq, loc, inCost, inDate, endDate):
        self.eventName=name
        self.organizer = organ
        self.participants = parti
        self.description = desc
        self.registrationRequired = regReq
        self.location = loc
        self.cost = inCost
        self.startTime = inDate
        self.endTime=endDate
    
    
    '''Converts existing data in the object into a dictionary, then returns it as a JSON object'''
    def getJSON(self):
        self.data = {"eventName":self.eventName, "organizer":self.organizer, "participants":self.participants, "description":self.description, \
                     "tags": self.tags, "registrationRequired":self.registrationRequired, "location":self.location, \
                     "address":self.address, "city":self.city, "zipCode":self.zipCode, "startTime":self.startTime, \
                     "endTime": self.endTime, "duration":self.duration, "cost":self.cost, "minCost":self.minCost, \
                     "maxCost":self.maxCost, "refundPolicy":self.refundPolicy, "subOrganizers":self.subOrganizers, \
                     "sponsors": self.sponsors, "ID":self.ID}
        json_data = json.dumps(self.data)
        return json_data
    
    def getDictionary(self):
        return self.dictionary
    
    '''Reads in JSON file and saves it into the object'''
    def jsonToEventObject(self,fileName):
        with open(fileName) as data_file:    
            self.data = json.load(data_file)
        
        for key,value in self.data.items():
            #self.eval(key)=value
            #yeah i know this is bad way to reference things
            if(key=="eventName"):
                self.eventName=value
            elif(key=="organizer"):
                self.organizer=value
            elif(key=="participants"):
                self.participants=value
            elif(key=="description"):
                self.description=value
            elif(key=="tags"):
                self.tags=value
            elif(key=="registrationRequired"):
                self.registrationRequired=value
            elif(key=="location"):
                self.location=value
            elif(key=="address"):
                self.address=value
            elif(key=="city"):
                self.city=value
            elif(key=="zipCode"):
                self.zipCode=value
            elif(key=="startTime"):
                self.startTime=value
            elif(key=="endTime"):
                self.endTime=value
            elif(key=="duration"):
                self.duration=value
            elif(key=="cost"):
                self.cost=value
            elif(key=="minCost"):
                self.minCost=value
            elif(key=="maxCost"):
                self.maxCost=value
            elif(key=="refundPolicy"):
                self.refundPolicy=value
            elif(key=="subOrganizers"):
                self.subOrganizers=value
            elif(key=="sponsors"):
                self.sponsors=value
            elif(key=="ID"):
                self.ID=value
        self.getJSON() #update the data dictionary as well
    
    
    ''' Various get and set functions'''    
    def updateEventName(self,updateTerm):
        self.eventName=updateTerm

    def getEventName(self):
        return self.eventName

    def updateOrganizer(self, updateTerm):
        self.organizer=updateTerm
    
    def getOrganizer(self):
        return self.organizer
        
    def updateParticipants(self, updateTerm):
        self.participants=updateTerm
    
    def getParticipants(self):
        return self.participants
        
    def updateDescription(self, updateTerm):
        self.description=updateTerm
    
    def getDescription(self):
        return self.description
    
    def updateTags(self, updateTerm):
        self.tags=updateTerm
    
    def getTags(self):
        return self.tags
    
    def inputNewTag(self, newTag):
        self.tags.append(newTag)
    
    def removeTag(self, removeTag):
        for i in range(len(self.tags)):
            if(self.tags[i]==removeTag):
                del(self.tags[i])
                
    def updateRegRequired(self, updateTerm):
        self.registrationRequired = updateTerm
    
    def getRegRequired(self):
        return self.registrationRequired
    
    def updateWholeLocation(self, location, address, city, zipCode):
        self.location=location
        self.address=address
        self.city=city
        self.zipCode=zipCode
    
    def getWholeAddress(self):
        return (self.location,self.address, self.city, self.zipCode)
        
    def updateLocation(self, updateTerm):
        self.location=updateTerm
    
    def getLocation(self):
        return self.location
        
    def updateAddress(self, updateTerm):
        self.address=updateTerm
        
    def getAddress(self):
        return self.address
        
    def updateCity(self, updateTerm):
        self.city=updateTerm
    
    def getCity(self):
        return self.city
        
    def updateZipCode(self, updateTerm):
        self.zipCode=updateTerm
    
    def getZipCode(self):
        return self.zipCode
        
    def updateStartTime(self, updateTerm):
        self.startTime=updateTerm
    
    def getStartTime(self):
        return self.startTime
        
    def updateEndTime(self, updateTerm):
        self.endTime=updateTerm
    
    def getEndTime(self):
        return self.endTime
        
    def updateCost(self, updateTerm):
        self.cost=updateTerm
    
    def getCost(self):
        return self.cost
        
    def updateMinCost(self, updateTerm):
        self.minCost=updateTerm  
    
    def getMinCost(self):
        return self.minCost

    def updateMaxCost(self, updateTerm):
        self.maxCost=updateTerm   
    
    def getMaxCost(self):
        return self.maxCost
        
    def updateRefundPolicy(self, updateTerm):
        self.refundPolicy=updateTerm    
    
    def getRefundPolicy(self):
        return self.refundPolicy
    
    def updateSubOrganizers(self, updateTerm):
        self.subOrganizers= updateTerm
    
    def getSubOrganizers(self):
        return self.subOrganizers
    
    def addSubOrganizers(self, newSub):
        self.subOrganizers.append(newSub)
    
    def updateSponsors(self, updateTerm):
        self.sponsors=updateTerm
    
    def getSponsors(self):
        return self.Sponsors
        
    def addSponsors(self, newSponsor):
        self.sponsors.append(newSponsor)
        
    def setID(self, updateTerm):
        self.ID=updateTerm
        
    def getID(self):
        return self.ID
    
    
        
        

