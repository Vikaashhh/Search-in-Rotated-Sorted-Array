class Solution:
    def search(self, arr, key):
        # Low aur high pointers set kar lo
        low, high = 0, len(arr) - 1
        
        # Jab tak low aur high cross nahi karte
        while low <= high:
            mid = (low + high) // 2  # Mid point nikal lo
            
            # Agar mid pe hi key mil gaya
            if arr[mid] == key:
                return mid

            # Check karo left sorted part hai ya nahi
            if arr[low] <= arr[mid]:
                # Agar key left part me hai toh wahi pe search karo
                if arr[low] <= key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # Nahi toh right part sorted hoga
                if arr[mid] < key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        # Agar key nahi mila toh -1 return karo
        return -1
