# nilan_proxy

Library that talks to Nilan Gateway and Genvex Connect ventilation units over the
Nabto/uNabto UDP protocol. Published to PyPI as `nilan_proxy` and consumed by the
Home Assistant integration [nilan_connect](https://github.com/HairingX/nilan_connect).

The library must stay usable outside Home Assistant. Anything Home Assistant
specific belongs in `nilan_connect`, not here.

## Layout

| Path | Purpose |
|---|---|
| `src/nilan_proxy/nilan_proxy.py` | Socket, discovery, connection and the receive thread |
| `src/nilan_proxy/nilan_proxy_modeladapter.py` | Maps a device to a model, decodes responses, holds values |
| `src/nilan_proxy/models/basemodel.py` | Point keys, typed dicts, units, `DEFAULT_CONFIGS` |
| `src/nilan_proxy/models/*.py` | One file per controller model |
| `src/nilan_proxy/const.py` | Timings and intervals |
| `test/` | unittest suite, run from inside `test/` |

## Releasing

**The version is never edited by hand, and the draft release is never published by
hand.** Both are done for you, and doing either yourself breaks the release. See the
pitfalls below.

1. **Merge a pull request into `main`.** `.github/workflows/release-drafter.yml`
   creates or updates a **draft release**, computing the next version and writing the
   changelog from merged pull request titles.
2. **Check the draft** at
   [releases](https://github.com/HairingX/nilan_proxy/releases). It is named `vX.Y.Z`
   and holds the accumulated notes since the last release.
3. **Run the `Release` workflow from the Actions tab.** That is the release step.
   Do not press Publish on the draft.

`Release` takes an optional version. Leave it empty and it reads the version from the
newest draft; fill it in to jump a minor or major without relabelling merged pull
requests. Either way it hands the version to the composite action in
`.github/actions/release-publish`, which does the whole thing in one direction:

```
validate version -> check the tag is free -> check PyPI does not have it
-> bump __version__ -> commit -> push -> tag -> build -> verify the built version
-> capture the draft body, delete the draft -> gh release create -> publish to PyPI
```

**There is deliberately only one release workflow.** PyPI verifies the workflow
filename, so a release cut from any other file would tag and publish on GitHub but
never reach PyPI, leaving `nilan_connect` unable to install the version it pins.

### How the next version number is chosen

`.github/release-drafter.yml` resolves it from the labels on the merged pull
requests:

| Label on the PR | Result |
|---|---|
| `major` | major bump |
| `minor` | minor bump |
| `patch` | patch bump |
| no label | **patch bump**, this is the default |

The same file groups the changelog by label (`breaking-change`, `enhancement` /
`feature request`, `bug` / `fix` / `bugfix`, `chore`, `dependencies`) and drops
anything labelled `skip-changelog`. An autolabeler adds `bug` for branches named
`fix/...` and `feature request` for `feature/...`.

So: **to release anything other than a patch, label the pull request before merging
it**, or type the version into `Release`.

### Pitfall: never publish the draft by hand

Publishing the draft creates the tag immediately, at whatever `main` points to. The
version bump would then land *after* the tag, so the tag would carry the previous
version. That is exactly what the old event driven workflow did, and every tag it
produced is wrong:

```
tag v1.0.1 -> __version__ says 1.0.0
tag v1.0.2 -> __version__ says 1.0.1
```

`Release` bumps, commits and only then tags, so the tag and the code agree.
Publishing by hand also builds and uploads nothing at all now, because nothing
listens for `release: published` any more.

### Pitfall: PyPI is bound to release.yml

Trusted publishing verifies the repository and the **workflow filename**, both of
which are required in the publisher configuration. The OIDC token is bound to the
workflow, so a workflow at `foo.yml` cannot impersonate one at `bar.yml`. Renaming
`release.yml` therefore breaks the upload, silently. It is also why the release is a
single workflow with an optional version input rather than a second file: a second
file could not publish to PyPI.

The **GitHub environment is optional** in the publisher configuration, and for this
project it is currently unset, meaning PyPI accepts a publish from any environment.
The `environment: pypi` in `release.yml` is therefore declared but not enforced on
PyPI's side. PyPI recommends constraining it, and once that is done the environment
name becomes part of the binding too and must not be renamed either.

PyPI refuses to overwrite an existing version, so the composite action checks up
front and fails before tagging rather than after.

### Coordinating with nilan_connect

`nilan_connect/custom_components/nilan_connect/manifest.json` pins this library under
`requirements`, and Home Assistant pip installs it from PyPI. A new pin cannot be
installed until the matching version exists there, so **release `nilan_proxy` first,
then `nilan_connect`.**

## Tests

```
cd test
python3 -m unittest discover -s . -p "test_*.py"
```

They must be run from inside `test/`; `common.py` puts `../src` on the path.
`.github/workflows/test.yml` runs them on push and pull request for Python 3.12,
3.13 and 3.14.

`test/modelTester.py` holds the checks every model must pass. A new model gets a
subclass that sets `loadedModel`, `expectedName` and `expectedManufacturer`, and
inherits all of them.

## Things that have bitten us

- **Class attributes are shared.** `datapoints`, `setpoints`, `_configs`,
  `_values` and the handler collections are declared on the class for typing.
  Every one of them must be rebound in `__init__`, or two models or two devices in
  the same process silently share state.
- **Entries in `DEFAULT_CONFIGS` are shared objects.** `set_default_configs`
  copies them. Never write into a config you did not copy first.
- **Order inside `__init__` matters.** `NilanProxyCTS602` looks up `self._quirks`
  while building its point set, so the quirk table has to be defined first.
- **The receive thread swallows everything.** `_receive_thread` catches every
  exception and logs one line. A model that raises during loading therefore
  surfaces to the user as a setup timeout with no hint of the real cause. Test
  model loading rather than relying on it failing loudly.
- **`_is_connected` is not availability.** It gates polling and reconnecting; if
  you clear it when a device goes silent, the reconnect logic stops and the device
  never comes back. Availability is `is_available()` and is derived from
  `_last_response`.
- **The device address is a cache, not configuration.** The device id is the
  stable identity. Discovery refreshes the address, which is what lets a unit
  change DHCP lease without breaking anything. Do not store an address as if it
  were permanent, and do not accept a hostname where an address is expected.
