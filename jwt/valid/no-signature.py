import os
import subprocess

import requests


# 定义要调用的curl命令
curl_command = '''
curl 'https://chatpt.cn/chatglm/backend-api/assistant/stream' \
  -H 'Accept-Language: zh-CN,zh;q=0.9' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlZTUxNGU4MDg4NmY0OWMwOTI5MGI0ZjZhYzdkZGVmNSIsImV4cCI6MTcxNjYzMTk3NywibmJmIjoxNzE2NTQ1NTc3LCJpYXQiOjE3MTY1NDU1NzcsImp0aSI6ImNlYTUxODk1MTI5NzRjZGZhNTFiYzgxY2FmOGU1NjVjIiwidWlkIjoiNjYwMTcyNDZlN2UxZTAxNWYzNDY4MDIyIiwidHlwZSI6ImFjY2VzcyJ9.' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://chatpt.cn' \
  -H 'Referer: https://chatpt.cn/main/alltoolsdetail' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' \
  -H 'accept: text/event-stream' \
  -H 'sec-ch-ua: "Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '{"assistant_id":"65940acff94777010aa6b796","conversation_id":"66502c865cc0b0919f1fa1ff","meta_data":{"mention_conversation_id":"","is_test":false,"input_question_type":"xxxx","channel":"","draft_id":"","quote":""},"messages":[{"role":"user","content":[{"type":"text","text":"1+1"}]}]}'
'''

# 使用subprocess运行curl命令
result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 输出结果
print(result.stdout)
