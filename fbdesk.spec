Summary:	Application to create and manage icons on fluxbox desktop
Summary(pl):	Aplikacja do tworzenia i zarz±dzania ikonami w fluxboksie
Name:		fbdesk
Version:	1.1.5
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://fluxbox.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	c41319c9a2a03cf4d7d5e0586e57cba6
Patch0:		%{name}-XFT.patch
BuildRequires:	XFree86-devel
BuildRequires:	XFree86-xft-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpng-devel
Requires:	fluxbox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package include an application to create and manage icons on
fluxbox desktop. It supports antialiasing, XPM and PNG icons. You can
put text above or below, at the left or right side icons. Supports
UTF-8.

%description -l pl
Ten pakiet zawiera narzêdzie do tworzenia i zarz±dzania ikonami na
pulpicie fluxboksa. Wspiera antyaliasing, ikony zarówno w formacie XPM
jak i PNG. Tekst mo¿e byæ umiejscowiony pod lub nad ikonami, z lewej
albo z prawej strony. Obs³uguje UTF-8.

%prep
%setup  -q
%patch0 -p0

%build
%{__aclocal}
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
%doc COPYING ChangeLog INSTALL README
%attr(755,root,root) %{_bindir}/*
