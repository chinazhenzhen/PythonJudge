import time
import subprocess
import psutil
import os
import pymysql


# pymysql.install_as_MySQLdb()

class MyConfig():
    """
    配置文件
    """
    dir_work = "./"

    ans_in_file = "./ansin"

    ans_out_file = "./ansout"
    user_out_file = "./user.out"

    code_file = {
        1: ".cpp",
        2: ".c",
    }


    language_code = {
        1: "g++",
        2: "gcc",
    }
    code_state = {
        1: "accept",
        2: "Presentation Error",
        3: "Wrong Answer",
        4: "Runtime Error",
        5: "Time Limit Exceeded",
        6: "Memery Limit Exceeded",
        8: "compile Error",

    }


def db():
    db = pymysql.connect(host="127.0.0.1", user="root", password="12345678", db="oj", port=3306)

    while True:
        cursor = db.cursor()
        time.sleep(0.5)
        cursor.execute("select * from problem_status  WHERE result = 0")

        problem_infor = {}
        try:
            i = cursor.fetchone()
            # print(i) #debug
            problem_infor["run_id"] = i[0]  #题目运行id
            problem_infor["code"] = i[9]  # debug代码，代码code
            problem_infor["id"] = i[1]  # 题目编号
            problem_infor["language"] = i[8]  # debug语言编号
            cursor.execute("select * from problem  where id = %d " % int(problem_infor["id"]))
            one = cursor.fetchone()

            #fin = open(MyConfig.ans_in_file, "w+")
            #fout = open(MyConfig.ans_out_file, "w+")
            #fin = one[11]
            #fout = one[12]
            #fin.close()
            #fout.close()
            language_code = problem_infor["language"]
            codepath = "./"+str(problem_infor["run_id"])+MyConfig.code_file[language_code]
            #codepath = MyConfig.code_file[language_code]

            fcode = open(codepath, "w+")
            fcode.write(problem_infor["code"])
            fcode.close()


            if compile(MyConfig.language_code[language_code],codepath[2:],'main'+str(problem_infor['run_id'])):

                ansinpath = MyConfig.ans_in_file+str(problem_infor["run_id"])
                ansoutpath = MyConfig.ans_out_file+str(problem_infor["run_id"])
                fin = open(ansinpath, "w+")
                fout = open(ansoutpath, "w+")
                fin.write(one[11])
                fout.write(one[12])
                fin.close()
                fout.close()
                judge_code = time_mem(MyConfig.language_code[language_code],ansinpath,ansoutpath,str(problem_infor["run_id"]))
                # print(judge_code)


            else:
                judge_code = {
                "result":0,
                "time":-1,
                "memory":-1,
                "is_ac":"0"
                }
                judge_code["result"] = 8 #编译错误
                # print("compile failed")
                # cursor.execute()
            #print(judge_code)# debug
            try:
                os.remove(codepath)
                os.remove('./main'+str(problem_infor['run_id']))
            except:
                pass

            cursor.execute( "update problem_status set result = %d,memory = %d,runtime = %d,code_len = %d where run_id = %d"%(int(judge_code["result"]),int(judge_code["memory"]),int(judge_code["time"]),len(problem_infor["code"]),int(problem_infor["run_id"])))
            print(judge_code)

        except :
            pass

        db.commit()#事务的更新
        cursor.close()
        db.close()


def compile(language,codepath,id):
    build_cmd = {
        "gcc": "gcc {} -o {} -Wall -lm -O2 -std=c99 --static -DONLINE_JUDGE".format(codepath,id),
        "g++": "g++ {} -O2 -Wall -lm --static -DONLINE_JUDGE -o {}".format(codepath,id),
        # "java": "javac Main.java",
        # "ruby": "ruby -c main.rb",
        # "perl": "perl -c main.pl",
        # "pascal": 'fpc main.pas -O2 -Co -Ct -Ci',
        # "go": '/opt/golang/bin/go build -ldflags "-s -w"  main.go',
        # "lua": 'luac -o main main.lua',
        # "python2": 'python2 -m py_compile main.py',
        # "python3": 'python3 -m py_compile main.py',
        # "haskell": "ghc -o main main.hs",
    }
    p = subprocess.Popen(build_cmd[language], shell=True, cwd=MyConfig.dir_work, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)  # cwd设置工作目录
    out, err = p.communicate()  # 获取编译错误信息
    if p.returncode == 0:  # 返回值为0,编译成功
        return True
    # update_compile_info(solution_id,err+out) #编译失败，更新题目编译错误信息
    print(err, out)
    return False


