"""
This is the config file for the blend shapes.
This defines which shapes connects to which controllers.
Please add or change any of the shapes you wish, but don't remove the connection entirely.
The in-between shapes will take the naming into consideration so no need to put them in here.
But for the corrective shapes we need to assign them to a controller here, please refer bellow for the corrective shape 
instructions.
For corrective shapes please refer bellow for the shape locations.
upLt-----> A
dnLt-----> B
dnRt-----> C
upRt-----> D
"""

facialConnectionsDict = {
    'A': '_AA_M',
    'O': '_OO_M',
    'Fv': '_FF_M',
    'MBP': '_MM_M',
    'L': '_LL_M',
    'U': '_UU_M',
    'CDGK': '_EE_M',

    'Smileleft': '_smile_L',
    'Smileright': '_smile_R',

    'Scream_happy': '_screamhappy_M',
    'Scream_feared': '_screamfeared_M',

    'l_brow_sad': '_sad_L',
    'r_brow_sad': '_sad_R',

    'l_brow_wor': '_wor_L',
    'r_brow_wor': '_wor_R',

    'l_eye_popout': '_popout_L',
    'r_eye_popout': '_popout_R',

    'l_brow_agr': '_angry_L',
    'r_brow_agr': '_angry_R',

    'l_half_eye_squint': '_halfsquint_L',
    'r_half_eye_squint': '_halfsquint_R',

    'l_sneerup': '_upsneer_L',
    'r_sneerup': '_upsneer_R',

    'l_sneerdown': '_dwnsneer_L',
    'r_sneerdown': '_dwnsneer_R',

    'l_upper_eyelid': '_upblink_L',
    'r_upper_eyelid': '_upblink_R',

    'l_lower_eyelid': '_dwnblink_L',
    'r_lower_eyelid': '_dwnblink_R',

    'Smile2': '_opensmile_M',
    'Smile1': '_Smile_M',

    'lwr_teeth_clench': '',
    'upr_teeth_clench': '',
    'open': '',

    'l_eyesquint_yPlus': '',
    'l_eyesquint_yMin': '_squint_L',
    'r_eyesquint_yPlus': '',
    'r_eyesquint_yMin': '_squint_R',

    'l_cheek_puff': '',
    'r_cheek_puff': '',

    'jaw_yPlus': '_jawup_M',
    'jaw_yMin': '_jawdown_M',

    '_slide_yPlus': '',
    '_slide_yMin': '',
    '_slide_xPlus': '',
    '_slide_xMin': '',

    'l_brow_yPlus': '',
    'l_brow_yMin': '',
    'r_brow_yPlus': '',
    'r_brow_yMin': '',

    'l_cnr_yPlus': '_cnrup_L',
    'l_cnr_yMin': '_cnrdwn_L',
    'l_cnr_xPlus': '_cnrout_L',
    'l_cnr_xMin': '_cnrin_L',

    'r_cnr_yPlus': '_cnrup_R',
    'r_cnr_yMin': '_cnrdwn_R',
    'r_cnr_xPlus': '_cnrout_R',
    'r_cnr_xMin': '_cnrin_R',

    'upr_teeth_clench_mov_xPlus': '',
    'lwr_teeth_clench_mov_xPlus': '',
    'upr_teeth_clench_mov_xMin': '',
    'lwr_teeth_clench_mov_xMin': '',

    'l_lip_pinch_xPlus': '_curl_L',
    'l_lip_pinch_xMin': '_pinch_L',
    'r_lip_pinch_xPlus': '_curl_R',
    'r_lip_pinch_xMin': '_pinch_R',

    'mouthbnk_xPlus': '_bank_L',
    'mouthbnk_xMin': '_bank_R',

    'mouth_slide_upLt': '',
    'mouth_slide_dnRt': '',
    'mouth_slide_upRt': '',
    'mouth_slide_dnLt': '',

    'r_cnr_upLt': '_crnCorA_R',
    'r_cnr_dnRt': '',
    'r_cnr_upRt': '',
    'r_cnr_dnLt': '_crnCorB_R',

    'l_cnr_upLt': '_crnCorA_L',
    'l_cnr_dnRt': '',
    'l_cnr_upRt': '',
    'l_cnr_dnLt': '_crnCorB_L'
}
