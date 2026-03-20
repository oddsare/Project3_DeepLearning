"""
Run this script once from the Project3_DeepLearning folder to copy
all result images into submission/report/images/ for the webpage.

  python submission/report/copy_images.py
"""
import os, shutil

DST = os.path.join(os.path.dirname(__file__), 'images')
os.makedirs(DST, exist_ok=True)

sources = [
    # Part 1
    'results/part1/Config1_baseline_loss.png',
    'results/part1/Config2_larger_hidden_loss.png',
    'results/part1/Config3_low_lr_high_drop_loss.png',
    'results/part1/Config4_more_data_loss.png',
    'results/part1/all_configs_train_loss.png',
    'results/part1/attention_sent1.png',
    'results/part1/attention_sent2.png',
    'results/part1/attention_sent3.png',
    # Part 2
    'results/part2/MultiHead_1h_loss.png',
    'results/part2/MultiHead_4h_loss.png',
    'results/part2/MultiHead_8h_loss.png',
    'results/part2/bleu_vs_heads.png',
    'results/part2/MultiHead_4h_sent1_heads.png',
    'results/part2/MultiHead_4h_sent1_fullseq.png',
    'results/part2/MultiHead_4h_sent2_heads.png',
    'results/part2/MultiHead_4h_sent2_fullseq.png',
    # Part 3
    'results/part3/Transformer_baseline_loss.png',
    'results/part3/Bahdanau_for_comparison_loss.png',
    'results/part3/MultiHead4_for_comparison_loss.png',
    'results/part3/Transformer_no_pos_enc_loss.png',
    'results/part3/Transformer_no_self_attn_loss.png',
    'results/part3/all_models_loss.png',
    'results/part3/bleu_comparison.png',
]

for src in sources:
    if os.path.exists(src):
        shutil.copy(src, os.path.join(DST, os.path.basename(src)))
        print(f'  copied {src}')
    else:
        print(f'  MISSING: {src}')

print(f'\nDone. Images in {DST}')
