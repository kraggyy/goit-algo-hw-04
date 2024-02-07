def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r') as fh:
            for line in fh:
                name, salary = line.strip().split(',')
                total += int(salary)
                count += 1
            average = total / count if count > 0 else 0
            return total, average
    except FileNotFoundError:
        print('File not found')
        return None, None
    except FileExistsError:
        print("File don`t exist")


if __name__ == "__main__":
    total, average = total_salary('./task1.txt')
    print(f"Total is {total}, avarage is {average}")