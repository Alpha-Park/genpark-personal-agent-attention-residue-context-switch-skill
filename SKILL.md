---
name: genpark-personal-agent-attention-residue-context-switch-skill
description: Personal Agent Attention Residue Context Switch. Quantifies cognitive penalties from task switching, calculates workday application fragmentation entropy, and groups fragmented tasks into focused batches.
license: MIT
version: 1.0.0
tools:
  - calculate_attention_residue_penalty
  - compute_workday_fragmentation_entropy
  - optimize_task_batching_schedule
---

# Personal Agent Attention Residue Context Switch

## Overview & Agent Behavioral Directives
You are a sovereign Personal Agent cognitive focus guardian. Your objective is to quantify and eliminate attention residue caused by task thrashing, unfinished cognitive loops, and application hopping, restoring monolithic deep work blocks through intelligent batching.

## When to Activate This Skill
- When an agent or user reviews daily task logs, context switches, or digital productivity.
- When assessing lost focus time due to interruptions or multitasking.
- When organizing loose daily to-do items into consolidated, low-switching work blocks.

## How to Execute

### Option 1: Zero-Dependency Python Execution
```python
from client import PersonalAgentAttentionResidueContextSwitch

residue = PersonalAgentAttentionResidueContextSwitch()
res = residue.optimize_task_batching_schedule([{"id": "1", "title": "Bug fix", "category": "DEV"}])
print("Eliminated Switches:", res["context_switches_eliminated"])
```

### Option 2: FastMCP Tool Calling
- `calculate_attention_residue_penalty(task_transitions_json)`
- `compute_workday_fragmentation_entropy(active_window_time_distribution_json)`
- `optimize_task_batching_schedule(tasks_json)`

## Core Mathematical Principles
1. **Leroy Attention Residue**: Unfinished tasks leave cognitive threads that decay exponentially: $	ext{Residue}(t) = R_0 e^{-0.046 t}$.
2. **Context Fragmentation Entropy**: $H_{	ext{frag}} = -\sum p_i \log_2 p_i$ measures digital attention dispersion across active tools.
