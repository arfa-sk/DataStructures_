# Basic Operations on Arrays
def create_array():
    arr = [1, 2, 3, 4, 5]  # Creating an array
    print("Initial Array:", arr)
    return arr

def access_element(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    return "Index out of bounds!"

def update_element(arr, index, new_value):
    if 0 <= index < len(arr):
        arr[index] = new_value
        return arr
    return "Index out of bounds!"

def delete_element(arr, index):
    if 0 <= index < len(arr):
        del arr[index]
        return arr
    return "Index out of bounds!"

# Example Usage
if __name__ == "__main__":
    arr = create_array()
    print("Access element at index 2:", access_element(arr, 2))
    print("Update element at index 3:", update_element(arr, 3, 10))
    print("Delete element at index 1:", delete_element(arr, 1))
