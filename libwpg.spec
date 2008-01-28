Summary:	Library for importing and converting Corel WordPerfect(TM) Graphics images
Summary(pl.UTF-8):	Biblioteka do importowania i konwersji obrazów Corel WordPerfect Graphics
Name:		libwpg
Version:	0.1.2
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://dl.sourceforge.net/libwpg/%{name}-%{version}.tar.gz
# Source0-md5:	317cee27f380c394c6e4eec02d45cab8
URL:		http://libwpg.sourceforge.net/
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libwpg project is a collection of library and tools to work with
graphics in WPG (WordPerfect Graphics) format. WPG is the format used
among others in Corel software, such as WordPerfect(TM) and
Presentations(TM).

%description -l pl.UTF-8
Projekt libwpg to zestaw biblioteki i narzędzi do pracy z obrazami w
formacie WPG (WordPerfect Graphics). WPG to format używany między
innymi w programach firmy Corel, takich jak WordPerfect(TM) i
Presentations(TM).

%package devel
Summary:	Header files for libwpg library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwpg
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for libwpg library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwpg.

%package static
Summary:	Static libwpg library
Summary(pl):	Statyczna biblioteka libwpg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwpg library.

%description static -l pl.UTF-8
Statyczna biblioteka libwpg.

%package tools
Summary:	Tools to transform WordPerfect Graphics into other formats
Summary(pl.UTF-8):	Narzędzia do konwersji plików z formatu WordPerfect Graphics do innych
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description tools
Tools to transform WordPerfect Graphics (WPG) into other formats.

%description tools -l pl.UTF-8
Narzędzia do konwersji plików z formatu WordPerfect Graphics do innych
formatów.

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libwpg*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wpg2raw
%attr(755,root,root) %{_bindir}/wpg2svg
%attr(755,root,root) %{_bindir}/wpg2svgbatch.pl
