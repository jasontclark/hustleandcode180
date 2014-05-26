def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def list_of_numbers(first, second, third):
    print "Your first number is: %d" % first
    print "Your second number is: %d" % second
    print "Your third number is: %d" % third
    
print("First attempt:")
list_of_numbers(10, 20, 30)

print("Second attempt:")
list_of_numbers(10 + 5, 20 + 5, 30 + 5)

print("Third attempt:")

first_num  = 100
second_num = 200
third_num  = 300
list_of_numbers(first_num, second_num, third_num)

print("Fourth Attempt:")
list_of_numbers(first_num * 2, second_num, third_num)

print("Fifth Attempt:")
list_of_numbers(first_num, second_num * 2, third_num)

print("Sixth Attempt:")
list_of_numbers(first_num, second_num, third_num * 2)

print("Seventh Attempt:")
list_of_numbers(first_num + second_num, second_num, third_num)

print("Eight Attempt:")
list_of_numbers(first_num, 45, third_num)

print("Ninth Attempt:")
list_of_numbers(third_num / 5, first_num + 5, second_num * 3)

print("Tenth Attempt:")
list_of_numbers(first_num + second_num + third_num, 20, 24)  
