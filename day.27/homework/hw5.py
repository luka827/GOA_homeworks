
# 1. ფუნქცია, რომელიც სტრინგს დააბრუნებს upper_case-ში
def to_upper(text):
    return text.upper()

# 4. ფუნქცია ორი არგუმენტით: ერთი upper, მეორე lower, და შეერთება
def format_and_combine(arg1, arg2):
    return arg1.upper() + arg2.lower()

# 2. მომხმარებლის სახელის შეყვანა და პირველი ასოს გამოყვანა upper_case-ში
name = input("შეიყვანე შენი სახელი: ")
first_letter = name[0].upper()
print("შენი სახელის პირველი ასო დიდი ასოთი:", first_letter)

# 3. წინადადება და სიტყვაზე ძებნა
sentence = input("შეიყვანე წინადადება: ")
word_to_find = input("რომელი სიტყვის მოძებნა გინდა ამ წინადადებაში? ")

if word_to_find in sentence:
    print(f"სიტყვა '{word_to_find}' მოიძებნა წინადადებაში ✅")
else:
    print(f"სიტყვა '{word_to_find}' არ მოიძებნა ❌")

# 1. მაგალითი ფუნქციის გამოყენებაზე (upper_case)
text = input("შეიყვანე ნებისმიერი ტექსტი, რომელიც გადაიქცევა დიდი ასოებად: ")
print("მიღებული ტექსტი დიდი ასოებით:", to_upper(text))

# 4. მაგალითი ფუნქციის გამოყენებაზე (format_and_combine)
arg1 = input("შეიყვანე პირველი სიტყვა (დაიპრინტება დიდი ასოებით): ")
arg2 = input("შეიყვანე მეორე სიტყვა (დაიპრინტება პატარა ასოებით): ")
combined = format_and_combine(arg1, arg2)
print("შედეგი:", combined)


print("Hello World".upper())
print("123abc".upper())
print("მოგესალმებით".upper())
print("test123".upper())


print("python" in "I love python")
print("Java" in "Python is awesome")
print("სიყვარული" in "სიყვარული ბედნიერებაა")
print("sun" in "rainy day")

