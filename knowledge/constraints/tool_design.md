# Tool design constraints (from research)

- Descriptions state when to invoke + how to build arguments.
- Developer instructions disambiguate similar tools and preferred ordering.
- Similarity/overlap matters more than raw count: >15 distinct tools OK; <10
  overlapping tools can fail.
- Require absolute filepaths (poka-yoke) - fixed SWE-bench errors.
- Choose formats the model writes easily (close to natural text, no formatting
  overhead); give tokens to think.
- Return structured errors for retry, never raise into the loop.
- Cross-provider schema: {name, description, parameters} (JSON Schema). OpenAI
  strict: all params in required, additionalProperties false.
- Run read-only/concurrency_safe tools in parallel (asyncio.gather); stateful
  tools sequentially in call order.
- Iterate descriptions with held-out tasks; collect metrics; avoid overfitting.