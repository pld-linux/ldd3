Summary:	Linux Device Drivers, Third Edition book
Summary(pl.UTF-8):	Książka "Linux Device Drivers, Third Edition"
Name:		ldd3
Version:	3
Release:	1
License:	Creative Commons Attribution-ShareAlike 2.0
Group:		Documentation
Source0:	http://lwn.net/images/pdf/LDD3/ldd3_pdf.tar.bz2
# Source0-md5:	5cfce7586b3eed87d57c715d5ba86e17
URL:		http://lwn.net/Kernel/LDD3/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains PDF version of the Third Edition of Linux Device
Drivers, by Jonathan Corbet, Alessandro Rubini, and Greg
Kroah-Hartman.

This book is available under the terms of the Creative Commons
Attribution-ShareAlike 2.0 license. That means that you are free to
download and redistribute it. The development of the book was made
possible, however, by those who purchase a copy from O'Reilly or
elsewhere.

LDD3 is current as of the 2.6.10 kernel. See the LWN 2.6 API changes
page at http://lwn.net/Articles/2.6-kernel-api/ for information on
subsequent changes.

%description -l pl.UTF-8
Ten pakiet zawiera wersję PDF trzeciego wydania książki Linux Device
Drivers autorstwa Jonathana Corbeta, Alessandro Rubiniego i Grega
Kroah-Hartmana.

Książka ta jest dostępna na warunkach licencji Creative Commons
Attribution-ShareAlike 2.0. Oznacza to, że można ją za darmo ściągać i
rozpowszechniać. Jednak jej stworzenie było możliwe dzięki tym, którzy
zakupili egzemplarz z wydawnictwa O'Reilly lub innego źródła.

LDD3 jest aktualne dla jądra 2.6.10. Informacje o późniejszych
zmianach można znaleźć na stronie "LWN 2.6 API changes" pod adresem
<http://lwn.net/Articles/2.6-kernel-api/>.

%prep
%setup -q -n ldd3_pdf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/ldd3

cp -a *.pdf $RPM_BUILD_ROOT%{_docdir}/ldd3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/ldd3
