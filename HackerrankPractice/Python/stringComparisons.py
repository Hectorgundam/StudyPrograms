def encrypt_message(message):
    def error(str1, str2):
        error_sum = 0
        for i in range(len(str1)):
            error_sum += abs(ord(str1[i]) - ord(str2[i]))
        return error_sum

    n = len(message)
    k = len(message[0])
    total_error = 0

    for i in range(k):  # Iterate over each character position
        column = [message[j][i] for j in range(n)]
        column_sorted = sorted(column)
        middle_element = column_sorted[n // 2]

        encrypted_column = error(column, [middle_element] * n)  # Calculate error for the entire column
        total_error += encrypted_column

    return total_error

# Example usage:
message = ['abd', 'daf']
total_error = encrypt_message(message)
print("Total Error:", total_error)

