import pickle
class ParaTxtProcess():
    """def __init__(self):
        # Nothing to init
"""
    def read_para_file(self):
        self.Para_list = list()
        try:
            with open("main.txt", "r",encoding="utf-8") as fp:
                for line in fp:
                    if len(line) > 0:
                        line = line.rstrip("\n").split("=")
                        self.Para_list.append([line[0], float(line[1])])

        except IOError:
            print('An error occured trying to read the file.')

        return self.Para_list

    def restore_para_file(self, Para_list):
        restore_student = ""
        self.Para_list = Para_list
        try:
            for i in range(len(self.Para_list)):
                restore_student = restore_student + str(self.Para_list[i][0]) + "=" + str(self.Para_list[i][1]) + "\n"

            with open('./main.txt', 'w', encoding="utf-8") as f:
                f.write(restore_student)
                restore_success = True
                #To append data to a file use the 'a' or 'a+' mode 

        except Exception as e:      #若try有錯誤，則執行except
            print("The exception {} occurs.".format(e))
            restore_success = False

        finally:                    #不管try有沒有錯誤，最後一定會執行final
            if(restore_success == True):
                print("存檔成功")
            else:
                print("存檔失敗")
        print("Execution result is {}".format(restore_success))
        return self.Para_list
        