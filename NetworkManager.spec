#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : NetworkManager
Version  : 1.42.6
Release  : 98
URL      : https://download.gnome.org/sources/NetworkManager/1.42/NetworkManager-1.42.6.tar.xz
Source0  : https://download.gnome.org/sources/NetworkManager/1.42/NetworkManager-1.42.6.tar.xz
Summary  : Convenience library for clients of NetworkManager
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0 LGPL-2.1
Requires: NetworkManager-autostart = %{version}-%{release}
Requires: NetworkManager-bin = %{version}-%{release}
Requires: NetworkManager-config = %{version}-%{release}
Requires: NetworkManager-data = %{version}-%{release}
Requires: NetworkManager-lib = %{version}-%{release}
Requires: NetworkManager-libexec = %{version}-%{release}
Requires: NetworkManager-license = %{version}-%{release}
Requires: NetworkManager-locales = %{version}-%{release}
Requires: NetworkManager-man = %{version}-%{release}
Requires: NetworkManager-services = %{version}-%{release}
Requires: dhcp
Requires: ppp
BuildRequires : ModemManager-dev
BuildRequires : bluez-dev
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : buildreq-kde
BuildRequires : curl-dev
BuildRequires : dbus-dev
BuildRequires : dbus-glib-dev
BuildRequires : dhcp
BuildRequires : dnsmasq
BuildRequires : docbook-xml
BuildRequires : elfutils
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : iptables
BuildRequires : iptables-dev
BuildRequires : jansson-dev
BuildRequires : libndp-dev
BuildRequires : libnl-dev
BuildRequires : libsoup-dev
BuildRequires : libxslt-bin
BuildRequires : linux-firmware-wifi
BuildRequires : mobile-broadband-provider-info
BuildRequires : ncurses-dev
BuildRequires : newt-dev
BuildRequires : nss-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(bluez)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(mobile-broadband-provider-info)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(uuid)
BuildRequires : ppp-dev
BuildRequires : pygobject
BuildRequires : readline-dev
BuildRequires : systemd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-clr-all-ifs-option.patch

%description
There is a client library in Python, named python-networkmanager.
This library is developed outside of the core NetworkManager project.

%package autostart
Summary: autostart components for the NetworkManager package.
Group: Default

%description autostart
autostart components for the NetworkManager package.


%package bin
Summary: bin components for the NetworkManager package.
Group: Binaries
Requires: NetworkManager-data = %{version}-%{release}
Requires: NetworkManager-libexec = %{version}-%{release}
Requires: NetworkManager-config = %{version}-%{release}
Requires: NetworkManager-license = %{version}-%{release}
Requires: NetworkManager-services = %{version}-%{release}

%description bin
bin components for the NetworkManager package.


%package config
Summary: config components for the NetworkManager package.
Group: Default

%description config
config components for the NetworkManager package.


%package data
Summary: data components for the NetworkManager package.
Group: Data

%description data
data components for the NetworkManager package.


%package dev
Summary: dev components for the NetworkManager package.
Group: Development
Requires: NetworkManager-lib = %{version}-%{release}
Requires: NetworkManager-bin = %{version}-%{release}
Requires: NetworkManager-data = %{version}-%{release}
Provides: NetworkManager-devel = %{version}-%{release}
Requires: NetworkManager = %{version}-%{release}

%description dev
dev components for the NetworkManager package.


%package doc
Summary: doc components for the NetworkManager package.
Group: Documentation
Requires: NetworkManager-man = %{version}-%{release}

%description doc
doc components for the NetworkManager package.


%package extras
Summary: extras components for the NetworkManager package.
Group: Default

%description extras
extras components for the NetworkManager package.


%package lib
Summary: lib components for the NetworkManager package.
Group: Libraries
Requires: NetworkManager-data = %{version}-%{release}
Requires: NetworkManager-libexec = %{version}-%{release}
Requires: NetworkManager-license = %{version}-%{release}

%description lib
lib components for the NetworkManager package.


%package libexec
Summary: libexec components for the NetworkManager package.
Group: Default
Requires: NetworkManager-config = %{version}-%{release}
Requires: NetworkManager-license = %{version}-%{release}

%description libexec
libexec components for the NetworkManager package.


%package license
Summary: license components for the NetworkManager package.
Group: Default

%description license
license components for the NetworkManager package.


%package locales
Summary: locales components for the NetworkManager package.
Group: Default

%description locales
locales components for the NetworkManager package.


%package man
Summary: man components for the NetworkManager package.
Group: Default

%description man
man components for the NetworkManager package.


%package services
Summary: services components for the NetworkManager package.
Group: Systemd services
Requires: /usr/bin/busctl
Requires: systemd

%description services
services components for the NetworkManager package.


