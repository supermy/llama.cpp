# https://modelscope.cn/models/shaowenchen/chinese-llama-2-13b-16k-gguf/summary


import torch
# 下载
from modelscope.hub.file_download import model_file_download
model_dir = model_file_download(model_id='shaowenchen/chinese-alpaca-2-13b-16k-gguf',file_path='chinese-alpaca-2-13b-16k.Q3_K_S.gguf',cache_dir="../models")
# 推理
./main -m ../models/shaowenchen/chinese-alpaca-2-13b-16k-gguf/chinese-alpaca-2-13b-16k.Q3_K_S.gguf -n 128 -p "展示上个季度所有销售额超过 10000 美元的订单,写出SQL" -t 2 -ngl 10