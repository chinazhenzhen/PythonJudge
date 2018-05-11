import time
import subprocess
import psutil
import os

from system import MyConfig

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