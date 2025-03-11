import argparse
import sys
import os
from generator import generate_exercises
from calculator import calculate
from checker import check_answers

def main():
    parser = argparse.ArgumentParser(description="四则运算题目生成器")
    parser.add_argument('-n', type=int, help="生成题目数量")
    parser.add_argument('-r', type=int, help="数值范围（必填）")
    parser.add_argument('-e', type=str, help="判卷的题目文件")
    parser.add_argument('-a', type=str, help="判卷的答案文件")
    args = parser.parse_args()


    if args.n is not None:
        if args.r is None:
            parser.error("使用 -n 时必须提供 -r 参数")
        exercises = generate_exercises(args.n, args.r)

        with open('Exercises.txt', 'w') as ef, open('Answers.txt', 'w') as af:
            for expr in exercises:
                ef.write(expr + '\n')  # 题目存入 Exercises.txt
                answer = calculate(expr)
                af.write(answer + '\n')  # 答案存入 Answers.txt

        print(f"✅ {args.n} 道题目已生成，并存入 Exercises.txt 和 Answers.txt")

    elif args.e and args.a:
        if not os.path.exists(args.e):
            print(f"❌ 错误：题目文件 {args.e} 不存在！")
            return
        if not os.path.exists(args.a):
            print(f"❌ 错误：答案文件 {args.a} 不存在！")
            return

        print(f"📌 开始判卷，题目文件：{args.e}，答案文件：{args.a}")
        
        try:
            check_answers(args.e, args.a)
        except Exception as e:
            print(f"❌ 判卷时发生错误: {e}")

    else:
        parser.print_help()

    # if args.n and args.r:
    #     if args.n <= 0 or args.r <= 0:
    #         print("Error: Invalid n or r value. n and r must be positive integers.", file=sys.stderr)
    #         sys.exit(1)
    #     try:
    #         generate_exercises(args.n, args.r)
    #     except Exception as e:
    #         print(f"An error occurred during exercise generation: {e}", file=sys.stderr)
    #         sys.exit(1)
    # elif args.e and args.a:
    #     try:
    #         check_answers(args.e, args.a)
    #     except FileNotFoundError:
    #         print(f"Error: One or both of the files do not exist.", file=sys.stderr)
    #         sys.exit(1)
    #     except Exception as e:
    #         print(f"An error occurred during grading: {e}", file=sys.stderr)
    #         sys.exit(1)
    # else:
    #     parser.print_help()
    #     sys.exit(1)

if __name__ == "__main__":
    main()