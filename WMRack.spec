Summary:	A WindowMaker Dock CD+Sound Applet
Summary(pl):	Dock CD+Sound aplet do WindowMakera
Name:		WMRack
Version:	1.0b5
Release:	3
Copyright:	GPL
Vendor:		FGA bitart Furch & Graf GbR
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source:		WMRack-%{version}.tar.bz2
Icon:		wmrack.gif
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6
%define	_mandir	%{_prefix}/man

%description
This is the second and hopefully last beta release of WMRack. It
features cdrom and mixer functions. Please repeat any bugs. Compiled
with extra verbose output.

Read the manpage for a description of the supported functions and
how to install the applet to your button bar (Wharf, Dock, etc...)

Sorry, styles not updated. Wait for the non-beta. Old styles
still work but need an extra (middle) button.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--mandir=%{_mandir}
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*
gzip -9nf README TODO WARRANTY

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz TODO.gz WARRANTY.gz
%{_prefix}/GNUstep/Library/WMRack

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue Feb  9 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [1.0b5-2d]
- added gzipping man pages and documentation
- removed LICENSE form %doc (GPL)
- added %clean section

* Sun Nov  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0b5-3]
- added -q %setup parameter,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- changed instal prefix to /usr/X11R6
- added LDFLAGS="-s" to ./configure enviroment,
- changed Group to X11/Window Managers/Tools,
- added Group(pl) and Summary(pl),
- added %attr and %defattr macros in %files (allow build package from
  non-root account).

* Thu Aug  6 1998 Oliver Graf <ograf@fga.de>
- started changelog
- added defines for version and release
