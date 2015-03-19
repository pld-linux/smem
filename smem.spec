Summary:	Report application memory usage in a meaningful way
Name:		smem
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.selenic.com/smem/download/%{name}-%{version}.tar.gz
# Source0-md5:	fe79435c3930389bfdb560255c802162
URL:		http://www.selenic.com/smem/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python >= 1:2.7
Requires:	python-modules >= 1:2.7
Requires:	uname(release) >= 2.6.27
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
smem is a tool that can give numerous reports on memory usage on Linux
systems. Unlike existing tools, smem can report proportional set size
(PSS), which is a more meaningful representation of the amount of
memory used by libraries and applications in a virtual memory system.

Because large portions of physical memory are typically shared among
multiple applications, the standard measure of memory usage known as
resident set size (RSS) will significantly overestimate memory usage.
PSS instead measures each application's "fair share" of each shared
area to give a realistic measure.

%prep
%setup -q

%build
%{__make} smemcap \
	CC="%{__cc}" \
	CPU_OPTS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
install -p smem $RPM_BUILD_ROOT%{_bindir}
install -p smemcap $RPM_BUILD_ROOT%{_bindir}
cp -p smem.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_bindir}/smem
%attr(755,root,root) %{_bindir}/smemcap
%{_mandir}/man8/smem.8*
