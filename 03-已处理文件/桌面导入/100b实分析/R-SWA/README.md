<!-- 来源：Windows 桌面 2026-11-23 导入；未核对归属，可能需人工归位 -->

# Sliding Window Attention on Apple Silicon (MPS)

**Reference Sliding Window Attention (R-SWA)** — the constant-KV-cache mechanism behind Baidu's [Unlimited OCR Works](https://arxiv.org/abs/2606.23050) — reproduced from scratch in PyTorch and runnable on a **Mac**. Apple Silicon (MPS) and CPU, **no CUDA required**.

[未定位] 外链 shield badge（python-3.13）原引用 https://img.shields.io/badge/python-3.13-blue.svg ，未内嵌；链接语义保留：[Python 3.13](https://www.python.org/)
[未定位] 外链 shield badge（license-MIT）原引用 https://img.shields.io/badge/license-MIT-green.svg ，未内嵌；链接语义保留：[License: MIT](LICENSE)
[未定位] 外链 shield badge（arXiv-2606.23050）原引用 https://img.shields.io/badge/arXiv-2606.23050-b31b1b.svg ，未内嵌；链接语义保留：[arXiv:2606.23050](https://arxiv.org/abs/2606.23050)

Baidu's model is CUDA-only. This repo rebuilds the *mechanism* in plain PyTorch so it runs on a laptop — CPU or Apple MPS, no GPU required — and ships the experiments that show what the mechanism actually does. It reproduces the cache policy and measures its behaviour; it is **not** Baidu's trained model and makes no claim about OCR accuracy.

## What R-SWA does

A normal decoder attends to every previous token, so its KV cache grows with output length (`m + T`) and each token costs a little more than the last. R-SWA keeps two things instead:

- a **reference region** of size `m` (the prompt and, for OCR, the encoded page) that every later token can always see, and
- a **sliding window** of the last `n` generated tokens (default 128). Older generated tokens are physically evicted.

The cache is capped at `m + n` and never grows.

## Results

Measured on an Apple M2 Max. Reproduce with `./run_all.sh`.

**Memory is bounded, and the formula is exact.** At 8k tokens the full cache hits 311 MB; R-SWA stays flat at 14 MB — 22× smaller, matching `2·L·H·d·b·(m+min(n,T))` to the byte.

[未定位] KV-cache memory vs output length → 原引用 `assets/memory.png`：R-SWA 项目图（非 TBB 教材图），仓内无该文件，无法从 TBB 原书 PDF 裁回。

**The quality trade-off is the interesting part.** Hide a fact in the generated stream and recall falls off a cliff the moment its distance exceeds the window `n` (right to 0.00). Keep that fact in the always-visible reference region and recall is unaffected at any window size. That is exactly why R-SWA is free for OCR — the page never leaves the reference region — and why it is *not* free for tasks that must recall their own distant output.

[未定位] Recall: stream cliff vs safe reference region → 原引用 `assets/recall.png`：R-SWA 项目图（非 TBB 教材图），仓内无该文件，无法从 TBB 原书 PDF 裁回。

**Speed depends on what dominates the step.** The attention op is O(cache length), and throughput is ~1.8× higher at 8k. But on a small model the per-token latency is dominated by fixed overhead, so full attention's growth only shows clearly on CPU (synchronous compute) — a useful caveat when reading efficiency claims.

[未定位] Latency growth shape, CPU vs MPS → 原引用 `assets/cpu_vs_mps.png`：R-SWA 项目图（非 TBB 教材图），仓内无该文件，无法从 TBB 原书 PDF 裁回。

See [the write-up](#background) for the full analysis.

## Install

```bash
git clone https://github.com/iamirulofficial/sliding-window-attention-mps.git
cd sliding-window-attention-mps
python -m venv .venv && source .venv/bin/activate   # or use your env of choice
pip install -r requirements.txt
```

Python 3.13, PyTorch 2.12. Works on macOS (MPS) and any CPU; pass `--device cpu` if you don't have Apple Silicon.

## Usage

```bash
# 0. correctness gate — proves eviction is real and positions are preserved
python -m rswa.attention

# 1. efficiency: memory, latency, throughput, attention-only microbench
python -m rswa.bench_efficiency --device mps --dtype bf16

# 2. quality: associative-recall cliff + perplexity vs window (downloads Qwen2.5-0.5B)
python -m rswa.quality --model Qwen/Qwen2.5-0.5B --device mps

# 3. aggregate everything into results/findings.md
python -m rswa.analyze
```

Or run the whole thing: `./run_all.sh`. Outputs land in `results/` (figures, `summary.csv`, `findings.md`).

Use the library directly:

```python
import torch
from rswa import ModelConfig, make_model

model = make_model(ModelConfig(), device="mps", dtype=torch.bfloat16)
full = model.new_cache("full", m=256, n=128, T_max=4096)   # standard, grows to m+T
swa  = model.new_cache("rswa", m=256, n=128, T_max=4096)   # bounded ring at m+n
```

## How it works

`rswa/attention.py` implements a small decoder with three cache policies that differ **only** in which tokens survive: `full` (standard, growing), `rswa` (a fixed ring buffer with real eviction and pinned prefix), and `rswa_mask` (a brute-force reference used only to verify correctness). RoPE is applied at absolute positions and baked into the stored keys, so a surviving token keeps its true position after its neighbours are evicted.

The correctness gate (`python -m rswa.attention`) checks three things before any benchmark is trusted:

1. for `T ≤ n`, `rswa` is bit-identical to `full` (nothing evicted yet);
2. past the window, the ring buffer matches the brute-force reference to ~1e-6 and stays bounded at `m + n`;
3. past the window, `rswa` genuinely differs from `full` — so eviction isn't a silent no-op.

## Scope and limitations

- This reproduces the **cache policy**, not Baidu's weights, encoder, or training. No OmniDocBench numbers are claimed.
- A small model on MPS is overhead-bound, so the end-to-end latency curve understates the asymptotic win; the CPU run and the attention-only microbench show the O(T) trend honestly.
- The recall probe uses token-level induction, which measures whether *evicted* information is recoverable — the property R-SWA changes — not OCR quality.

## Background

This code accompanies a write-up reproducing the efficiency and quality claims of R-SWA from scratch. The short version: the constant-memory claim is exact and scale-free; the "no quality loss" claim is real *because OCR keeps its source in the reference region the whole time*, and breaks cleanly for any task that needs to recall its own distant output.

## Citation

R-SWA is from Baidu's paper; please cite it:

```bibtex
@misc{yin2026unlimitedocrworks,
  title={Unlimited OCR Works},
  author={Youyang Yin and others},
  year={2026}, eprint={2606.23050}, archivePrefix={arXiv}, primaryClass={cs.CV},
  url={https://arxiv.org/abs/2606.23050}
}
```

## Acknowledgements

Thanks to the authors of [Unlimited OCR](https://github.com/baidu/Unlimited-OCR) and [DeepSeek-OCR](https://github.com/deepseek-ai/DeepSeek-OCR) for the models and ideas this reproduction is built on.

## License

[MIT](LICENSE).
