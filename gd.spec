Summary:	Library for PNG, JPEG creation
Summary(es):	Biblioteca para manipulaciÛn de im·genes
Summary(pl):	Biblioteka do tworzenia grafiki w formacie PNG, JPEG
Summary(pt_BR):	Biblioteca para manipulaÁ„o de imagens
Name:		gd
Version:	2.0.1
Release:	4
License:	BSD-style
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.boutell.com/ftp-materials/boutell/gd/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
URL:		http://www.boutell.com/gd/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	freetype-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		shlibver	%(echo %{version} | cut -f-2 -d.)

%description
gd library creates PNG, JPEG and WBMP images, not GIF images. This is
a good thing. PNG is a more compact format, and full compression is
available. JPEG works well with photographic images, and is still more
compatible with the major Web browsers than even PNG is. WBMP is
intended for wireless devices (not regular web browsers). Existing
code will need modification to call or gdImageJpeg instead of
gdImageGif.

This library allows you to easily create and manipulate PNG, JPEG
image files from your C programs.

%description -l es
Esta es la biblioteca gd para el manejo de im·genes. Fue creada para
uso en la Web, creando gr·ficos autom·ticamente. Pero es ˙til para
cualquier programa que necesite de im·genes personalizados. No es un
programa de dibujo; es una biblioteca.

%description -l pl
Biblioteka pozwalaj±ca na proste tworzenie i manipulowanie plikami
graficznymi w formacie PNG, JPEG i WBMP, ale nie GIF.

%description -l pt_BR
Esta È a biblioteca gd para manipulaÁ„o de imagens. Ela foi criada
para uso na Web, gerando gr·ficos automaticamente. Mas È ˙til para
qualquer programa que precise de imagens personalizados. N„o È um
programa de desenho; È uma biblioteca.

%package devel
Summary:	Development part of the GD library
Summary(es):	Archivos de inclusiÛn y bibliotecas para desarrollar programas usando gd
Summary(pl):	CzÍ∂Ê biblioteki GD przeznaczona dla developerÛw
Summary(pt_BR):	Arquivos de inclus„o e bibliotecas para desenvolver programas usando gd
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	libpng-devel
Requires:	zlib-devel
Requires:	libjpeg-devel
Requires:	freetype-devel >= 2.0
Requires:	%{name} = %{version}

%description devel
This package contains the files needed for development of programs
linked against GD.

%description devel -l es
Este paquete contiene los archivos de inclusiÛn y las bibliotecas
necesarias para desarrollar programas usando gd.

%description devel -l pl
Pakiet ten zawiera pliki potrzebne do rozwoju programÛw korzystaj±cych
z biblioteki GD.

%description devel -l pt_BR
Este pacote contÈm os arquivos de inclus„o e as bibliotecas
necess·rias para desenvolver programas usando gd.

%package static
Summary:	Static GD library
Summary(es):	Static libraries for libgd development
Summary(pl):	Statyczna biblioteka GD
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com libgd
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
This package contains static GD library.
This is the gd image manipulating library. It was created to allow
graphs, charts and the like to be generated on the fly for use on the
World wide Web, but is useful for any application in which custom
images are useful. It is not a paint program; it is a library.

This package contains static libraries for libgd development.

%description static -l pl
Pakiet ten zawiera statyczn± bibliotekÍ GD.

%description static -l pt_BR
Este pacote contem bibliotecas est·ticas para desenvolvimento com
libgd.

%package progs
Summary:	Utility programs that use libgd
Summary(es):	Programas utilitarios libgd
Summary(pl):	NarzÍdzia ktÛre uøywaj± libgd
Summary(pt_BR):	Programas utilit·rios libgd
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Group(pt):	AplicaÁıes/Gr·ficos
Requires:	%{name} = %{version}

%description progs
These are utility programs supplied with gd, the .jpeg graphics
library.
The libgd-progs package contains a group of scripts for manipulating
the graphics files in formats which are supported by the libgd
library.

%description progs -l pl
Pakiet ten zawiera dodatkowe programy uzywaj±ce libgd.

%description progs -l pt_BR
Este pacote inclui v·rios utilit·rios para manipulaÁ„o de arquivos gd
para uso pelos programas que usam a libgd.

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal
automake -a -c
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf readme.txt index.html

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc readme.txt.gz
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc index.html.gz
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
