# clion-snap
[![Snap Status](https://build.snapcraft.io/badge/nsg/clion-snap.svg)](https://build.snapcraft.io/user/nsg/clion-snap)

This is the source of the snap `clion-nsg`, if you like to contribute please make a PR. Feel free to open a issue if you have any comments or need help.

## Install

```
sudo snap install --classic clion-nsg
```

Note: because we use classic mode for this snap it's somewhat dependent on your base system. I have only tested it under Ubuntu.

## Build

```
snapcraft cleanbuild
sudo snap install --dangerous --classic clion-nsg*.snap
```

Note: cleanbuild requires a local working copy of LXD. To build it outside a container use `build`.

## Security

The snap is build with the build service, all code is here for you to inspect. It's not really sandboxed when we use classic-mode, but it's no worse than the official way to run it.

## Why classic?

A normal snap with strict mode has the filesystem from the `core` snap mounted as /, and a few cherry picked folders like `$SNAP_DATA`, `$SNAP_USER_DATA`, ... are mounted in. `core` is a stable Ubuntu install that you can target and it do not matter if we are running Ubuntu 18.04, 15.10 or even Fedora.

In classic mode your real filesystem is used as /, meaning that the snap can access and use all software that you have installed on your system. This is important for CLion that not only is a editor but also calls gcc, cmake and so on.

It's of course possible to run CLion in strict mode, connect the home plug to grant it access to `$HOME` and bundle all build tools inside the snap. The biggest problem with that is that you may need a specific version of gcc, or cmake or some other tool. With classic mode everything just works like you expect.

## Why this?

* For me it's a more convenient way to install it on several systems
* It was fun to try to package something a little different
* A chance to use my newly learnt Python GTK3 skills
