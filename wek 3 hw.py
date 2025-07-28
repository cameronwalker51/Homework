### "An algorithm is a sequence of steps that provides a solution to a specific problem or task."   
### "A Number or a special Character"
### "A sematic error is a mistake in the logic of the program that causes it to behave incorrectly, even though it may run without crashing."   
### "The number one rule of coding is to write code that is easy to read and understand."


# if 
# else
# while
# def
# return

multi_line = """Cameron Walker, pizza and Wings, Software Engineer"""
print(multi_line)

# Assign 5 different data types to 5 different variables. At least one datatype must be a string
my_string = "Hello, World!"
my_integer = 72
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3)
my_boolean = True
print(len(my_string))
print(my_string[3])

savvy = "Learning Data Analytics and Python is Awesome!"
print(savvy)

savvy = "Learning Data Analytics and Python is Awesome!"
start = savvy.find("ing")
end = savvy.find("and")
slice_result = savvy[start:end]
print(slice_result)
savvy_replaced = savvy.replace("Awesome", "great")
print(savvy_replaced)

name, age, length = "Cameron", 23, 6.5
print(name)
print(age)
print(length)

name, tall, so = "Cameron", "6.5 feet", 23
miniBio = f"Hi my name is {name}, I am {tall} and {so} old today."
print(miniBio)
age = 23
print(float(age))

mixed_list = ["pizza", 42, 6.18, True, [1, 2, 3]]
mixed_list[1] = "apple"
mixed_list.append("new item")
mixed_list.insert(4, False)
mixed_list.append(82)
print(mixed_list)
print(len(mixed_list))
second_list = mixed_list[1:4]
print(second_list)
mixed_list.extend(second_list)
print(mixed_list)

simList = [10, 25, 7, 42, 3]
print(simList)
simList.sort()
print(simList)
third_list = simList.copy()
print(third_list)
fourth_list = second_list + third_list
print(fourth_list)

my_tuple = (1, "apple", 6.18, True, "pizza")
second_tuple = my_tuple * 3
print(my_tuple)
print(second_tuple)
print(second_tuple[11])
sorted_tuple = tuple
print(sorted_tuple)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

third_tuple = (second_tuple[0], second_tuple[3], second_tuple[6], second_tuple[9])
a, b, c, d = third_tuple
print(a)
print(b)
print(c)
print(d)

fourth_tuple = (50,)
print(fourth_tuple)
fifth_tuple = second_tuple + third_tuple
print(fifth_tuple)

my_set = {"red", 42, True}
print(my_set)
fruits = ["grape", "grapefruit", "orange"]
my_set.update(fruits)
print(my_set)
my_set.add("car")
print(my_set)
second_set = {3.14, "blue", False}
print(second_set)
third_set = my_set.union(second_set)
print(third_set)
popped_item = second_set.pop()
print(f"Popped item: {popped_item}")
print(second_set)
my_set.clear()
print(my_set)
third_set.discard("banana")  # Discard does not raise error if item not found
third_set.remove("car")      # Remove raises error if item not found
print(third_set)