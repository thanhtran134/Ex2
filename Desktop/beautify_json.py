import json
import ast

# The input string (Python dict representation)
input_str = """{'node_id': 'b388cf42-b24f-45af-89ca-72cbe3f8a8e7::n19', 'type': 'KHOẢN', 'title': '8. Thi hành án phạt quản chế là việc cơ quan, người có thẩm quyền theo quy định của Luật này buộc người chấp hành án phải cư trú, làm ăn sinh sống ở một địa phương nhất định dưới sự kiểm soát, giáo dục của chính quyền và nhân dân địa phương theo bản án đã có hiệu lực pháp luật.', 'text': '8. Thi hành án phạt quản chế là việc cơ quan, người có thẩm quyền theo quy định của Luật này buộc người chấp hành án phải cư trú, làm ăn sinh sống ở một địa phương nhất định dưới sự kiểm soát, giáo dục của chính quyền và nhân dân địa phương theo bản án đã có hiệu lực pháp luật.', 'raw': {'level': 4, 'type': 'KHOẢN', 'content': '8. Thi hành án phạt quản chế là việc cơ quan, người có thẩm quyền theo quy định của Luật này buộc người chấp hành án phải cư trú, làm ăn sinh sống ở một địa phương nhất định dưới sự kiểm soát, giáo dục của chính quyền và nhân dân địa phương theo bản án đã có hiệu lực pháp luật.', 'children': []}}"""

# Parse the string as a Python dict
data = ast.literal_eval(input_str)

# Pretty-print as JSON
beautified_json = json.dumps(data, indent=4, ensure_ascii=False)

print(beautified_json)
