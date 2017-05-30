import pprint
# base letters.
facialConnectionsDict = {
    'A': 'body_fac_lipsync_AA_M',
    'O' : 'body_fac_lipsync_OO_M',
    'Fv': 'body_fac_lipsync_FF_M',
    'MBP': 'body_fac_lipsync_MM_M',
    'L':  'body_fac_lipsync_LL_M',
    'U':  'body_fac_lipsync_UU_M',
    'CDGK': 'body_fac_lipsync_EE_M',

    'Smileleft': 'body_fac_mouth_smile_L',
    'Smileright':  'body_fac_mouth_smile_R',

    'Scream_happy':  'body_fac_mouth_screamhappy_M',
    'Scream_feared':  'body_fac_mouth_screamfeared_M',

    'l_brow_sad': 'body_fac_brw_sad_L' ,
    'r_brow_sad':  'body_fac_brw_sad_R',

    'l_brow_wor':  'body_fac_brw_wor_L',
    'r_brow_wor':  'body_fac_brw_wor_R',

    'l_eye_popout': 'body_fac_eye_popout_L',
    'r_eye_popout':  'body_fac_eye_popout_R',

    'l_brow_agr':  'body_fac_brw_angry_L',
    'r_brow_agr':  'body_fac_brw_angry_R',

    'l_half_eye_squint':  'body_fac_eye_halfsquint_L',
    'r_half_eye_squint':  'body_fac_eye_halfsquint_R',

    'l_sneerup': 'body_fac_lip_upsneer_L',
    'r_sneerup': 'body_fac_lip_upsneer_R',

    'l_sneerdown': 'body_fac_lip_dwnsneer_L',
    'r_sneerdown': 'body_fac_lip_dwnsneer_R',

    'l_upper_eyelid': 'body_fac_eye_upblink_L',
    'r_upper_eyelid':  'body_fac_eye_upblink_R',

    'l_lower_eyelid':  'body_fac_eye_dwnblink_L',
    'r_lower_eyelid':  'body_fac_eye_dwnblink_R',

    'Smile2' :'body_fac_mouth_opensmile_M',
    'Smile1':'body_fac_mouth_Smile_M',

    'lwr_teeth_clench' : '',
    'upr_teeth_clench' : '',
    'mouthopen' : '',

    'l_eyesquint_yPlus' : '',
    'l_eyesquint_yMin' : 'body_fac_eye_squint_L',
    'r_eyesquint_yPlus' : '',
    'r_eyesquint_yMin' : 'body_fac_eye_squint_R',

    'l_cheek_puff' : '',

    'jaw_yPlus' : 'body_fac_mouth_jawup_M',
    'jaw_yMin' : 'body_fac_mouth_jawdown_M',

    'mouth_slide_yPlus' : '',
    'mouth_slide_yMin' : '',
    'mouth_slide_xPlus' : '',
    'mouth_slide_xMin' : '',


    'l_brow_yPlus' : '',
    'l_brow_yMin' : '',
    'r_brow_yPlus' : '',
    'r_brow_yMin' : '',

    'l_cnr_yPlus' : 'body_fac_lip_cnrup_L',
    'l_cnr_yMin' : 'body_fac_lip_cnrdwn_L',
    'l_cnr_xPlus' : 'body_fac_lip_cnrout_L',
    'l_cnr_xMin' : 'body_fac_lip_cnrin_L',

    'r_cnr_yPlus' : 'body_fac_lip_cnrup_R',
    'r_cnr_yMin' : 'body_fac_lip_cnrdwn_R',
    'r_cnr_xPlus' : 'body_fac_lip_cnrout_R',
    'r_cnr_xMin' : 'body_fac_lip_cnrin_R',

    'upr_teeth_clench_mov_xPlus' : '',
    'lwr_teeth_clench_mov_xPlus' : '',
    'upr_teeth_clench_mov_xMin' : '',
    'lwr_teeth_clench_mov_xMin' : '',

    'l_lip_pinch_xPlus' : 'body_fac_lip_curl_L',
    'l_lip_pinch_xMin' : 'body_fac_lip_pinch_L',
    'r_lip_pinch_xPlus' : 'body_fac_lip_curl_R',
    'r_lip_pinch_xMin' : 'body_fac_lip_pinch_R',

    'mouthbnk_xPlus' : 'body_fac_mouth_bank_L',
    'mouthbnk_xMin' : 'body_fac_mouth_bank_R',

    'face_mouth_slide_fac_ctl_upLt' : '',
    'face_mouth_slide_fac_ctl_dnRt' : '',
    'face_mouth_slide_fac_ctl_upRt' : '',
    'face_mouth_slide_fac_ctl_dnLt' : '',

    'face_r_cnr_fac_ctl_upLt' : '',
    'face_r_cnr_fac_ctl_dnRt' : '',
    'face_r_cnr_fac_ctl_upRt' : '',
    'face_r_cnr_fac_ctl_dnLt' : '',

    'face_l_cnr_fac_ctl_upLt' : '',
    'face_l_cnr_fac_ctl_dnRt' : '',
    'face_l_cnr_fac_ctl_upRt' : '',
    'face_l_cnr_fac_ctl_dnLt' : ''
}
