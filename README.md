# Aseprite Auto Build

[![Auto build Aseprite](https://github.com/hardingadonis/aseprite-auto-build/actions/workflows/auto-build.yml/badge.svg)](https://github.com/hardingadonis/aseprite-auto-build/actions/workflows/auto-build.yml)
![GitHub contributors](https://img.shields.io/github/contributors/hardingadonis/aseprite-auto-build)
![GitHub top language](https://img.shields.io/github/languages/top/hardingadonis/aseprite-auto-build)
![GitHub repo size](https://img.shields.io/github/repo-size/hardingadonis/aseprite-auto-build)
![GitHub License](https://img.shields.io/github/license/hardingadonis/aseprite-auto-build)

> Auto build Aseprite via GitHub Actions

## About:

[Aseprite](https://www.aseprite.org/) is a popular animated sprite editor and pixel art tool. While Aseprite is a paid application, its [source code is publicly available](https://github.com/aseprite/aseprite) and can be compiled for free under its [EULA](https://github.com/aseprite/aseprite/blob/main/EULA.md).

This project uses **GitHub Actions** to automatically:

1. Fetch the latest stable release of Aseprite from the official repository
2. Download the required [Skia](https://github.com/aseprite/skia) library
3. Compile Aseprite for **Windows x64**
4. Publish the compiled binary as a GitHub Release

This means you can simply use this repository as a template and get a ready-to-use Aseprite build without needing to set up a local build environment.

> [!IMPORTANT]  
> Only supports Windows x64  
> **MUST INSTALL OpenSSL v3 BEFORE RUNNING ASEPRITE**

## Requirements:

### OpenSSL v3 Installation (Required)

Before running Aseprite, you **must** install OpenSSL v3 on your Windows system. Without this, you will encounter the following error:

![OpenSSL Error](images/error.png)

**Error message:** `The code execution cannot proceed because libcrypto-3-x64.dll was not found`

**Solution:**

1. Download OpenSSL v3 for Windows from: [https://slproweb.com/products/Win32OpenSSL.html](https://slproweb.com/products/Win32OpenSSL.html)
2. Install the **Win64 OpenSSL v3.x.x** (NOT the Light version)
3. During installation, make sure to select the option to copy OpenSSL DLLs to the Windows system directory
4. Restart your computer after installation
5. Run Aseprite

## Usage:

- Click `Use this template` to create a new repository.
- Wait for the build to complete.
- Download the built Aseprite from the releases.
- **Install OpenSSL v3** (see Requirements section above).
- Run Aseprite.

## YouTube:

[![YouTube](https://img.youtube.com/vi/Qx4GaWHLt40/0.jpg)](https://www.youtube.com/watch?v=Qx4GaWHLt40)

## Contributors:

<a href="https://github.com/hardingadonis/aseprite-auto-build/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=hardingadonis/aseprite-auto-build" />
</a>

## Licenses:

- [Auto Build Aseprite](https://github.com/hardingadonis/aseprite-auto-build) is under the [MIT license](https://github.com/hardingadonis/aseprite-auto-build/blob/main/LICENSE).
