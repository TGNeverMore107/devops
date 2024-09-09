import csv
import subprocess

def remove_s3_folders():
    # Đường dẫn của file "list-data.csv"
    csv_file_path = "list-data6.csv"
    bucket_name = '3sfarm-assets-storage-prod'

    # Mở file CSV để đọc
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        # Tạo một đối tượng đọc CSV
        csv_reader = csv.reader(csv_file)
        # Duyệt qua từng dòng trong file CSV
        for row in csv_reader:
            # Trong vòng lặp lấy giá trị email trong cột đầu là cột A của file list-data.csv
            folder = row[0]
            # Kiểm tra nếu folder không rỗng và không chứa ký tự "*"
            if folder and '*' not in folder:
                # tạo biến uri để chạy câu lệnh xóa
                folder_uri = f"s3://{bucket_name}/3sfarmspaces/{folder}"
                print("Đang xóa folder:", folder_uri)
                subprocess.run(['aws', 's3', 'rm', folder_uri, '--recursive', '--profile', 'thanhhv'])

if __name__ == "__main__":
    remove_s3_folders()

        # aws s3 rm s3://3sfarm-assets-storage-prod/3sfarmspaces/metviktormet@gmail.com --recursive --profile thanhhv

        