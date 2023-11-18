my_list = [2, 6, 12, 5, 67, 8, 83, 2, 322, 5, 4, 73, 3, 22]
# my_list_1 = [2, 8, 12, 5, 4, 72]

# Nhập mảng từ bàn phím
# my_list = [int(x) for x in input("Nhập các phần tử của mảng, cách nhau bởi dấu cách: ").split()]

# def merge_arrays(arr1, arr2):
#     merged_array = arr1 + arr2
#     return merged_array

# Nhập chỉ mục i từ bàn phím
i = int(input("Nhập phần tử thứ i: "))

# Kiểm tra xem chỉ mục có hợp lệ không
if 0 <= i - 1 < len(my_list):
    # Tìm phần tử thứ i
    element_i = my_list[i - 1]
    print(f"Phần tử thứ {i} trong mảng là: {element_i}")
else:
    print("Nhập i không hợp lệ.")

# Hàm tìm phần tử trung bình
def find_average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Hàm in độ dài của danh sách
def find_length(numbers):
    return len(numbers)

# Hàm in ra các số chẵn
def find_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

# Hàm in ra các số lẻ
def find_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

# Hàm sắp xếp tăng dần
def sort_ascending(numbers):
    return sorted(numbers)

# Hàm sắp xếp giảm dần
def sort_descending(numbers):
    return sorted(numbers, reverse=True)

# Tìm số lớn nhất và số nhỏ nhất
max_number = max(my_list)
min_number = min(my_list)

def add_element(arr):
    element = int(input("Nhập phần tử để thêm vào mảng: "))
    arr.append(element)
    print(f"Phần tử {element} đã được thêm vào mảng.\n")
    return arr

def remove_element(arr):
    n = int(input("Nhập vị trí cần xóa : "))
    
    if 1 <= n <= len(arr):
        removed_element = arr.pop(n - 1)
        print(f"Phần tử {removed_element} đã được xóa khỏi mảng. ")
    else:
        print("Số nhập không hợp lệ. Không có phần tử nào bị xóa.")
        
    return arr

#  Gộp hai mảng
# result_array = merge_arrays(my_list, my_list_1)

# In kết quả
# print("Mảng sau khi gộp:", result_array)


average = find_average(my_list)
length = find_length(my_list)
even_numbers = find_even_numbers(my_list)
odd_numbers = find_odd_numbers(my_list)
ascending_order = sort_ascending(my_list)
descending_order = sort_descending(my_list)


# Thêm phần tử mới
my_list = add_element(my_list)
print("Mảng sau khi thêm phần tử:", my_list,"\n")

# Xóa phần tử thứ n
my_list = remove_element(my_list)
print("Mảng sau khi xử lí:", my_list,"\n")

print("Số lớn nhất:", max_number)
print("Số nhỏ nhất:", min_number)
print("Phần tử trung bình:", average)
print("Độ dài của danh sách:", length)
print("Các số chẵn:", even_numbers)
print("Các số lẻ:", odd_numbers)
print("Sắp xếp tăng dần:", ascending_order)
print("Sắp xếp giảm dần:", descending_order)
