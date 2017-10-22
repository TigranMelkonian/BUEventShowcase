# -*- coding: utf-8 -*-
"""
Event Object Sketch for PCT Project
"""
class Event:
    organizer = ""
    participants = ""
    description = ""
    #tags = ??
    registrationRequired= False
    
    location = ""
    address = ""
    city = ""
    zipCode = ""
    
    #date = ??
    #start = ??
    #end= ??
    #duration = int hours?
    
    cost = 0.00
    minCost = 0.00
    maxCost = 0.00
    refundPolicy = False
    
    subOrganizers = ["subOrganizer1", "subOrganizer2"]
    sponsors = ["Sponsor1" , "Sponsor2"]
    #websiteLinker = img or String #this is what they click
    websiteLink = "" #this is where it goes <href>
    socialMediaLinks = ["Facebook link", "twitter link"]
    
    ID = 123
    otherID = "asdf"
    
    def __init__(self, organ, parti, desc, regReq, loc, inCost, inDate):
        organizer = organ
        participants = parti
        description = desc
        registrationRequired = regReq
        location = loc
        cost = inCost
        date = inDate
        
        
        

