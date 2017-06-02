import pymel.core as pm


def getShapeNode(passedObject):
    """
    This gets the shapeNodes name
    Returns:

    """
    objNode = pm.PyNode(passedObject)
    if type(objNode) == pm.nodetypes.Mesh:
        return objNode
    else:
        return objNode.getShape()


def getBlendShapeNode(passedObject):
    """
    This gets the blendShape node.  
    Returns:

    """
    shapeNode = getShapeNode(passedObject)
    blendShapeNodes = [x for x in shapeNode.listHistory(pdo=1) if type(x) == pm.nodetypes.BlendShape]
    if len(blendShapeNodes):
        return blendShapeNodes
    return False


def hasNumeric(inputString):
    """
    This checks for the string for any numeric values.
    Returns:

    """
    return any(char.isdigit() for char in inputString)


def decompileNames(passedName, pattern):
    """
    Splits the passed name with the filters and give them back,
    Returns:

    """
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
    """
    This adds the list of blendShapes to the main mesh.
    Returns:

    """
    return pm.blendShape(shapeList, baseMesh, n='%s_blendShapeNode' % baseMesh)[0]


def addIntermidiateBlendShapes(blendShapeNode, baseMesh, mainShape, intermidiatePattern, intermidiateShapeList=list()):
    """
    This adds the intermediate shapes to the baseMesh.
    Returns:

    """
    blendShapeNode = pm.PyNode(blendShapeNode)
    weightCount = len(blendShapeNode.listAttr(m=True, k=True)) - 1
    pm.blendShape(blendShapeNode, e=1, t=(baseMesh, weightCount, mainShape, 1))
    for each in intermidiateShapeList:
        ret = decompileNames(each, intermidiatePattern)
        pm.blendShape(blendShapeNode, e=1, ib=1, t=(baseMesh, weightCount, each, float(ret[1]['#value']) / 100))
