# Name: Weevern Gong
# Project Title: MSCS532_Assignment3
# Description: This program implements a hash table with chaining to store integer key-value pairs.
# The hash table supports insert, search, and delete operations and uses dynamic resizing to control the load factor.

# Hash table with chaining explanation: A hash table uses a hash function to determine the table slot where a key
# should be stored. When two or more keys are assigned to the same slot, a collision occurs. This implementation uses
# chaining, which stores all key-value pairs assigned to the same slot together in a list. Insert searches the selected
# chain before adding a new key so an existing value can be updated. Search checks only the chain selected by the hash
# function, and delete removes the matching key-value pair from that chain.
# The load factor is the number of stored key-value pairs divided by the number of table slots. When the load factor
# becomes greater than 0.75, the table size is doubled and the stored values are rehashed into the new table.
# The universal hash function follows the form h(k) = ((a * k + b) mod p) mod m, where p is prime and m is the current
# table capacity. Under suitable hashing assumptions, chaining provides expected Θ(1 + α) search time, where α is the
# load factor.


import random


class HashTable:

    PRIME = 2147483647

    def __init__(self, initial_capacity=8, max_load_factor=0.75, random_seed=532):

        self.capacity = initial_capacity
        self.max_load_factor = max_load_factor
        self.size = 0

        # Create one empty chain for each slot in the hash table
        self.buckets = [[] for i in range(self.capacity)]

        random_generator = random.Random(random_seed)

        # Select values used by the universal hash function
        self.a = random_generator.randint(1, self.PRIME - 1)
        self.b = random_generator.randint(0, self.PRIME - 1)


    def hash_key(self, key):

        # Confirm that the key is a nonnegative integer supported by this implementation
        if not isinstance(key, int):
            raise TypeError("Hash table keys must be integers.")

        if key < 0 or key >= self.PRIME:
            raise ValueError("Hash table keys must be nonnegative integers smaller than PRIME.")

        # Calculate the table slot for the key
        return ((self.a * key + self.b) % self.PRIME) % self.capacity


    def get_load_factor(self):

        # Divide the number of stored elements by the number of table slots
        return self.size / self.capacity


    def insert(self, key, value):

        bucket_index = self.hash_key(key)
        bucket = self.buckets[bucket_index]

        # Check the selected chain for an existing key
        for i in range(len(bucket)):
            stored_key, stored_value = bucket[i]

            if stored_key == key:

                # Replace the value when the key is already stored
                bucket[i] = (key, value)
                return

        # Add the new key-value pair to the selected chain
        bucket.append((key, value))
        self.size += 1

        # Resize the table when the load factor becomes too high
        if self.get_load_factor() > self.max_load_factor:
            self.resize(self.capacity * 2)


    def search(self, key):

        bucket_index = self.hash_key(key)
        bucket = self.buckets[bucket_index]

        # Search only the chain associated with the key
        for stored_key, stored_value in bucket:
            if stored_key == key:
                return stored_value

        return None


    def delete(self, key):

        bucket_index = self.hash_key(key)
        bucket = self.buckets[bucket_index]

        # Search the selected chain for the key that should be removed
        for i in range(len(bucket)):
            stored_key, stored_value = bucket[i]

            if stored_key == key:

                # Remove the key-value pair and reduce the stored element count
                del bucket[i]
                self.size -= 1
                return True

        return False


    def resize(self, new_capacity):

        old_buckets = self.buckets

        # Create a larger empty table
        self.capacity = new_capacity
        self.buckets = [[] for i in range(self.capacity)]

        # Rehash every stored key-value pair because the table capacity changed
        for bucket in old_buckets:
            for key, value in bucket:
                bucket_index = self.hash_key(key)
                self.buckets[bucket_index].append((key, value))


    def display(self):

        # Print each table slot and the chain stored in that slot
        for i in range(self.capacity):
            print(f"Slot {i}: {self.buckets[i]}")


def main():

    hash_table = HashTable()

    # Insert sample key-value pairs into the hash table
    hash_table.insert(2, "Apple")
    hash_table.insert(13, "Banana")
    hash_table.insert(24, "Orange")
    hash_table.insert(40, "Grape")
    hash_table.insert(50, "Pear")
    hash_table.insert(60, "Peach")
    hash_table.insert(70, "Plum")

    print("Hash table after insertions:")
    hash_table.display()

    print("\nSearch for key 13:", hash_table.search(13))
    print("Search for key 99:", hash_table.search(99))

    print("\nDelete key 13:", hash_table.delete(13))
    print("Search for key 13 after deletion:", hash_table.search(13))

    print("\nHash table after deletion:")
    hash_table.display()

    print("\nNumber of stored elements:", hash_table.size)
    print("Table capacity:", hash_table.capacity)
    print("Load factor:", round(hash_table.get_load_factor(), 3))


if __name__ == "__main__":
    main()
    