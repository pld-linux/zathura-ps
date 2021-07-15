Summary:	PostScript support for zathura
Summary(pl.UTF-8):	Obsługa PostScriptu dla zathury
Name:		zathura-ps
Version:	0.2.7
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-ps/download/%{name}-%{version}.tar.xz
# Source0-md5:	735c626270ff6279cc3ae818e6a03eb4
URL:		https://pwmt.org/projects/zathura-ps/
BuildRequires:	cairo-devel
# C11
BuildRequires:	gcc >= 6:4.7
BuildRequires:	girara-devel >= 0.1.8
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libspectre-devel
BuildRequires:	meson >= 0.43
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 0.3.8
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.1.8
Requires:	zathura >= 0.3.8
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
