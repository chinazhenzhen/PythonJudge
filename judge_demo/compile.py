import subprocess
from system import MyConfig

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