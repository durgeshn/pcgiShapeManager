import pymel.core as pm

mainController = pm.PyNode('face_facial_ctl')

directConnections = ['face_Fv_fac_ctl', 'face_MBP_fac_ctl', 'face_r_eye_popout_fac_ctl', 'face_r_upper_eyelid_fac_ctl',
                     'face_r_sneerdown_fac_ctl',
                     'face_O_fac_ctl', 'face_l_eye_popout_fac_ctl', 'face_Scream_happy_fac_ctl',
                     'face_Smileleft_fac_ctl', 'face_r_brow_agr_fac_ctl',
                     'face_Scream_feared_fac_ctl', 'face_l_half_eye_squint_fac_ctl', 'face_L_fac_ctl',
                     'face_r_lower_eyelid_fac_ctl',
                     'face_r_brow_sad_fac_ctl', 'face_A_fac_ctl', 'face_r_brow_wor_fac_ctl', 'face_l_brow_wor_fac_ctl',
                     'face_r_half_eye_squint_fac_ctl',
                     'face_l_upper_eyelid_fac_ctl', 'face_Smileright_fac_ctl', 'face_l_lower_eyelid_fac_ctl',
                     'face_r_sneerup_fac_ctl', 'face_CDGK_fac_ctl',
                     'face_l_brow_agr_fac_ctl', 'face_l_brow_sad_fac_ctl', 'face_l_sneerup_fac_ctl', 'face_U_fac_ctl',
                     'face_l_sneerdown_fac_ctl', 'face_lwr_teeth_clench_fac_ctl', 'face_upr_teeth_clench_fac_ctl',
                    'face_l_cheek_puff_fac_ctl', 'face_mouthopen_fac_ctl', 'face_Smile1_fac_ctl', 'face_Smile2_fac_ctl']

for eachConnection in directConnections:
    connectionName = (eachConnection.replace('face_', '')).replace('_fac_ctl', '')
    mainController.addAttr(connectionName, at='double', min=0, max=1, dv=1)
    pm.connectAttr('%s.ty' % eachConnection, '%s.%s' % (mainController, connectionName))


biDirectionConectionsY = ['face_l_eyesquint_fac_ctl', 'face_r_eyesquint_fac_ctl',
                          'face_l_brow_fac_ctl', 'face_r_brow_fac_ctl', 'face_jaw_fac_ctl',
                          'face_mouth_slide_fac_ctl', 'face_r_cnr_fac_ctl', 'face_l_cnr_fac_ctl']

directionalList = [('Y', 0, 1), ('Y', 0, 0), ('X', 1, 1), ('X', 1, 0)]
yPlus = 1
yMin = 1
xPlus = 0
xMin = 0

for idx, each in enumerate(['yPlus', 'yMin']):  # , xPlus, xMin]):
    for eachConnection in biDirectionConectionsY:
        connectionName = '%s_%s' % ((eachConnection.replace('face_', '')).replace('_fac_ctl', ''), each)
        print connectionName
        mainController.addAttr(connectionName, at='double', min=0, max=1, dv=0)

        xMinMax = pm.transformLimits(eachConnection, q=True, tx=True)
        yMinMax = pm.transformLimits(eachConnection, q=True, ty=True)
        dirVallist = [yMinMax, xMinMax]
        valGrp = directionalList[idx][1]
        valAx = directionalList[idx][2]
        getDV = dirVallist[valGrp][valAx]

        f = '%s.%s' % (mainController, connectionName)
        pm.setDrivenKeyframe(f, cd='{0}.translate{1}'.format(eachConnection, directionalList[idx][0]), dv=0, v=0)
        pm.setDrivenKeyframe(f, cd='{0}.translate{1}'.format(eachConnection, directionalList[idx][0]), dv=getDV, v=1)



biDirectionConectionsX = ['face_upr_teeth_clench_mov_fac_ctl', 'face_lwr_teeth_clench_mov_fac_ctl',
                          'face_l_lip_pinch_fac_ctl', 'face_r_lip_pinch_fac_ctl', 'face_mouthbnk_fac_ctl',
                          'face_mouth_slide_fac_ctl', 'face_r_cnr_fac_ctl', 'face_l_cnr_fac_ctl']


yPlus = 0
yMin = 0
xPlus = 1
xMin = 1

for idx, each in enumerate(['xPlus', 'xMin']):  # , xPlus, xMin]):
    for eachConnection in biDirectionConectionsX:
        connectionName = '%s_%s' % ((eachConnection.replace('face_', '')).replace('_fac_ctl', ''), each)
        print connectionName
        mainController.addAttr(connectionName, at='double', min=0, max=1, dv=0)

        xMinMax = pm.transformLimits(eachConnection, q=True, tx=True)
        yMinMax = pm.transformLimits(eachConnection, q=True, ty=True)
        dirVallist = [yMinMax, xMinMax]
        valGrp = directionalList[idx][1]
        valAx = directionalList[idx][2]
        getDV = dirVallist[valGrp][valAx]

        f = '%s.%s' % (mainController, connectionName)
        pm.setDrivenKeyframe(f, cd='{0}.translate{1}'.format(eachConnection, directionalList[idx][0]), dv=0, v=0)
        pm.setDrivenKeyframe(f, cd='{0}.translate{1}'.format(eachConnection, directionalList[idx][0]), dv=getDV,
                             v=1)

# for the correctives.

for each in ['face_mouth_slide_fac_ctl', 'face_r_cnr_fac_ctl', 'face_l_cnr_fac_ctl']:
    controller = pm.PyNode(each)
    controllerGroup = controller.listRelatives(p=True)
    for key, val in {'upLt': (1, 1), 'dnLt': (1, -1), 'dnRt': (-1, -1), 'upRt': (-1, 1)}.iteritems():
        connectionName = '%s_%s' % (controller, key)
        mainController.addAttr(connectionName, at='double', min=0, max=1, dv=0)
        loc = pm.spaceLocator(n='%sLoc_%s_Corrrective' % (key, controller))
        pm.parent(loc, controllerGroup[0])
        loc.visibility.set(0)
        # upper right locator.
        loc.tx.set(val[0])
        loc.ty.set(val[1])
        loc.tz.set(0)
        distNode = pm.createNode('distanceBetween', n='%sDB_%s_Corrective' % (key, controller))
        pm.connectAttr(controller + '.t', distNode + '.point1', f=True)
        pm.connectAttr(loc + '.t', distNode + '.point2', f=True)
        # set Driven.
        pm.setDrivenKeyframe('%s.%s' % (mainController, connectionName), cd='%s.distance' % distNode, dv=1, v=0)
        pm.setDrivenKeyframe('%s.%s' % (mainController, connectionName), cd='%s.distance' % distNode, dv=0, v=1)


