
class ModifyPara():

    def modify_para_file(self, Para_list, name, new_num):
        self.success = False
        self.Para_list = Para_list
        try:
            print("更新資料")
            self.name = name
            self.new_num = new_num

            for i in range(len(self.Para_list)):
                if self.name == str(self.Para_list[i][0]):
                    self.Para_list[i][1] = self.new_num
                    self.success = True
            
        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            self.success = False
            print(self.new_num)
        else:                       
            print(self.name)
            
        finally:                    #不管try有沒有錯誤，最後一定會執行final
            #print(student_list)
            if(self.success == True):
                print("修改成功，{}分數變為{}".format(self.name, self.new_num))
            else:
                print("修改失敗")

            print("Execution result is {}".format(self.success))
            return self.Para_list, self.success
    """
    student_list = [["dog",30],["cat",80]]
    main(student_list)
    """
