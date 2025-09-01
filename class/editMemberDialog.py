from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os
import sys
import json
import EditMemberDialog_UI

# set current user ID
userID = os.popen("logname").read().strip()


# 회의실용
if userID == "conf3":
    userID = "sungoh.moon"


currentPath = os.path.dirname(os.path.abspath(__file__))

# import json file
teamInfo_json = []
jsonFilePath = os.path.dirname(currentPath) + "/.team_Info"
jsonFile = os.path.join(jsonFilePath, userID+"_teamInfo.json")


NameInfoJson_path = os.path.dirname(currentPath) + "/.user_Info"
NameInfoJson = os.path.join(NameInfoJson_path, "user_name_info.json")


#if (os.path.exists(jsonFile)):
#    with open(jsonFile) as f:
#        teamInfo_json = json.load(f)

    #for member in teamInfo_json:
    #    teamMember.append(member["name"])



class EditMemberDialog(QDialog):
    def __init__(self):
        super(EditMemberDialog, self).__init__()
        
        self.getJsonData()

        self.ui = EditMemberDialog_UI.Ui_teamEdit_frm()
        self.ui.setupUi(self)

        self.model = QStringListModel()

        parts = ["MMV", "RIG", "ANI"]
        self.ui.part_comboBox.addItems(parts)

        self.ui.part_comboBox.setStyleSheet("QComboBox { font-size: 14px;}")


        self.getMemberInfo()

        #self.model.setStringList(teamInfo_json)
        self.ui.member_listView.setModel(self.model)


        self.ui.add_btn.clicked.connect(self.addMember)
        #self.ui.rename_btn.clicked.connect(self.renameMember)
        self.ui.remove_btn.clicked.connect(self.removeMember)
        self.ui.apply_btn.clicked.connect(self.updateJson)




    def getJsonData(self):

        global teamInfo_json
        if (os.path.exists(jsonFile)):
            with open(jsonFile) as f:
                teamInfo_json = json.load(f)




    # Retrieve member list from JSON Data
    def getMemberInfo(self):
        
        if teamInfo_json != []:
            listMember = []
            memberList = list(teamInfo_json[0].keys())

            """
            for member in memberList:
                listMember.append(member)                

            self.model.setStringList(listMember)                
            """

            for member in memberList:
                #listMember.append(member)                
                userInfo = getUserInfo(member)
                item = userInfo[0] + " / " + member + " / " + userInfo[4]
                listMember.append(item)                

            self.model.setStringList(listMember)                







    def exportJson(self, exportJson):

        try:
            with open(jsonFile, 'w') as file:
                json.dump(exportJson, file, indent=4)
            return True                

        except Exception as e:
            print (f"Error saving to file: {e} ")
            return False





    def updateJson(self):

        memberInfo = {}
        teamInfo_json = [memberInfo]
        #listNameEn = self.model.stringList()

        listUserInfo = self.model.stringList()

        listNameEn = []
        for user in listUserInfo:
            nameEN = user.split(" / ")[1]
            listNameEn.append(nameEN)

        for name in listNameEn:
            if name != userID:
                memberData = {}

                nameKr, role, team, job, department = getUserInfo(name)

                memberData["nameKr"] = nameKr
                memberData["role"] = role
                memberData["team"] = team
                memberData["job"] = job
                memberData["department"] = department

                memberInfo[name] = memberData


        self.exportJson(teamInfo_json)  
        self.close()





            
    '''
    def renameMember(self):

        sel_index = self.ui.member_listView.selectedIndexes()
        if sel_index:

            if sel_index[0].isValid():
                selMember = self.model.data(sel_index[0])

                new_name, ok = QInputDialog.getText(self, "Rename name", "Enter new Name:", QLineEdit.Normal, selMember)

                if ok:

                    if getUserInfo(new_name) != False:
                        index = sel_index[0]
                        self.model.setData(index, new_name)

                    else:
                        QMessageBox.critical(self, "Error", "\""+new_name+"\"\n" +"이 이름의 팀원이 존재하지 않습니다")

            #self.updateJson()                
    '''



    def removeMember(self):

        sel_index = self.ui.member_listView.selectedIndexes()

        if sel_index[0].isValid():
            removeName = self.model.data(sel_index[0]).split(" / ")[1]

            index = sel_index[0]
            self.model.removeRow(index.row())

            if removeName in teamInfo_json[0]:
                del teamInfo_json[0][removeName]









    def addMember(self):

        if os.path.exists(NameInfoJson):
            with open(NameInfoJson) as f:
                memberNameInfo = json.load(f)


        sel_part = self.ui.part_comboBox.currentText()

        member = self.ui.addLineEdit.text()
        

        if member!="" and member in memberNameInfo[sel_part]:
            newMember = memberNameInfo[sel_part][member]

            if newMember:
                self.getMember_ENname(newMember, sel_part)

        else:
            QMessageBox.critical(self, "Error", "\""+member+"\"\n" +"이 이름의 팀원이 " + sel_part + "파트에 존재하지 않습니다")

        #else:
        #    self.getMember_ENname(member, sel_part)            




        """
        if newMember and newMember != userID:
            if newMember in self.model.stringList():
                QMessageBox.warning(self, "Warning", "Member Name already exists")

            elif getUserInfo(newMember) == False:
                QMessageBox.critical(self, "Error", "\""+newMember+"\"\n" +"이 이름의 팀원이 존재하지 않습니다")

            else:
                self.model.insertRow(self.model.rowCount())
                index = self.model.index(self.model.rowCount() - 1)
                self.model.setData(index, newMember)
                self.ui.addLineEdit.clear()
        """


    def getMember_ENname(self, memberName, part):

        if memberName and memberName != userID:

            userInfo = getUserInfo(memberName)

            if userInfo:
                addItem = userInfo[0] + " / " + memberName + " / " + part

                #if memberName in self.model.stringList():
                if addItem in self.model.stringList():
                    QMessageBox.warning(self, "Warning", "Member Name already exists")

                elif getUserInfo(memberName) == False:
                    QMessageBox.critical(self, "Error", "\""+memberName+"\"\n" +"이 이름의 팀원이 " + part + "파트에 존재하지 않습니다")

                else:
                    self.model.insertRow(self.model.rowCount())
                    index = self.model.index(self.model.rowCount() - 1)
                    self.model.setData(index, addItem)
                    self.ui.addLineEdit.clear()




        """
        newMember = self.ui.addLineEdit.text()

        #if newMember and newMember in memberNameInfo[sel_part]:
            #newMember = memberNameInfo[sel_part][new]


        if newMember and newMember != userID:
            if newMember in self.model.stringList():
                QMessageBox.warning(self, "Warning", "Member Name already exists")

            elif getUserInfo(newMember) == False:
                QMessageBox.critical(self, "Error", "\""+newMember+"\"\n" +"이 이름의 팀원이 존재하지 않습니다")

            else:
                self.model.insertRow(self.model.rowCount())
                index = self.model.index(self.model.rowCount() - 1)
                self.model.setData(index, newMember)
                self.ui.addLineEdit.clear()
        """




def getUserInfo(user):
    import dxConfig
    import requests
    import json


    API_KEY = "c70181f2b648fdc2102714e8b5cb344d"
    requestParam = {}
    requestParam['api_key'] = API_KEY
    requestParam['code'] = user
    
    infos = requests.get("http://%s/dexter/search/user.php" %(dxConfig.getConf('TACTIC_IP')), params=requestParam).json()

    try:
        unicodeName = infos["name_kr"]
        role = infos["role"]
        department = infos["department"]
        job = infos["job_title"]
        department_short = infos["department_short"]

        return unicodeName, role, department, job, department_short


    except Exception as e:
            QMessageBox.critical(None, "에러", f"{user}와 같은 영문이름이 존재하지 않습니다.")
            #print (f"error: {user} 존재하지 않는 이름입니다.")
            return False






