Summary:	SuckMT, a multithreaded suck replacement
Summary(pl):	SuckMT - wielow±tkowy zamiennik sucka
Name:		suckmt
Version:	0.54
Release:	2
License:	GPL
Group:		Applications/News
Source0:	http://www.wirehub.nl/~basjesn/Files/%{name}-%{version}.tar.gz
Source1:	%{name}-scripts.tar.gz
Patch0:		%{name}-DESTDIR.patch
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
SuckMT to program do ¶ci±gania newsów z serwera NNTP na twój lokalny
komputer. Inspiracj± by³ program suck, od którego SuckMT do¶æ wyra¼nie
siê odró¿nia: SuckMT otwiera kilka równoleg³ych po³±czeñ z serwerem
NNTP aby ograniczyæ czas po³±czenia. Aby przes³aæ artyku³y z powrotem
do serwera NNTP potrzebujesz narzêdzi z pakietu suck.

%prep
%setup -q
%patch -p0

%build
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/lib/suckmt
tar zx -f %{SOURCE1} -C $RPM_BUILD_ROOT%{_var}/lib/suckmt

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf INSTALL README ChangeLog suckmt.ini.sample AUTHORS COPYING NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/suckmt
%attr(750,news,news) %dir %{_sysconfdir}/suckmt
%config(noreplace,missingok) %verify(not md5 size mtime) %attr(660,news,news) %{_sysconfdir}/suckmt/suckmt.ini
%attr(750,news,news) %dir %{_var}/spool/suckmt
%attr(750,news,news) %dir %{_var}/spool/suckmt/in.coming
%attr(750,news,news) %dir %{_var}/lib/suckmt
%attr(750,news,news) %{_var}/lib/suckmt/*
