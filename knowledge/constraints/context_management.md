# Context management constraints (from research)

- Budget tokens per request; compact when estimated tokens exceed ~80% of budget.
- Keep system + tools (cached) + last K turns verbatim; summarize the middle.
- Clear raw tool results beyond a window, keeping only summaries.
- Keep intermediate values in a per-run state dict; inject compact summary into
  messages, not full data (scratchpad vs messages).
- Use just-in-time retrieval for long-term memory; don't always inject.
- Prompt cache: stable prefixes first, volatile content last. Never put timestamps
  or user-specific data in the cached prefix.
- Anthropic cache order: tools -> system -> messages. 5-min TTL default (refreshed
  free on use); reads 0.1x, writes 1.25x/2x.
- Over-specified prompts hurt with stronger models; calibrate to the model.