%prep
%setup -q -n NetworkManager-1.42.6
cd %{_builddir}/NetworkManager-1.42.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1682360796
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static --enable-ppp \
--disable-teamdctl \
--with-nmcli=yes \
--disable-json-validation \
--with-config-plugins-default=keyfile \
--with-dhclient=/usr/libexec/dhclient \
--with-session-tracking=systemd \
--with-suspend-resume=systemd \
--with-systemd-logind=yes \
--with-systemd-journal=yes \
--enable-modify-system \
--enable-polkit-agent \
--enable-polkit=yes \
--with-kernel-firmware-dir=/usr/lib/firmware \
--with-dbus-sys-dir=/usr/share/dbus-1/system.d \
--enable-wifi \
--enable-bluez5-dun \
--with-system-ca-path=/var/cache/ca-certs/anchors \
--with-iptables=/usr/bin/iptables \
--disable-ovs \
--with-modem-manager-1 \
--with-libnm-glib \
--with-iwd \
PYTHON=/usr/bin/python3 --with-nmtui=yes
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1682360796
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/NetworkManager
cp %{_builddir}/NetworkManager-%{version}/COPYING %{buildroot}/usr/share/package-licenses/NetworkManager/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/NetworkManager-%{version}/COPYING.GFDL %{buildroot}/usr/share/package-licenses/NetworkManager/7205ad2e7451e9c4a518d105d5144987cdaf9bfa || :
cp %{_builddir}/NetworkManager-%{version}/COPYING.LGPL %{buildroot}/usr/share/package-licenses/NetworkManager/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
%make_install
%find_lang NetworkManager
## Remove excluded files
rm -f %{buildroot}*/usr/lib/udev/rules.d/84-nm-drivers.rules
## install_append content
# Ensure dbus activation will work without requiring enable at boot
pushd %{buildroot}/usr/lib/systemd/system
ln -s NetworkManager.service dbus-org.freedesktop.NetworkManager.service
ln -s NetworkManager-dispatcher.service dbus-org.freedesktop.nm-dispatcher.service
popd
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
pushd %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -sf ../NetworkManager.service NetworkManager.service
popd
mkdir -p %{buildroot}/usr/lib/systemd/system/network-online.target.wants
pushd %{buildroot}/usr/lib/systemd/system/network-online.target.wants
ln -sf ../NetworkManager-wait-online.service NetworkManager-wait-online.service
popd
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/NetworkManager/dispatcher.d/90-nm-cloud-setup.sh
/usr/lib/NetworkManager/dispatcher.d/no-wait.d/90-nm-cloud-setup.sh
/usr/lib/firewalld/zones/nm-shared.xml

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/NetworkManager.service
/usr/lib/systemd/system/network-online.target.wants/NetworkManager-wait-online.service

%files bin
%defattr(-,root,root,-)
/usr/bin/NetworkManager
/usr/bin/nm-online
/usr/bin/nmcli

