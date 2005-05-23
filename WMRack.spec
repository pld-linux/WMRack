Summary:	A WindowMaker Dock CD+Sound Applet
Summary(pl):	Dokowalny aplet CD+Sound do WindowMakera
Name:		WMRack
Version:	1.0b5
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://dl.sourceforge.net/wmrack/%{name}-%{version}.tar.gz
# Source0-md5:	0832e522a3641d74698c98e47d981de7
Patch0:		%{name}-DESTDIR.patch
#Icon:		wmrack.gif
URL:		http://wmrack.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
It features cdrom and mixer functions.

Read the manpage for a description of the supported functions and how
to install the applet to your button bar (Wharf, Dock, etc...)

Sorry, styles not updated. Wait for the non-beta. Old styles still
work but need an extra (middle) button.

%description -l pl
WMRack zawiera funkcje miksera i odtwarzacza cdrom.

Przeczytaj stronê manuala, je¿eli szukasz opisu obs³ugiwanych funkcji
oraz jak zainstalowaæ aplet na swoim pasku przycisków (Wharf, Dock,
itp).

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO WARRANTY
%attr(755,root,root) %{_bindir}/*
#%%{_prefix}/GNUstep/Library/WMRack
%{_libdir}/WMRack
%{_mandir}/man1/*
