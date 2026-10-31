# -*- coding: utf-8 -*-
"""
Personal Agent Attention Residue Context Switch Client
Zero-dependency Leroy attention residue decay modeler, multi-application context
fragmentation entropy calculator, and optimal task batching schedule optimizer.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentAttentionResidueContextSwitch:
    """
    Models cognitive attention residue from unfinished tasks and context switching.
    Calculates workday fragmentation entropy and batches tasks to maximize deep work blocks.
    """

    def calculate_attention_residue_penalty(
        self,
        task_transitions: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates Leroy attention residue penalty across task switches.
        Switch Penalty = alpha * Divergence + beta * Residue_0 * exp(-lambda * delta_t).
        Transition format: {"task_a": "Code Review", "task_b": "Email Inbox", "is_task_a_finished": False, "cognitive_load_a": 0.85, "minutes_since_switch": 5}
        """
        if not task_transitions:
            raise ValueError("Task transitions list cannot be empty.")

        total_penalty_minutes = 0.0
        switch_count = len(task_transitions)

        for tr in task_transitions:
            is_finished = bool(tr.get("is_task_a_finished", False))
            load_a = max(0.1, min(1.0, float(tr.get("cognitive_load_a", 0.5))))
            t_elapsed = max(0.0, float(tr.get("minutes_since_switch", 0.0)))

            # Baseline residue magnitude
            r0 = 0.20 if is_finished else (0.85 * load_a)
            # Residue exponential decay with half-life of 15 minutes (lambda = ln(2)/15 = 0.046)
            current_residue = r0 * math.exp(-0.046 * t_elapsed)
            # Cognitive penalty in lost productivity minutes (approx 15 to 25 mins for unfinished deep tasks)
            penalty_min = current_residue * 20.0
            total_penalty_minutes += penalty_min

        avg_penalty = round(total_penalty_minutes / switch_count, 1)

        return {
            "total_context_switches_audited": switch_count,
            "total_attention_residue_loss_minutes": round(total_penalty_minutes, 1),
            "average_penalty_per_switch_minutes": avg_penalty,
            "fragmentation_severity": "SEVERE_COGNITIVE_TAX" if total_penalty_minutes >= 60.0 else ("MODERATE_FRICTION" if total_penalty_minutes >= 25.0 else "MINIMAL_RESIDUE"),
            "primary_driver": "Unfinished deep tasks leaving lingering cognitive threads" if any(not tr.get("is_task_a_finished", False) for tr in task_transitions) else "Routine switching overhead"
        }

    def compute_workday_fragmentation_entropy(
        self,
        active_window_time_distribution: Dict[str, float]
    ) -> Dict[str, Any]:
        """
        Calculates Shannon entropy of time spent across different applications/windows:
        H = -sum(p_i * log2(p_i)).
        High entropy = extreme window thrashing; low entropy = deep monolithic focus.
        """
        if not active_window_time_distribution:
            raise ValueError("Window time distribution cannot be empty.")

        total_time = sum(active_window_time_distribution.values())
        if total_time <= 0:
            raise ValueError("Total time must be greater than zero.")

        n_apps = len(active_window_time_distribution)
        entropy = 0.0

        for t in active_window_time_distribution.values():
            if t > 0:
                p = t / total_time
                entropy -= p * math.log2(p)

        max_entropy = math.log2(n_apps) if n_apps > 1 else 1.0
        norm_entropy = round(entropy / max_entropy, 3) if max_entropy > 0 else 1.0

        return {
            "total_tracked_minutes": round(total_time, 1),
            "unique_applications": n_apps,
            "fragmentation_entropy_score": norm_entropy,
            "focus_mode": "DEEP_MONOLITHIC_FLOW" if norm_entropy <= 0.45 else ("BALANCED_MULTI_TASKING" if norm_entropy <= 0.75 else "HYPER_FRAGMENTED_THRASHING"),
            "cognitive_drag_verdict": "Low cognitive overhead" if norm_entropy <= 0.45 else "User losing up to 30% mental capacity to context thrashing"
        }

    def optimize_task_batching_schedule(
        self,
        tasks: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Clusters and batches tasks by context category to minimize cross-domain switching penalties.
        Task format: {"id": "t1", "title": "Reply to Vendor", "category": "COMMUNICATION", "duration_minutes": 15}
        """
        if not tasks:
            raise ValueError("Task list cannot be empty.")

        batches = {}
        for t in tasks:
            cat = str(t.get("category", "GENERAL")).upper()
            if cat not in batches:
                batches[cat] = []
            batches[cat].append(t)

        batched_schedule = []
        for cat, items in batches.items():
            tot_dur = sum(int(item.get("duration_minutes", 15)) for item in items)
            batched_schedule.append({
                "batch_category": cat,
                "task_count": len(items),
                "total_duration_minutes": tot_dur,
                "tasks": [item.get("title", item.get("id")) for item in items]
            })

        # Calculate saved switching penalties (each eliminated internal switch saves ~15 mins of residue)
        raw_switches = len(tasks) - 1
        batched_switches = len(batches) - 1
        switches_saved = max(0, raw_switches - batched_switches)
        saved_minutes = switches_saved * 15

        return {
            "initial_unbatched_switches": raw_switches,
            "optimized_batched_switches": batched_switches,
            "context_switches_eliminated": switches_saved,
            "estimated_recovered_focus_minutes": saved_minutes,
            "batched_work_blocks": batched_schedule
        }