%files config
%defattr(-,root,root,-)
/usr/lib/udev/rules.d/85-nm-unmanaged.rules
/usr/lib/udev/rules.d/90-nm-thunderbolt.rules

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/NM-1.0.typelib
/usr/share/bash-completion/completions/nmcli
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.AccessPoint.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.AgentManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Checkpoint.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Connection.Active.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DHCP4Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DHCP6Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Adsl.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bluetooth.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bond.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Bridge.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Dummy.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Generic.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.IPTunnel.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Infiniband.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Loopback.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Lowpan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Macsec.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Macvlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Modem.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OlpcMesh.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OvsBridge.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OvsInterface.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.OvsPort.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Ppp.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Statistics.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Team.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Tun.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Veth.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Vlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Vrf.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Vxlan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.WiMax.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.WifiP2P.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.WireGuard.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wired.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wireless.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.Wpan.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Device.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.DnsManager.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.IP4Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.IP6Config.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.PPP.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.SecretAgent.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Settings.Connection.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.Settings.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.VPN.Connection.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.VPN.Plugin.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.WiMax.Nsp.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.WifiP2PPeer.xml
/usr/share/dbus-1/interfaces/org.freedesktop.NetworkManager.xml
/usr/share/dbus-1/system-services/org.freedesktop.nm_dispatcher.service
/usr/share/dbus-1/system-services/org.freedesktop.nm_priv_helper.service
/usr/share/dbus-1/system.d/nm-dispatcher.conf
/usr/share/dbus-1/system.d/nm-priv-helper.conf
/usr/share/dbus-1/system.d/org.freedesktop.NetworkManager.conf
/usr/share/gir-1.0/*.gir
/usr/share/polkit-1/actions/org.freedesktop.NetworkManager.policy
/usr/share/vala/vapi/libnm.deps
/usr/share/vala/vapi/libnm.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/libnm/NetworkManager.h
/usr/include/libnm/nm-access-point.h
/usr/include/libnm/nm-active-connection.h
/usr/include/libnm/nm-autoptr.h
/usr/include/libnm/nm-checkpoint.h
/usr/include/libnm/nm-client.h
/usr/include/libnm/nm-conn-utils.h
/usr/include/libnm/nm-connection.h
/usr/include/libnm/nm-core-enum-types.h
/usr/include/libnm/nm-core-types.h
/usr/include/libnm/nm-dbus-interface.h
/usr/include/libnm/nm-device-6lowpan.h
/usr/include/libnm/nm-device-adsl.h
/usr/include/libnm/nm-device-bond.h
/usr/include/libnm/nm-device-bridge.h
/usr/include/libnm/nm-device-bt.h
/usr/include/libnm/nm-device-dummy.h
/usr/include/libnm/nm-device-ethernet.h
/usr/include/libnm/nm-device-generic.h
/usr/include/libnm/nm-device-infiniband.h
/usr/include/libnm/nm-device-ip-tunnel.h
/usr/include/libnm/nm-device-loopback.h
/usr/include/libnm/nm-device-macsec.h
/usr/include/libnm/nm-device-macvlan.h
/usr/include/libnm/nm-device-modem.h
/usr/include/libnm/nm-device-olpc-mesh.h
/usr/include/libnm/nm-device-ovs-bridge.h
/usr/include/libnm/nm-device-ovs-interface.h
/usr/include/libnm/nm-device-ovs-port.h
/usr/include/libnm/nm-device-ppp.h
/usr/include/libnm/nm-device-team.h
/usr/include/libnm/nm-device-tun.h
/usr/include/libnm/nm-device-veth.h
/usr/include/libnm/nm-device-vlan.h
/usr/include/libnm/nm-device-vrf.h
/usr/include/libnm/nm-device-vxlan.h
/usr/include/libnm/nm-device-wifi-p2p.h
/usr/include/libnm/nm-device-wifi.h
/usr/include/libnm/nm-device-wimax.h
/usr/include/libnm/nm-device-wireguard.h
/usr/include/libnm/nm-device-wpan.h
/usr/include/libnm/nm-device.h
/usr/include/libnm/nm-dhcp-config.h
/usr/include/libnm/nm-enum-types.h
/usr/include/libnm/nm-errors.h
/usr/include/libnm/nm-ethtool-utils.h
/usr/include/libnm/nm-ip-config.h
/usr/include/libnm/nm-keyfile.h
/usr/include/libnm/nm-object.h
/usr/include/libnm/nm-remote-connection.h
/usr/include/libnm/nm-secret-agent-old.h
/usr/include/libnm/nm-setting-6lowpan.h
/usr/include/libnm/nm-setting-8021x.h
/usr/include/libnm/nm-setting-adsl.h
/usr/include/libnm/nm-setting-bluetooth.h
/usr/include/libnm/nm-setting-bond-port.h
/usr/include/libnm/nm-setting-bond.h
/usr/include/libnm/nm-setting-bridge-port.h
/usr/include/libnm/nm-setting-bridge.h
/usr/include/libnm/nm-setting-cdma.h
/usr/include/libnm/nm-setting-connection.h
/usr/include/libnm/nm-setting-dcb.h
/usr/include/libnm/nm-setting-dummy.h
/usr/include/libnm/nm-setting-ethtool.h
/usr/include/libnm/nm-setting-generic.h
/usr/include/libnm/nm-setting-gsm.h
/usr/include/libnm/nm-setting-hostname.h
/usr/include/libnm/nm-setting-infiniband.h
/usr/include/libnm/nm-setting-ip-config.h
/usr/include/libnm/nm-setting-ip-tunnel.h
/usr/include/libnm/nm-setting-ip4-config.h
/usr/include/libnm/nm-setting-ip6-config.h
/usr/include/libnm/nm-setting-loopback.h
/usr/include/libnm/nm-setting-macsec.h
/usr/include/libnm/nm-setting-macvlan.h
/usr/include/libnm/nm-setting-match.h
/usr/include/libnm/nm-setting-olpc-mesh.h
/usr/include/libnm/nm-setting-ovs-bridge.h
/usr/include/libnm/nm-setting-ovs-dpdk.h
/usr/include/libnm/nm-setting-ovs-external-ids.h
/usr/include/libnm/nm-setting-ovs-interface.h
/usr/include/libnm/nm-setting-ovs-other-config.h
/usr/include/libnm/nm-setting-ovs-patch.h
/usr/include/libnm/nm-setting-ovs-port.h
/usr/include/libnm/nm-setting-ppp.h
/usr/include/libnm/nm-setting-pppoe.h
/usr/include/libnm/nm-setting-proxy.h
/usr/include/libnm/nm-setting-serial.h
/usr/include/libnm/nm-setting-sriov.h
/usr/include/libnm/nm-setting-tc-config.h
/usr/include/libnm/nm-setting-team-port.h
/usr/include/libnm/nm-setting-team.h
/usr/include/libnm/nm-setting-tun.h
/usr/include/libnm/nm-setting-user.h
/usr/include/libnm/nm-setting-veth.h
/usr/include/libnm/nm-setting-vlan.h
/usr/include/libnm/nm-setting-vpn.h
/usr/include/libnm/nm-setting-vrf.h
/usr/include/libnm/nm-setting-vxlan.h
/usr/include/libnm/nm-setting-wifi-p2p.h
/usr/include/libnm/nm-setting-wimax.h
/usr/include/libnm/nm-setting-wired.h
/usr/include/libnm/nm-setting-wireguard.h
/usr/include/libnm/nm-setting-wireless-security.h
/usr/include/libnm/nm-setting-wireless.h
/usr/include/libnm/nm-setting-wpan.h
/usr/include/libnm/nm-setting.h
/usr/include/libnm/nm-simple-connection.h
/usr/include/libnm/nm-utils.h
/usr/include/libnm/nm-version-macros.h
/usr/include/libnm/nm-version.h
/usr/include/libnm/nm-vpn-connection.h
/usr/include/libnm/nm-vpn-dbus-interface.h
/usr/include/libnm/nm-vpn-editor-plugin.h
/usr/include/libnm/nm-vpn-editor.h
/usr/include/libnm/nm-vpn-plugin-info.h
/usr/include/libnm/nm-vpn-plugin-old.h
/usr/include/libnm/nm-vpn-service-plugin.h
/usr/include/libnm/nm-wifi-p2p-peer.h
/usr/include/libnm/nm-wimax-nsp.h
/usr/lib64/libnm.so
/usr/lib64/pkgconfig/libnm.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/NetworkManager/*
/usr/share/gtk-doc/html/NetworkManager/NetworkManager-dispatcher.html
/usr/share/gtk-doc/html/NetworkManager/NetworkManager-wait-online.service.html
/usr/share/gtk-doc/html/NetworkManager/NetworkManager.conf.html
/usr/share/gtk-doc/html/NetworkManager/NetworkManager.devhelp2
/usr/share/gtk-doc/html/NetworkManager/NetworkManager.html
/usr/share/gtk-doc/html/NetworkManager/ch01.html
/usr/share/gtk-doc/html/NetworkManager/dbus-secret-agent.html
/usr/share/gtk-doc/html/NetworkManager/dbus-types.html
/usr/share/gtk-doc/html/NetworkManager/dbus-vpn-plugin.html
/usr/share/gtk-doc/html/NetworkManager/dbus-vpn-types.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.AccessPoint.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.AgentManager.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Checkpoint.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Connection.Active.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.DHCP4Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.DHCP6Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Adsl.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Bluetooth.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Bond.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Bridge.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Dummy.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Generic.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.IPTunnel.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Infiniband.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Loopback.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Lowpan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Macsec.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Macvlan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Modem.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.OlpcMesh.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.OvsBridge.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.OvsInterface.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.OvsPort.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Ppp.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Statistics.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Team.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Tun.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Veth.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Vlan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Vrf.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Vxlan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.WifiP2P.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.WireGuard.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Wired.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Wireless.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.Wpan.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Device.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.DnsManager.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.IP4Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.IP6Config.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.PPP.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.SecretAgent.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Settings.Connection.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.Settings.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.VPN.Connection.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.VPN.Plugin.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.WifiP2PPeer.html
/usr/share/gtk-doc/html/NetworkManager/gdbus-org.freedesktop.NetworkManager.html
/usr/share/gtk-doc/html/NetworkManager/home.png
/usr/share/gtk-doc/html/NetworkManager/index.html
/usr/share/gtk-doc/html/NetworkManager/ix01.html
/usr/share/gtk-doc/html/NetworkManager/left-insensitive.png
/usr/share/gtk-doc/html/NetworkManager/left.png
/usr/share/gtk-doc/html/NetworkManager/license.html
/usr/share/gtk-doc/html/NetworkManager/manpages.html
/usr/share/gtk-doc/html/NetworkManager/nm-cloud-setup.html
/usr/share/gtk-doc/html/NetworkManager/nm-dbus-types.html
/usr/share/gtk-doc/html/NetworkManager/nm-initrd-generator.html
/usr/share/gtk-doc/html/NetworkManager/nm-online.html
/usr/share/gtk-doc/html/NetworkManager/nm-openvswitch.html
/usr/share/gtk-doc/html/NetworkManager/nm-settings-dbus.html
/usr/share/gtk-doc/html/NetworkManager/nm-settings-ifcfg-rh.html
/usr/share/gtk-doc/html/NetworkManager/nm-settings-keyfile.html
/usr/share/gtk-doc/html/NetworkManager/nm-settings-nmcli.html
/usr/share/gtk-doc/html/NetworkManager/nm-vpn-dbus-types.html
/usr/share/gtk-doc/html/NetworkManager/nmcli-examples.html
/usr/share/gtk-doc/html/NetworkManager/nmcli.html
/usr/share/gtk-doc/html/NetworkManager/nmtui.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-access-points.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-active-connections.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-agent-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-checkpoint.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-devices.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-dhcp4-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-dhcp6-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-dns-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-ip4-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-ip6-configs.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-settings-manager.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-settings.html
/usr/share/gtk-doc/html/NetworkManager/ref-dbus-wifi-p2p-peers.html
/usr/share/gtk-doc/html/NetworkManager/ref-settings.html
/usr/share/gtk-doc/html/NetworkManager/right-insensitive.png
/usr/share/gtk-doc/html/NetworkManager/right.png
/usr/share/gtk-doc/html/NetworkManager/secret-agents.html
/usr/share/gtk-doc/html/NetworkManager/secrets-flags.html
/usr/share/gtk-doc/html/NetworkManager/settings-6lowpan.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-11-olpc-mesh.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-11-wireless-security.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-11-wireless.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-1x.html
/usr/share/gtk-doc/html/NetworkManager/settings-802-3-ethernet.html
/usr/share/gtk-doc/html/NetworkManager/settings-adsl.html
/usr/share/gtk-doc/html/NetworkManager/settings-bluetooth.html
/usr/share/gtk-doc/html/NetworkManager/settings-bond-port.html
/usr/share/gtk-doc/html/NetworkManager/settings-bond.html
/usr/share/gtk-doc/html/NetworkManager/settings-bridge-port.html
/usr/share/gtk-doc/html/NetworkManager/settings-bridge.html
/usr/share/gtk-doc/html/NetworkManager/settings-cdma.html
/usr/share/gtk-doc/html/NetworkManager/settings-connection.html
/usr/share/gtk-doc/html/NetworkManager/settings-dcb.html
/usr/share/gtk-doc/html/NetworkManager/settings-dummy.html
/usr/share/gtk-doc/html/NetworkManager/settings-ethtool.html
/usr/share/gtk-doc/html/NetworkManager/settings-generic.html
/usr/share/gtk-doc/html/NetworkManager/settings-gsm.html
/usr/share/gtk-doc/html/NetworkManager/settings-hostname.html
/usr/share/gtk-doc/html/NetworkManager/settings-infiniband.html
/usr/share/gtk-doc/html/NetworkManager/settings-ip-tunnel.html
/usr/share/gtk-doc/html/NetworkManager/settings-ipv4.html
/usr/share/gtk-doc/html/NetworkManager/settings-ipv6.html
/usr/share/gtk-doc/html/NetworkManager/settings-loopback.html
/usr/share/gtk-doc/html/NetworkManager/settings-macsec.html
/usr/share/gtk-doc/html/NetworkManager/settings-macvlan.html
/usr/share/gtk-doc/html/NetworkManager/settings-match.html
/usr/share/gtk-doc/html/NetworkManager/settings-ovs-bridge.html
/usr/share/gtk-doc/html/NetworkManager/settings-ovs-dpdk.html
/usr/share/gtk-doc/html/NetworkManager/settings-ovs-external-ids.html
/usr/share/gtk-doc/html/NetworkManager/settings-ovs-interface.html
/usr/share/gtk-doc/html/NetworkManager/settings-ovs-other-config.html
/usr/share/gtk-doc/html/NetworkManager/settings-ovs-patch.html
/usr/share/gtk-doc/html/NetworkManager/settings-ovs-port.html
/usr/share/gtk-doc/html/NetworkManager/settings-ppp.html
/usr/share/gtk-doc/html/NetworkManager/settings-pppoe.html
/usr/share/gtk-doc/html/NetworkManager/settings-proxy.html
/usr/share/gtk-doc/html/NetworkManager/settings-serial.html
/usr/share/gtk-doc/html/NetworkManager/settings-sriov.html
/usr/share/gtk-doc/html/NetworkManager/settings-tc.html
/usr/share/gtk-doc/html/NetworkManager/settings-team-port.html
/usr/share/gtk-doc/html/NetworkManager/settings-team.html
/usr/share/gtk-doc/html/NetworkManager/settings-tun.html
/usr/share/gtk-doc/html/NetworkManager/settings-user.html
/usr/share/gtk-doc/html/NetworkManager/settings-veth.html
/usr/share/gtk-doc/html/NetworkManager/settings-vlan.html
/usr/share/gtk-doc/html/NetworkManager/settings-vpn.html
/usr/share/gtk-doc/html/NetworkManager/settings-vrf.html
/usr/share/gtk-doc/html/NetworkManager/settings-vxlan.html
/usr/share/gtk-doc/html/NetworkManager/settings-wifi-p2p.html
/usr/share/gtk-doc/html/NetworkManager/settings-wimax.html
/usr/share/gtk-doc/html/NetworkManager/settings-wireguard.html
/usr/share/gtk-doc/html/NetworkManager/settings-wpan.html
/usr/share/gtk-doc/html/NetworkManager/spec.html
/usr/share/gtk-doc/html/NetworkManager/style.css
/usr/share/gtk-doc/html/NetworkManager/up-insensitive.png
/usr/share/gtk-doc/html/NetworkManager/up.png
/usr/share/gtk-doc/html/NetworkManager/vpn-plugins.html
/usr/share/gtk-doc/html/libnm/NMAccessPoint.html
/usr/share/gtk-doc/html/libnm/NMActiveConnection.html
/usr/share/gtk-doc/html/libnm/NMCheckpoint.html
/usr/share/gtk-doc/html/libnm/NMClient.html
/usr/share/gtk-doc/html/libnm/NMConnection.html
/usr/share/gtk-doc/html/libnm/NMDevice.html
/usr/share/gtk-doc/html/libnm/NMDevice6Lowpan.html
/usr/share/gtk-doc/html/libnm/NMDeviceAdsl.html
/usr/share/gtk-doc/html/libnm/NMDeviceBond.html
/usr/share/gtk-doc/html/libnm/NMDeviceBridge.html
/usr/share/gtk-doc/html/libnm/NMDeviceBt.html
/usr/share/gtk-doc/html/libnm/NMDeviceDummy.html
/usr/share/gtk-doc/html/libnm/NMDeviceEthernet.html
/usr/share/gtk-doc/html/libnm/NMDeviceGeneric.html
/usr/share/gtk-doc/html/libnm/NMDeviceIPTunnel.html
/usr/share/gtk-doc/html/libnm/NMDeviceInfiniband.html
/usr/share/gtk-doc/html/libnm/NMDeviceLoopback.html
/usr/share/gtk-doc/html/libnm/NMDeviceMacsec.html
/usr/share/gtk-doc/html/libnm/NMDeviceMacvlan.html
/usr/share/gtk-doc/html/libnm/NMDeviceModem.html
/usr/share/gtk-doc/html/libnm/NMDeviceOlpcMesh.html
/usr/share/gtk-doc/html/libnm/NMDeviceOvsBridge.html
/usr/share/gtk-doc/html/libnm/NMDeviceOvsInterface.html
/usr/share/gtk-doc/html/libnm/NMDeviceOvsPort.html
/usr/share/gtk-doc/html/libnm/NMDevicePpp.html
/usr/share/gtk-doc/html/libnm/NMDeviceTeam.html
/usr/share/gtk-doc/html/libnm/NMDeviceTun.html
/usr/share/gtk-doc/html/libnm/NMDeviceVeth.html
/usr/share/gtk-doc/html/libnm/NMDeviceVlan.html
/usr/share/gtk-doc/html/libnm/NMDeviceVrf.html
/usr/share/gtk-doc/html/libnm/NMDeviceVxlan.html
/usr/share/gtk-doc/html/libnm/NMDeviceWifi.html
/usr/share/gtk-doc/html/libnm/NMDeviceWifiP2P.html
/usr/share/gtk-doc/html/libnm/NMDeviceWimax.html
/usr/share/gtk-doc/html/libnm/NMDeviceWireGuard.html
/usr/share/gtk-doc/html/libnm/NMDeviceWpan.html
/usr/share/gtk-doc/html/libnm/NMDhcpConfig.html
/usr/share/gtk-doc/html/libnm/NMIPConfig.html
/usr/share/gtk-doc/html/libnm/NMObject.html
/usr/share/gtk-doc/html/libnm/NMRemoteConnection.html
/usr/share/gtk-doc/html/libnm/NMSecretAgentOld.html
/usr/share/gtk-doc/html/libnm/NMSetting.html
/usr/share/gtk-doc/html/libnm/NMSetting6Lowpan.html
/usr/share/gtk-doc/html/libnm/NMSetting8021x.html
/usr/share/gtk-doc/html/libnm/NMSettingAdsl.html
/usr/share/gtk-doc/html/libnm/NMSettingBluetooth.html
/usr/share/gtk-doc/html/libnm/NMSettingBond.html
/usr/share/gtk-doc/html/libnm/NMSettingBondPort.html
/usr/share/gtk-doc/html/libnm/NMSettingBridge.html
/usr/share/gtk-doc/html/libnm/NMSettingBridgePort.html
/usr/share/gtk-doc/html/libnm/NMSettingCdma.html
/usr/share/gtk-doc/html/libnm/NMSettingConnection.html
/usr/share/gtk-doc/html/libnm/NMSettingDcb.html
/usr/share/gtk-doc/html/libnm/NMSettingDummy.html
/usr/share/gtk-doc/html/libnm/NMSettingEthtool.html
/usr/share/gtk-doc/html/libnm/NMSettingGeneric.html
/usr/share/gtk-doc/html/libnm/NMSettingGsm.html
/usr/share/gtk-doc/html/libnm/NMSettingHostname.html
/usr/share/gtk-doc/html/libnm/NMSettingIP4Config.html
/usr/share/gtk-doc/html/libnm/NMSettingIP6Config.html
/usr/share/gtk-doc/html/libnm/NMSettingIPConfig.html
/usr/share/gtk-doc/html/libnm/NMSettingIPTunnel.html
/usr/share/gtk-doc/html/libnm/NMSettingInfiniband.html
/usr/share/gtk-doc/html/libnm/NMSettingLoopback.html
/usr/share/gtk-doc/html/libnm/NMSettingMacsec.html
/usr/share/gtk-doc/html/libnm/NMSettingMacvlan.html
/usr/share/gtk-doc/html/libnm/NMSettingMatch.html
/usr/share/gtk-doc/html/libnm/NMSettingOlpcMesh.html
/usr/share/gtk-doc/html/libnm/NMSettingOvsBridge.html
/usr/share/gtk-doc/html/libnm/NMSettingOvsDpdk.html
/usr/share/gtk-doc/html/libnm/NMSettingOvsExternalIDs.html
/usr/share/gtk-doc/html/libnm/NMSettingOvsInterface.html
/usr/share/gtk-doc/html/libnm/NMSettingOvsOtherConfig.html
/usr/share/gtk-doc/html/libnm/NMSettingOvsPatch.html
/usr/share/gtk-doc/html/libnm/NMSettingOvsPort.html
/usr/share/gtk-doc/html/libnm/NMSettingPpp.html
/usr/share/gtk-doc/html/libnm/NMSettingPppoe.html
/usr/share/gtk-doc/html/libnm/NMSettingProxy.html
/usr/share/gtk-doc/html/libnm/NMSettingSerial.html
/usr/share/gtk-doc/html/libnm/NMSettingSriov.html
/usr/share/gtk-doc/html/libnm/NMSettingTCConfig.html
/usr/share/gtk-doc/html/libnm/NMSettingTeam.html
/usr/share/gtk-doc/html/libnm/NMSettingTeamPort.html
/usr/share/gtk-doc/html/libnm/NMSettingTun.html
/usr/share/gtk-doc/html/libnm/NMSettingUser.html
/usr/share/gtk-doc/html/libnm/NMSettingVeth.html
/usr/share/gtk-doc/html/libnm/NMSettingVlan.html
/usr/share/gtk-doc/html/libnm/NMSettingVpn.html
/usr/share/gtk-doc/html/libnm/NMSettingVrf.html
/usr/share/gtk-doc/html/libnm/NMSettingVxlan.html
/usr/share/gtk-doc/html/libnm/NMSettingWifiP2P.html
/usr/share/gtk-doc/html/libnm/NMSettingWimax.html
/usr/share/gtk-doc/html/libnm/NMSettingWireGuard.html
/usr/share/gtk-doc/html/libnm/NMSettingWired.html
/usr/share/gtk-doc/html/libnm/NMSettingWireless.html
/usr/share/gtk-doc/html/libnm/NMSettingWirelessSecurity.html
/usr/share/gtk-doc/html/libnm/NMSettingWpan.html
/usr/share/gtk-doc/html/libnm/NMSimpleConnection.html
/usr/share/gtk-doc/html/libnm/NMVpnConnection.html
/usr/share/gtk-doc/html/libnm/NMVpnEditor.html
/usr/share/gtk-doc/html/libnm/NMVpnEditorPlugin.html
/usr/share/gtk-doc/html/libnm/NMVpnPluginInfo.html
/usr/share/gtk-doc/html/libnm/NMVpnPluginOld.html
/usr/share/gtk-doc/html/libnm/NMVpnServicePlugin.html
/usr/share/gtk-doc/html/libnm/NMWifiP2PPeer.html
/usr/share/gtk-doc/html/libnm/NMWimaxNsp.html
/usr/share/gtk-doc/html/libnm/annotation-glossary.html
/usr/share/gtk-doc/html/libnm/api-index-full.html
/usr/share/gtk-doc/html/libnm/ch02.html
/usr/share/gtk-doc/html/libnm/ch03.html
/usr/share/gtk-doc/html/libnm/ch04.html
/usr/share/gtk-doc/html/libnm/ch05.html
/usr/share/gtk-doc/html/libnm/ch06.html
/usr/share/gtk-doc/html/libnm/home.png
/usr/share/gtk-doc/html/libnm/index.html
/usr/share/gtk-doc/html/libnm/left-insensitive.png
/usr/share/gtk-doc/html/libnm/left.png
/usr/share/gtk-doc/html/libnm/libnm-nm-conn-utils.html
/usr/share/gtk-doc/html/libnm/libnm-nm-dbus-interface.html
/usr/share/gtk-doc/html/libnm/libnm-nm-errors.html
/usr/share/gtk-doc/html/libnm/libnm-nm-ethtool-utils.html
/usr/share/gtk-doc/html/libnm/libnm-nm-keyfile.html
/usr/share/gtk-doc/html/libnm/libnm-nm-utils.html
/usr/share/gtk-doc/html/libnm/libnm-nm-version-macros.html
/usr/share/gtk-doc/html/libnm/libnm-nm-version.html
/usr/share/gtk-doc/html/libnm/libnm-nm-vpn-dbus-interface.html
/usr/share/gtk-doc/html/libnm/libnm.devhelp2
/usr/share/gtk-doc/html/libnm/libnm.png
/usr/share/gtk-doc/html/libnm/license.html
/usr/share/gtk-doc/html/libnm/object-tree.html
/usr/share/gtk-doc/html/libnm/ref-overview.html
/usr/share/gtk-doc/html/libnm/right-insensitive.png
/usr/share/gtk-doc/html/libnm/right.png
/usr/share/gtk-doc/html/libnm/style.css
/usr/share/gtk-doc/html/libnm/up-insensitive.png
/usr/share/gtk-doc/html/libnm/up.png
/usr/share/gtk-doc/html/libnm/usage.html

%files extras
%defattr(-,root,root,-)
/usr/bin/nmtui
/usr/bin/nmtui-connect
/usr/bin/nmtui-edit
/usr/bin/nmtui-hostname

%files lib
%defattr(-,root,root,-)
/usr/lib64/NetworkManager/1.42.6/libnm-device-plugin-adsl.so
/usr/lib64/NetworkManager/1.42.6/libnm-device-plugin-bluetooth.so
/usr/lib64/NetworkManager/1.42.6/libnm-device-plugin-wifi.so
/usr/lib64/NetworkManager/1.42.6/libnm-device-plugin-wwan.so
/usr/lib64/NetworkManager/1.42.6/libnm-ppp-plugin.so
/usr/lib64/NetworkManager/1.42.6/libnm-wwan.so
/usr/lib64/libnm.so.0
/usr/lib64/libnm.so.0.1.0
/usr/lib64/pppd/2.4.5/nm-pppd-plugin.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/nm-cloud-setup
/usr/libexec/nm-daemon-helper
/usr/libexec/nm-dhcp-helper
/usr/libexec/nm-dispatcher
/usr/libexec/nm-initrd-generator
/usr/libexec/nm-priv-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/NetworkManager/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/NetworkManager/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/NetworkManager/7205ad2e7451e9c4a518d105d5144987cdaf9bfa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/nm-online.1
/usr/share/man/man1/nmcli.1
/usr/share/man/man1/nmtui-connect.1
/usr/share/man/man1/nmtui-edit.1
/usr/share/man/man1/nmtui-hostname.1
/usr/share/man/man1/nmtui.1
/usr/share/man/man5/NetworkManager.conf.5
/usr/share/man/man5/nm-settings-dbus.5
/usr/share/man/man5/nm-settings-keyfile.5
/usr/share/man/man5/nm-settings-nmcli.5
/usr/share/man/man5/nm-settings.5
/usr/share/man/man5/nm-system-settings.conf.5
/usr/share/man/man7/nmcli-examples.7
/usr/share/man/man8/NetworkManager-dispatcher.8
/usr/share/man/man8/NetworkManager-wait-online.service.8
/usr/share/man/man8/NetworkManager.8
/usr/share/man/man8/nm-cloud-setup.8
/usr/share/man/man8/nm-initrd-generator.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/NetworkManager.service
%exclude /usr/lib/systemd/system/network-online.target.wants/NetworkManager-wait-online.service
/usr/lib/systemd/system/NetworkManager-dispatcher.service
/usr/lib/systemd/system/NetworkManager-wait-online.service
/usr/lib/systemd/system/NetworkManager.service
/usr/lib/systemd/system/dbus-org.freedesktop.NetworkManager.service
/usr/lib/systemd/system/dbus-org.freedesktop.nm-dispatcher.service
/usr/lib/systemd/system/nm-cloud-setup.service
/usr/lib/systemd/system/nm-cloud-setup.timer
/usr/lib/systemd/system/nm-priv-helper.service

%files locales -f NetworkManager.lang
%defattr(-,root,root,-)

