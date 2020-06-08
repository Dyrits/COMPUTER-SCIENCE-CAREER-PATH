from stack import Stack
print()
print("Let's play Towers of Hanoi!!")
print()

#Create the Stacks
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks = [left_stack, middle_stack, right_stack]

#Set up the Game
num_disks = "None"
while not num_disks.isnumeric():
    num_disks = input("How many disks do you want to play with? ")
num_disks = int(num_disks) 
while num_disks < 3:
    num_disks = input("Enter a number greater than or equal to 3: ")
    if num_disks.isnumeric():
        num_disks = int(num_disks)
    else:
        num_disks = 0

for disk in range(num_disks, 0, -1):
    left_stack.push(disk)
    
num_optimal_moves = 2 ** num_disks - 1
print()
print(f"The fastest way to solve this game is in {num_optimal_moves} moves. Good luck!")

#Get User Input
def get_input():
    choices = [stack.name[0] for stack in stacks]
    [print(f"Enter {stack.name[0]} for {stack.name}.") for stack in stacks]
    user_input = input("").upper()
    while user_input not in choices:
        user_input = input("Please, select a valid option: ").upper()
    for choice in range(len(choices)):
        if user_input == choices[choice]:
            return stacks[choice]
        
    

#Play the Game
num_user_moves = 0
while right_stack.size != num_disks:
    print()
    print("=" * 75)
    print(f"STATUS OF THE GAME (TURN {num_user_moves + 1}):")
    print()
    [stack.print_items() for stack in stacks]
    
    while True:
        print()
        print("-" * 50)
        print("Which stack do you want to move from?")
        from_stack = get_input()
        if from_stack.is_empty():
            print()
            print("This stack is empty. Try again!".upper())
            break
        print()
        print("Which stack do you want to move to?")
        to_stack = get_input()
        if to_stack.is_empty() or from_stack.peek() < to_stack.peek():
            to_stack.push(from_stack.pop())
            num_user_moves += 1
            break
        else:
            print()
            print("This move is invalid. Try Again!".upper())
            break
            
print(f"You completed the game in {num_user_moves}.")
if num_user_moves == num_optimal_moves:
    print("That's the fastest way to solve this game!")
else:
    print(f"You can still improve. You could have done it with {num_user_moves - num_optimal_moves} less moves.")