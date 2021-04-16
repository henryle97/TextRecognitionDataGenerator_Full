1 . Install 
```bash
pip install -r requirement.txt
```
2 .Running 

```bash
cd trdg 
python run.py -c 100 --dict dicts/address_full.txt -ws --font_dir fonts/vn --name_format 2 --thread_count 4 --image_dir images/bg --background 0 --output_dir text_result/simple
python run.py -c 100 --dict dicts/address_full.txt -ws --font_dir fonts/vn --name_format 2 --thread_count 4 --image_dir images/bg --background 1 --output_dir text_result/complex

python run.py -c 100 --dict dicts/address_full.txt -ws --font_dir fonts/handwritten_vi --name_format 2 --thread_count 4 --image_dir images/bg --background 0 --output_dir text_result/simple -f 64


python run.py -c 100000 --dict dicts/sentences_200k.txt -ws --font_dir fonts/handwritten_vi --name_format 2 --thread_count 2 --image_dir images/bg --background 0 --output_dir text_result/hw2 -f 64


# Handwriting 
python run.py -c 100 --dict dicts/word_dict_order.txt -ws --font_dir fonts/handwritten_vi --name_format 2 --thread_count 2 --image_dir images/bg --background 0 --output_dir text_result/hw2 -f 64 -hw
python run.py -c 20 --dict dicts/word_dict_order.txt -ws --font_dir fonts/handwritten_vi --name_format 2 --thread_count 2 --image_dir images/paper --background 1 --output_dir text_result/hw_word -f 64 -hw

```

