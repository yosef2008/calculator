# مرحبًا بك في تطبيق الآلة الحاسبة
print("مرحبًا بك في تطبيق الآلة  الحاسبة من تطوير يوسف")

# عرض الخيارات للمستخدم
print("1. جمع (+)")
print("2. طرح (-)")
print("3. ضرب (*)")
print("4. قسمة (/)")

# طلب اختيار المستخدم
choice = input("اختر العملية التي تريدها (1/2/3/4): ")

# طلب إدخال الرقمين
num1 = float(input("أدخل الرقم الأول: "))
num2 = float(input("أدخل الرقم الثاني: "))

# تنفيذ العملية بناءً على اختيار المستخدم
if choice == '1':
    print("النتيجة:", num1 + num2)
elif choice == '2':
    print("النتيجة:", num1 - num2)
elif choice == '3':
    print("النتيجة:", num1 * num2)
elif choice == '4':
    if num2 != 0:  # التأكد من أن القاسم ليس صفرًا
        print("النتيجة:", num1 / num2)
    else:
        print("خطأ: لا يمكن القسمة على صفر!")
else:
    print("خيار غير صالح!")