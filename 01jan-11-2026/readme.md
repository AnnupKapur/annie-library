# 🔐 The Decoy Safe Challenge

## Background

You have encountered a locked safe. The attached document (your puzzle input)
contains a sequence of rotations, one per line, which seemingly tell you how to
open it.

However, your recent **North Pole Secret Entrance Security Training** taught you
a crucial detail: **the safe is actually a decoy.** To find the *actual*
password, you must analyze the behavior of the dial rather than just opening it.

---

## The Mechanics

The safe dial operates on a circular ring of numbers ranging from **0 to 99**.

* **L (Left):** Rotates the dial toward **lower** numbers.
* **R (Right):** Rotates the dial toward **higher** numbers.
* **Circular Wrapping:**
  * Turning **Left** from `0` wraps around to `99`.
  * Turning **Right** from `99` wraps around to `0`.

**Note:** This behavior mimics modulo arithmetic (specifically `modulo 100`).

---

## Starting Conditions

* The dial begins pointing at **50**.

## Examples of Movement

1. **Basic Movement:**
    * If the dial points at `11`, a rotation of `R8` moves it to `19`.
    * From `19`, a rotation of `L19` moves it to `0`.

2. **Wrapping Around:**
    * If the dial points at `5`, a rotation of `L10` moves it to `95`
      (wrapping backward past 0).
    * From `95`, a rotation of `R5` moves it to `0` (wrapping forward past 99).

---

## 🎯 The Objective

You must process the sequence of rotations given in your input file.

**The actual password is the total number of times the dial is left pointing
at `0` after completing a rotation.**

## Input Format

The input file contains a list of instructions, one per line.

* **Format:** `[Direction][Distance]`
* **Example:**

    ```text
    R8
    L19
    L10
    R5
    ```
