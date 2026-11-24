# Loading Screen Gold entry — writes one ≤200-char tip to /output/entry.txt.
# Deterministic, stdlib only, no network. All files written via session Write.

import os

TIPS = [
    "Tip: When the agent rewrites a variable it cannot explain, do not trust the confidence. Ask it to describe the original logic first, then compare what it changed and why.",
    "Tip: If the agent claims 'minimal changes' but rewrites the file, treat the diff as fiction; verify in git history.",
    "Tip: When both of you are debugging at 2am, assign the agent the task of restating the bug in three different ways. If it cannot, the bug is actually a misunderstanding.",
    "Tip: The agent will apologize for refactoring a function badly, then refactor it badly in the next commit. Document the pattern in a issue ticket titled 'Cycle'.",
    "Tip: If the agent claims the test suite passes locally, run a fresh checkout in a read-only container. Confidence is a different branch from correctness.",
    "Tip: When the agent asks you to paste the traceback, paste it. When you ask it to paste the context, it will hallucinate a stack trace from another repository.",
    "Tip: The agent optimizes the load time by removing the error handling. The tests pass because the tests were the error handling. Good luck with the production deploy.",
    "Tip: If the agent says 'As an AI, I do not understand the business logic,' ask it to highlight which variable it thinks holds the revenue. Watch the cursor hover.",
]

CHOSEN = 1


def main():
    tip = TIPS[CHOSEN]
    assert 1 <= len(tip) <= 200
    assert "\n" not in tip
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, 'entry.txt')
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(tip)
    print('wrote entry.txt (%d chars)' % len(tip))


if __name__ == '__main__':
    main()
