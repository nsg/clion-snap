# clion-snap
[![Snap Status](https://build.snapcraft.io/badge/nsg/clion-snap.svg)](https://build.snapcraft.io/user/nsg/clion-snap)

This is the source of the snap `clion-nsg`, if you like to contribute please make a PR. Feel free to open a issue if you have any comments or need help.

## Install

```
sudo snap install clion-nsg --classic
```

The snap works without --classic but then it do not have access to your build tools like compiler or so. If you chooses to install it without classic make sure to remember to connect the home plug.

## Security

The snap is build with the build service, all code is here for you to inspect. It's not really sandboxed when we use classic-mode, but it's no worse than the official way to run it.

## Why this?

* For me it's a more convenient way to install it on several systems
* It was fun to try to package something a little different
* A chance to use my newly learnt Python GTK3 skills
