# 软件工程作业03-结对项目

| Info |                         Detail                          |
|:----:|:-------------------------------------------------------:|
|  成员  |              3123004449(林奕宏) / 3122004018（麦凯翔）       | 
| 作业要求 | 🔗[作业要求链接](https://edu.cnblogs.com/campus/gdgy/SoftwareEngineeringClassof2023/homework/13326) |
| 仓库链接 | 🔗[Github仓库传送门](https://github.com/MikeMak123/Arithmetic-Generator) |

---

# 程序运行

## 用法
- 生成题目并保存到文件
```shell
python main.py -n <题目数量> -r <数值范围>
```
- 批改题目与答案
```shell
python main.py -e Exercises.txt -a Answers.txt
```


# PSP2.1

| PSP2.1                                    | Personal Software Process Stages                 | 预估耗时（分钟） | 实际耗时（分钟） |
|:------------------------------------------|:-------------------------------------------------|:----------------:|:----------------:|
| **Planning**                              | 计划                                             |                  |                  |
| · _Estimate_                              | 估计这个任务需要多少时间                           |       30       |       30       |
| **Development**                           | 开发                                             |                  |                  |
| · _Analysis_                              | 需求分析 (包括学习新技术)                         |       20       |       15       |
| · _Design Spec_                           | 生成设计文档                                     |       15       |       20       |
| · _Design Review_                         | 设计复审                                         |       10       |       10       |
| · _Coding Standard_                       | 代码规范 (为目前的开发制定合适的规范)               |       10       |        5       |
| · _Design_                                | 具体设计                                         |       20       |       25       |
| · _Coding_                                | 具体编码                                         |       40       |       35       |
| · _Code Review_                           | 代码复审                                         |       15       |       10       |
| · _Test_                                  | 测试（自我测试，修改代码，提交修改）               |       30       |       40       |
| **Reporting**                             | 报告                                             |                  |                  |
| · _Test Report_                           | 测试报告                                         |       15       |       15       |
| · _Size Measurement_                      | 计算工作量                                       |        5       |        5       |
| · _Postmortem & Process Improvement Plan_ | 事后总结, 并提出过程改进计划                      |       10       |       15       |
| **Total**                                 | 合计                                             |      220       |      225       |


---

# 程序流程

```shell

📦
│  Answers.txt     # 答案文件
│  calculator.py   # 计算结果
│  checker.py      # 判卷并生成成绩报告
│  Exercises.txt   # 四则运算练习文件
│  generator.py    # 四则运算生成
│  Grade.txt       # 成绩文件
│  main.py         # 程序入口
│  utils.py        # 处理分数的四则运算
│
├─UniTest # 单元测试
│      test_calculator.py 
│      test_checker.py
│      test_generator.py
│      test_main.py
│      test_utils.py



```

---

# 程序

```mermaid
graph TD
    A[启动程序] --> B[解析命令行参数]

    B -->|提供了 n 和 r| C[生成题目]
    C --> D[存入 Exercises.txt]
    C --> E[计算答案]
    E --> F[存入 Answers.txt]
    F --> G[打印生成成功消息]

    B -->|提供了 e 和 a| H[检查文件是否存在]
    H -->|文件存在| I[开始判卷]
    I --> J{判卷是否发生错误}
    J -- 是 --> K[打印错误信息]
    J -- 否 --> L[判卷成功]

    H -- 文件不存在 --> M[打印文件不存在错误]

    B -- 参数错误 --> N[打印帮助信息]
```


# 生成

```mermaid
graph TD
    A[开始生成题目] --> B[初始化 used_expressions]
    B --> C[循环生成表达式，直到满足数量]
    
    C -->|生成表达式| D[调用 generate_expression]
    D --> E[随机选择运算符并组合表达式]
    E --> F{是否符合规则?}
    
    F -- 否 --> G[跳过该表达式]
    F -- 是 --> H[检查是否重复]
    
    H -- 重复 --> I[跳过该表达式]
    H -- 唯一 --> J[加入 exercises 列表]

    J -->|达到数量限制?| K{结束生成?}
    K -- 否 --> C
    K -- 是 --> L[返回生成的题目列表]
```

# 判卷

```mermaid
graph TD
    A[开始判卷] --> B[读取题目文件和答案文件]

    B -->|文件不存在| C[打印错误信息] --> Z[结束]
    B -->|文件存在| D[检查题目和答案数量]

    D -->|数量不匹配| E[打印错误信息] --> Z
    D -->|匹配| F[初始化正确和错误列表]

    F --> G[遍历题目和答案]
    G --> H[计算题目答案]
    
    H -->|计算错误| I[加入错误列表]
    H -->|计算成功| J{答案是否匹配?}

    J -- 否 --> K[加入错误列表]
    J -- 是 --> L[加入正确列表]

    K --> M[继续遍历]
    L --> M

    M -->|遍历完成| N[生成成绩报告]
    N --> O[写入 Grade.txt]
    O --> P[打印判卷完成消息]
    P --> Z
```

# 计算

```mermaid
graph TD
    A[开始计算] --> B[接收表达式]
    B --> C[替换运算符（×、÷）为标准符号]
    C --> D[解析表达式树]
    D --> E[遍历树的每个节点]

    E --> F{节点类型?}
    F -- 二元运算符 --> G[计算左子树和右子树的值]
    G --> H[根据运算符（+ - × ÷）进行计算]
    H --> I[返回计算结果]

    F -- 数字节点 --> J[返回数字作为分数]

    E --> K{有除以零错误?}
    K -- 是 --> L[抛出 ZeroDivisionError]

    K -- 否 --> M[格式化计算结果为分数格式]

    M --> N[返回计算结果]
    N --> O[返回给 `calculate函数`]

    O --> P[完成计算]

    N --> Q[计算过程结束]
```
---

# 测试

![](./Assets/maintest.png)

![](./Assets/testchecker.png)

