# Template Mod Generator
A Python script that can be used instead of the [Fabric Template Mod Generator](https://fabricmc.net/develop/template/)

# Changes
This is an overview of why using this is different from using the normal generator.
* Set an author placeholder for all projects
* Set a package placeholder for all projects
* Build.gradle is setup to make more descriptive jar names (mod-id-v1.0.0+mc1.21.5.jar)
* Sources jar is disabled from generating by default
* MIT License by default
* Autofill for most of the fabric.mod.json (description and links are default)
* Copying files is faster than downloading new ones

# Setup/Usage
You will need Python 3 and Selenium

`python`

`pip install selenium`

Selenium is used to automatically grab the latest version for Fabric, Yarn, and Loom based on your requested Minecraft version from the [Fabric Development Page](https://fabricmc.net/develop/). This is the slowest part of the script, but the entire process still only takes a few seconds after you are done inputting information.

Set your author name and modding package in `ModMakerUtils.py`, then run `ModMaker.py` and enter the name of the new mod, the Minecraft version, and its environment.

# Misc
Everyone is welcome to create their own alterations based on their needs (maybe you don't like my naming scheme, or want a different LICENSE).

If you need any help with setup, usage, alterations, or fabric modding in general, then join my [Discord](https://discord.gg/ZCaGkZeb4C).
