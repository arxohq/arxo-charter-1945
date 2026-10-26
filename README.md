# arxo-charter-1945

[![LightNow capabilities](https://lightnow.ai/badge/io.arxo/charter)](https://lightnow.ai/servers/io.arxo/charter)

Pinned canon, executable as it stands: source text with provenance, the
model built over it and the scenarios that check its answers. The norms
here are data — they are executed by `law`; this repository carries no
rule code of its own.

## Contents

| Package | Version | Scenarios | Dependencies |
|---|---|---|---|
| `doctrine.iura_humana` | 0.1.0 | 1 | 0 |
| `un.charter` | 0.1.0 | 169 | 1 |

## How it is verified

Every package is built by `package.py` with the pinned toolchain: compilation,
§267 scenarios on both evaluators, replay of saved evaluations and a rebuild
from the release itself. A failure of any step stops the build.

```sh
python3 tools/toolchain.py download --lock toolchain.lock.json --out /tmp/law-tools
python3 /tmp/law-tools/package.py packages/<name> \
    --lawc /tmp/law-tools/law-cli --offline --out /tmp/<name>-release
```

## Dependencies

Dependency bytes are pinned under `packages/<name>/deps/` and verified against the `contentHash` recorded in `law.lock`: the build and the CI are offline.

## Worked cases

Each collection is a case package of its own: the facts, the questions and
the answers, with the pinned canon as its dependency. Ask one from its
directory with `law ask .` — nothing is downloaded.

| Collection | Cases | Questions |
|---|---:|---:|
| [`packages/un.charter/examples/amendment`](packages/un.charter/examples/amendment/README.md) | 7 | 9 |
| [`packages/un.charter/examples/army-and-authorization`](packages/un.charter/examples/army-and-authorization/README.md) | 5 | 2 |
| [`packages/un.charter/examples/article-51-silence`](packages/un.charter/examples/article-51-silence/README.md) | 11 | 5 |
| [`packages/un.charter/examples/binding-or-not`](packages/un.charter/examples/binding-or-not/README.md) | 9 | 10 |
| [`packages/un.charter/examples/membership-arc`](packages/un.charter/examples/membership-arc/README.md) | 7 | 7 |
| [`packages/un.charter/examples/pacific-settlement`](packages/un.charter/examples/pacific-settlement/README.md) | 7 | 8 |
| [`packages/un.charter/examples/same-vote`](packages/un.charter/examples/same-vote/README.md) | 6 | 8 |

## Rights

Code and model: see `LICENSE`. The pinned texts of the publishers keep their
own terms of reproduction, listed per package in `NOTICE`; those terms are
not covered by the code licence.

Maintainer: Rifat Dzhumagulov (hi@arxo.io). Address: https://github.com/arxohq/arxo-charter-1945.
