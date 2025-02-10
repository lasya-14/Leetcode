class Solution:
    def clearDigits(self, s: str) -> str:
        result = []  # List to store valid characters dynamically
        for char in s:
            if char.isdigit():
                if result:  # Ensure we don’t pop from an empty list
                    result.pop()  # Remove the last appended character
            else:
                result.append(char)  # Add non-digit characters
        return ''.join(result)  # Convert list back to a string

        