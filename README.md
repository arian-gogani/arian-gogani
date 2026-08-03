## Nobulex

**The independent reliability registry for agent tools.**

An agent calls a tool. The tool returns a response that is well formed, plausible, and materially wrong. Empty where it should have been populated. Stale while claiming to be current. Scoped to a different entity than the one requested. Truncated with no signal that anything was cut. Nothing raises, nothing logs, and the schema validates, because a well formed lie validates perfectly.

Uptime does not measure that. Stars do not measure it. A green CI badge does not measure it. Every existing reliability signal in this ecosystem answers "did it respond." None of them answer "was the response true."

One test: **does it fail loud, or does it lie quiet?**

Financial data first, because it is the one category where the right answer is unambiguous, timestamped, and independently obtainable.

### Where it is

[**nobulex-registry**](https://github.com/arian-gogani/nobulex-registry) is the method: the harness that speaks raw JSON-RPC to a subject and never imports its code, the self-test that runs every classifier against fixtures known to be bad, and the publication gate. MIT.

[**nobulex.com**](https://nobulex.com) is the register, the method, and the argument. The argument is written to be attacked.

### The state of it, plainly

Every record this registry has issued is held under right of reply. Nothing is published, no reply window has opened, and no verdict here is checkable by a stranger yet. No buyer has paid. The site says all of that on its own pages, because a project whose product is grading other people's honesty does not get to round its own status up.

One thing is checkable right now:

```
curl -sS https://nobulex.com/register | shasum -a 256
```

That should equal the hash of `brand/register.html` in the registry repository. The page is compiled from the records by a generator that writes identical bytes to every publish target in a single build, so no hand reaches the page in between. A downstream copy step is a second author, and a second author of that page is a second chance to publish a name that is under embargo. If those two hashes ever disagree, something edited the published page afterward, and it is worth saying so loudly.

### Elsewhere

Earlier work under the same name is at [nobulex](https://github.com/arian-gogani/nobulex), kept rather than deleted, with a header saying what changed.

[nobulex.com](https://nobulex.com) · [@AGoganiii](https://x.com/AGoganiii) · nobulex.dev@gmail.com
