#
# Conditional build:
%bcond_without	xpm	# without XPM support (requires X11 libs)
#
Summary:	Library for PNG, JPEG creation
Summary(es):	Biblioteca para manipulaci�n de im�genes
Summary(pl):	Biblioteka do tworzenia grafiki w formacie PNG, JPEG
Summary(pt_BR):	Biblioteca para manipula��o de imagens
Name:		gd
Version:	2.0.30
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.boutell.com/gd/http/%{name}-%{version}.tar.gz
# Source0-md5:	8ec99b54b1e985d27f2b871deae953e3
Patch0:		%{name}-fontpath.patch
Patch1:		%{name}-rotate_from_php.patch
URL:		http://www.boutell.com/gd/
%{?with_xpm:BuildRequires:	XFree86-devel}
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	zlib-devel
%{!?with_xpm:BuildConflicts:	XFree86-devel}
Provides:	gd(gif) = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gd is the image manipulating library. It was created to allow graphs,
charts and the like to be generated on the fly for use on the World
wide Web, but is useful for any application in which custom images are
useful. It is not a paint program; it is a library. gd library creates
PNG, JPEG, GIF and WBMP images. PNG is a more compact format, and full
compression is available. JPEG works well with photographic images,
and is still more compatible with the major Web browsers than even PNG
is. WBMP is intended for wireless devices (not regular web browsers).

%description -l es
Esta es la biblioteca gd para el manejo de im�genes. Fue creada para
uso en la Web, creando gr�ficos autom�ticamente. Pero es �til para
cualquier programa que necesite de im�genes personalizados. No es un
programa de dibujo; es una biblioteca.

%description -l pl
gd to biblioteka do obr�bki obraz�w. Zosta�a stworzona, aby umo�liwi�
dynamiczne generowanie wykres�w i podobnych rzeczy na potrzeby WWW,
ale mo�e by� przydatna tak�e dla ka�dej aplikacji tworz�cej w�asne
obrazy. Biblioteka ta pozwala na tworzenie plik�w graficznych w
formatach PNG, JPEG, GIF i WBMP. PNG jest zwartym formatem z
bezstratn� kompresj�. JPEG dobrze nadaje si� do obraz�w
fotograficznych i jest obs�ugiwany nawet przez wi�cej przegl�darek WWW
ni� PNG. WBMP jest przeznaczony dla urz�dze� bezprzewodowych (a nie
zwyk�ych przegl�darek WWW).

%description -l pt_BR
Esta � a biblioteca gd para manipula��o de imagens. Ela foi criada
para uso na Web, gerando gr�ficos automaticamente. Mas � �til para
qualquer programa que precise de imagens personalizados. N�o � um
programa de desenho; � uma biblioteca.

%package devel
Summary:	Development part of the GD library
Summary(es):	Archivos de inclusi�n y bibliotecas para desarrollar programas usando gd
Summary(pl):	Cz�� biblioteki GD przeznaczona dla developer�w
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para desenvolver programas usando gd
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_xpm:Requires:	XFree86-devel}
Requires:	fontconfig-devel
Requires:	freetype-devel >= 2.0
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	zlib-devel
Provides:	gd-devel(gif) = %{version}-%{release}

%description devel
This package contains the files needed for development of programs
linked against GD.

%description devel -l es
Este paquete contiene los archivos de inclusi�n y las bibliotecas
necesarias para desarrollar programas usando gd.

%description devel -l pl
Pakiet ten zawiera pliki potrzebne do rozwoju program�w korzystaj�cych
z biblioteki GD.

%description devel -l pt_BR
Este pacote cont�m os arquivos de inclus�o e as bibliotecas
necess�rias para desenvolver programas usando gd.

%package static
Summary:	Static GD library
Summary(pl):	Statyczna biblioteka GD
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libgd
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	gd-static(gif) = %{version}-%{release}

%description static
This package contains static gd library.

%description static -l pl
Ten pakiet zawiera statyczn� bibliotek� gd.

%description static -l pt_BR
Este pacote contem bibliotecas est�ticas para desenvolvimento com
libgd.

%package progs
Summary:	Utility programs that use libgd
Summary(es):	Programas utilitarios libgd
Summary(pl):	Narz�dzia u�ywaj�ce libgd
Summary(pt_BR):	Programas utilit�rios libgd
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
These are utility programs supplied with gd, the image manipulation
library. The libgd-progs package contains a group of scripts for
manipulating the graphics files in formats which are supported by the
libgd library.

%description progs -l pl
Ten pakiet zawiera programy u�ywaj�ce biblioteki gd, s�u��ce do
obr�bki plik�w graficznych w formatach obs�ugiwanych przez libgd.

%description progs -l pt_BR
Este pacote inclui v�rios utilit�rios para manipula��o de arquivos gd
para uso pelos programas que usam a libgd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# hack to avoid inclusion of -s or -L/usr/%{_lib} in --ldflags
%{__perl} -pi -e 's,\@LDFLAGS\@,-L/usr/X11R6/%{_lib},g' config/gdlib-config.in

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoheader}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING index.html
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdlib-config
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/gdlib-config
