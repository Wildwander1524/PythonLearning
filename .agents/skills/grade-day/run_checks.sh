#!/usr/bin/env bash
# grade-day automated checks: pyright (type/hygiene GATE) + pytest (behavior, base env).
# Usage:  bash .claude/skills/grade-day/run_checks.sh week01/dayNN_topic [--gate-tests]
#
#   default        : pyright type-gates ONLY the homework code (test_*.py excluded).
#   --gate-tests   : also type-gate test_*.py — use when WRITING the tests is part of the
#                    homework spec (e.g. a day whose Part C is "write the tests").
#
# Either way, pytest ALWAYS executes the test files (that's the behavior check).
# Run from the repo root. Exits non-zero if pyright finds errors or pytest fails.
set -uo pipefail

DAY="${1:?usage: run_checks.sh <day_folder> [--gate-tests]}"
GATE_TESTS="${2:-}"
if [ ! -d "$DAY" ]; then
  echo "!! not a directory: $DAY" >&2
  exit 2
fi

echo "### grade-day checks for: $DAY"
fail=0

echo
if [ "$GATE_TESTS" = "--gate-tests" ]; then
  echo "== pyright (homework + tests — tests are part of THIS homework) =="
  PYRIGHT_TARGETS=("$DAY")
else
  echo "== pyright (homework code only; test_*.py excluded from the type gate) =="
  mapfile -t PYRIGHT_TARGETS < <(find "$DAY" -name "*.py" ! -name "test_*.py" ! -path "*/__pycache__/*")
fi

if command -v pyright >/dev/null 2>&1; then
  if [ "${#PYRIGHT_TARGETS[@]}" -eq 0 ]; then
    echo "(no homework .py found to type-check)"
  else
    pyright "${PYRIGHT_TARGETS[@]}" || fail=1
  fi
else
  echo "!! pyright not on PATH — run: npm install -g pyright (then /reload-plugins)" >&2
  fail=1
fi

echo
echo "== pytest (base env, Python 3.13.9) =="
if command -v conda >/dev/null 2>&1; then
  conda run -n base python -m pytest "$DAY" -v || fail=1
else
  echo "!! conda not on PATH — falling back to current python (may not be base)" >&2
  python -m pytest "$DAY" -v || fail=1
fi

echo
if [ "$fail" -eq 0 ]; then
  echo ">> CHECKS PASS — pyright clean + tests green. Proceed to spec-precision grading."
else
  echo ">> CHECKS INCOMPLETE — fix pyright/pytest above before the day counts as done."
fi
exit "$fail"
