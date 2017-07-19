# clion-snap
[![Snap Status](https://build.snapcraft.io/badge/nsg/clion-snap.svg)](https://build.snapcraft.io/user/nsg/clion-snap)

This is the source of the snap `clion-nsg`, if you like to contribute please make a PR. Feel free to open a issue if you have any comments or need help.

## Install

```
sudo snap install --classic clion-nsg
```

## Build

```
snapcraft cleanbuild
sudo snap install --dangerous --classic clion-nsg*.snap
```

Note: cleanbuild requires a local working copy of LXD. To build it outside a container use `build`.

## Security

The snap is build with the build service, all code is here for you to inspect. It's not really sandboxed when we use classic-mode, but it's no worse than the official way to run it.

## Why this?

* For me it's a more convenient way to install it on several systems
* It was fun to try to package something a little different
* A chance to use my newly learnt Python GTK3 skills
