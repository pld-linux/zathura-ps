%define		_zathura_api_ver	%(pkg-config --variable=apiversion zathura 2> /dev/null || echo -1)
%define		_zathura_abi_ver	%(pkg-config --variable=abiversion zathura 2> /dev/null || echo -1)

Summary:	PostScript support for zathura
Summary(pl.UTF-8):	Obsługa PostScriptu dla zathury
Name:		zathura-ps
Version:	2026.02.03
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-ps/download/%{name}-%{version}.tar.xz
# Source0-md5:	9ff1aed26d41b215ebc4c9305cba59b9
URL:		https://pwmt.org/projects/zathura-ps/
BuildRequires:	cairo-devel
# C17
BuildRequires:	gcc >= 6:8.1.0
BuildRequires:	girara-devel >= 2026.02.03
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libspectre-devel
BuildRequires:	meson >= 0.61
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 2026.01.30
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 2026.02.03
Requires:	zathura >= 2026.01.30
Requires:	zathura(plugin-abi) = %_zathura_abi_ver
Requires:	zathura(plugin-api) = %_zathura_api_ver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-ps plugin adds PostScript support to zathura by using the
libspectre library.

%description -l pl.UTF-8
Wtyczka zathura-ps dodaje do zathury obsługę PostScriptu z
wykorzystaniem biblioteki libspectre.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%attr(755,root,root) %{_libdir}/zathura/libps.so
%{_desktopdir}/org.pwmt.zathura-ps.desktop
%{_datadir}/metainfo/org.pwmt.zathura-ps.metainfo.xml
