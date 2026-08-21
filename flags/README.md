# Overview

These are flag style markers used for test cases that need specific strings to
search for in a repo.

# Format

```ebnf
flag   = prefix "{" value "}"
prefix = "LTKF"
value  = "secret" | "cui" | "infra" | "ioc" | "pii" | "vuln" | "phi"
```
