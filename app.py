total_amount = int(input('合計金額を教えてね(円):'))
number_of_people = int(input('人数を教えてね(人):'))

print(total_amount)
print(number_of_people)

print(f"{total_amount // number_of_people}円, 端数:{total_amount % number_of_people}")
