import os
from flask import Blueprint, render_template, redirect, url_for, flash
from Utilities.Header2HTMLConverter import Header2HTMLConverter
# <editor-fold desc="[SDK imports]">
# iOS 13.5
from SDKs.iOS135.layout import Frameworks as iOS135Framework
from SDKs.iOS135.layout_priv import Frameworks as iOS135PrivateFramework
from SDKs.iOS135.layout_libs import Libs as iOS135Libs
from SDKs.iOS135.layout_protocols import Protocols as iOS135Protocols

# iOS 12.4
from SDKs.iOS124.layout import Frameworks as iOS124Framework
from SDKs.iOS124.layout_priv import Frameworks as iOS124PrivateFramework
from SDKs.iOS124.layout_libs import Libs as iOS124Libs
from SDKs.iOS124.layout_springboard import SBLayout as iOS124SpringBoardProtocol
# </editor-fold>


FirmwareTable = {
    "13.5": {
        "FolderName": "iOS135",
        "Frameworks": iOS135Framework,                  # Folder
        "PrivateFrameworks": iOS135PrivateFramework,    # Folder
        "Libraries": iOS135Libs,        # Folder
        "Protocols": iOS135Protocols,    # Files!
        "OtherName": "Protocols",
        "Dumper": "Runtime Browser"
    },
    "12.4": {
        "FolderName": "iOS124",
        "Frameworks": iOS124Framework,
        "PrivateFrameworks": iOS124PrivateFramework,
        "Libraries": iOS124Libs,
        "Protocols": iOS124SpringBoardProtocol,
        "OtherName": "SpringBoard",
        "Dumper": "class-dump"
    }
}

BrowserBP = Blueprint("BrowserBP", __name__)
convH2Web = Header2HTMLConverter()


# <editor-fold desc="[Getters]">
@BrowserBP.route('/<ios_version>/Frameworks/<framework>/<file>')
def getFFile(ios_version, framework, file):
    if ios_version in FirmwareTable:
        print("Found OS VERSION")
        for item in FirmwareTable[ios_version]["Frameworks"]:
            if item == framework:
                print("FOUND FRAMEWORK")
                files = []
                fpath = "./SDKs/" + FirmwareTable[ios_version]["FolderName"] + "/Frameworks/" + item
                for (dirpath, dirnames, filenames) in os.walk(fpath):
                    files.extend(filenames)
                    break
                for fn in files:
                    if fn == file:
                        html_s = convH2Web.getHTMLString(fpath + "/" + file)
                        return render_template('Browser.html', content=html_s, iosv=ios_version, frameworkName=framework, fileName=file)
                return redirect(url_for('BrowserBP.listFrameworksF', ios_version=ios_version, framework=framework))
        return redirect(url_for('BrowserBP.listFrameworks', ios_version=ios_version))
    return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/PrivateFrameworks/<framework>/<file>')
def getPFFile(ios_version, framework, file):
    if ios_version in FirmwareTable:
        print("Found OS VERSION")
        for item in FirmwareTable[ios_version]["PrivateFrameworks"]:
            if item == framework:
                print("FOUND FRAMEWORK")
                files = []
                fpath = "./SDKs/" + FirmwareTable[ios_version]["FolderName"] + "/PrivateFrameworks/" + item
                for (dirpath, dirnames, filenames) in os.walk(fpath):
                    files.extend(filenames)
                    break
                for fn in files:
                    if fn == file:
                        html_s = convH2Web.getHTMLString(fpath + "/" + file)
                        return render_template('Browser.html', content=html_s, iosv=ios_version, frameworkName=framework, fileName=file, private=True)
                return redirect(url_for('BrowserBP.listPrivateFrameworksF', ios_version=ios_version, framework=framework))
        return redirect(url_for('BrowserBP.listPrivateFrameworks', ios_version=ios_version))
    return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/lib/<library>/<file>')
def getLFile(ios_version, library, file):
    if ios_version in FirmwareTable:
        print("Found OS VERSION")
        for item in FirmwareTable[ios_version]["Libraries"]:
            if item == library:
                print("FOUND LIB")
                files = []
                fpath = "./SDKs/" + FirmwareTable[ios_version]["FolderName"] + "/lib/" + item
                for (dirpath, dirnames, filenames) in os.walk(fpath):
                    files.extend(filenames)
                    break
                for fn in files:
                    if fn == file:
                        html_s = convH2Web.getHTMLString(fpath + "/" + file)
                        return render_template('Browser.html', content=html_s, iosv=ios_version, isLib=True, lib=library, fileName=file)
                return redirect(url_for('BrowserBP.listLibrariesF', ios_version=ios_version, library=library))
        return redirect(url_for('BrowserBP.listLibraries', ios_version=ios_version))
    return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/other/<file>')
