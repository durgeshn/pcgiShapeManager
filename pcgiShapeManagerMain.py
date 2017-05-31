# general imports
import os
import importlib

# Qt related imports.
from PySide import QtGui
from PySide import QtCore
from shiboken import wrapInstance

# maya related imports.
import pymel.core as pm
import maya.OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

# custom imports.
from ui import pcgiShapeManegerUI
from core import blendShapeUtils

reload(pcgiShapeManegerUI)
reload(blendShapeUtils)


class ShapeManager(MayaQWidgetDockableMixin, QtGui.QMainWindow, pcgiShapeManegerUI.Ui_MainWindow):
    def __init__(self, prnt=None):
        super(ShapeManager, self).__init__(prnt)
        self.baseMesh = None
        self.baseMeshShapeNode = None
        self.blendShapeNode = None
        self.facialFileLocation = None
        self.configLocation = None
        self.setupUi(self)
        self.makeConnections()
        self.mainShapes_tw.setHeaderLabel('Shapes')

        self.mainfileter_le.setText('body_fac_#part_#shape_#side')
        self.interFileter_le.setText('body_fac_#part_#shape_#value_#side')
        self.updateFacialUI()
        self.updateFacialConfig()

    def makeConnections(self):
        self.selectBaseMesh_tb.clicked.connect(self.selectBaseMesh)
        self.addShapes_b.clicked.connect(self.addShapes)
        self.loadShapes_tb.clicked.connect(self.loadShapes)
        self.makeConnections_b.clicked.connect(self.makeUIConnections)

    def updateFacialUI(self):
        rootPath = __file__
        self.facialFileLocation = os.path.join(os.path.dirname(rootPath), 'config/facialUI').replace('\\', '/')
        self.configLocation = os.path.join(os.path.dirname(rootPath), 'config').replace('\\', '/')
        # get only the maya files.
        # facialUIs = [x for x in os.listdir(facialUILocation) if x.endswith('.mb') or x.endswith('.ma')]
        # taking only the maya ascii files.
        facialUIs = [x for x in os.listdir(self.facialFileLocation) if x.endswith('.ma')]
        facialUIs.insert(0, 'Select Facial UI.')
        self.facialUI_cb.addItems(facialUIs)

    def updateFacialConfig(self):
        self.facialConfig_cb.addItem('Select a config file')
        for each in os.listdir(self.configLocation):
            if not each.startswith('__') and each.endswith('.py'):
                self.facialConfig_cb.addItem(each)

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

        if not pm.objExists('BM_nodes'):
            self.makeBasicNodes()

    def makeBasicNodes(self):
        baseMesh = self.baseMeshName_le.text()
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
        intermediateShapes = list()
        for eachShape in allBlendShapeNodes:
            if not blendShapeUtils.hasNumeric(str(eachShape)):
                itm = QtGui.QTreeWidgetItem()
                itm.setText(0, str(eachShape))
                self.mainShapes_tw.addTopLevelItem(itm)
            else:
                intermediateShapes.append(eachShape)

        for each in intermediateShapes:
            matchingIntermediates, patterns = blendShapeUtils.decompileNames(str(each), interFilter)
            if matchingIntermediates:
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
        interMediateShapesDict = dict()
        for i in range(0, allShapesCount):
            itm = self.mainShapes_tw.topLevelItem(i)
            shapeName = itm.text(0)
            # print shapeName, itm.childCount()
            if itm.childCount() > 0:
                interMidiateShapes = list()
                for eachChild in range(0, itm.childCount()):
                    childItem = itm.child(eachChild)
                    interMidiateShapes.append(childItem.text(0))
                # print 'Adding IntermediateShapes for %s with [%s]' % (shapeName, ','.join(interMidiateShapes))
                interMediateShapesDict[shapeName] = interMidiateShapes
            else:
                allShapes.append(shapeName)

        self.blendShapeNode = blendShapeUtils.addBlendShapeNodes(self.baseMeshShapeNode, allShapes)
        print self.blendShapeNode, '<------------------------------'
        for key, val in interMediateShapesDict.iteritems():
            blendShapeUtils.addIntermidiateBlendShapes(self.blendShapeNode, self.baseMeshShapeNode, key,
                                                       self.interFileter_le.text(),
                                                       val)

    def makeUIConnections(self):
        print 'Making connections for the shapes to the UI...'
        bmNode = pm.PyNode('BM_nodes')
        if not bmNode.objExists():
            pm.displayError('Missing %s, Please check and try again.' % bmNode)
            return False
        if not bmNode.guiimport.get():
            facialFile = self.facialUI_cb.currentText()
            if not facialFile:
                pm.displayError('Please select a proper facial file.')
                return False
            facialFilePath = os.path.join(self.facialFileLocation, str(facialFile)).replace('\\', '/')
            pm.importFile(facialFilePath)
            bmNode.guiimport.set(1)

        # Now read the config and make the connections...
        configFile = self.facialConfig_cb.currentText().replace('.py', '')
        importStatement = "pcgiShapeManager.config.%s" % configFile
        baseConfig = importlib.import_module(importStatement)
        reload(baseConfig)

        mainController = pm.PyNode('face_facial_ctl')
        for key, val in baseConfig.facialConnectionsDict.iteritems():
            print '%s.%s' % (self.blendShapeNode, val), '<------------------------------------------'
            if pm.objExists('%s.%s' % (self.blendShapeNode, val)):
                if val:
                    print '%s.%s' % (str(mainController), key), '------------------------>>>>>', '%s.%s' % (
                        self.blendShapeNode, val)
                    pm.connectAttr('%s.%s' % (str(mainController), key), '%s.%s' % (self.blendShapeNode, val))


# Get maya main window as Qt wrapped instance.
def mayaMainWindow():
    """
    This is to get the maya window QT pointer.
    :return:
    :rtype:
    """
    # noinspection PyArgumentList
    mainWindowPointer = omui.MQtUtil.mainWindow()
    return wrapInstance(long(mainWindowPointer), QtGui.QWidget)


def main():
    import sys
    make_app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    main_form = ShapeManager()  # We set the form to be our ExampleApp (design)
    main_form.show()  # Show the form
    # return main_form
    return make_app.exec_()  # and execute the app


if __name__ == '__main__':
    main()
