from selfdrive.car import dbc_dict

class CAR:
  CX5 = "Mazda CX-5 GT 2017"
  MAZDA3 = "Mazda 3 2019"
  CX30 = "Mazda CX-30"

FINGERPRINTS = {
  CAR.CX5: [{
    64: 8, 70: 8, 80: 8, 117: 8, 118: 8, 120: 8, 121: 8, 130: 8, 134: 8, 145: 8, 154: 8, 155: 8, 157: 8, 158: 8, 159: 8, 253: 8, 304: 8, 305: 8, 357: 8, 358: 8, 359: 8, 512: 8, 514: 8, 515: 8, 529: 8, 533: 8, 535: 8, 539: 8, 540: 8, 541: 8, 542: 8, 543: 8, 552: 8, 576: 8, 577: 8, 578: 8, 579: 8, 580: 8, 581: 8, 582: 8, 605: 8, 606: 8, 607: 8, 608: 8, 628: 8, 832: 8, 836: 8, 863: 8, 865: 8, 866: 8, 867: 8, 868: 8, 869: 8, 870: 8, 976: 8, 977: 8, 978: 8, 1034: 8, 1045: 8, 1056: 8, 1061: 8, 1067: 8, 1070: 8, 1078: 8, 1080: 8, 1085: 8, 1086: 8, 1088: 8, 1093: 8, 1108: 8, 1114: 8, 1115: 8, 1116: 8, 1139: 8, 1143: 8, 1147: 8, 1154: 8, 1157: 8, 1160: 8, 1163: 8, 1166: 8, 1177: 8, 1178: 8, 1179: 8, 1180: 8, 1183: 8, 1233: 8, 1236: 8, 1237: 8, 1238: 8, 1239: 8, 1241: 8, 1242: 8, 1243: 8, 1244: 8, 1264: 8, 1266: 8, 1267: 8, 1269: 8, 1270: 8, 1271: 8, 1272: 8, 1274: 8, 1275: 8, 1277: 8, 1278: 8, 1409: 8, 1416: 8, 1425: 8, 1430: 8, 1435: 8, 1440: 8, 1446: 8, 1456: 8, 1479: 8
  }],
  CAR.MAZDA3: [{
  16: 8, 17: 8, 18: 8, 20: 8, 21: 8, 22: 8, 24: 8, 26: 8, 28: 8, 29: 8, 31: 8, 32: 8, 33: 8, 35: 8, 37: 8, 41: 8, 43: 8, 44: 8, 49: 8, 50: 8, 51: 8, 54: 8, 55: 8, 56: 8, 59: 8, 72: 8, 80: 8, 96: 8, 128: 8, 129: 8, 145: 8, 176: 8, 256: 8, 257: 8, 258: 8, 259: 8, 260: 8, 261: 8, 262: 8, 263: 8, 264: 8, 265: 8, 266: 8, 267: 8, 272: 8, 273: 8, 274: 8, 275: 8, 276: 8, 277: 8, 278: 8, 279: 8, 280: 8, 281: 8, 282: 8, 283: 8, 288: 8, 289: 8, 290: 8, 291: 8, 292: 8, 293: 8, 294: 8, 295: 8, 296: 8, 297: 8, 298: 8, 299: 8, 304: 8, 305: 8, 306: 8, 307: 8, 308: 8, 310: 8, 320: 8, 321: 8, 322: 8, 323: 8, 324: 8, 325: 8, 328: 8, 329: 8, 336: 8, 337: 8, 338: 8, 339: 8, 340: 8, 341: 8, 342: 8, 343: 8, 344: 8, 345: 8, 346: 8, 347: 8, 352: 8, 354: 8, 355: 8, 356: 8, 357: 8, 358: 8, 1034: 8, 1035: 8, 1120: 8, 1184: 8, 1192: 8, 1193: 8, 1200: 8, 1209: 8, 1216: 8, 1436: 8, 1475: 8, 2015: 8
  }],
  CAR.CX30: [{
  16: 8, 17: 8, 18: 8, 20: 8, 21: 8, 22: 8, 24: 8, 26: 8, 28: 8, 29: 8, 31: 8, 32: 8, 33: 8, 35: 8, 37: 8, 41: 8, 43: 8, 44: 8, 49: 8, 50: 8, 51: 8, 54: 8, 55: 8, 56: 8, 59: 8, 72: 8, 80: 8, 96: 8, 128: 8, 129: 8, 145: 8, 176: 8, 256: 8, 257: 8, 258: 8, 259: 8, 260: 8, 261: 8, 262: 8, 263: 8, 264: 8, 265: 8, 266: 8, 267: 8, 272: 8, 273: 8, 274: 8, 275: 8, 276: 8, 277: 8, 278: 8, 279: 8, 280: 8, 281: 8, 282: 8, 283: 8, 288: 8, 289: 8, 290: 8, 291: 8, 292: 8, 293: 8, 294: 8, 295: 8, 296: 8, 297: 8, 298: 8, 299: 8, 304: 8, 305: 8, 306: 8, 307: 8, 308: 8, 310: 8, 320: 8, 321: 8, 322: 8, 323: 8, 324: 8, 325: 8, 328: 8, 329: 8, 336: 8, 337: 8, 338: 8, 339: 8, 340: 8, 341: 8, 342: 8, 343: 8, 344: 8, 345: 8, 346: 8, 347: 8, 352: 8, 354: 8, 355: 8, 356: 8, 357: 8, 358: 8, 896: 8, 897: 8, 898: 8, 899: 8, 900: 8, 901: 8, 902: 8, 903: 8, 944: 8, 960: 8, 976: 8, 977: 8, 978: 8, 979: 8, 980: 8, 1034: 8, 1035: 8, 1120: 8, 1128: 8, 1129: 8, 1184: 8, 1192: 8, 1193: 8, 1200: 8, 1209: 8, 1216: 8, 1224: 8, 1225: 8, 1421: 8, 1436: 8, 1475: 8, 1503: 8 
  }],
}

class ECU:
  CAM = 0

ECU_FINGERPRINT = {
  ECU.CAM: [579],   # steer torque cmd
}


DBC = {
  CAR.CX5: dbc_dict('mazda_cx5_gt_2017', None),
  CAR.MAZDA3: dbc_dict('mazda_3_2019', None),
  CAR.CX30: dbc_dict('mazda_3_2019', None),
}
