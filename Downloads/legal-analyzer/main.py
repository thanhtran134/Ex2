# import json
# import argparse
# from pathlib import Path

# from van_ban_analyzer.services.analyzer import VanBanAnalyzer
# from van_ban_analyzer.config import Config


# def main():
#     """Hàm main để chạy phân tích văn bản"""
#     parser = argparse.ArgumentParser(
#         description='Phân tích quan hệ giữa hai văn bản pháp luật'
#     )
#     parser.add_argument(
#         '--van-ban-a',
#         type=str,
#         required=True,
#         help='Đường dẫn đến file JSON của văn bản A'
#     )
#     parser.add_argument(
#         '--van-ban-b',
#         type=str,
#         required=True,
#         help='Đường dẫn đến file JSON của văn bản B'
#     )
#     parser.add_argument(
#         '--output',
#         type=str,
#         default='output.json',
#         help='Đường dẫn file output (mặc định: output.json)'
#     )
    
#     args = parser.parse_args()
    
#     # Đọc dữ liệu văn bản
#     print(f"Đang đọc văn bản A từ: {args.van_ban_a}")
#     with open(args.van_ban_a, 'r', encoding='utf-8') as f:
#         van_ban_a = json.load(f)
    
#     print(f"Đang đọc văn bản B từ: {args.van_ban_b}")
#     with open(args.van_ban_b, 'r', encoding='utf-8') as f:
#         van_ban_b = json.load(f)
    
#     # Khởi tạo analyzer
#     print("Khởi tạo analyzer...")
#     config = Config()
#     config.validate()
#     analyzer = VanBanAnalyzer(config)
    
#     # Phân tích quan hệ
#     print("Đang phân tích quan hệ văn bản...")
#     result = analyzer.analyze_relation(van_ban_a, van_ban_b)
    
#     # Kiểm tra lỗi
#     if "error" in result:
#         print(f"Lỗi: {result['error']}")
#         if "raw_response" in result:
#             print(f"Raw response: {result['raw_response']}")
#         return
    
#     # Lưu kết quả
#     print(f"Đang lưu kết quả vào: {args.output}")
#     output_path = Path(args.output)
#     output_path.parent.mkdir(parents=True, exist_ok=True)
    
#     with open(args.output, 'w', encoding='utf-8') as f:
#         json.dump(result, f, ensure_ascii=False, indent=2)
    
#     print("Hoàn thành!")
#     print(f"\nKết quả:")
#     print(f"- Văn bản A: {result.get('van_ban_a', {}).get('so_hieu_vb', 'N/A')}")
#     print(f"- Văn bản B: {result.get('van_ban_b', {}).get('so_hieu_vb', 'N/A')}")
#     print(f"- Số quan hệ tìm thấy: {len(result.get('quan_he_van_ban', []))}")
    
#     for i, relation in enumerate(result.get('quan_he_van_ban', []), 1):
#         print(f"  {i}. {relation.get('loai_quan_he', 'N/A')}")


# if __name__ == "__main__":
#     main()