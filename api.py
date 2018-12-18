
# coding: utf-8

# In[ ]:


import cherrypy
from Craigslist import *
import os

obj = Craigslist()


cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '10001')),})


class HelloWorld(object):
    
    @cherrypy.expose
    def index(self):
        return "Craigslist Sales!"

    
    @cherrypy.expose
    def getsorteddata(self,**args):
        if('True'):
            rev = 'True'
        else:
            rev = 'False'
        srt = obj.sort_by_price(rev)
        
        return json.dumps(srt)
    
    @cherrypy.expose
    def getitem(self,**args):
        if('id' in args):
            id = cherrypy.request.params.get('id')
            a = obj.item_by_ID(id)
            
        elif('location' in args):
            location = cherrypy.request.params.get('location')
            a = obj.item_by_loc(location)
            
        return json.dumps(a)

    
    @cherrypy.expose
    def getitemslist(self,**args):
        
        if('status' in args):
            status = cherrypy.request.params.get('status')
            b = obj.item_by_status(status)
            
        if('userId' in args):
            userId = cherrypy.request.params.get('userId')
            b = obj.item_by_status(userId)
            
        return json.dumps(b)
    
    def get_items_in_radius(self, **args):
        
        radius = cherrypy.request.params.get("radius")
        latitude = cherrypy.request.params.get("latitude")
        longitude = cherrypy.request.params.get("longitude")
        items = obj.getItemsInRadius(radius, latitude,longitude)
    
        return json.dumps(items)
    
if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())

