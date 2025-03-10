import argparse
from generator import generate_exercises
from calculator import calculate
from checker import check_answers

def main():
    parser = argparse.ArgumentParser(description="Arithmetic Exercise Generator")
    parser.add_argument('-n', type=int, help="Number of exercises to generate")
    parser.add_argument('-r', type=int, help="Range of numbers (mandatory for generation)")
    parser.add_argument('-e', type=str, help="Exercise file for grading")
    parser.add_argument('-a', type=str, help="Answer file for grading")
    args = parser.parse_args()

    if args.n is not None:
        if args.r is None:
            parser.error("The -r parameter is required when using -n")
        exercises = generate_exercises(args.n, args.r)
        with open('Exercises.txt', 'w') as ef, open('Answers.txt', 'w') as af:
            for i, expr in enumerate(exercises, 1):
                ef.write(f"{i}. {expr}\n")
                ans = calculate(expr)
                af.write(f"{i}. {ans}\n")
    elif args.e and args.a:
        check_answers(args.e, args.a)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()