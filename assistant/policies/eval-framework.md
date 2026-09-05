# Evalramverk – snabbpolicy

Alla nya evals bör följa `tests/evals/framework/README.md`.

Kärnkrav:
- stabilt test-ID,
- tydlig kategori,
- prompt,
- förväntat beteende,
- must_include/must_not_include när relevant,
- severity,
- pass/fail-kriterier.

Critical FAIL ska blockera release.
Regressionsfel ska alltid få ett permanent evaltest.
