import os
import pymysql

from system import MyConfig
from compile import compile
from judge import time_mem

def work(i):
    db = pymysql.connect(host="127.0.0.1", user="root", password="12345678", db="oj", port=3306)
    try:
        problem_infor = {}
        cursor = db.cursor()
        #i = cursor.fetchone()
        # print(i) #debug
        problem_infor["run_id"] = i[0]  # 题目运行id
        problem_infor["code"] = i[9]  # debug代码，代码code
        problem_infor["id"] = i[1]  # 题目编号
        problem_infor["language"] = i[8]  # debug语言编号
        cursor.execute("select * from problem  where id = %d " % int(problem_infor["id"]))
        one = cursor.fetchone()

        # fin = open(MyConfig.ans_in_file, "w+")
        # fout = open(MyConfig.ans_out_file, "w+")
        # fin = one[11]
        # fout = one[12]
        # fin.close()
        # fout.close()

        language_code = problem_infor["language"]
        codepath = "./" + str(problem_infor["run_id"]) + MyConfig.code_file[language_code]
        # codepath = MyConfig.code_file[language_code]

        fcode = open(codepath, "w+")
        fcode.write(problem_infor["code"])
        fcode.close()

        if compile(MyConfig.language_code[language_code], codepath[2:], 'main' + str(problem_infor['run_id'])):

            ansinpath = MyConfig.ans_in_file + str(problem_infor["run_id"])
            ansoutpath = MyConfig.ans_out_file + str(problem_infor["run_id"])
            fin = open(ansinpath, "w+")
            fout = open(ansoutpath, "w+")
            fin.write(one[11])
            fout.write(one[12])
            fin.close()
            fout.close()
            judge_code = time_mem(MyConfig.language_code[language_code], ansinpath, ansoutpath,
                                  str(problem_infor["run_id"]))
            # print(judge_code)


        else:
            judge_code = {
                "result": 0,
                "time": -1,
                "memory": -1,
                "is_ac": "0"
            }
            judge_code["result"] = 8  # 编译错误
            # print("compile failed")
            # cursor.execute()
        # print(judge_code)# debug
        try:
            os.remove(codepath)
            os.remove('./main' + str(problem_infor['run_id']))
        except:
            pass

        cursor.execute(
            "update problem_status set result = %d,memory = %d,runtime = %d,code_len = %d where run_id = %d" % (
            int(judge_code["result"]), int(judge_code["memory"]), int(judge_code["time"]), len(problem_infor["code"]),
            int(problem_infor["run_id"])))
        print(judge_code)

    except:
        pass

    db.commit()
    cursor.close()
    db.close()
