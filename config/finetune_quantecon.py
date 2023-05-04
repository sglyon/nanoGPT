import time

out_dir = 'out-quantecon-finetune'
eval_interval = 250
eval_iters = 10
log_interval = 10
wandb_log = False # feel free to turn on
wandb_project = 'quantecon'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'quantecon'
init_from = 'gpt2-medium' 

# only save checkpoints if the validation loss improves
# always_save_checkpoint = False
always_save_checkpoint = True

# the number of examples per iter:
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 1
max_iters = 50000

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False


# for larger models
# init_from = 'gpt2-large'
# device = 'cpu'