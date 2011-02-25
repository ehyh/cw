# Filename: classes.py
# Author: Esther Hong
# Centre No/ Index No: 3024 /
# Description: Support classes for music library

''' Super class Resource '''
class Resource:

    ''' Constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType): # private data: self.__
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    ''' Accessor - getty'''
    def getResourceNo(self):
        return self.__ResourceNo
    def getTitle(self):
        return self.__Title
    def getDateAcquired(self):
        return self.__DateAcquired
    def getResourceType(self):
        return self.__ResourceType


    ''' Modifier - mutator ''' # no return
    def setTitle(self, newTitle):
        self.__Title = newTitle
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    ''' Display helper function '''
    def display(self):
        return "{0}{1}{2}{3}".format \
               (self.getResourceNo(), self.getTitle(), self.getDateAcquired(), self.getResourceType())


''' Subclass MusicCD '''
class MusicCD(Resource): #subclass(superclass)

    ''' Constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType) # calling super class init method
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks

    ''' Accessor '''
    def getArtist(self):
        return self.__Artist
    def getNoOfTracks(self):
        return self.__NoOfTracks

    ''' Mutator'''
    def setArtist(self, newArtist):
        self.__Artist = newArtist
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks

    ''' Helper '''
    def display(self):
        return "{0}{1:50}{2}".format(super().display(), self.getArtist(), self.getNoOfTracks()) # superclass display!

        
''' Subclass FilmDVD '''
class FilmDVD(Resource):
    
    ''' Constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType) # calling super class init method
        self.__Director = Director
        self.__RunningTime = RunningTime
        
    ''' Accessor'''
    def getDirector(self):
        return self.__Director
    def getRunningTime(self):
        return self.__RunningTime

    ''' Mutator '''
    def setDirector(self, newDirector):
        self.__Director = newDirector
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime

    ''' Helper '''
    def display(self):
        return "{0}{1:50}{2}".format(super().display(), self.getDirector(), self.getRunningTime()) # superclass display!
    

### main
##r1 = Resource("00001", "Best of SHINee", "030309", "C") #"00001" is a string
##print(r1.getResourceNo())
##r1.setTitle("SHINee 2011")
##print(r1.getTitle())
##print(r1.display())
##
##r2 = Resource("00002", "", "", "")
##r2.setTitle("Super Junior Collection")
##r2.setDateAcquired("050510")
##r2.setResourceType("C")
##print(r2.display())

# print(r2.__Title) # illegal should not access private data directly
                    # data/information hiding (encapsulation)

cd1 = MusicCD("00003", "FT Island Beautiful Journey", "070708", "C", "FT Island", 5)
print(cd1.getResourceNo()) # inherited method
print(cd1.getArtist()) # class method
print(cd1.display()) # overriding - look at subclass for method first

dvd1 = FilmDVD("00004", "New Shaolin Temple", "020211", "D", "Mr Andy", 120)
print(dvd1.display())

resource_list = []
resource_list.append(cd1)
resource_list.append(dvd1)
print(resource_list)

for item in resource_list:
    item.display() # polymorphism