def getPRTCLFile(ios_version, file):
    if ios_version in FirmwareTable:
        print("Found OS VERSION")
        for item in FirmwareTable[ios_version]["Protocols"]:
            if item == file:
                print("FOUND FILE")
                fpath = "./SDKs/" + FirmwareTable[ios_version]["FolderName"] + "/" + FirmwareTable[ios_version]["OtherName"] + "/" + item
                html_s = convH2Web.getHTMLString(fpath)
                return render_template('Browser.html', content=html_s, iosv=ios_version, fileName=file, isOther=True, oName=FirmwareTable[ios_version]["OtherName"])
        return redirect(url_for('BrowserBP.listProtocols', ios_version=ios_version))
    return redirect(url_for('BrowserBP.listiOSV'))
# </editor-fold>


# <editor-fold desc="[List SDK Contents' FILES]">
@BrowserBP.route('/<ios_version>/Frameworks/<framework>')
def listFrameworksF(ios_version, framework):
    if ios_version in FirmwareTable:
        for item in FirmwareTable[ios_version]["Frameworks"]:
            if item == framework:
                files = []
                fpath = "./SDKs/" + FirmwareTable[ios_version]["FolderName"] + "/Frameworks/" + item
                for (dirpath, dirnames, filenames) in os.walk(fpath):
                    files.extend(filenames)
                    break
                return render_template('Browser.html', iosv=ios_version, frameworkName=framework, entries=files, linkType=1)
        return redirect(url_for('BrowserBP.listFrameworks', ios_version=ios_version))
    return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/PrivateFrameworks/<framework>')
def listPrivateFrameworksF(ios_version, framework):
    if ios_version in FirmwareTable:
        for item in FirmwareTable[ios_version]["PrivateFrameworks"]:
            if item == framework:
                files = []
                fpath = "./SDKs/" + FirmwareTable[ios_version]["FolderName"] + "/PrivateFrameworks/" + item
                for (dirpath, dirnames, filenames) in os.walk(fpath):
                    files.extend(filenames)
                    break
                return render_template('Browser.html', iosv=ios_version, frameworkName=framework, entries=files, linkType=2, private=True)
        return redirect(url_for('BrowserBP.listPrivateFrameworks', ios_version=ios_version))
    return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/lib/<library>')
def listLibrariesF(ios_version, library):
    if ios_version in FirmwareTable:
        for item in FirmwareTable[ios_version]["Libraries"]:
            if item == library:
                files = []
                fpath = "./SDKs/" + FirmwareTable[ios_version]["FolderName"] + "/lib/" + item
                for (dirpath, dirnames, filenames) in os.walk(fpath):
                    files.extend(filenames)
                    break
                return render_template('Browser.html', iosv=ios_version, isLib=True, lib=library, entries=files, linkType=5)
        return redirect(url_for('BrowserBP.listPrivateFrameworks', ios_version=ios_version))
    return redirect(url_for('BrowserBP.listiOSV'))
# </editor-fold>


# <editor-fold desc="[List SDK Content Folder]">
@BrowserBP.route('/<ios_version>/Frameworks/available')
def listFrameworks(ios_version):
    if ios_version in FirmwareTable:
        return render_template('Browser.html', iosv=ios_version, entries=FirmwareTable[ios_version]["Frameworks"], linkType=3)
    else:
        return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/PrivateFrameworks/available')
def listPrivateFrameworks(ios_version):
    if ios_version in FirmwareTable:
        return render_template('Browser.html', iosv=ios_version, entries=FirmwareTable[ios_version]["PrivateFrameworks"], private=True, linkType=4)
    else:
        return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/lib/available')
def listLibraries(ios_version):
    if ios_version in FirmwareTable:
        return render_template('Browser.html', iosv=ios_version,
                               entries=FirmwareTable[ios_version]["Libraries"], linkType=5, isLib=True)
    else:
        return redirect(url_for('BrowserBP.listiOSV'))


@BrowserBP.route('/<ios_version>/other/available')
def listProtocols(ios_version):
    if ios_version in FirmwareTable:
        return render_template('Browser.html', iosv=ios_version,
                               entries=FirmwareTable[ios_version]["Protocols"], linkType=7, isOther=True, oName=FirmwareTable[ios_version]["OtherName"])
    else:
        return redirect(url_for('BrowserBP.listiOSV'))
# </editor-fold>


# <editor-fold desc="[Other Components]">
@BrowserBP.route('/available')
def listiOSV():
    available_iOS = FirmwareTable.keys()
    return render_template('iOSPicker.html', entries=available_iOS)


@BrowserBP.route('/<ios_version>/available')
def listSDKOptions(ios_version):
    return render_template('Categories.html', iosv=ios_version)
# </editor-fold>
