#Implement a class Counter with a class variable count that keeps track of 
# the number of instances created. Increment the count in the constructor. 
# Print the total count after creating several instances

class Counter:
    count = 0

    def __init__(self):
        # Increment the count in the constructor
        Counter.count += 1

# Print the total count after creating several instances.
instance1 = Counter()
instance2 = Counter()
instance3 = Counter()

print(f"Total Instances Created: {Counter.count}")