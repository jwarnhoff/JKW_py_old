import hou


def updateCameraParm(ropsToUpdate,cameraPath):
#small function to call instead for updating parms so if new render engines arrive should not be a problem
    ropsUpdated = []
    
    for i in ropsToUpdate:
        curNodeType = i.type().name()
        if(curNodeType == 'ifd'):
            i.setParms({'camera':str(cameraPath)})
        elif(curNodeType == 'Redshift_ROP'):
            i.setParms({'RS_renderCamera':str(cameraPath)})
        ropsUpdated.append(i)
        
    hou.ui.displayMessage(text='rops to update',details=str(ropsUpdated),buttons=('ok',),details_expanded=True)    

#Get new path of camera from user from tree selection.
newCameraPath = hou.ui.selectNode(node_type_filter=hou.nodeTypeFilter.ObjCamera)

#info stored for the user upon method of updating ROP nodes
basicInfo = 'Update Render Camera with\n' + str(newCameraPath)
displayMessage = 'Choose to update to the selected selected camera,\n'+ str(newCameraPath) +'\nfrom selection or all rops' 


updateRopButton = hou.ui.displayMessage(text=basicInfo, details=displayMessage,title='Update Render Camera',buttons=('All Rops','Selected ROPs','Cancel',),close_choice=-1,severity=hou.severityType.ImportantMessage)

if(updateRopButton == 0):
    #send all rops to update function
    redshiftROPstoUpdate = hou.nodeType(hou.ropNodeTypeCategory(),'Redshift_ROP').instances()
    mantraRopstoUpdate = hou.nodeType(hou.ropNodeTypeCategory(),'ifd').instances()
    allROPS = mantraRopstoUpdate + redshiftROPstoUpdate
    updatedCams = updateCameraParm(allROPS,newCameraPath)
    
elif(updateRopButton == 1):
    selection = hou.selectedNodes()
    if(len(selection) <= 0):
        hou.ui.displayMessage(text='No Nodes Selected.',severity=hou.severityType.Error)
    elif(len(selection)>=1):
        ropstoUpdate = []
        for j in selection:
            curNodeType = j.type().name()
            if(curNodeType == 'Redshift_ROP' or curNodeType == 'ifd'):
                ropstoUpdate.append(j)
        updateCameraParm(ropstoUpdate,newCameraPath)
        
    

