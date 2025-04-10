import hou

curNode = hou.selectedNodes()[0].children()
sortedNodes = hou.sortedNodes(curNode)
renderFlag = 'render'
nodesList = list(sortedNodes)

#print(nodesList)
reverseList = nodesList.reverse()

for k in nodesList:
    print(k.type().name())


for j in nodesList:
    iterNodeName = str(j).lower()
    #print(iterNodeName)
    print(j)
    if(renderFlag in iterNodeName and str(j.type().name()) == 'output'):
        print('Render Null Found')
        print(j.path())
        hou.node(j.path()).setGenericFlag(hou.nodeFlag.Display, True)
        hou.node(j.path()).setGenericFlag(hou.nodeFlag.Render, True)
        break   