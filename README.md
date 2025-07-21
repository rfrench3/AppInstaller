# AppInstaller

AppInstaller is an application that allows users to point-and-click install any kind of application file by integrating various popular programs for each format. It integrates distrobox for distro-specific packages, uses flatpak for flatpak packages, (uncertain) uses Gearlever for appimages, and (uncertain) uses marcosnils/bin for binaries.

<hr>

Select file:

- [ ] deb
- [ ] rpm
- [ ] appimage
- [ ] flatpak
- [ ] tars
<hr>

Install files by interfacing with:

- [ ] rpm/deb: distrobox
- [ ] appimage: gearlever, if possible
- [ ] flatpak: flatpak
- [ ] tars: marcosnils/bin fork or upstream PR that accepts local files and not just websites
