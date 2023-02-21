# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()


import PyPDF2
import nltk
import re

pdf_file = open('/Users/alex/Desktop/二手车交易的案例.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ''
for i in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[i]
    text += page.extract_text()

pdf_file.close()
# print(text)
# 分句和分词
sentences = nltk.sent_tokenize(text)
words = [nltk.word_tokenize(sent) for sent in sentences]

# 提取原告的上诉请求
appeal_request = ''
for sent in sentences:
    if re.search(r'上诉⼈.*上诉请求', sent):
        appeal_request = sent
        break

# 提取判决结果
judgement = ''
# for i, sent in enumerate(sentences):
#     if re.search(r'判决', sent):
#         if re.search(r'如下', sent):
#             # 如果判决结果在本句中，则提取本句中的内容
#             judgement = sent.split('如下')[1]
#         else:
#             # 否则，在下一句中查找判决结果
#             next_sent = sentences[i + 1]
#             judgement = next_sent.strip()
#         break
# 提取上诉人的诉求
appeal_pattern = r'上诉人(.*?)，.*?(要求|请求|诉称|诉请)(.*?)。'
appeal_match = re.search(appeal_pattern, text, re.DOTALL)
if appeal_match:
    appeal = appeal_match.group(3)
else:
    appeal = ''

# 提取判决结果
judgment_pattern = r'(判决如下|裁定如下|决定如下).*?：(.*?)\n'
judgment_match = re.search(judgment_pattern, text, re.DOTALL)
if judgment_match:
    judgment = judgment_match.group(2)
else:
    judgment = ''

# 输出结果
print('上诉人的诉求：', appeal)
print('判决结果：', judgment)
