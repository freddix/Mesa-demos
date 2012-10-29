Summary:	Mesa Demos source code
Name:		Mesa-demos
Version:	8.0.1
Release:	3
License:	various (MIT, SGI, GPL - see copyright notes in sources)
Group:		Development/Libraries
Source0:	ftp://ftp.freedesktop.org/pub/mesa/demos/%{version}/mesa-demos-%{version}.tar.bz2
# Source0-md5:	320c2a4b6edc6faba35d9cb1e2a30bf4
URL:		http://www.mesa3d.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	glew-devel
BuildRequires:	pkg-config
BuildRequires:	rpm-pythonprov
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-libXext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenGL utilities from Mesa-demos: glxgears and glxinfo.

%prep
%setup -qn mesa-demos-%{version}

%build
%configure \
	--disable-silent-rules

%{__make} -C src/xdemos glxinfo glxgears

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -p src/xdemos/{glxinfo,glxgears} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glxgears
%attr(755,root,root) %{_bindir}/glxinfo

