Summary:	Application to create and manage icons on fluxbox desktop
Summary(pl.UTF-8):	Aplikacja do tworzenia i zarządzania ikonami w fluxboksie
Name:		fbdesk
Version:	1.4.1
Release:	2
License:	MIT
Group:		X11/Window Managers/Tools
Source0:	http://fluxbox.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	b65136d2d52524492c8a5bc233b7f34b
Source1:	xft.m4
URL:		http://www.fluxbox.org/fbdesk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib2-devel >= 1.0.0
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXrender-devel
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package include an application to create and manage icons on
fluxbox desktop. It supports antialiasing, XPM and PNG icons. You can
put text above or below, at the left or right side icons. Supports
UTF-8.

%description -l pl.UTF-8
Ten pakiet zawiera narzędzie do tworzenia i zarządzania ikonami na
pulpicie fluxboksa. Wspiera antyaliasing, ikony zarówno w formacie XPM
jak i PNG. Tekst może być umiejscowiony pod lub nad ikonami, z lewej
albo z prawej strony. Obsługuje UTF-8.

%prep
%setup -q
install %{SOURCE1} .

%build
%{__aclocal} -I .
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/fbdesk
