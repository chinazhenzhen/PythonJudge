# Judge-Demo参考文档  
### 版本与环境配置 
- python版本：Python 3.6.5  
- Linux版本：Ubuntu 18.04  
- GCC版本：gcc (Ubuntu 7.3.0-16ubuntu3) 7.3.0  
- G++版本：g++ (Ubuntu 7.3.0-16ubuntu3) 7.3.0  
- 需要的Python包：系统所使用的Python包，均保存在该目录的 requirements.txt 文件中，导入这些Python包， 执行 pip3 install -r  requirements.txt 即可。  
### 如何启动该程序
在环境配置好后，直接在judge_demo目录下，终端执行 python3 main.py 即可。  
### 简单介绍
- main.py ： 启动程序。主要是从数据库取数据，然后将取出来的每条数据进行分发,分发到work.py进行数据处理（多线程处理，生产者-消费者模式）。  
- compile.py : 编译。  
- judge.py : 判题。  
- work.py : 工作，调用编译函数和判题函数，将最后的结果写回到数据库中。  
- system.py : 里边只有一个MyConfig类（配置文件类）是有用的，

