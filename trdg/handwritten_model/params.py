save_path = 'logs/exp1'
load_path = "handwritten_model/model_ep150.pt"

dec_hidden_size = 400
dec_n_layers = 3
n_mixtures_attention = 10
n_mixtures_output = 20


path = './my_data'

batch_size = 64
lr = 0.001

# scheduler onecycle
max_lr = 0.01
pct_start = 0.1  # 10% of epochs

# scheduler reduce lr
factor = 0.1
patience = 5

epochs = 1000
log_interval = 50
val_epoch_per = 10

seq_len = 512   # sub length for training
MAX_STROKE_LENGTH = 450   #4300
MAX_SENTENCE_LENGTH = 108
PADDING_LEN = 50
bias = 5.0

scale_data = 1.0
vocab_path = 'handwritten_model/vocab.npy'
resume_from = None
pretrained_model = None

# moniter
num_samples = 5