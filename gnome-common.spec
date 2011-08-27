Name:           gnome-common
Version:        2.28.0
Release:        1.1%{?dist}
Summary:        Useful things common to building gnome packages from scratch

Group:          Development/Tools
BuildArch:      noarch
License:        GPLv2
URL:            http://developer.gnome.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.28/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Hmmm.... gnome-common needs all of these.  But it doesn't necessarily need
# a particular version.  We could install automake14 and not automake, for
# instance, and things would still work....  Is it better to drop requirements
# altogether?  (gnome-common programs will run but give an error without
# doing anything useful.)
#Requires: automake
#Requires: autoconf
# gnome-common can be used in a way that doesn't require either of these.
# Unrequiring them for the moment.
#Requires: libtool
#Requires: gettext
Requires: pkgconfig

%description
This package contains sample files that should be used to develop pretty much
every GNOME application.  The programs included here are not needed for running
gnome apps or building ones from distributed tarballs.  They are only useful
for compiling from CVS sources or when developing the build infrastructure for
a GNOME application.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}
cp doc-build/README doc-README
# No sense making a doc subdir in the rpm pkg for one file.
cp doc/usage.txt usage.txt

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc-README README COPYING usage.txt ChangeLog
%{_bindir}/*
%{_datadir}/aclocal/*
%{_datadir}/%{name}

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.28.0-1.1
- Rebuilt for RHEL 6

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun  3 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-2
- Support automake 1.11

* Sun Mar 29 2009  Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 2.24.0-1
- Update to version 2.24.0

* Mon Apr 7 2008 Toshio Kuratomi <toshio@fedoraproject.org> - 2.20.0-1
- Update to version 2.20.0.

* Sun Aug 12 2007 Toshio Kuratomi <a.badger@gmail.com> - 2.18.0-1
- Update to version that matches gnome-2.18.
- Update license tag to strict GPLv2.

* Wed Dec 06 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.12.0-4
- Add a patch from gnome-common cvs to address bug #218717 (gnome-common
  does not work with automake-1.10).

* Mon Sep 04 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.12.0-3
- Bump and rebuild for FC6.

* Thu Feb 16 2006 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.12.0-2
- Bump and rebuild for FC5.

* Tue Oct 18 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.12.0-1
- Upgrade to 2.12.0.
- Add dist tag.

* Thu May 12 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.8.0-3
- Bump and rebuild to get versions synced across architectures.

* Fri Mar 18 2005 Toshio Kuratomi <toshio-tiki-lounge.com> - 2.8.0-2
- Rebuild for FC4t1

* Tue Sep 14 2004 Toshio Kuratomi <toshio-tiki-lounge.com> - 0:2.8.0-1
- Update to 2.8.0
  + This release supports automake thru version 1.9 and has had a lot of
    deprecated stuff cleaned out.
- Removed BuildRequires.  A base mach build environment will build it now.
- Removed Requires.  Although gnome-common still requires autoconf and
  friends, it doesn't require a specific version of them.  There's no virtual
  provides in the automake14,15,16,17 automake packages that could help here.

* Mon Mar 22 2004 Toshio Kuratomi <toshio-tiki-lounge.com> - 0:2.4.0-0.fdr.3
- Add COPYING file to the docs
- Add bin/Changelog to the docs as ChangeLog.bin

* Sun Dec 28 2003 Toshio Kuratomi <toshio-tiki-lounge.com> - 0:2.4.0-0.fdr.2
- Update the Requires line (rpm doesn't automatically detect most of the
  dependencies.)
- Remove the AUTHORS file as it's currently empty

* Fri Dec 19 2003 Toshio Kuratomi <toshio-tiki-lounge.com> - 0:2.4.0-0.fdr.1
- Initial RPM release.
