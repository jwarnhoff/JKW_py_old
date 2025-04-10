#creating a node requires a parent context
import hou

def createROPNET():
    #creates an empty ropNet and returns it for later use
    objContext = hou.node('/obj/')
    fetchNet = objContext.createNode('ropnet','ProceduralFetchNetwork')
    print(fetchNet)
    return fetchNet

def getCacheNodes():
    #creates a list of the connected cache list
    cacheList = []
    
    #Get the Cache Nodes
    cacheNodes = hou.nodeType(hou.sopNodeTypeCategory(),'filecache::2.0').instances()
    if len(cacheNodes) <= 0:
        print('No Cache Nodes Found')
        return 0
    else:
        print('Cache Nodes Found')
        for i in cacheNodes:
            connectionsLength = len(i.inputConnections())
            if connectionsLength < 1:
                print(i)
                print(' This Node has no connection check please check for connection issue of filecache.')
                print('\n')
            else:
                #print('Fileache with connection found.')
                #print(i)
                i.setParms({'loadfromdisk':1,'initsim':1})
                cacheList.append(i)
        return cacheList
            

def createFetches(fetchNet,cacheList):
    #creates the fetchNodes for valid file cache nodes
    ropPath = fetchNet.path()
    for i in cacheList:
        
        cacheRenderChild = i.children()[0]
        print(cacheRenderChild)
        
        if cacheRenderChild.type().name() != 'rop_geometry':
            print(i)
            print('Not a render node \n')
        else:            
            renderPath = i.children()[0].path()
            currentFetch = hou.node(ropPath).createNode('fetch', i.name())
            currentFetch.setParms({'source':renderPath})     


myROP = createROPNET()
cacheNodes = getCacheNodes()
createFetches(myROP, cacheNodes)