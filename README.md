# Heads In The Cloud
> iOS Public & Private Headers | Python 3.6+ | Fast | Any SDK

## Introduction
_Heads In The Cloud_ is a Flask-app to serve header files. 

This is reminiscent to Limneos' iOS Header service and serves as alternative to it.

Features:
- Syntax Highlighting of Headers
- Barebone and Modular: Add SDKs on the fly
- Simple and intuitive UX

iOS 13.5 and iOS 12.4 Headers are included/ should be shipped by default (date: 12.06.2020)
## Installation Guide
Prerequisites:
- VPS (any Linux distro)
- Python3
- Flask, Pygments
- regular webstack

Ensure that your VPS is capable of running a regular Flask HelloWorld. If you are able to, then setting this up will be analogous to the HelloWorld.
## Extensibility / SDK Management
_HITC_ allows you to add and remove SDKs as needed. the following structure is accepted as "SDK":
```
<iOSVersion>
    |_Frameworks
    |   |_<framework>.framework
    |       |_<headers>    <-- .h Files!
    |_lib
    |   |_<libName>
    |       |_<headers>
    |_PrivateFrameworks
    |   |_<framework>.framework
    |       |_<headers>
    |_<Other>
    |   |_<headers>
```
Once this is given, we'll _"cache"_ the directory into a dictionary. See the `layout.py` for example!

Finally, goto the `BrowserBP`'s route and add another entry in the `FirmwareTable` as follows:
```
# Assuming you have imported appropriately, this is the new entry:
# Example: Add iOS 14.0 SDK
"14.0": {
    "FolderName": "iOS140",
    "Frameworks": MyImportediOSFrameworkDict,
    "PrivateFramework": MyImportediOSPrivateFrameworkDict,
    "Libraries": MyImportediOSLibsDict,
    "Protocols": MyImportediOS<Other>Dict,
    "OtherName": <Other>,
    "Dumper": <dumping-tool-name>
}

```

And there you go, new SDK added!


If there are any questions regarding _HITC_, please do email me under saadatdev (at) googlemail (dot) com

## Extras
- An optimization idea would be to create indiviual html files for each header. Keeping everything static & with the help of pygments actually doable.

## Credits
- Limneos - Original iOS Headers' Webpage
- Amarytha - HeadsInTheCloud Icon
- Local Pigeon Gang - always scoutin'

## License
**THIS PROJECT IS LICENSED UNDER THE AGPLv3**
