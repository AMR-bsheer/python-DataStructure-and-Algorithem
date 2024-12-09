def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # نحدد العنصر الأوسط
        
        # إذا وجدنا العنصر
        if arr[mid] == target:
            return mid
        
        # إذا كان العنصر في النصف الأيسر
        elif arr[mid] > target:
            right = mid - 1
        
        # إذا كان العنصر في النصف الأيمن
        else:
            left = mid + 1
    
    # إذا لم يتم العثور على العنصر
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"العنصر موجود في الفهرس {result}")
else:
    print("العنصر غير موجود في القائمة")
