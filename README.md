1 . Install 
```bash
pip install -r requirement.txt
```
2 .Running 
```bash
cd trdg 
python run.py -c 1000 --dict dicts/word_dict_order.txt -ws --font_dir fonts/vn --name_format 3 --thread_count 8 --image_dir background/images --background 5 --output_dir 'text_result/complex_3'
python run.py -c 1000 --dict dicts/word_dict_order.txt -ws --font_dir fonts/vn --name_format 3 --thread_count 8 --background 1 --output_dir 'text_result/complex_3'

python run.py -c 100000 --dict dicts\address_full.txt --name_format 3 --thread_count 4 --image_dir images\bg --background 5 --output_dir text_result/address --font_dir fonts\id
```