def judge_result(fout,uout):
    '''对输出数据进行评测'''
    currect_result = fout
    user_result = uout
    try:
        curr = currect_result.replace('\r', '').rstrip()  # 删除\r,删除行末的空格和换行
        # print(curr) #debug
        user = user_result.replace('\r', '').rstrip()  # python2中使用file函数
        # print(user) #debug
    except:
        return False
    if curr == user:  # 完全相同:AC
        return 1
    if curr.split() == user.split():  # 除去空格,tab,换行相同:PE
        return 2
    if curr in user:  # 输出多了
        return 1  # 这个地方有问题
    return 3  # 其他WA


def time_mem(language,ansinpath,ansoutpath,id):
    """
    执行程序获取执行时间与内存
    """

    fin = open(ansinpath, "r+")
    useroutpath = ansoutpath+"user"
    fout = open(useroutpath, "w+")

    p_cmd = {  # 运行程序的命令,这里以C++、C语言为例
        "gcc": "./main"+str(id),
        "g++": "./main"+str(id),
    }

    time_limit = 1  # second
    mem_limit = 128 * 1024  # kb
    max_rss = 0
    problem_info = {}  # 时间单位ms 内存单位kb
    problem_info["is_ac"] = 0;
    p = subprocess.Popen(p_cmd[language], shell=True, cwd=MyConfig.dir_work, stdin=fin, stdout=fout,
                         stderr=subprocess.PIPE)  # cwd设置工作目录
    start = time.time()  # 开始时间
    # print("程序开始运行的时间是%s" % start)
    pid = p.pid
    glan = psutil.Process(pid)  # 监听控制进程

    while True:
        time_now = time.time() - start  # ??
        if psutil.pid_exists(pid) is False:  # 运行错误
            problem_info['time'] = time_now * 1000
            problem_info['memory'] = max_rss / 1024.0
            problem_info['result'] = 8
            return problem_info
        m_infor = glan.memory_info()
        # print(m_infor) #debug
        rss = m_infor[0]  # 获取程序占用内存空间 rss
        if p.poll() == 0:  # 运行正常结束，跳出循环，继续判断
            end = time.time()
            break
        if max_rss < rss:
            max_rss = rss
            # print("max_rss=%s" % max_rss)  #debug
        if time_now > time_limit:  # 时间超限
            problem_info['time'] = time_now * 1000
            problem_info['memory'] = max_rss / 1024.0
            problem_info['result'] = 5
            glan.terminate()
            return problem_info
        if max_rss > mem_limit:  # 内存超限
            problem_info['time'] = time_now * 1000
            problem_info['memory'] = max_rss / 1024.0
            problem_info['result'] = 6

    problem_info['time'] = time_now * 1000
    problem_info['memory'] = max_rss / 1024.0

    currect_result = os.path.join(ansoutpath)
    user_result = os.path.join(useroutpath)
    uout = open(user_result).read()
    fout = open(currect_result).read()

    os.remove(useroutpath)
    os.remove(ansoutpath)
    os.remove(ansinpath)
    #os.remove('./' + str(id) + '.out')

    problem_info['result'] = judge_result(fout,uout)
    if problem_info['result'] == 1:
        problem_info['is_ac'] = 1
    return problem_info


if __name__ == '__main__':
    '''language = input("输入编译环境")
    if compile(language):
        judge_code = time_mem(language)
        print(judge_code)
    else:
        print("compile failed")'''

    db()
