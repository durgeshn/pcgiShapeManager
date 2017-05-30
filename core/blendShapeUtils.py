import pymel.core as pm


def getShapeNode(passedObject):
    objNode = pm.PyNode(passedObject)
    if type(objNode) == pm.nodetypes.Mesh:
        return objNode
    else:
        return objNode.getShape()


def getBlendShapeNode(passedObject):
    shapeNode = getShapeNode(passedObject)
    blendShapeNodes = [x for x in shapeNode.listHistory(pdo=1) if type(x) == pm.nodetypes.BlendShape]
    if len(blendShapeNodes):
        return blendShapeNodes
    return False


def hasNumeric(inputString):
    return any(char.isdigit() for char in inputString)


def decompileNames(passedName, pattern):
    # passedName = 'body_fac_#part_#shape_#side'
    patterns = pattern.split('_')
    prefix = pattern.split('#')[0]
    mainPattern = [prefix]
    mainPattern.extend([x for x in patterns if x.startswith('#')])
    tmp = passedName.replace(prefix, '')
    tmp = tmp.split('_')
    tmp.insert(0, prefix)
    retDict = dict()
    retDict['#prefix'] = prefix
    if len(mainPattern) != len(tmp):
        return False, {}
    for i in range(1, len(mainPattern)):
        retDict[mainPattern[i]] = tmp[i]
        i += 1
    return True, retDict


def addBlendShapeNodes(baseMesh, shapeList=list()):
    return pm.blendShape(shapeList, baseMesh, n='%s_blendShapeNode' % baseMesh)[0]


def addIntermidiateBlendShapes(blendShapeNode, baseMesh, mainShape, intermidiatePattern, intermidiateShapeList=list()):
    blendShapeNode = pm.PyNode(blendShapeNode)
    weightCount = len(blendShapeNode.listAttr(m=True, k=True)) - 1
    pm.blendShape(blendShapeNode, e=1, t=(baseMesh, weightCount, mainShape, 1))
    for each in intermidiateShapeList:
        ret = decompileNames(each, intermidiatePattern)
        pm.blendShape(blendShapeNode, e=1, ib=1, t=(baseMesh, weightCount, each, float(ret[1]['#value']) / 100))
