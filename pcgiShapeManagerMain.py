# Qt related imports.
from PySide import QtGui
from PySide import QtCore

# maya related imports.
import pymel.core as pm

# custom imports.
from ui import pcgiShapeManegerUI
from core import blendShapeUtils

reload(pcgiShapeManegerUI)
reload(blendShapeUtils)


class ShapeManager(QtGui.QMainWindow, pcgiShapeManegerUI.Ui_MainWindow):
    def __init__(self, prnt=None):
        super(ShapeManager, self).__init__(prnt)
        self.baseMesh = None
        self.baseMeshShapeNode = None
        self.blendShapeNode = None
        self.setupUi(self)
        self.makeConnections()
        self.mainShapes_tw.setHeaderLabel('Shapes')

        self.mainfileter_le.setText('body_fac_#part_#shape_#side')
        self.interFileter_le.setText('body_fac_#part_#shape_#value_#side')

    def makeConnections(self):
        self.selectBaseMesh_tb.clicked.connect(self.selectBaseMesh)
        self.addShapes_b.clicked.connect(self.addShapes)
        self.loadShapes_tb.clicked.connect(self.loadShapes)

    def selectBaseMesh(self):
        sel = pm.ls(sl=1)
        if not len(sel) or len(sel) > 1:
            raise RuntimeError(
                'Nothing is selected or more than one object is selected, please select the baseMesh then try again.')
        else:
            baseMesh = str(sel[0])
        self.baseMesh = sel[0]
        self.baseMeshName_le.setText(baseMesh)
        shapeNode = blendShapeUtils.getShapeNode(baseMesh)
        self.baseMeshShapeNode = shapeNode
        self.baseMeshShape_le.setText(str(shapeNode))

        makeBasicNodes = False
        for e in ['*_shapes_Grp', '*_shapes_Grp', '*_All_blends_Grp', '*_Xtra_shapes',
                  '*_INBetween_shapes']:
            if not pm.objExists(e):
                makeBasicNodes = True

        if makeBasicNodes:
            self.makeBasicNodes()

    def makeBasicNodes(self):
        baseMesh = self.baseMeshName_le.text()
        if pm.objExists("{0}_shapes_Grp".format(baseMesh)):
            return True
        topGrp = pm.group(n="{0}_shapes_Grp".format(baseMesh), em=1)
        pm.parent(pm.group(n="{0}_All_blends_Grp".format(baseMesh), em=1), topGrp)
        pm.parent(pm.group(n="{0}_Xtra_shapes".format(baseMesh), em=1), topGrp)
        pm.parent(pm.group(n="{0}_Inbetween_shapes".format(baseMesh), em=1), topGrp)
        if not pm.objExists('BM_nodes'):
            bmNode = pm.group(n='BM_nodes', em=1)
            bmNode.addAttr('guiimport', at='bool', k=1)
            bmNode.guiimport.set(0)
        pm.select(cl=1)

    def loadShapes(self):
        self.mainShapes_tw.clear()
        baseFilter = self.mainfileter_le.text()
        interFilter = self.interFileter_le.text()
        tmp = baseFilter.split('_')
        numberOfPlaceHolders = 0
        for e in tmp:
            if e.startswith('#'):
                numberOfPlaceHolders += 1

        '_'.join(tmp[:numberOfPlaceHolders - 1])

        mayaFilter = '%s%s' % ('_'.join(tmp[:numberOfPlaceHolders - 1]), '_*' * numberOfPlaceHolders)
        allBlendShapeNodes = pm.ls(mayaFilter, type='transform')
        interMidiateShapes = list()
        for eachShape in allBlendShapeNodes:
            if not blendShapeUtils.hasNumeric(str(eachShape)):
                itm = QtGui.QTreeWidgetItem()
                itm.setText(0, str(eachShape))
                self.mainShapes_tw.addTopLevelItem(itm)
            else:
                interMidiateShapes.append(eachShape)

        for each in interMidiateShapes:
            matchingIntermitiades, patterns = blendShapeUtils.decompileNames(str(each), interFilter)
            if matchingIntermitiades:
                tmp = baseFilter.split('_')
                parentName = ''
                i = 0
                for x in tmp:
                    if x.startswith('#'):
                        x = patterns[x]
                    if i == 0:
                        parentName += str(x)
                    else:
                        parentName += '_' + str(x)
                    i += 1
                parentItem = self.mainShapes_tw.findItems(parentName, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)
                if len(parentItem):
                    newItem = QtGui.QTreeWidgetItem(parentItem[0])
                    newItem.setText(0, str(each))

    def addShapes(self):
        allShapesCount = self.mainShapes_tw.topLevelItemCount()
        allShapes = list()
        interMidiateShapesDict = dict()
        for i in range(0, allShapesCount):
            itm = self.mainShapes_tw.topLevelItem(i)
            shapeName = itm.text(0)
            # print shapeName, itm.childCount()
            if itm.childCount() > 0:
                interMidiateShapes = list()
                for eachChild in range(0, itm.childCount()):
                    childItem = itm.child(eachChild)
                    interMidiateShapes.append(childItem.text(0))
                # print 'Adding IntermidiateShapes for %s with [%s]' % (shapeName, ','.join(interMidiateShapes))
                interMidiateShapesDict[shapeName] = interMidiateShapes
            else:
                allShapes.append(shapeName)

        ret = blendShapeUtils.addBlendShapeNodes(self.baseMeshShapeNode, allShapes)
        print ret, '<------------------------------'
        for key, val in interMidiateShapesDict.iteritems():
            # addIntermidiateBlendShapes(blendShapeNode, baseMesh, mainShape, intermidiatePattern, intermidiateShapeList=list()):
            blendShapeUtils.addIntermidiateBlendShapes(ret[0], self.baseMeshShapeNode, key, self.interFileter_le.text(), val)




def main():
    import sys
    make_app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    main_form = ShapeManager()  # We set the form to be our ExampleApp (design)
    main_form.show()  # Show the form
    # return main_form
    return make_app.exec_()  # and execute the app


if __name__ == '__main__':
    main()
