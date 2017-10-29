# -*- coding: utf-8 -*-
"""
Event Object Sketch for PCT Project
"""
import datetime

class Event:
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
    startTime = datetime.timedate()
    endTime = datetime.timedate()
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
    otherID = "asdf"
    
    def __init__(self, organ, parti, desc, regReq, loc, inCost, inDate, endDate):
        self.organizer = organ
        self.participants = parti
        self.description = desc
        self.registrationRequired = regReq
        self.location = loc
        self.cost = inCost
        self.startTime = inDate
        self.endTime=endDate
        
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
        
        

