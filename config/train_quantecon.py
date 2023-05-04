import time

out_dir = 'out-quantecon-fresh'
eval_interval = 250
eval_iters = 10
log_interval = 10

dataset = 'quantecon'
init_from = 'resume' 

gradient_accumulation_steps = 1
batch_size = 32
block_size = 256 # context of up to 256 previous characters

# baby GPT model :)
n_layer = 6
n_head = 6
n_embd = 384
dropout = 0.2

learning_rate = 1e-3 # with baby networks can afford to go a bit higher
max_iters = 50000
lr_decay_iters = 50000 # make equal to max_iters usually
min_lr = 1e-4 # learning_rate / 10 usually
beta2 = 0.99 # make a bit bigger because number of tokens per iter is small

warmup_iters = 100 # not super necessary potentially


# for larger models
# init_from = 'gpt2-large'
# device = 'cpu'