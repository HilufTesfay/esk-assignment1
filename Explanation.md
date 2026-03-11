# Here are the  Bugs and Fixes as follow

## Bug 1: Shared Header Mutation
- Bug: The request method mutated the caller-provided headers dictionary.
- Cause: Dictionaries are mutable; in-place assignment updated the original object.
- Fix: Copy headers before adding auth so changes stay local.

## Bug 2: Token Type Handling
- Bug: A dict token bypassed refresh and lacked `.as_header()`, so auth was missing.
- Cause: The refresh check only handled `None` or expired `OAuth2Token`; dicts are truthy.
- Fix: Require `OAuth2Token` via `isinstance`; otherwise refresh to a valid object.

## Bug 3: UTC vs Local Time
- Bug: `token_from_iso` produced different epoch values depending on server timezone for a "Z" timestamp.
- Cause: Naive/aware handling let `.timestamp()` apply local offsets.
- Fix: Force UTC-aware datetime before converting to epoch.

## Note on Validation Logic
Input validation (eg, malformed strings or empty fields) is excluded from this scope. 
These fixes prioritize state integrity, type safety, and timezone consistency within the core request flow.
