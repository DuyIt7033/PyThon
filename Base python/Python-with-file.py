# Tên file văn bản
file_name = "duy_test_file.txt"

def read_first_n_lines(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [file.readline().strip() for _ in range(n)]
    return lines

# def append_string_to_file(file_path, string_to_append):
#     with open(file_path, 'a', encoding='utf-8') as file:
#         file.write(string_to_append)

def count_lines_and_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        lines = content.split('\n')
        words = content.split()
    return len(lines), len(words)

def read_last_n_lines(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[-n:]
    return lines

# def word_frequency(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         words = content.split()
#         word_count = {}
#         for word in words:
#             word_count[word] = word_count.get(word, 0) + 1
#     return word_count


# Đếm số dòng và số từ trong tập tin
line_count, word_count = count_lines_and_words(file_name)
print(f"\nSố dòng trong file: {line_count}")
print(f"Số từ trong file: {word_count}\n\n")


# Đọc n dòng đầu tiên
n_fisrt = 4
first_n_lines = read_first_n_lines(file_name, n_fisrt)
print(f"\n{n_fisrt} dòng đầu tiên trong file:\n")
print("\n".join(first_n_lines))


#  Nối chuỗi vào cuối tập tin
# string_to_append = "\nChuỗi được nối vào cuối file."
# append_string_to_file(file_name, string_to_append)


# Đọc n dòng cuối cùng
n_last = 5
last_n_lines = read_last_n_lines(file_name, n_last)
print(f"\n{n_last} dòng đầu cuối trong file:\n")
print("".join(last_n_lines))

# Tính tần số xuất hiện của từ trong tập tin
# word_frequency_dict = word_frequency(file_name)
# print("\nTần số xuất hiện của từ trong file:")
# for word, frequency in word_frequency_dict.items():
#     print(f"{word}: {frequency} lần")


# Nhập dòng bắt đầu và dòng kết thúc từ bàn phím
def print_lines_range(file_path, start_line, end_line):
    try:
        start_line = int(start_line)
        end_line = int(end_line)
    except ValueError:
        print("Vui lòng nhập số nguyên cho dòng bắt đầu và dòng kết thúc.")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        all_lines = file.readlines()
        total_lines = len(all_lines)

        if 1 <= start_line <= total_lines and 1 <= end_line <= total_lines:
            lines_to_print = all_lines[start_line - 1:end_line]
            for line_number, line in enumerate(lines_to_print, start=start_line):
                print(f" {line_number}: {line.strip()}")
        else:
            print("Dòng bắt đầu hoặc dòng kết thúc không hợp lệ.")
            print("Nhập lại !")
            

def get_valid_input(prompt, error_message, max_value):
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            if 1 <= value <= max_value:
                return value
            else:
                print(f"Vui lòng nhập một giá trị từ 1 đến {max_value}.")
        except ValueError:
            print(error_message)

def main():
    show = input("Bạn có muốn xem thêm nội dung ? \n(Nhập 'yes' hoặc 'no'): ")
    if show.lower() == 'yes':
        # Tên file văn bản
        file_name = "duy_test_file.txt"

        # Đọc số dòng trong file
        with open(file_name, 'r', encoding='utf-8') as file:
            total_lines = len(file.readlines())

        start_line_input = get_valid_input("Nhập dòng bắt đầu: ", "Vui lòng nhập số nguyên cho dòng bắt đầu.", total_lines)
        end_line_input = get_valid_input("Nhập dòng kết thúc: ", "Vui lòng nhập số nguyên cho dòng kết thúc.", total_lines)

        # In các dòng từ a đến b
        print("\n\n")
        print_lines_range(file_name, start_line_input, end_line_input)

if __name__ == "__main__":
    main()
