#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    """
    Given a list of weights, a length, and a weight limit, return a tuple of the
    indices of two items whose weights add up to the limit. If there are not two
    that add up to the limit, then return None

    :param weights: List<int> the list of weights
    :param length: <int> The length of the list
    :param limit: <int> The limit to the weight of the package
    :return: None | Tuple<int, int>
    """
    ht = HashTable(16)
    found = None
    for (index, weight) in enumerate(weights):
        # Check if there is already a value associated with the weight
        found_index = hash_table_retrieve(ht, weight)

        if found_index is not None and weight == limit - weight:
            # If there is a found index, return the current index (which will always be higher) and the found_index
            found = (index, found_index)
        else:
            # Insert the new key value pair to the hash table
            hash_table_insert(ht, weight, index)

            if found is None:
                found_index = hash_table_retrieve(ht, limit - weight)

                if found_index is not None:
                    found = (index, found_index) if index > found_index else (
                        found_index, index)

    return found


def print_answer(answer):
    if answer is not None:
        print(f"{answer[0]}, {answer[1]}")
    else:
        print("None")
