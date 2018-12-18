
import json
from math import sqrt


class Craigslist(object):
    
    #def __init__(self):
    json_data=open("file.json").read()
    data = json.loads(json_data)
        
        
    def sort_by_price(self, rev):

        if(rev):
            sorted_data = sorted(self.data, key=lambda k: k['price'], reverse=True)
        else:
            sorted_data = sorted(self.data, key=lambda k: k['price'])
        

        return sorted_data
        
        
    def item_by_loc(self,location):
        
        for item in self.data:
            if(item["loc"] == location):
                print(item)
                break
                
        return item
    
    def item_by_id(self,Id):
        
        for item in self.data:
            if(item["id"] == Id):
                print(item)
                break
                
        return item
    
    def item_by_status(self,status):
        
        item_List = []
        for item in self.data:
            if(item["status"] == status):
                print(item)
                item_List.append(item)
                
        
        return item_List
    
    def item_by_userID(self,userId):
        
        item_List = []
        
        for item in self.data:
            if(item["userId"] == userId):
                print(item)
                item_List.append(item)
                
        
        return item_List
    
    def item_by_radius(self,radius, latitude, longitude):
        
        items = []
        c1 = float(latitude)
        c2 = float(longitude)
        for item in self.data:

            c3 = float(item["loc"][0])
            c4 = float(item["loc"][1])

            dst = sqrt((c1 - c3)**2 + (c2 - c4)**2)
            if(dst<float(radius)):

                print(item)
                items.append(item)
                
        return items
    
    

if __name__ == '__main__':
    obj = Craigslist()
    a = obj.item_by_id('540b90e3f9ffc9c9260000d3')

    print(a)






