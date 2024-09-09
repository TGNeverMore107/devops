sentence = "The islands are administratively part of Krabi province. Ko Phi Phi is the largest island of the group, and is the most populated island of the group, although the beaches of the second largest island, Ko Phi Phi Leh are visited by many people as well. The rest of the islands in the group, including Bida Nok, Bida Noi, and Bamboo Island are not much more than large limestone rocks jutting out of the sea. The Islands are reachable by speedboats or Long-tail boats most often from Krabi Town or from various piers in Phuket Province"

words = sentence.split()

# Tính toán vị trí của từ bắt đầu từ vị trí 5 trong mảng các từ
start_index = sum(len(word) + 1 for word in words[:5])  # Cộng thêm 1 để tính cả khoảng trắng

# Tính toán vị trí của từ kết thúc ở vị trí 11 trong mảng các từ
end_index = start_index + len(words[5]) - 1  # Trừ đi 1 để không tính khoảng trắng ở cuối từ

# Trích xuất từ trong câu ban đầu từ vị trí 5 đến 11
word_extracted = sentence[start_index:end_index]
print(word_extracted)