class JudgeConfig():
    """
    配置文件
    """

    dir_work = "./"
    ans_in_file = "./ans.in"
    ans_out_file = "./ans.out"
    user_out_file = "./user.out"

    codefile_id = {
        1: "./main.cpp",
        2: "./main.c",
    }

    language_id = {
        1: "C++",
        2: "C",
    }
    result_id = {
        "pending":0,
        "accept":1,
        "Presentation Error":2,
        "Wrong Answer":3,
        "Runtime Error":4,
        "Time Limit Exceeded":5,
        "Memery Limit Exceeded":6,
        "compile Error":8,
    }
    show_result = {
        0:"pending",
        1: "accept",
        2: "Presentation Error",
        3: "Wrong Answer",
        4: "Runtime Error",
        5: "Time Limit Exceeded",
        6: "Memery Limit Exceeded",
        8: "compile Error",
    }