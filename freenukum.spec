Summary:	clone of duke nukem
Summary(pl.UTF-8):	klon gry duke nukem
Name:		freenukum
Version:	0.2.10
Release:	1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://launchpad.net/freenukum/trunk/0.2/+download/%{name}-%{version}.tar.gz
# Source0-md5:	21c6d87944518ba88060988bbf78113e
Patch0:		%{name}-as-needed.patch
Patch1:		%{name}-no-wall-werror.patch
URL:		https://launchpad.net/freenukum/
BuildRequires:	ImageMagick-coder-png
BuildRequires:	ImageMagick-coder-svg
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	libzip-devel
BuildRequires:	pkgconfig >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Freenukum Jump'n Run game is a clone of the old EGA graphics based
2D game Duke Nukem. It uses the original Duke Nukem level and graphics
files.

%description -l pl.UTF-8
Gra typu Jump'n Run Freenukem to klon gry z ery kart graficznych EGA.
Wykorzystywane są oryginalne pliki z poziomami i grafikami.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/freenukum.6*
%{_desktopdir}/freenukum.desktop
%{_iconsdir}/*/*/*/*
