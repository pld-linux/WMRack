Summary:	A WindowMaker Dock CD+Sound Applet
Summary(pl):	Dokowalny aplet CD+Sound do WindowMakera
Name:		WMRack
Version:	1.0b5
Release:	3
License:	GPL
Vendor:		FGA bitart Furch & Graf GbR
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://prdownloads.sourceforge.net/wmrack/%{name}-%{version}.tar.gz
#Icon:		wmrack.gif
URL:		http://wmrack.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This is the second and hopefully last beta release of WMRack. It
features cdrom and mixer functions. Please repeat any bugs. Compiled
with extra verbose output.

Read the manpage for a description of the supported functions and how
to install the applet to your button bar (Wharf, Dock, etc...)

Sorry, styles not updated. Wait for the non-beta. Old styles still
work but need an extra (middle) button.

%description -l pl
WMRack zawiera funkcje miksera i odtwarzacza cdrom.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}" LDFLAGS="%{rpmldflags}" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}

gzip -9nf README TODO WARRANTY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz TODO.gz WARRANTY.gz
%{_prefix}/GNUstep/Library/WMRack

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
