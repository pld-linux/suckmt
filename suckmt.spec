Summary:	SuckMT, a multithreaded suck replacement
Summary(pl):	SuckMT - wielow�tkowy zamiennik sucka
Name:		suckmt
Version:	0.41
Release:	1
License:	GPL
Group:		Applications/News
Group(de):	Applikationen/News
Group(pl):	Aplikacje/News
Source0:	http://www.wirehub.nl/~basjesn/Files/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
Provides:	news-sucker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains software to download news from an NNTP server to
your local machine. This software was inspired by suck
(http://home.att.net/~bobyetman/) but has a major difference with
suck: SuckMT will open several NNTP connections simultaneously to
reduce the required connect time. To upload new messages back to the
NNTP server you will still need tools from the suck package.

%description -l pl
SuckMT to program do �ci�gania news�w z serwera NNTP na tw�j lokalny
komputer. Inspiracj� by� program suck, od kt�rego SuckMT do�� wyra�nie
si� odr�nia: SuckMT otwiera kilka r�wnoleg�ych po��cze� z serwerem
NNTP aby ograniczy� czas po��czenia. Aby przes�a� artyku�y z powrotem
do serwera NNTP potrzebujesz narz�dzi z pakietu suck.

%prep
%setup -q
%build
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf INSTALL README ChangeLog suckmt.ini.sample

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {INSTALL,README,ChangeLog,suckmt.ini.sample}.gz
%attr(755,root,root) %{_bindir}/suckmt
