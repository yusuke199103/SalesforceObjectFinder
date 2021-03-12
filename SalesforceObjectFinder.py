# coding: cp932
import sys
import codecs
import os
import re

def searchInfo():
    regexObj = re.compile(r"<[^>]*?>")
    searchPath = "C:\\PATH"
    fileArray = os.listdir(searchPath)
    objCounter = 1
    for fileItem in fileArray:
        tempObjName = ''
        descriptionStr = ''
        ObjNamelabelFromFlag = False
        fieldObjName = ''
        fieldAPIName = ''
        fieldTypeName = ''
        fieldFullNameFlag = False
        fieldLabelFlag = False
        fieldTypeFlag = False
        endFieldFlag = False
        fieldsFlag = False
        EndFlag = False
        prevLines = None
        fieldsCount = 0
        with codecs.open(searchPath + "\\" + fileItem, "r", encoding="utf_8") as fsDiskliptObj:
            for luneNum, lineObj in enumerate(fsDiskliptObj):
                if "<description>" in lineObj and "</description>" in lineObj and fieldsFlag == False:
                    descriptionStr = regexObj.sub("", lineObj.strip())
                if "<fields>" in lineObj:
                    fieldsFlag = True
                    fieldsCount += 1
                if "<fullName>" in lineObj and "</fullName>" in lineObj and fieldsFlag and not ObjNamelabelFromFlag:
                    fieldAPIName = fieldAPIName + '/' + regexObj.sub("", lineObj.strip())
                    fieldFullNameFlag = True
                if "<label>" in lineObj and "</label>" in lineObj and fieldsFlag and not ObjNamelabelFromFlag:
                    fieldObjName = fieldObjName + '/' + regexObj.sub("", lineObj.strip())
                    fieldLabelFlag = True
                if "<type>" in lineObj and "</type>" in lineObj and fieldsFlag and not ObjNamelabelFromFlag:
                    fieldTypeName = fieldTypeName + '/' + regexObj.sub("", lineObj.strip())
                    fieldTypeFlag = True
                if "</fields>" in lineObj:
                    fieldsFlag = False
                    endFieldFlag = True
                if "<label>" in lineObj and "</label>" in lineObj and not fieldsFlag and not ObjNamelabelFromFlag:
                    tempObjName = regexObj.sub("", lineObj.strip())
                    ObjNamelabelFromFlag = True
                if "</CustomObject>" in lineObj:
                    EndFlag = True
                if tempObjName != '' and EndFlag:
                    print("�ʔԁF" + str(objCounter))
                    print("�J�X�^���I�u�W�F�N�gAPI���F" + fileItem.replace('.object', ''))
                    print("�J�X�^���I�u�W�F�N�g���́F" + tempObjName)
                    print("�J�X�^���I�u�W�F�N�g�����F" + descriptionStr)
                    print("���ڃt�B�[���h���x�����́F" + fieldObjName)
                    print("���ڃt�B�[���hAPI���́F" + fieldAPIName)
                    print("���ڃt�B�[���h�^�C�v���́F" + fieldTypeName)
                    print("���ڃt�B�[���h���F" + str(fieldsCount))
                    print('')
                    fieldAPIName = ''
                    fieldObjName = ''
                    tempObjName = ''
                    fieldsFlag = False
                    ObjNamelabelFromFlag = False
                    fieldFullNameFlag = False
                    fieldLabelFlag = False
                    fieldTypeFlag = False
                    objCounter += 1

if __name__ == '__main__':  #���C���֐�
    reload(sys)
    sys.setdefaultencoding('cp932')
    searchInfo()
